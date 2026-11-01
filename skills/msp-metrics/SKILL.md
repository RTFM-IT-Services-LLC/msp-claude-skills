---
name: msp-metrics
description: >
  Use this skill whenever measuring or judging your MSP's business health or a client
  relationship: MRR, margin or profitability per client, effective hourly rate, "are we making
  money on [client]", tickets per user, SLA attainment, churn, aged receivables, revenue
  concentration, the monthly owner review, the underlying numbers behind the client health
  scorecard (msp-qbr owns the client-facing scorecard document), or any version of "should we
  fire this client" or "this client is a problem". Also trigger when building dashboards, review
  sheets, or reports about the business. Apply alongside msp-pricing (the cost model and floor
  that give the numbers meaning), msp-helpdesk (ticket hygiene is the data source), msp-qbr
  (where client-facing consequences land), msp-client-comms (the repricing letter), msp-legal
  (waivers and exits), and msp-offboarding (the exit path).
---

# {{COMPANY_NAME}} Business and Client Health Metrics

This skill is the source of truth for the small set of numbers {{COMPANY_NAME}} actually
watches, and for the framework that turns a bad number into an action. It is a monthly half-hour
discipline, not a BI project. The point of every number below is a decision: reprice, remediate,
require, or exit.

**The data honesty rule comes first:** every figure here is computed from your PSA (ticketing)
system's ticket time entries and agreement data. The msp-helpdesk hygiene rules (no work without
a ticket, same-day time entries) are what make these numbers real. When a margin looks
implausibly good, check the time entries before celebrating.

**Writing form:** the monthly owner review write-up, client health notes, and reports follow
msp-technical-writing in flavored mode (Zone 1). A client-facing consequence, such as a
repricing letter, belongs to msp-client-comms and msp-brand.

**Files:** every file (the filled monthly review sheet, a report, a client health note) follows
msp-brand section 4 (Document Versioning). Example:
`{{COMPANY_SLUG}}-monthly-review-october-2026-11-02-v1.0.xlsx`.

**Defaults you must review:** the specific numbers in this skill are shipped example defaults
from a working MSP. Review and replace them with your own before anything goes client-facing.

---

## The Monthly Owner Review (30 minutes, first week of the month)

Walk the same sheet every month.

**1. MRR and delta.** Total monthly recurring revenue, plus what moved: seats added or removed,
clients gained or lost, repricing that took effect. Website Care fees are MRR, and a Care-only
client counts as a client. Flat MRR with rising seat counts means
someone is being under-billed; check Change Order follow-through (msp-onboarding flags count
deltas, this review confirms they got papered).

**2. Effective hourly rate per client.** Monthly fee divided by hours logged that month. This is
the single most honest per-client number. Judge it against the cost basis and floor in
msp-pricing's cost model rather than a figure restated here; the working question is "is this
client paying above, near, or below the floor-equivalent rate for the labor they consume?" One
bad month is noise (a big project month, an incident); a bad quarter is a pattern.

**3. Tickets per endpoint per month.** The denominator is managed endpoints, not users:
account-only users (msp-onboarding) have no endpoint and are excluded, so when someone says
"tickets per user," translate to this metric before comparing to any benchmark. Industry
research puts an average MSP at 0.75 to 1.0 tickets per endpoint per month (industry data) and
top performers at 0.2 to 0.5 (industry data). A client sustained above roughly 1.5 (example
default flag; set your own) has one of three problems, each with its own fix: a broken
environment (fix: remediation project), a behavior pattern (fix: a conversation, sometimes
training), or a price that never accounted for their reality (fix: reprice). Figure out which
before acting.

**4. SLA attainment.** Performance against the msp-helpdesk targets, overall and per client.
This is also the number that makes the QBR honest.

**5. Aged receivables.** Anything past 30 days gets named, gets an owner, and gets a next
action. Unpaid invoices age worse than any other business problem.

