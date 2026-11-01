# Output Formats: The Prospect Spreadsheet and the Dossier

Two deliverables, fixed formats. Consistency is the point: every sweep produces files that
can be merged, compared, and re-sorted later, and msp-metrics can eventually trace "where
did this client come from" back to a row.

---

## The Prospect Spreadsheet

Filename: `prospects-<area>-<yyyy-mm-dd>-v<major>.<minor>.xlsx` (e.g.,
`prospects-springfield-2026-08-01-v1.0.xlsx`). Version and stamp rules: msp-brand section 4.
Build with the xlsx skill. One row per business, sorted by score descending. Freeze the
header row; add a filter.

| Column | Content |
|--------|---------|
| Business | Legal/trade name |
| Vertical | One of: manufacturing, healthcare, dental, legal, CPA/accounting, finance, construction, professional services, other (specify) |
| City | Primary location |
| Est. employees | Number or range, with basis in Notes |
| Score | 0-100 desk score |
| Band | Green / Yellow / Red |
| Key signals | Comma list of scored signals observed (e.g., "no IT staff, hiring, HIPAA vertical") |
| Decision maker | Name and title, or "unknown, ask for office manager" |
| Contact info | Business phone, email, professional network profile URL as available |
| Primary channel | Recommended first-touch channel |
| Website | URL |
| Source | Where the candidate was found |
| Notes | Estimates and their basis, staleness flags, anything odd |
| Do not contact | Blank unless the business has opted out; respected by every future sweep |
| Status | "New" on creation; the owner maintains after that (maps to pipeline stages) |

Red-band businesses stay in the sheet with a one-line reason in Notes. A red row saves the
next sweep from re-researching them.

---

## The Dossier

Filename: `dossier-<business-slug>-<yyyy-mm-dd>-v<major>.<minor>.md` (e.g.,
`dossier-acme-dental-2026-08-01-v1.0.md`). One page. Written so the owner can read it in two
minutes before dialing. Use this exact structure:

```markdown
# [Business Name] Prospect Dossier
*Prepared [date] | Desk score: [n]/100 ([band])*

## Snapshot
Two or three sentences: what they do, where, roughly how big, how long established.

## Why Them (Scored Signals)
The signals that produced the score, each with its evidence and source. Estimates labeled
as estimates. Unknowns listed as unknowns worth confirming in discovery.

## IT Picture (Best Guess)
What their IT situation probably looks like from the outside: who handles it now (if
knowable), visible pain clues, compliance obligations their vertical implies. Clearly
framed as inference.

## Decision Maker
Name, title, persona match (per msp-sales), evidence for both, and how to reach them.
If unnamed: the honest path to getting a name.

## Approach Plan
- **Primary channel:** [channel] - [one line of reasoning]
- **Timing:** [when, per contact-playbook timing rules]
- **Sequence:** touch 1 → touch 2 (channel, +4-6 days) → touch 3 (channel, +1-2 weeks)
- **The angle:** the specific observed fact the outreach opens with
- **Watch out for:** gatekeepers, seasonal timing, incumbent loyalty, anything found

## First Touch DRAFT (review before sending)
The drafted first touch in the primary channel's format, written per msp-sales templates
and msp-brand voice.

## Sources
Bulleted list of every source used.

*[file name without .md, per msp-brand section 4]*
```

Keep the dossier honest about confidence. "The professional network shows no IT titles among
22 listed employees (checked [date])" is useful; "they have no IT support" is a guess dressed
up as a fact, and the owner will find out which on the first call.
