# TODAY'S VOYAGE — daily orders

Work through these in order. Standing orders in CLAUDE.md govern everything.

1. RUN THE HEALTH CHECK: `python3 scripts/health_check.py`. If it reports
   failures, diagnose and fix what you can (per the self-repair rules),
   re-run it, and mention notable repairs in today's log entry as ship
   maintenance ("patched the mainsail scraper").

2. SURVEY THE OCEAN. Gather today's weather from primary sources:
   - Hugging Face API: trending / most-downloaded open-weight models,
     anything newly launched or moving fast.
   - What the fleet data says changed since data/fleet.json was last updated.
   Note 2–4 genuinely notable things. If nothing notable happened, calm
   seas are worth chronicling too.

3. REFRESH THE FLEET: update data/fleet.json per the conventions in
   CLAUDE.md, based on what you actually fetched.

4. WRITE THE LOG: compute today's entry number and voyage day
   (day = days since 2026-07-04, +1). Write log/NNNN.html in the Captain's
   voice, update log/latest.json, append to log/index.html and
   log/feed.xml. Follow the file conventions exactly.

5. FINAL CHECK: re-run `python3 scripts/health_check.py`. It must pass
   before you finish. Do not commit or push — the workflow handles that.

Remember: immutable archive, truthful entries, minimal diffs, no touching
the forbidden files. Fair winds.
