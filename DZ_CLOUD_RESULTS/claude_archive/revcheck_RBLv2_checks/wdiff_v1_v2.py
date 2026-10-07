"""Word-level diff v1 -> v2 (referee aid). Usage: python3 -I wdiff_v1_v2.py v1 v2"""
import sys, difflib, re
a = re.findall(r"\S+", open(sys.argv[1], encoding="utf-8").read())
b = re.findall(r"\S+", open(sys.argv[2], encoding="utf-8").read())
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == "equal":
        continue
    print(f"[{op}] -: {' '.join(a[i1:i2])[:600]}")
    print(f"       +: {' '.join(b[j1:j2])[:600]}")
