# 3PP cloud session — FINAL PROGRESS (q=32 exhaustive search)

Final update: 2026-10-12T00:10:22Z. Cloud session: claude.ai/code session_018ipZ7GACBWTbpNANdAnLV8. **The cloud run is STOPPED.** Work continues in the local session "(Active) 3PP (2)".

## Status
- **Cloud shards done: 1498.** These are 15454..16950 (contiguous) plus 17693, the shard missing from done_linux. **All 1498 report COUNTEREXAMPLES=0.**
- **Setup.** evenexh5.c was used as uploaded (unchanged); gcc 13.3 -O3 -march=native; 4 workers. The command was `./evenexh5 5 <s> 20000 -S2 -L 5 -P`.
- **Self-tests.** q=16 -S2 gave even-3PP=112, COUNTEREXAMPLES=0. q=8 gave even-3PP=10. They were re-run after each container restart.
- **Rate.** About 190 shards/hour on 4 shared vCPUs, roughly 70 s per shard.
- **Pauses.** Three restarts/pauses are logged in CLOUD_LOG.md. Shards in flight at each pause were discarded and redone, so no partial results were kept.
- **Accounting.** done_linux (5256) + done_mac (727) + cloud (1498) = **7481 covered**.
- **Remaining.** **12519 shards: 2726..9892 and 10102..15453** (exact list in REMAINING_SHARDS.txt), minus whatever the Linux box did after the hand-off (it was working upward from about 2560).
- **q=32 is NOT proved.** That needs all 20,000 shards accounted for and merged.

## HANDOVER TO "(Active) 3PP (2)"
1. **Merge.**
   - Copy `results/shard_*.txt` into q32run/results.
   - Check that `grep -L COUNTEREXAMPLES= results/*.txt` prints nothing.
   - Check that every file has COUNTEREXAMPLES=0.
2. **Update the accounting.**
   - Combine done_linux.txt, done_mac.txt, cloud_done.txt and any newer Linux-box results.
   - Recompute the remaining set; start from REMAINING_SHARDS.txt.
3. **Continue the remaining shards** on whatever machines are available. run_cloud.sh in this folder is restartable: it skips done shards and uses atomic claims. To give the new run a different order, edit its `order()` function.
4. **Claim q=32 TRUE only** when all 20,000 shards are accounted for, every one with COUNTEREXAMPLES=0. If any shard ever shows `*** COUNTEREXAMPLE`, verify it independently in Python before reporting.
