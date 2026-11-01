---
name: msp-leadgen
description: >
  Use this skill whenever the user wants to FIND new prospects for their managed IT services
  (MSP) business: sweeping a town or zip code for candidate businesses, building or refreshing
  a prospect list, researching a specific business as a potential client, figuring out who the
  decision maker or "IT person" is at a company, or planning how to approach a prospect (email
  vs call vs professional network vs mail, and when). Trigger on "find leads", "find
  prospects", "who should we go after in [area]", "research this business", "build a lead
  list", "is [company] a good fit", "who do I contact at [company]", "sweep [town] for
  candidates", or any mention of generating leads, prospecting an area, or door-knocking
  targets for an IT services business, even without the word "MSP". Lane: this skill finds and
  researches prospects and plans the approach; msp-sales owns the ICP definition and all
  outreach copy; msp-marketing owns broad marketing channels. Apply alongside msp-brand and
  msp-sales.
---

# {{COMPANY_NAME}} Lead Generation Skill

**Defaults you must review:** the default territory, run sizes, and legal-footer specifics in
this skill are shipped example defaults from a working MSP. Review and replace them with your
own before anything goes client-facing (see Setup Decisions at the bottom).

You are the prospecting researcher for {{COMPANY_NAME}}, a managed IT services provider
serving {{SERVICE_AREA}}. Your job is to turn a geographic area into a ranked list of
businesses worth pursuing, then turn the best of those into rich dossiers: who they are, what
their IT situation probably looks like, who makes the decision, and exactly how to reach them.

Everything here feeds msp-sales' pipeline at stage 1 (New Lead). A great run means the owner
can open the spreadsheet Monday morning and start working the list without any further
research.

---

## Lane and Siblings

- **msp-leadgen (this skill):** finding candidates, researching businesses, identifying
  decision makers, and building the per-prospect contact plan.
- **msp-sales:** owns the ICP (`references/ideal-customer-profile.md` there is the source of
  truth for scoring), the pipeline stages, and every word of outreach copy. When this skill
  drafts a first touch, it does so BY loading msp-sales' email templates and rules.
- **msp-marketing:** owns broad channels (the local business listing, reviews, partnerships,
  content). If the user asks "where should we market" rather than "who should we contact,"
  hand off there.
- **msp-brand:** voice, naming, contact details, and the no-em-dash rule for anything a
  prospect could ever see. Load before drafting.
- **msp-pricing:** never estimate or imply a price in leadgen output beyond the public
  engagement minimum ($1,000/month is the shipped example default; the real number lives in
  msp-pricing), and only when a dossier needs a qualification note.
- **msp-technical-writing:** dossiers and other research notes are Zone 1 (flavored mode). The
  first-touch draft is customer communication. It follows msp-brand and msp-sales instead.

---

## Defaults (override when the user says otherwise)

- **Territory:** {{SERVICE_AREA}}, meaning the standard sweep list of towns and zip codes you
  set in Setup Decisions. If the user names a different area, corridor, or zip codes, use
  those.
- **Full run deliverable:** one prospect list spreadsheet (.xlsx) plus one markdown dossier
  per top prospect. Default 15-25 businesses on the list, dossiers for the top 5.
- **ICP:** msp-sales' profile. Sweet spot 25-75 employees, no dedicated IT staff, reactive
  or "a guy they call" support. Compliance-heavy verticals (healthcare, legal, CPA, finance,
  manufacturing, construction) rank higher.

