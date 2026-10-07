# Numeric-token diff of v1 vs v2, and counts of headline numbers (unchanged-numbers check).
import re, sys
from collections import Counter
base = sys.argv[1]
v1 = open(base + '/inputs/R23_v1.md').read(); v2 = open(base + '/HYP_M2_ROUND23_owner_v2.md').read()
tok = lambda s: re.findall(r'\d+(?:\.\d+)?(?:/\d+)?', s)
c1, c2 = Counter(tok(v1)), Counter(tok(v2))
print("numeric tokens in v1 absent from v2:", sorted(set(c1) - set(c2)))
print("numeric tokens in v1 with lower count in v2:", sorted(k for k in c1 if 0 < c2[k] < c1[k]))
print("new numeric tokens in v2:", sorted(set(c2) - set(c1), key=lambda x: float(x.split('/')[0])))
heads = ['0.0925781', '101790647887837/1099511627776000', '0.092579', '0.240046', '0.238', '0.119', '0.4766',
         '443', '1260', '0.08263', '0.104306', '0.147704', '112', '2E/Q', '8E/Q', '32E/Q', '64E/Q']
for h in heads: print(f"{h!r}: v1 {v1.count(h)}  v2 {v2.count(h)}")
