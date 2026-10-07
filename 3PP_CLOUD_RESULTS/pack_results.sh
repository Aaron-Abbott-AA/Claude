#!/bin/bash
# pack_results.sh -- package cloud results as ../q32_CLOUD_RESULTS_<UTC>.tgz (plain shard_<s>.txt files + logs)
cd "$(dirname "$0")"
T=$(date -u +%Y%m%dT%H%MZ)
sort -n -u cloud_done.txt -o cloud_done.txt 2>/dev/null
tar czf ../q32_CLOUD_RESULTS_$T.tgz results/shard_*.txt cloud_done.txt CLOUD_LOG.md worker_log.txt run_cloud.sh pack_results.sh 2>/dev/null
echo ../q32_CLOUD_RESULTS_$T.tgz
