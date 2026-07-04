#!/usr/bin/env python3
"""
bury.py — seal a chest into the Hold.

Usage:
  python3 scripts/bury.py --message path/to/message.txt \
      --name "Sig of Chetek" --opens 2076-07-04 [--tier century] [--founder]

What it does (run from the PUBLIC repo root):
  1. Computes SHA-256 of the exact message bytes.
  2. Assigns the next chest id and appends it to hold/ledger.json.
  3. Inserts the ledger row into hold/index.html.
  4. Adds the burier to crew.html (the Ship's Manifest) with today's voyage day.
  5. Prints the private-custody filename to save the plaintext under in the
     PRIVATE repo (piratebai-hold-private). It does NOT copy the message
     anywhere public.
Then: commit + push the public repo (the commit timestamp is the public seal),
and commit the plaintext to the private repo.
"""
import argparse, hashlib, json, datetime, pathlib, re, sys

LAUNCH = datetime.date(2026, 7, 4)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--message", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--opens", required=True, help="YYYY-MM-DD")
    ap.add_argument("--tier", default="", choices=["", "decade", "generation", "century"])
    ap.add_argument("--founder", action="store_true")
    a = ap.parse_args()

    root = pathlib.Path(".")
    if not (root / "hold/ledger.json").exists():
        sys.exit("Run from the public repo root (hold/ledger.json not found).")

    raw = pathlib.Path(a.message).read_bytes()
    words = len(raw.decode(errors="replace").split())
    if words > 2000:
        sys.exit(f"Message is {words} words; the Articles allow 2,000. Refuse or trim.")
    opens = datetime.date.fromisoformat(a.opens)
    today = datetime.date.today()
    if opens <= today:
        sys.exit("Open date must be in the future.")
    if (opens - today).days > 36525:
        sys.exit("The ship carries chests up to 100 years. Beyond that, no honest promise can be made.")

    digest = hashlib.sha256(raw).hexdigest()
    ledger = json.loads((root / "hold/ledger.json").read_text())
    if any(c["sha256"] == digest for c in ledger["chests"]):
        sys.exit("A chest with this exact content is already sealed.")
    cid = f"{max(int(c['id']) for c in ledger['chests']) + 1:04d}"
    day = (today - LAUNCH).days + 1

    chest = {"id": cid, "buried_by": a.name, "sealed": today.isoformat(),
             "opens": opens.isoformat(), "sha256": digest, "status": "sealed"}
    if a.tier: chest["tier"] = a.tier
    if a.founder: chest["founder"] = True
    ledger["chests"].append(chest)
    ledger["updated"] = today.isoformat()
    (root / "hold/ledger.json").write_text(json.dumps(ledger, indent=1) + "\n")

    hold = (root / "hold/index.html").read_text()
    founder_mark = " ⚓ FOUNDER" if a.founder else ""
    row = (f'<tr>\n<td><span class="sealed">⬛ {cid}</span></td>\n'
           f'<td>{a.name}{founder_mark}</td>\n<td>{today.isoformat()}</td>\n'
           f'<td><b>{opens.isoformat()}</b></td>\n<td class="hash">{digest}</td>\n</tr>\n')
    hold = hold.replace("</tbody>", row + "</tbody>")
    (root / "hold/index.html").write_text(hold)

    crew = (root / "crew.html").read_text()
    cls = ' class="founder"' if a.founder else ""
    crew_row = (f'<tr><td>{day}</td><td{cls}>{a.name}{founder_mark}</td>'
                f'<td>Buried Chest {cid} (opens {opens.year}).</td></tr>\n')
    crew = crew.replace("</tbody>", crew_row + "</tbody>")
    (root / "crew.html").write_text(crew)

    print(f"Chest {cid} sealed.")
    print(f"  sha256: {digest}")
    print(f"  Save plaintext in PRIVATE repo as: chests/chest-{cid}.txt")
    print(f"  Then: git add -A && git commit -m 'hold: seal chest {cid} (opens {opens.isoformat()})' && git push")
    print(f"  The public commit timestamp is the seal. Do not edit past ledger rows, ever.")

if __name__ == "__main__":
    main()
