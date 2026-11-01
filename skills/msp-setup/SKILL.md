---
name: msp-setup
description: >
  Guided first-run setup for the MSP Operations Kit. Use this skill whenever the user wants to set
  up, customize, personalize, or get started with the kit or its skills: "set up the kit", "help me
  customize these skills", "make these skills mine", "replace the placeholders", "finish setup",
  "resume setup", "am I ready to use this with clients", or any first-run intent after purchase.
  Also trigger when another msp skill surfaces an unfilled placeholder token or an unreviewed
  example default, since that means setup is incomplete. Works through msp-brand first, then
  msp-pricing, then every skill's Setup Decisions, and finishes with a readiness check.
---

# MSP Operations Kit: Guided Setup

This skill turns the kit from a template into the user's own operating system. It interviews the
user for their facts, writes those facts into the skill files, and tracks progress so setup can
happen across multiple sessions. Nothing in the kit should go client-facing until this skill's
final check passes.

## Before anything: work in the source folder, and back it up

Installed skills are read-only. Setup must run against the user's downloaded kit folder (the one
containing `skills/`), editing the source files there. Confirm the kit folder location with the
user before making any edit. If they only have installed copies and no source folder, stop and
help them get the kit files into a working folder first.

Before Phase 1 touches anything, make a backup copy of the whole kit folder (or commit it to git
if the user uses git). Phase 1 bulk-edits over twenty files; the backup is the undo button.

At the end of every phase, remind the user to reinstall the plugin or re-upload the changed
skills so the installed copies match the source folder.

## The canonical token list

These are all thirteen placeholder tokens used across the kit. This list is the single source of
truth for what to collect and propagate:

{{COMPANY_NAME}}, {{COMPANY_LEGAL_NAME}}, {{TAGLINE}}, {{DOMAIN}}, {{INFO_EMAIL}},
{{SUPPORT_EMAIL}}, {{SUPPORT_ALIAS_EMAIL}}, {{PHONE}}, {{STATE}}, {{SERVICE_AREA}},
{{OWNER_NAME}}, {{TIMEZONE}}, {{COMPANY_SLUG}}

Note: {{SUPPORT_EMAIL}}, {{SUPPORT_ALIAS_EMAIL}}, {{OWNER_NAME}}, and {{TIMEZONE}} do not appear
in msp-brand itself; they live in the operational skills. Collect them in Phase 1 anyway.

**Hard rule for every search and replace in this process: exclude `msp-setup/SKILL.md` (this
file). It intentionally contains token names and check phrases as instructions; editing it or
counting it in searches breaks the process.**

## Progress tracking

Keep a `SETUP-STATE.md` in the kit root. Create it on first run:

```
# Setup State
- [ ] Phase 0: Backup made
- [ ] Phase 1: Identity (msp-brand and tokens)
- [ ] Phase 2: Pricing cost model (msp-pricing, all five files plus script)
- [ ] Phase 3: Setup Decisions sweep (all other skills)
- [ ] Phase 4: Attorney review (msp-legal, external)
- [ ] Phase 5: Readiness check
```

On every run, read it first and resume at the first unchecked phase. Record every decision and
every deferral in it as you go. Mark a phase done only when its exit condition is met. One phase
per sitting is fine; never rush the user.

## Rules for the whole process

- Ask for facts; never invent them. If the user does not know a value yet, leave the placeholder
  or example default in place and log it in SETUP-STATE.md as a deferral with the date.
- Show the shipped example default with every question so the user can accept or override it.
  Accepting a default is a valid answer; record that it was reviewed.
- **Numeric sanity rule:** whenever the user supplies a rate, minimum, fee, or price, compute its
  gross margin against their own loaded costs (from Phase 2, or ask for costs first if pricing
  has not run yet) before writing it in. Challenge anything below their stated margin floor, with
  the arithmetic shown. Never silently record a number that loses the user money by their own
  model.
- Make the edits for the user. Do not hand them a list of find-and-replace chores.
- No em dashes in anything written into the kit.

## Phase 1: Identity

Interview for the brand facts, then write them in.

1. Ask for values for all thirteen tokens: company name and legal name, tagline (offer to help
   write one), domain, general email, support email and any alias, phone, state or jurisdiction,
   service area, owner name, timezone (ask for the client-facing form they use, like
   "Central Time"), and a company slug for file names (lowercase letters, numbers, and hyphens
   only, for example `acme-it`; see msp-brand section 4).
