# Revision check R21 v2: text scan of v1 vs v2 for the audit's overclaims and for fix tags.
# Run: python3 -I R2_text_scan.py <v1.md> <v2.md>
import re, sys
v1 = open(sys.argv[1], encoding='utf-8').read().splitlines()
v2 = open(sys.argv[2], encoding='utf-8').read().splitlines()

patterns = {
    'FIX-1 "cannot be excluded"': r'cannot be excluded',
    'FIX-1 "every algebraic identity"': r'every algebraic identity',
    'FIX-1 "all/every available identit"': r'(all|every) available identit',
    'FIX-1 "every identity used"': r'every identity used',
    'FIX-1 FNAL/TSY mentions (inspect)': r'FNAL|TSY',
    'FIX-3 "Before this note"': r'Before this note',
    'FIX-3 "any n"': r'any n\b',
    'FIX-4 "0.1102q" / "<=0.1102"': r'0\.1102(?!3)',
    'FIX-4 "0.11q"': r'0\.11q',
    'FIX-5 "⊋"': r'⊋',
    'FIX-5 "cannot produce"': r'cannot produce',
    'FIX-5 "unavailable"/"no per-point"': r'unavailable|no per-point|not available',
    'FIX-6 "Since B is constant"': r'Since B is constant',
    'N4 "c_1c_2≠0"': r'c_1c_2≠0',
    'N6 defect "κ(u)" / "κ²" / "Z(κ)"': r'κ\(u\)|κ²|Z\(κ\)|κ≡0|κ≢0',
}
for name, pat in patterns.items():
    h1 = [i+1 for i, l in enumerate(v1) if re.search(pat, l)]
    h2 = [(i+1, l.strip()[:160]) for i, l in enumerate(v2) if re.search(pat, l)]
    print(f"== {name}: v1 lines {h1}; v2 hits {len(h2)}")
    for ln, txt in h2:
        print(f"   v2:{ln}: {txt}")

tags = {}
for i, l in enumerate(v2):
    for t in re.findall(r'\[v2: ([^\]]*)\]', l):
        for k in re.findall(r'(FIX-\d|N\d+|audit note)', t):
            tags.setdefault(k, []).append(i+1)
print("\n== [v2: ...] tags and their v2 lines")
for k in sorted(tags, key=lambda s: (s[0], int(re.sub(r'\D', '', s) or 0))):
    print(f"   {k}: {tags[k]}")
want = [f"FIX-{i}" for i in range(1, 7)] + [f"N{i}" for i in range(1, 13)]
print("   missing tags:", [w for w in want if w not in tags])

print("\n== label words per line in v2 status table (§6)")
start = next(i for i, l in enumerate(v2) if l.startswith('## 6.'))
for l in v2[start:]:
    if l.startswith('| ') and not l.startswith('| item') and not l.startswith('|---'):
        labs = re.findall(r'PROVED|CONDITIONAL|COMPUTED|HEURISTIC|OPEN|CITED', l)
        print(f"   {l.split('|')[1].strip()[:70]:70s} -> {labs}")