**6. Capacity check.** Hours logged per tech against roughly 140 available hours per month each
(example default; adjust to your own working-hours assumption). Sustained utilization above 80%
is the "when do we hire tech three" trigger, and it should be caught here, not when the SLA
starts slipping. The monthly review spreadsheet (`templates/msp-monthly-review.xlsx` in the kit) computes this for
you.

**7. Pipeline glance.** The msp-sales stages in one minute, so delivery capacity and sales
promises stay one conversation. A month with two closings coming and a red-EHR client consuming
a tech is a staffing conversation this review should catch early.

Also on a standing cadence, once real data accumulates: the support-hour estimates behind the
price sheet get revisited against actual ticket data about a year in (a standing note in
msp-pricing). This review is where that data quietly accrues.

---

## Client Health Scorecard (quarterly, feeds QBR prep)

Green, yellow, red per client across five dimensions. Internal only; it informs the QBR, it does
not appear in one.

| Dimension | Green looks like | Red looks like |
|---|---|---|
| Profitability | EHR comfortably above the floor-equivalent | Below floor two consecutive quarters |
| Ticket load | In or under the benchmark band | Sustained well above, no project underway |
| Payment | On time | Chronic lateness, broken promises |
| Security posture | Takes core recommendations | Stacking declined recommendations and waivers |
| Relationship | Respects scope and the team | Scope creep as habit, or mistreats staff |

---

## Fire or Fix

Default order: **fix first, exit second.** Most bad clients are mispriced, misconfigured, or
misinformed before they are truly bad. But the exit option existing, genuinely, is what makes
the fixes credible.

- **Underpriced (red profitability two consecutive quarters):** reprice. The conversation
  happens at the QBR (msp-qbr), the letter and mechanics run through msp-client-comms and
  msp-legal. If they refuse the new price and the math stays red, exit; a client below floor is
  you paying for the privilege.
- **Environment-driven ticket load:** quote the remediation project (msp-pricing). A client
  drowning in tickets from a dying server is a project prospect, not a firing candidate.
- **Refuses baseline security:** written Risk Acceptance Waiver at minimum (msp-legal; use a
  plain confirmation email until you have a template). The MSA's ransomware cost allocation has
  a negligence carveout, so undocumented client refusals are you holding risk you never agreed
  to hold. A client whose refusals create existential risk for you is an exit candidate no
  matter how well they pay.
- **Chronic late payment:** move them to prepay or autopay as a condition of continuing. If
  that fails, exit; the attorney path handles collection, never data or access leverage
  (msp-offboarding's rule).
- **Abusive to the team:** one direct conversation with the owner, then exit. This one moves
  faster than the others on purpose. The team watching how the owner handles it is part of what
  is being decided.

Every exit runs through msp-offboarding with the longer, gracious runway. Fired clients still
talk about you at their chamber of commerce.

---

## Annual Checks

- **Revenue concentration:** any client above 25 percent of MRR (example default) is a
  structural risk worth saying out loud and planning around, however pleasant the client. Note:
  with fewer than about six clients this flag trips by arithmetic alone; treat it as
  aspirational until then rather than letting it train you to ignore flags.
- **Price review:** costs against the sheet (the labor-rates levers in msp-pricing), feeding
  any needed increase letters with proper notice.
- **Churn review:** the year's loss reasons from msp-offboarding logs, read for patterns.

## Setup Decisions

Values below are the shipped example defaults from a working MSP. Decide your own before this
goes live.

- Two consecutive quarters below the floor-equivalent rate triggering the repricing conversation
  ships as the example default.
- Sustained ticket load above 1.5 tickets per endpoint per month flagging a problem client ships
  as the example default. The 0.75 to 1.0 industry band and the 0.2 to 0.5 top-performer band
  above are industry data, not a choice to change; the 1.5 flag threshold is yours to set.
- The revenue concentration flag at 25 percent of MRR ships as the example default.

The monthly review spreadsheet ships in the kit at `templates/msp-monthly-review.xlsx`; update
its threshold cells once you have settled your own thresholds above.
