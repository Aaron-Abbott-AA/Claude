# Compare numeric tokens and label tokens between R24 v1 and v2 (multiset), and list v2-only/v1-only items.
import re, sys, collections
v1 = open(sys.argv[1], encoding='utf-8').read(); v2 = open(sys.argv[2], encoding='utf-8').read()
num = re.compile(r'\d+(?:[./]\d+)*(?:\^\d+)?')
def toks(s): return collections.Counter(num.findall(s))
def strip_v2(s):  # remove the v2 annotations "[v2: ...]" (non-nested) and the version-history block
    s = re.sub(r'\[v2(?:\.\d)?:[^\]]*\]', '', s)
    return s
c1, c2 = toks(v1), toks(v2)
print("numeric tokens only in v1 (count diff):", dict(c1 - c2))
print("numeric tokens only in v2 (count diff):", dict(c2 - c1))
# headline numbers
for h in ['0.167242', '1551', '91941792089517/549755813888000', '0.1672411', '32480243592761/219902325555200', '0.147704', '0.104306', '0.167228', '3780', '280', '120', '150/150', '15/15', '625', '2048', '452/625', '512', '256']:
    print("  %-34s v1=%d v2=%d" % (h, v1.count(h), v2.count(h)))
labs = ['PROVED', 'CONDITIONAL', 'COMPUTED', 'HEURISTIC', 'OPEN', 'CITED']
print("label counts v1:", {l: len(re.findall(r'\b' + l + r'\b', v1)) for l in labs})
print("label counts v2:", {l: len(re.findall(r'\b' + l + r'\b', v2)) for l in labs})
# status table rows
def table(s):
    i = s.index('## 7. Status'); return [l for l in s[i:].splitlines() if l.startswith('|')]
t1, t2 = table(v1), table(v2)
print("status rows v1=%d v2=%d" % (len(t1), len(t2)))
for a, b in zip(t1, t2):
    if a != b: print("  v1:", a, "\n  v2:", b)
# all [v2: ...] tags
tags = re.findall(r'\[v2(?::\s*([A-Z]+-?\d+))?', v2)
print("v2 tag occurrences:", collections.Counter(t if t else 'v2' for t in tags))