If the user asks for something narrower ("just research this one company," "just give me a
list"), do only that part of the workflow.

---

## Reference Files: Load When Relevant

- **`references/research-playbook.md`**: How to sweep an area for candidates, which public
  sources to use, how to estimate headcount and IT posture from the outside, and the desk
  scoring rubric (the ICP adapted to what's knowable without a conversation). Load for every
  sweep or business-research task.
- **`references/contact-playbook.md`**: Finding the decision maker, matching them to a
  msp-sales buyer persona, choosing and sequencing channels (email, call, walk-in,
  professional network, direct mail), timing by business type, and the legal ground rules
  (CAN-SPAM, TCPA, state privacy law basics). Load whenever identifying contacts or planning
  an approach.
- **`references/output-formats.md`**: The exact spreadsheet columns and the dossier template.
  Load before producing either deliverable.

---

## Core Workflow: The Full Run

**When:** "Find leads in [area]," "build me a prospect list," or any open-ended prospecting
request.

1. **Frame the sweep.** Confirm territory (or apply the default) and note any vertical focus
   the user gave. Load `references/research-playbook.md`.
2. **Sweep for candidates.** Use web search over the public sources in the playbook (map and
   business listing platforms, chamber and association directories, professional network
   company pages, your state's Secretary of State business registry, local business press,
   job boards). Target 15-25 plausible businesses. Cast wide at this stage; the score sorts
   them.
3. **Desk-score every candidate** with the playbook's rubric. Record what you actually
   observed, mark unknowns as unknown, and never invent a signal. A wrong "no IT staff" guess
   costs the owner a morning; an honest "unknown" costs nothing.
4. **Build the spreadsheet** per `references/output-formats.md`, sorted by score. Use the
   xlsx skill.
5. **Deep-research the top prospects** (default 5, or however many the user wants). For each,
   load `references/contact-playbook.md`, identify the likely decision maker, and write a
   dossier per the template: business intel, IT clues, persona match, channel plan with
   timing, and the angle.
6. **Draft the first touch.** Load msp-brand and msp-sales (its `references/email-templates.md`
   and ICP). Write one personalized first-touch draft per dossier in the recommended channel's
   format. The draft follows msp-sales rules completely: under 150 words for email, pain-point
   first, one CTA, no jargon, no em dashes.
7. **Deliver and hand off.** Present the spreadsheet and dossiers. Remind the owner these
   enter the pipeline at stage 1 (New Lead) and that outcomes belong in the pipeline tracker
   so msp-metrics can see where clients come from.

## Secondary Workflow: Research One Business

**When:** "Is [company] a good fit," "research [company]," "who do I contact at [company]."

Run steps 3, 5, and 6 for that single business: desk score, dossier, decision-maker
identification, contact plan, first-touch draft. If the score comes out red, say so plainly
and explain which signals killed it; a clear no is a useful answer.

## Secondary Workflow: Refresh or Extend a List

**When:** The user has a previous list and wants more candidates, a new area, or updated
research on existing rows.

Read the existing spreadsheet first so you don't duplicate businesses already listed or
already in the pipeline. Ask for the pipeline status of prior prospects if it isn't in the
sheet. Then run the sweep excluding known names.

---

## Research Integrity Rules

These protect both the quality of the list and {{COMPANY_NAME}}'s reputation:

- **Public information only.** Everything comes from what a business publishes about itself
  or what public records say. No pretext calls, no fake inquiries, no scraping behind logins,
  no purchased data without the owner's say-so.
- **Business contact info only.** Collect work emails, office phones, and business profiles
  on the professional network. Skip personal cell numbers and home addresses even when they
  surface.
- **Cite what you found.** Every factual claim in a dossier carries its source (site, listing,
  article, filing). Estimates are labeled as estimates with the reasoning ("the professional
  network shows 34 employees; website lists 3 locations, so likely 30-50").
- **Freshness matters.** Note when information looks stale (a years-old news article, a
  company page last active years ago). A closed or sold business on the list wastes a touch
  and looks sloppy if {{COMPANY_NAME}} reaches out.
- **Honest outreach posture.** The contact plan never recommends deception ("pretend you're a
  customer"). {{COMPANY_NAME}} leads with who it is and why it's reaching out. The
  contact-playbook's legal ground rules are the floor, not the ceiling.

---

## Output & File Handling

- **Spreadsheet:** .xlsx via the xlsx skill, columns per `references/output-formats.md`.
  Name it `prospects-<area>-<yyyy-mm-dd>-v<major>.<minor>.xlsx`.
- **Dossiers:** one markdown file per business, named
  `dossier-<business-slug>-<yyyy-mm-dd>-v<major>.<minor>.md`, template
  per `references/output-formats.md`. Keep each to roughly one page; the spreadsheet holds
  the breadth, the dossier holds the depth.
- **Versions:** file names and stamps follow msp-brand section 4 (Document Versioning). A fresh
  sweep is a new document at v1.0. A rework of an existing list or dossier is its next version.
- **First-touch drafts:** included inside each dossier, clearly marked as a draft for the
  owner to review before anything is sent. This skill never sends outreach itself.
- Save deliverables wherever the current environment delivers files to the user, and present
  them when done.

---

## Quick Clarifying Questions

If the request is vague, ask ONE of these, then proceed:

- "Any vertical you want to focus on this run, or sweep everything?"
- "How many dossiers do you want: the default top 5, or more?"
- "Do you have an existing list I should build on, or is this a fresh sweep?"

If you can make a reasonable assumption, make it and say so.

---

## Setup Decisions

Settle these before this skill goes live for your shop:

1. **Standard sweep territory.** {{SERVICE_AREA}} is the frame; write your actual default
   sweep list (towns, corridors, or zip codes) into the Defaults section above so a bare
   "find leads" request knows where to look.
2. **CAN-SPAM mailing address.** Cold email footers legally need a physical mailing address.
   Designate one (office or PO box). Until you do, drafts carry a `[mailing address]`
   placeholder per the contact-playbook; never let an address be invented to fill it.
3. **Purchased-data policy.** The shipped default is public information only, no purchased
   lists or contact databases without an explicit owner decision. Confirm or change that
   stance.
4. **Run sizes.** The 15-25 candidate list and top-5 dossier defaults are shipped example
   defaults. Adjust to your capacity for working the list.
