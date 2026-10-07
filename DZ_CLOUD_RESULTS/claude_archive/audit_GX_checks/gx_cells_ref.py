#!/usr/bin/env python3
"""Referee check (GX audit, 7 Oct 2026). Independent coverage arithmetic for GX section 3 [C].
- Recount cells: even rho in [10,40], rho+3 <= g <= min(2rho, ceil(3rho/2)+2), a* = rho - ceil(g/2).
- Sufficient gate (PTH v2.2 GO): no r in [rho-a*, rho] divides g + rho/2.
- Check the referee's closed form: gate fails  <=>  g = rho/2 (mod 2) and g <= 3rho/2,
  and then the unique offending r is (g+rho/2)/2 = m/4.  Checked for even rho in [10, 400].
- Check kernel bound rho - a* >= a* + 3 (equivalently a* <= (rho-3)/2) in the whole band rho+3<=g<=2rho.
- Compare with GO(e) coverage: cells with a* <= (rho-4)/3 (78) and gate-pass among them (51).
Pure integer arithmetic; reads no files.  Usage: python3 -I gx_cells_ref.py"""

def cells(rho, lo_extra=3, hi=None):
    top = min(2 * rho, -(-3 * rho // 2) + 2) if hi is None else hi
    for g in range(rho + lo_extra, top + 1):
        yield g, rho - (-(-g // 2))

def gate_bad(rho, g, a):
    N = g + rho // 2
    return [r for r in range(rho - a, rho + 1) if N % r == 0]

tot = gp = 0; fails = []; go78 = go51 = 0; new = []
for rho in range(10, 41, 2):
    for g, a in cells(rho):
        assert a >= 1
        tot += 1
        bad = gate_bad(rho, g, a)
        if bad: fails.append((rho, g, a, bad))
        else: gp += 1
        if 3 * a <= rho - 4:
            go78 += 1
            if not bad: go51 += 1
        elif not bad:
            new.append((rho, g, a))
print(f"rho in [10,40]: cells={tot} gate_pass={gp} gate_fail={len(fails)}")
print(f"GO(e) range a*<=(rho-4)/3: cells={go78} gate_pass={go51}")
print(f"gate-pass cells newly covered by GX (outside GO(e) range): {len(new)}")
print("first new cells:", new[:12])

# closed form, wide range
mism = 0; multi = 0; kern = 0; nb = 0
for rho in range(10, 401, 2):
    for g, a in cells(rho):
        bad = gate_bad(rho, g, a)
        pred = (g % 2 == (rho // 2) % 2) and (2 * g <= 3 * rho)
        if bool(bad) != pred: mism += 1
        if bad and bad != [(g + rho // 2) // 2]: multi += 1
    for g in range(rho + 3, 2 * rho + 1):     # whole band, incl. NWF-covered and a*=0 cells
        a = rho - (-(-g // 2)); nb += 1
        if not (rho - a >= a + 3): kern += 1
print(f"closed form check rho in [10,400]: mismatches={mism}, cells with offending r != m/4: {multi}")
print(f"kernel bound rho-a*>=a*+3 over whole band rho+3<=g<=2rho, rho in [10,400] ({nb} cells): failures={kern}")
