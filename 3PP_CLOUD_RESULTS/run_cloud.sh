#!/bin/bash
# run_cloud.sh NWORKERS -- cloud runner for the q=32 exhaustive search (written in the cloud session;
# the original run_cloud.sh was not transferred). Restartable: finished shards are skipped.
# Order: 17693 (missing from done_linux), then DESCENDING 16950..0, then any other unfinished shard.
# Command per shard (from HANDOFF_README): ./evenexh5 5 <shard> 20000 -S2 -L 5 -P
# A shard is complete iff results/shard_<s>.txt contains "COUNTEREXAMPLES=".
cd "$(dirname "$0")"
N=${1:-$(nproc)}
mkdir -p results claims logs
order() { echo 17693; seq 16950 -1 0; seq 16951 19999; }
is_done() { grep -qx "$1" done_linux.txt done_mac.txt 2>/dev/null && return 0
            [ -f results/shard_$1.txt ] && grep -q COUNTEREXAMPLES= results/shard_$1.txt; }
worker() {
  local w=$1
  order | while read s; do
    [ -f STOP ] && exit 0
    is_done $s && continue
    mkdir claims/$s 2>/dev/null || continue          # atomic claim
    local t0=$(date +%s)
    ./evenexh5 5 $s 20000 -S2 -L 5 -P > results/.shard_$s.tmp 2> logs/shard_$s.err
    if grep -q COUNTEREXAMPLES= results/.shard_$s.tmp; then
      mv results/.shard_$s.tmp results/shard_$s.txt; rm -f logs/shard_$s.err
      echo $s >> cloud_done.txt
      echo "$(date -u +%FT%TZ) w$w shard $s $(( $(date +%s)-t0 ))s $(grep -o 'COUNTEREXAMPLES=[0-9]*' results/shard_$s.txt)" >> worker_log.txt
      if grep -q '\*\*\* COUNTEREXAMPLE' results/shard_$s.txt || ! grep -q 'COUNTEREXAMPLES=0 ' results/shard_$s.txt; then
        echo "COUNTEREXAMPLE in shard $s" > STOP; exit 0; fi
    else
      rmdir claims/$s                                   # interrupted/failed: release the claim
    fi
  done
}
rm -rf claims; mkdir claims        # stale claims from an interrupted run are released on restart
for w in $(seq 1 $N); do worker $w & done
wait
echo "$(date -u +%FT%TZ) all workers finished" >> worker_log.txt
