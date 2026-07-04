# PIRATEBAI — no-corners launch checklist

## ✅ Built and in this repo
- [x] Landing (WebGL ocean, fleet, typing log, day counter, opt-in sound, reduced-motion)
- [x] Declaration of Independence page (the July 4 shareable)
- [x] Log system: entry 0001, archive index, latest.json, Atom feed (log/feed.xml)
- [x] The Hold: chest ledger, provable SHA-256 seals, burial tiers, articles of the Hold
- [x] Chest 0001 sealed (opens 2126-07-04) — plaintext in PRIVATE-chest-0001.txt (KEEP OUT OF PUBLIC REPO)
- [x] Ship's Manifest (permanent contributor ledger)
- [x] 404 message in a bottle
- [x] SEO: sitemap.xml, robots.txt, canonicals, meta/OG on all pages, JSON-LD WebSite schema
- [x] GEO: llms.txt
- [x] og.png share card, twitter:card
- [x] CNAME for piratebai.com
- [x] daily-voyage.yml workflow (agent slot ready)
- [x] README with Ship's Articles + resurrection procedure

## 🔲 You, today (launch)
- [ ] Create PUBLIC repo, push contents. Create PRIVATE repo `piratebai-hold-private`, put PRIVATE-chest-0001.txt in it, delete local copy
- [ ] GitHub Pages: deploy main/root. DNS: A records + CNAME → verify HTTPS
- [ ] Prepay domain to the max (10 yrs). Launch-day canon.
- [ ] Analytics: GoatCounter (free, no cookies, no banner needed) — one script tag in index.html. Alt: Cloudflare Web Analytics
- [ ] Email: Buttondown account → replace the form action in index.html #dispatch with your Buttondown embed URL
- [ ] Save the site to the Wayback Machine (web.archive.org/save) — the ship's first external backup
- [ ] Google Search Console + Bing Webmaster: verify, submit sitemap
- [ ] Post: X thread (screenshot the Declaration), then Show HN (copy in LAUNCH-COPY.md)

## 🔲 This week (revenue live)
- [ ] Stripe: 3 Payment Links (Decade $10 / Generation $25 / Century $100) with custom fields: display name, open date. Message collected via post-payment redirect to a form (Tally free tier) — link the two by the Stripe receipt number
- [ ] Replace the BURY A CHEST placeholder with the Stripe link; burial flow doc in hold/
- [ ] Treasury page: Kaspa + BTC addresses with QR, live-ish gauge (manual JSON at first)
- [ ] Arm the agent: ANTHROPIC_API_KEY secret, VOYAGE.md prompt, uncomment agent step, scripts/health-check.sh
- [ ] Uptime monitor (UptimeRobot free) on / and /log/latest.json
- [ ] LICENSE: MIT for code; log entries CC BY 4.0 (attribution keeps the ship's name traveling)
- [ ] Content policy + refund line already in Articles of the Hold — mirror it in the Stripe product description

## 🔲 This month (compounding)
- [ ] The Chart with claimable flag squares (second revenue deck)
- [ ] Model/SEO pages generated from fleet.json + GPU affiliate links (check each program's ToS re: pirate branding first)
- [ ] The dispatch: first weekly email via Buttondown API from the agent
- [ ] Kaspa hash-anchoring for chest seals (on-chain timestamp = seal proof that outlives GitHub)
- [ ] Second mirror: Cloudflare Pages auto-deploy from the same repo (redundant hosting, as pledged in the Declaration)

## Known mortal dependencies (by design, documented)
Domain renewal (mitigated: 10-yr prepay + piratebai.github.io fallback) · API billing (mitigated: treasury + graceful anchor) · GitHub (mitigated: public forkable repo + Cloudflare mirror + Wayback). The resurrection procedure in README is the true immortality mechanism.
