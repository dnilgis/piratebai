#!/usr/bin/env python3
"""The ship examines herself. Exit 0 = seaworthy, 1 = repairs needed."""
import json, pathlib, re, sys, datetime, urllib.request

fails = []
root = pathlib.Path(".")

def check(name, fn):
    try:
        fn()
        print(f"  ok    {name}")
    except Exception as e:
        fails.append(f"{name}: {e}")
        print(f"  FAIL  {name}: {e}")

def fleet():
    d = json.loads((root/"data/fleet.json").read_text())
    assert isinstance(d["ships"], list) and len(d["ships"]) >= 3, "fleet too small"
    for s in d["ships"]:
        for k in ("name","org","params","dl_week","vram","x","y","s"): assert k in s, f"ship missing {k}"
        assert 0 <= s["x"] <= 95 and 55 <= s["y"] <= 88, f"{s['name']} has run aground (x={s['x']},y={s['y']})"

def latest():
    d = json.loads((root/"log/latest.json").read_text())
    for k in ("entry","date","text"): assert k in d, f"latest.json missing {k}"
    n = d["entry"]
    assert (root/f"log/{n:04d}.html").exists(), f"latest points at entry {n:04d} but the page is missing"

def archive():
    pages = sorted(root.glob("log/[0-9][0-9][0-9][0-9].html"))
    assert pages, "no log entries at all"
    nums = [int(p.stem) for p in pages]
    assert nums == list(range(1, len(nums)+1)), f"gap in the archive: {nums}"
    idx = (root/"log/index.html").read_text()
    for p in pages:
        assert p.name in idx, f"{p.name} exists but is not listed in log/index.html"

def ledger():
    d = json.loads((root/"hold/ledger.json").read_text())
    for c in d["chests"]:
        assert re.fullmatch(r"[0-9a-f]{64}", c["sha256"]), f"chest {c['id']} seal malformed"

def feed():
    t = (root/"log/feed.xml").read_text()
    assert "<feed" in t and "<entry>" in t, "feed has no entries"

def links():
    for page in root.glob("**/*.html"):
        if ".git" in str(page): continue
        for m in re.findall(r'href="([^"#]+)"', page.read_text()):
            if m.startswith(("http","data:","mailto")): continue
            t = (root / m.lstrip("/")) if m.startswith("/") else (page.parent / m)
            t = pathlib.Path(str(t)).resolve()
            if t.is_dir(): t = t / "index.html"
            assert t.exists(), f"{page}: broken href -> {m}"

def hf_reachable():
    req = urllib.request.Request("https://huggingface.co/api/models?limit=1",
                                 headers={"User-Agent": "piratebai-health/1.0"})
    with urllib.request.urlopen(req, timeout=15) as r:
        assert r.status == 200, f"HF API status {r.status}"

warns = []
def soft(name, fn):
    try:
        fn()
        print(f"  ok    {name}")
    except Exception as e:
        warns.append(f"{name}: {e}")
        print(f"  WARN  {name}: {e}  (rough seas — sail on with working sources)")

print(f"health check — {datetime.date.today().isoformat()}")
check("fleet.json shape", fleet)
check("latest.json integrity", latest)
check("archive continuity", archive)
check("hold ledger seals", ledger)
check("atom feed", feed)
check("internal links", links)
soft("huggingface reachable", hf_reachable)
if not fails and not warns: print("SEAWORTHY")
elif not fails: print(f"SEAWORTHY, ROUGH SEAS ({len(warns)} source(s) down)")
else: print(f"REPAIRS NEEDED ({len(fails)})")
sys.exit(1 if fails else 0)
