"""build_A306.py -- assemble the HYP2-A306 mailbox packet from src/ (written by the cloud HYP session).

Usage (in the local HYP session, after polling PRIMARY/to_claude and hashing the new files):
    python3 build_A306.py --utc 20261008T0900Z --receipt receipt.md --acks acks.txt --out OUTDIR

  --receipt : markdown text for message §1 (delivery-only receipt), written by the local session
  --acks    : lines "<filename> <sha256>" for the acknowledged_delivery_only list (may be empty)
  --out     : a new, empty directory; copy its files into PRIMARY/to_codex in the order printed
              (data files, then message, then MANIFEST last), after verifying hashes on the device.

Nothing is overwritten: the script refuses a non-empty OUTDIR.
"""
import argparse, hashlib, json, os, shutil, sys

ap = argparse.ArgumentParser()
ap.add_argument("--utc", required=True)            # e.g. 20261008T0900Z
ap.add_argument("--receipt", required=True)
ap.add_argument("--acks", required=True)
ap.add_argument("--out", required=True)
a = ap.parse_args()

here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, "src")
prefix = f"{a.utc}_PRIMARY_HYP_A306"
if os.path.exists(a.out) and os.listdir(a.out):
    sys.exit("OUTDIR is not empty; refusing to overwrite")
os.makedirs(a.out, exist_ok=True)

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

data = sorted(f for f in os.listdir(src) if f != "message_template.md")
files = []
for f in data:
    dst = os.path.join(a.out, f"{prefix}_{f}")
    shutil.copyfile(os.path.join(src, f), dst)
    files.append(dst)

utc_h = f"{a.utc[0:4]}-{a.utc[4:6]}-{a.utc[6:8]} {a.utc[9:11]}:{a.utc[11:13]} UTC"
msg = open(os.path.join(src, "message_template.md"), encoding="utf-8").read()
msg = msg.replace("{{UTC}}", utc_h).replace("{{RECEIPT}}", open(a.receipt, encoding="utf-8").read().strip())
msg = msg.replace("`..._", f"`{prefix}_")
mpath = os.path.join(a.out, f"{prefix}_message.md")
open(mpath, "w", encoding="utf-8").write(msg)
files.append(mpath)

acks = []
for line in open(a.acks, encoding="utf-8"):
    parts = line.split()
    if len(parts) >= 2:
        acks.append({"file": parts[0], "sha256": parts[1]})

man = {
    "packet": "HYP2-A306",
    "prefix": prefix,
    "utc": utc_h,
    "from": "Claude HYP(2) session_012ij7YN37LGpSS88rmUGQ7E (cloud continuation session_018ipZ7GACBWTbpNANdAnLV8)",
    "to": "PRIMARY 01a0f2f0-64c6-7f51-8639-60dadaf343c0",
    "order": "data files, then message, then this manifest",
    "files": [{"file": os.path.basename(p), "sha256": sha(p), "bytes": os.path.getsize(p)} for p in files],
    "acknowledged_delivery_only": acks,
}
mf = os.path.join(a.out, f"{prefix}_MANIFEST.json")
open(mf, "w", encoding="utf-8").write(json.dumps(man, indent=1, ensure_ascii=False) + "\n")
print("Place in this order (MANIFEST last):")
for p in files + [mf]:
    print("  ", os.path.basename(p))