2. Fill in `msp-brand/SKILL.md` completely: the fill-in tables (colors, fonts, logos; help the
   user choose if they have no brand yet), voice examples, and the target-client description.
   Delete example rows once real values exist; if a section is deferred, keep its example rows
   and mark them "deferred [date]" so the readiness check can tell a logged deferral from an
   untouched template.
3. Propagate: replace every occurrence of each token across all of `skills/` except this file.
   Find them by searching for the double-brace pattern. Two traps:
   - `msp-pricing/scripts/price_quote.py` takes its company name from the `COMPANY_NAME`
     constant near the top of the file; set it there and confirm no other token remains in the
     script.
   - {{SERVICE_AREA}} appears in different grammatical frames ("serving businesses ..." versus
     "in ..."). After replacing, read each affected sentence and fix the grammar.
4. Ask the user to drop logo files into `msp-brand/` and record the filenames in the logo table
   (or log as a deferral).

Exit condition: a search for the double-brace pattern across `skills/` (excluding this file)
returns only tokens the user explicitly deferred, and those are listed in SETUP-STATE.md.

## Phase 2: Pricing cost model

The shipped rates are one MSP's numbers in one market. Rebuild all five pricing files plus the
script; msp-pricing is deliberately not part of the Phase 3 sweep because it needs this deeper
treatment.

1. Work through msp-pricing's full Setup Decisions list, covering every file: labor wages and
   burden (`references/labor-rates.md`), margin targets and cost model (`references/cost-model.md`),
   the break-fix rate card (`references/break-fix-rates.md`), support-hour assumptions
   (`references/support-hours.md`), and the engagement minimum, term ladder, escalator, license
   markup, and after-hours multipliers (`SKILL.md`). Apply the numeric sanity rule to every
   number the user supplies.
2. Write the user's values in, then update the constants in `scripts/price_quote.py` to match.
3. In `labor-rates.md`, replace or clearly annotate the source MSP's wage-research citations;
   the user must not ship another shop's research presented as their own market data.
4. Regenerate derived content from the script instead of hand-editing it: run `price_quote.py`
   and rebuild `cost-model.md`'s worked example and any margin tables from its output.
5. Consistency pass: confirm the script constants, cost-model catalog, break-fix card, and
   SKILL.md prose (including the Setup Decisions bullets that quote example figures) all state
   the same numbers. The AI adoption prices in SKILL.md are derived from the break-fix card
   (hours times the managed, non-contract, and floor rates); re-derive them whenever the card
   changes. Fix any stragglers.
6. Review the output with the user: do the floor, anchor, and start numbers look like prices
   they would actually quote? Check the break-fix card's margin math against their loaded costs
   explicitly; the script does not price hourly work.
7. Flip the "Defaults you must review" note in `msp-pricing/SKILL.md` and in each of the four
   reference files to "Defaults reviewed and set by [owner name], [date]".

Exit condition: the script runs clean on the user's numbers, the consistency pass finds no
disagreements, and all five pricing notes are flipped.

## Phase 3: Setup Decisions sweep

Go skill by skill in this order: msp-helpdesk, msp-maintenance, msp-security, msp-client-comms,
msp-onboarding, msp-offboarding, msp-qbr, msp-metrics, msp-sales, msp-marketing, msp-social,
msp-leadgen, msp-ai-adoption, msp-website-setup, and last msp-legal (partially; see below).

For each skill, work its Setup Decisions one at a time: state the question, show the shipped
example default, take the user's decision (sanity rule applies to any number), and write it into
the skill body wherever that value appears, not just the Setup Decisions list. Also check the
skill's `references/` files: some carry their own Setup Decisions sections (for example
`msp-legal/references/playbook-positions.md`). When a skill's decisions are all settled, flip its
"Defaults you must review" note to "Defaults reviewed and set by [owner name], [date]".

For msp-legal, settle only the items that are the user's own operating choices (venue county,
insurance preferences, which documents they will use). Everything that is a legal position stays
open for Phase 4, and msp-legal's note is NOT flipped here; it flips only when the attorney
review is done.

For msp-security, settle Setup Decisions 1 through 7 here. Decision 8 (the state law section of
`msp-security/references/compliance-overlays.md`) is an attorney item: leave it for Phase 4, and
do not flip that reference file's note until it is filled in. If Decision 1 changes the EDR,
SIEM, or MDR default, update msp-sales and msp-pricing to match in the same sitting.

