---
name: msp-qbr
description: >
  Use this skill whenever preparing, running, or following up a client business review:
  "QBR", "quarterly review", "business review", "account review", "prep for the [client]
  meeting", building a client scorecard, planning a client's technology roadmap or budget, or
  preparing the renewal and repricing conversation. Also trigger when someone asks how often to
  meet with clients or what to show them. Apply alongside msp-metrics (the numbers and the client
  health scorecard), msp-helpdesk (performance against targets), msp-pricing (any cost band shown
  to the client), msp-client-comms (the price letter and follow-up), msp-legal (waivers for
  declined recommendations), and msp-brand (anything the client sees).
---

# {{COMPANY_NAME}} Quarterly Business Reviews

This skill is the source of truth for how {{COMPANY_NAME}} runs recurring client business
reviews. The QBR is the retention engine: it is the meeting that makes {{COMPANY_NAME}} a
partner with a plan rather than a vendor who answers tickets. It is also the honest venue for
the roadmap, the budget conversation, and repricing. Clients rarely leave a provider who shows
up every quarter with their numbers, their risks, and a plan.

The QBR is never a sales pitch. Recommendations get framed as risk and outcome in the client's
own numbers, per the sales philosophy in msp-sales. Selling and serving are the same thing here
or the meeting dies.

**Defaults you must review:** the specific numbers in this skill are shipped example defaults
from a working MSP. Review and replace them with your own before anything goes client-facing.

---

## Cadence (example default)

- Quarterly for every managed client while the client count is small ships as the example
  default. The owner may flex the smallest accounts to twice a year as the count grows; until
  that decision is made, quarterly is the default.
- The first review lands about 90 days after go-live, built on the roadmap seeded by the 30-day
  review in msp-onboarding.
- 45 to 60 minutes, with the owner or decision-maker in the room. A QBR held only with a
  front-desk contact is a status call, not a QBR; reschedule rather than downgrade.

---

## Prep Checklist (about 45 minutes, the day before)

Pull from your PSA (ticketing) system and the stack:

- Ticket volume for the quarter, by category, and the top requesters
- Response performance against the msp-helpdesk targets
- Backup success rate and the monthly test-restore log (cadence per msp-maintenance)
- Patch compliance and endpoint protection status
- Security posture items: MFA coverage, open advisories, incidents this quarter, and open
  findings against the msp-security baseline
- Project status: done, in flight, proposed
- AI project progress, if the client bought it: what stuck, what did not, and the next tasks
  worth trying (msp-ai-adoption). If your public AI page promises this review to managed
  clients, keep that promise.
- Horizon items: warranty expirations, OS end-of-life dates, license renewals, hardware age
- Open recommendations, and any declined ones with their waiver status (msp-legal)
- The client's health scorecard from msp-metrics (internal; informs tone, does not get shown)

Then build the client-facing scorecard.

## The Scorecard

One page. Green, yellow, or red across five rows, each with a plain-English sentence.

| Area | What it answers for the owner |
|---|---|
| Backups | If the worst happened tomorrow, would your data come back? |
| Security | Are the doors locked: sign-ins protected, machines protected, staff alert? |
| Updates | Are your systems current, or is anything running unsupported? |
| Hardware | What is aging out, and when will it need money? |
| Support | How fast did we answer, and how much did your team need us? |

Score the Security row with the msp-security Green/Yellow/Red table.

Score honestly. A yellow that {{COMPANY_NAME}} flags itself builds more trust than a green that
quietly should not be; the client eventually learns the truth either way, and only one version
of that story has {{COMPANY_NAME}} as the one who said it first.

## Meeting Agenda

1. **Their business first (5 to 10 min).** What is changing: hiring, moving, new software, busy
   season. This is where scope changes surface early instead of as surprise tickets.
2. **Quarter in review (5 min).** The support numbers and what they mean. Keep it short; nobody
   hired {{COMPANY_NAME}} to admire ticket counts.
3. **Scorecard walk (10 min).** The five rows, plainly.
4. **Risks and recommendations (10 to 15 min).** For each: the risk in plain English, what fixing
   it looks like, a rough cost band from msp-pricing, and a clear recommendation. Never invent a
   precise number in the room; "roughly" plus a follow-up quote beats a guessed figure that
   becomes a promise. Declined security recommendations start the waiver conversation
   (msp-legal), gently: "I need us to write down that we suggested it and you passed, so we are
   both protected."
5. **Roadmap (10 min).** The next two to four quarters: refreshes, projects, budget shape. A
   budget the owner can plan around is one of the most valuable things {{COMPANY_NAME}} hands
   them all year.
6. **"What should we do better?" (5 min).** Ask it plainly, then be quiet and write down the
   answer.

**Repricing lands here.** When a rate needs to change, the QBR is where it is said out loud, with
the year's value on the table, followed by the formal letter per msp-client-comms and the notice
mechanics per msp-legal. A price change that arrives cold in an inbox costs trust the QBR exists
to build.

---

## Output and Follow-Up

- **Client-facing:** the one-page scorecard, branded per msp-brand. For most clients a clean
  one-pager beats a slide deck. If a deck is warranted (larger client, board audience), 8 slides
  maximum, built with the pptx skill on msp-brand formatting.
- **Follow-up within 2 business days:** a short email in msp-client-comms style listing
  decisions made, quotes to follow, and scheduled items. Decisions that live only in the meeting
  evaporate.
- **Internal:** log decisions, declined recommendations, and scope observations in your PSA
  (ticketing) system. Feed scope drift and health observations to msp-metrics; the QBR is where
  the fire-or-fix data gets collected in person.
- **File names and versions:** the scorecard and any deck follow
  msp-brand section 4 (Document Versioning). Example:
  `acme-dental-qbr-scorecard-q4-2026-11-01-v1.0.docx`.
- **Prose form:** internal prep notes are Zone 1 of msp-technical-writing (flavored mode). The
  client scorecard follows msp-brand. The description of what each fix involves is Zone 2.

## Setup Decisions

Values below are the shipped example defaults from a working MSP. Decide your own before this
goes live.

- **Cadence:** quarterly for every managed client ships as the example default. Decide your own
  cadence, and whether and when to flex smaller accounts to semi-annual.
- **Scorecard areas:** the five areas below (Backups, Security, Updates, Hardware, Support) ship
  as the standing default set.

The scorecard one-pager template ships in the kit at `templates/msp-qbr-scorecard-template.docx`; restyle it per msp-brand once your brand is set.
