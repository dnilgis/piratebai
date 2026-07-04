# Chest fulfillment runbook (manual, until the agent takes over)

When a burial payment lands (Stripe email) + message arrives (Tally):
1. Match them by the buyer's email / receipt number.
2. Sanity-read the message against the Articles of the Hold
   (illegal / harmful / doxxing → refund in Stripe, reply kindly, done).
3. Save message EXACTLY as received to a local file (byte-exact — the hash
   seals these bytes; don't fix typos, don't trim whitespace).
4. From the public repo root:
   python3 scripts/bury.py --message msg.txt --name "Their Name" \
       --opens YYYY-MM-DD --tier decade|generation|century --founder
   (--founder for the first 100 chests)
5. Commit + push public repo. Save plaintext to the PRIVATE repo as
   chests/chest-NNNN.txt, commit, push. Delete local copies.
6. Reply with their ledger link + hash: "Yer chest is sealed. Verify it
   yerself: sha256sum your message and match the ledger."
SLA to hold yourself to: sealed within 24 hours of payment.