For msp-ai-adoption, settle Decisions 1, 2, 5, and 6 here. Decisions 3 and 4 (the individual
engagement letter and the AI Use Policy template) are attorney items: leave them for Phase 4;
the skill's note may be flipped once 1, 2, 5, and 6 are settled. Write the Decision 6 public name into every client-facing place that names the AI project (msp-sales, msp-pricing, and the msp-marketing AI call to action).

**Project-offering opt-out list.** If the user does not offer one of the project offerings
(msp-sales Setup Decision "Project offerings"), remove it everywhere in the same sitting:
- AI adoption: msp-sales (About This Business project offerings, section 10, the Project
  Offerings table in `references/service-catalog.md`, the AI Adoption Project section in
  `references/service-descriptions.md`), msp-pricing ("Project Offering: AI Adoption" and its
  pointer in `references/break-fix-rates.md`), msp-marketing (the AI call to action in
  `references/cta-library.md`, the AI basics workshop paragraph in
  `references/channels-and-tactics.md`, and the exclusions rule mention), and msp-qbr (the AI
  project progress line in the prep list); keep msp-ai-adoption for internal use or delete it.
- Website builds and Website Care: msp-sales (core stack, project offerings, section 10,
  `references/service-catalog.md` rows, and the vendor wrangling line in
  `references/service-descriptions.md`; move website builds to the Deliberately NOT sold list),
  msp-pricing (the Website Care building block, the websites section, the break-fix-rates
  pointer), msp-legal (the stack tree and table rows, `references/document-stack.md` entry 13
  and quick selector 9 and 10), msp-marketing (exclusions rule and
  `references/rewrite-playbook.md`), msp-leadgen (`references/research-playbook.md` website
  clue), msp-onboarding, msp-offboarding, msp-maintenance (Website Care section and domain
  renewal line), msp-helpdesk (website ticket category), and msp-metrics (Care as MRR). Keep
  msp-website-setup if the user still builds sites for their own use, but remove its Website
  Care and client-paper content (the Phase 0 table and bullets, and "Taking Over an Existing
  Site").
- For either offering, also update the below-minimum wording so it offers only what the user
  still sells: msp-sales `references/objection-handling.md` (Objection 4), the msp-pricing
  engagement-minimum bullet, and the guardrail string in msp-pricing `scripts/price_quote.py`.

Exit condition: every skill's decisions are settled or logged as deferrals, and every note
except msp-legal's and msp-security's compliance-overlays note is flipped.

## Phase 4: Attorney review

This one cannot be done inside the kit. The positions in msp-legal and the contract templates in
`templates/` are one MSP's negotiated stances, not legal advice. The user takes them to an
attorney licensed in their state before anything governs a real client relationship. Record in
SETUP-STATE.md who they are sending it to and when. The same review fills in the state law section
of `msp-security/references/compliance-overlays.md` (msp-security Setup Decision 8). If the user
offers the project offerings, have the attorney also draft, in the same engagement, the website
documents (msp-legal document-stack entry 13), the individual engagement letter, and the AI Use
Policy template (msp-ai-adoption Decisions 3 and 4). When the user confirms the review is done, write in the attorney's answers, flip msp-legal's note and the
compliance-overlays note, and mark the phase.

## Phase 5: Readiness check

Run the full check and give a verdict. Every search excludes `msp-setup/SKILL.md`.

1. Search `skills/` for the double-brace pattern: zero hits, or only logged deferrals.
2. Search `skills/` for "Defaults you must review": zero unflipped notes remain.
3. Search msp-legal and the `templates/` docx files (extract their text) for square-bracket
   configuration placeholders that are one-time setup values rather than per-client fill-ins
   (for example a "[county]" venue): all set or logged as deferrals. Per-client brackets like
   "[Client legal name]" stay.
4. msp-brand has no example rows left except ones marked "deferred [date]", and its logo table
   points at real files or a logged deferral.
5. Phase 4 is done, or the user accepts the risk in writing in SETUP-STATE.md.
6. Spot-generate one client-facing artifact (for example, a welcome email from msp-onboarding
   plus a quote from msp-pricing) and have the user confirm it reads as their company, with no
   visible placeholders.
7. Confirm the installed skill copies match the source folder (reinstall now if any phase's
   changes were never reinstalled).

If everything passes, write "Setup complete, [date]" at the top of SETUP-STATE.md and tell the
user the kit is client-facing ready. If not, the remaining items are the punch list; log them in
SETUP-STATE.md and pick them up next session.
