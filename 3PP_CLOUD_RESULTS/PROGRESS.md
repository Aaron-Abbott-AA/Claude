# 3PP cloud session — PROGRESS (q=32 exhaustive search)

Updated 2026-10-07T18:20:38Z. Cloud session: claude.ai/code session_018ipZ7GACBWTbpNANdAnLV8.

- **Setup.** 4 workers run evenexh5, built from the uploaded evenexh5.c (unchanged; gcc 13.3 -O3 -march=native). The command is `./evenexh5 5 <s> 20000 -S2 -L 5 -P`.
- **Self-tests.** q=16 -S2: even-3PP=112, COUNTEREXAMPLES=0. q=8: even-3PP=10.
- **Order.** 17693 first (it was missing from done_linux), then descending from 16950.
- **Scripts.** run_cloud.sh and pack_results.sh were rewritten here, because the originals were not transferred.
- **Shards done by the cloud run: 90.** Shards with COUNTEREXAMPLES≠0: 0.
- **Rate.** About 2.3 shards/min (shared vCPUs).
- **Accounting.** done_linux (5256) + done_mac (727) + cloud (90), with 17693 included. Remaining ≈ 13927, minus whatever the Linux box has done since the hand-off.
- **Status.** q=32 is NOT yet proved. The conjecture must not be claimed TRUE at q=32 until all 20,000 shards are accounted for and merged.

**Merge.** Copy results/shard_*.txt into q32run/results, then check that `grep -L COUNTEREXAMPLES= results/*.txt` prints nothing and that every count is COUNTEREXAMPLES=0.
