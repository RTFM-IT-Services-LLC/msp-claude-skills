---
name: msp-pricing
description: >
  Use this skill whenever pricing or packaging a managed-services or break-fix engagement for
  your MSP: building a quote or proposal, deciding what to charge a prospect, assembling options
  for a client, working out a price band for negotiation, or sanity-checking margin on a deal.
  Triggers include "how much should we charge", "price this client", "put together options for",
  "what should I quote", "build a package for", "what's the floor on this deal", "per-user price",
  "how deep can we discount", "should this include on-site", or any mention of quoting devices,
  seats, servers, network gear, on-site visits, contract length, or monthly recurring revenue for
  an IT services deal. Also trigger when revising the price sheet or building blocks, or pricing
  a website or AI adoption project. Always load this skill before producing any number a client could see. Apply
  alongside msp-sales (value conversation), msp-brand (presentation), and msp-client-comms
  (price-increase letters).
---

# {{COMPANY_NAME}} Pricing

**Defaults you must review:** every dollar figure, margin, floor, anchor, and multiplier in this
skill is one working MSP's numbers in one market. Rebuild the cost model with your own labor
costs and license costs before quoting anything to a client. See `references/labor-rates.md` for
the wage research behind the loaded costs and the levers that re-cost the whole sheet, and
`references/support-hours.md` for the labor-hour assumptions behind every building block.

This skill is a configurator. It knows the building blocks {{COMPANY_NAME}} sells and what each
one costs, and it takes what you learn about a prospect and assembles a few custom options for
that specific client, each priced to protect margin. The options may look like tiers, but they
are built per client from set parts, and you sell them as "here is what I put together for you,"
not "here is our Gold plan."

The governing idea comes from an MSP industry pricing methodology (Package, Price, Profit) and
the trusted-advisor shift:
diagnose first, then prescribe. Cost-plus math is the floor under every number, never the answer.
Your costs tell you the lowest price you can survive on. The client's situation tells you the
highest price they will happily pay. The skill finds that ceiling and opens near it.

Apply this with `msp-sales` (the discovery that surfaces requirements and value factors, and the
conversation that delivers the number) and `msp-brand` (voice and formatting once a number reaches
the client).

---

## The Three Numbers

Every line, every option, resolves to a band with three reference points. Always compute all three.

1. **FLOOR**: the walk-away. Loaded cost times 2.128 (a 50% gross margin after the 3% payment
   fee). Never quote below this without owner sign-off. This is what stops fear-based discounting.

2. **ANCHOR**: the published standard. Loaded cost times 2.703, rounded up to the nearest $10 (a
   60% gross margin after the 3% payment fee). This is the honest, sustainable default and the
   basis of the contract ladder. Both multipliers carry the ~3% cost of accepting card payments,
   so clients pay however they like with no surcharge and no margin leak; see the cost model.

3. **START**: the opening ask. The anchor lifted by value factors specific to this prospect, capped
   at 40% over anchor so the first number is ambitious but not insulting.

You open at START, concede down the contract-length ladder, and stop at FLOOR. The realistic landing
is between the anchor and the contract price for the term they commit to.

Do not eyeball any of this. Run `scripts/price_quote.py`. See `references/cost-model.md` for the
math, the full building-block catalog with costs, and the standing decisions about the sheet. The
remote and on-site labor costs are built up from researched market wages (decent L1 phone tech, good
field tech) rather than flat guesses; `references/labor-rates.md` documents that research and the
levers that re-cost the sheet when wages or drive times change. The per-device labor-hour estimates
were checked against industry support-load benchmarks too; `references/support-hours.md` has that
research and the per-line verdicts (notably why a server is 1.5 hours, not 1.0).

---

## The Building Blocks

These are the set parts you assemble from. Full costs and prices are in `references/cost-model.md`;
this is the menu.

**Recurring, per user (monthly):** two kinds of user. A **workstation** is a full "account and
computer" user: a managed machine plus that person's support. An **account-only** user has a managed
account but no managed machine (BYOD staff and 1099 contractors): identity, password and MFA, account
security monitoring, and licensing. Account-only is lighter and priced well below a full user, so
support people who do not have a company computer without charging them like they do.

**Recurring, per device (monthly):** server, mobile device, network base fee, firewall or router,
switch, wireless access point, camera, printer (business-class, networked only), special software.

**Per-endpoint add-ons (load onto the devices that need them):** endpoint protection (EDR), ZTNA
(secure access), MDM small-business or MDM enterprise tier (Mac management). These are real costs;
loading them keeps the anchor honest instead of quietly eating margin. They do not apply to
account-only users, who have no managed endpoint.

**On-site support (monthly allowance):** a set number of on-site hours bundled into the monthly fee,
expressed to the client as visits ("about one visit a month"). The current sheet is remote-first, so
this is the block that lets you cover clients who need hands on site. On-site work beyond the
included allowance bills per incident at the managed on-site rate on the break-fix card
(`references/break-fix-rates.md`).

**Website Care (monthly, optional):** {{COMPANY_NAME}} manages a client's website hosting, domain,
and DNS in a hosting account in the client's own name. It is a managed line item with its own
Service Order, term ladder, and tiers, and it can be the only thing {{COMPANY_NAME}} manages for a
client. It does not run through the configurator; numbers are in "Websites: Builds and Website
Care" below.

**One-time:** onboarding and migration, always quoted separately from the monthly using break-fix
rates. Never absorb the cost of moving a client onto your stack. Website builds are one-time
projects priced in "Websites: Builds and Website Care" below.

---

## How to Build and Price a Client's Options

**Step 1: Gather requirements, not guesses.** From discovery you need the headcount split (how many
full users with a company computer versus how many account-only BYOD or contractor users), device
counts (servers, mobile, and each kind of network device), the OS mix (any Macs to manage), the
security and compliance picture, and what on-site expectations they have. A wrong count quietly
breaks the margin, so ask rather than assume. The `msp-sales` discovery framework drives this.

**Step 2: Select blocks against the requirements.** Map what they need to the building blocks:

- Each user with a company computer is a workstation; each BYOD or 1099 contractor who only needs a
  managed, secured account is an account-only line. Set the per-client headcount to the sum of both.
- Macs in the fleet pull in an MDM block.
- A regulated industry or a cyber-insurance requirement pulls in ZTNA and the compliance value
  factor.
- A real need for hands on site pulls in an on-site allowance.
- Servers, cameras, special software: include only what they actually run.
- Endpoint protection (EDR) belongs on essentially every managed computer (not account-only
  users).

**Step 3: Assemble two or three options.** Not standard tiers: options you built for this client.
A workable shape is a lean option (the minimum that responsibly covers them), a recommended option
(what a sensible owner in their situation should choose, and where you want them to land), and a
fuller option (everything that genuinely fits, which also makes the recommended one look reasonable).
Mark the recommended option so the configurator anchors on it. Keep the options honestly different in
what they include, never in response time.

**Step 4: Score value factors per option.** Flag a factor only when discovery actually surfaced it.
These lift the opening ask because the prospect's situation makes a stable, secure environment worth
more to them than the average client.

| Factor | Uplift | Flag it when |
|--------|--------|--------------|
| Compliance | +20% | Regulated data: healthcare/HIPAA, payment/PCI, financial, legal |
| Downtime sensitive | +15% | An hour of downtime is measurable lost revenue |
| Security pressure | +12% | A cyber-insurance mandate or a recent scare is driving the talk |
| Power users | +12% | Specialized software, heavy workflows, high support volume |
| High pain | +8% | Acute pain, weak or absent incumbent, urgency to move |

Manufacturing factors to inflate the number is transparent and costs the deal. The +40% cap keeps the
opening honest.

msp-security Tier 2 items (quoted per client) and security remediation projects found in an
assessment are priced here, as add-ons or SOW projects. Tier 1 baseline controls are part of the
managed fee and are never itemized as extras.

**Step 5: Run the configurator.** Write a small JSON file describing the client and the options,
then:

    python3 scripts/price_quote.py --packages client.json

It prices every option (floor, anchor, contract price for the term, opening START, per-user, margin
at every line) and prints a side-by-side. For a quick one-off check, the CLI flags work too:

    python3 scripts/price_quote.py --workstation 24 --mobile 5 --server 1 --users 25 \
        --years 3 --edr --ztna --onsite-hours 2 --compliance --downtime-sensitive

**Step 6: Present the options, then stop talking.** Lead with the recommended option, open at its
START, and let silence do its work. "For everything we set up here, it is $X a month." Full stop. If
they push back, ask a question before touching the price. Do not pre-discount, do not apologize for
the number. The contract ladder is how you reward a longer commitment, not a reflex give-away.

---

## Standards and Minimums (do not break without owner sign-off)

- **One year is the minimum term, so the 1-year price is the highest price you ever show.** There is
  no month-to-month or sub-year rate. Every quote presents a term ladder with the 1-year at the top,
  and longer terms (2, 3, and 5 years) stepping down beneath it. State this in plain words on the
  quote: the highest price shown is the one-year term, and committing longer locks in a lower
  monthly rate. Never let a client believe there is a cheaper short-term option, because there is
  not.
- **Marketing carries no prices.** The only public number, in marketing material of any kind, is
  the $1,000/month engagement minimum (example default; see msp-sales presentation rules).
  Anchors, ladders, and per-user figures appear only in quotes and live conversations, after
  discovery. Published package pricing invites price shopping and commoditization.
- **50% gross margin is the floor**, on every line and every option, including on-site, measured
  after the 3% payment-processing skim that is baked into the multipliers.
- **Payment processing is baked in.** Clients pay by any method with no surcharge; a 3% processing
  cost is built into every price. Never add a card fee or convenience fee line to a quote, and never
  offer a "cash discount" -- the price is the price.
- **The contract ladder never breaks the floor.** Each year of commitment beyond the first removes 4%
  of the client's 1-year opening price (the START when value factors apply, otherwise the anchor;
  this matches what price_quote.py actually computes), so a five-year deal is 16% off and still
  comfortably above the floor. The
  discount is a real incentive to commit, deliberately tuned so longer terms never push you into
  thin margin. (Five percent per year is the absolute ceiling; it would land the five-year price
  a hair above the floor with no useful buffer, so 4% is the standing choice.)
- **Engagement minimum is $1,000/month.** Below this a managed client costs more attention than it
  returns. Re-scope or raise it. If the client cannot clear it, do not sell managed IT. Offer
  projects (the AI adoption project, a website) and Website Care, which can stand alone below the
  minimum.
- **Response time never varies by option or by price.** Differentiate options by what is included and
  how proactive you are, never by how fast you answer. Every client gets your best response.
- **Onboarding and migration are billed separately**, always, at the managed-client rates on
  the break-fix card (`references/break-fix-rates.md`).
- **Onboarding fee waiver.** The onboarding SOW fee may be discounted 50 to 100% as a
  closing incentive, only when the client signs a Service Order with at least a
  one-year term on or before the SOW date, and only with the clawback in the Service
  Order (waived amount becomes due on early termination, except for Provider's
  uncured material breach). The fee is still quoted in full on the SOW; the waiver is
  a stated discount against it, never a silent absorption. Anything outside these
  conditions needs owner sign-off.
- **After-hours hourly work bills at 1.5x and holiday work at 2x.** This skill is the owning
  source for both multipliers; msp-legal (the MSA states them) and msp-helpdesk (the desk
  applies them) both defer here. Never invent or waive multipliers ad hoc. They multiply the
  hourly rates on the break-fix card (example default: managed $110 remote / $220 on-site,
  non-contract $150 remote / $220 on-site).
- **There is no retainer rate.** The old $120/hr on-site courtesy is retired everywhere. Managed
  clients get managed hourly rates, non-contract callers get non-contract rates, nothing bills
  below the floor.
- **Multi-year terms carry a 3% annual escalator** (example default). On each anniversary
  after year one, the monthly fee increases 3%, stated plainly in the Order so it is never a
  surprise letter. The ladder discount is real and so is wage drift; the escalator is what lets
  both be true.
- **Third-party licenses bill at cost plus 15%** (example default), presented as a single
  line covering procurement, license management, and vendor liaison. Never quote licenses at
  bare cost, and never break out the markup as its own line.
- **You control the stack.** Pricing assumes your tools. A client who insists on theirs is buying
  custom work: quote it higher or decline.

---

## Websites: Builds and Website Care

The numbers in this section are shipped example defaults, like everything else in this skill (see
Setup Decisions).

{{COMPANY_NAME}} builds simple static websites and manages the client's own hosting.
{{COMPANY_NAME}} never hosts a client site in its own account: every site runs on your static
hosting platform in a hosting account in the client's name (most small sites fit the platform's
free plan), with {{COMPANY_NAME}} as an administrator. The build process and ownership model live
in msp-website-setup; the paper lives in msp-legal (document-stack entry 13).

After launch the client picks one of two paths, the same split as the rest of the business:
**Website Care** (managed, monthly fee) or **break-fix** (hourly when they need something).

**Build (one-time, Website Development SOW)**

| Item | Price |
|---|---|
| Site setup and launch (domain, DNS, hosting setup, SSL, deployment) | $300, waived when the client signs a Website Care Service Order with at least a one-year term on or before the SOW date |
| Pages | $150 per page |

- Payment: 50% on signing and before work begins, 50% at launch approval or deemed acceptance.
- The fixed fee includes content drafting from client-supplied material and two revision rounds
  per page. Extra rounds and post-launch changes bill hourly, or come out of the Website Care
  edit allowance if the client has Care.
- Brochure sites only. E-commerce, logins, booking or payment systems, databases, and custom web
  apps are excluded; so are SEO, ads, photography, and logo design.
- If the setup fee was waived and the Care Order ends early (other than for {{COMPANY_NAME}}'s
  uncured breach), the $300 becomes due.

**Taking over an existing site**

When a client wants Website Care on a site {{COMPANY_NAME}} did not build, the takeover work
(moving the site into accounts in the client's name, setting up the repo and pipeline, connecting
hosting) is a fixed-fee SOW, priced from estimated hours at the managed-client rates on the
break-fix card, the same way onboarding and migration are quoted. Quote it before any work
starts. Whether a site that is not a static site on your static hosting platform can go on Care
as it is gets decided case by case (msp-website-setup, "Taking Over an Existing Site").

**Website Care (recurring, Website Hosting and Care Service Order)**

A managed line item like any other managed service. It can sit alongside a managed IT agreement
(its own Service Order under the same MSA) or be the only thing {{COMPANY_NAME}} manages for a
client.

Includes: domain and DNS management, monitoring and upkeep of the hosting configuration, backups
of the site source sufficient to restore it, and content edits up to 30 minutes per calendar month
(no rollover). Excludes redesigns, new pages, and new features (SOW or Change Order).

| Term | Monthly fee (Standard tier) |
|---|---|
| 1 year (minimum) | $60 |
| 2 years | $58 |
| 3 years | $55 |
| 5 years | $50 |

| Tier | When it applies | Monthly fee |
|---|---|---|
| Standard | Typical brochure site on the hosting platform's included (free) service level | $60 |
| Plus | Site features (such as form processing) exceed the platform's included limits | $70 |
| Pro | Traffic, security, or media needs require the hosting platform's paid pro-level plan | $150 |
| Business | The hosting platform's business-level plan is required | Quoted at need |

- One-year minimum term. Care uses its own ladder above, not the managed 4% ladder, and the
  $1,000/month engagement minimum (example default) does not apply to it; a Care-only client is
  below that minimum by design.
- Tier changes need 30 days' written notice to the client, and {{COMPANY_NAME}} first offers site
  changes that would keep it in the lower tier where feasible.
- Care clients are clients under agreement, so edit time beyond the 30 minutes bills at the
  managed remote rate on the break-fix card.
- **No Care = break-fix.** A site owner without Care calls when they need something and pays the
  non-contract rate on the break-fix card. No block hours, no prepaid website hours.
- Marketing carries no website prices, same as every other price.

---

## Project Offering: AI Adoption

The AI adoption project is a one-time project, not part of the managed agreement. Use your
public name for the AI project (msp-ai-adoption Setup Decision 6) in every quote and
client-facing line. Website builds work the same way. Website Care, by contrast, is a managed
line item. Like every {{COMPANY_NAME}} offering, the AI adoption project is a path to managed
services (msp-sales, section 10). It serves three cases:

- managed clients who ask about AI
- any small business that comes in through your public AI page on {{DOMAIN}}
- small clients or individuals outside the ICP

The small-client group is a volume play. Many small, quick projects produce more happy clients
than one large client ever will, and so more reviews and referrals. The delivery process lives
in msp-ai-adoption. This section owns every number. All figures here are shipped example
defaults (see Setup Decisions).

It is a one-time, fixed-fee project priced from break-fix hours. The configurator does not apply
(there are no recurring blocks), the $1,000/month engagement minimum (example default) does not
apply, and value factors do not apply.

**Standard scope and hours**

| Piece | Hours |
|---|---|
| Review the discovery answers or questionnaire | 0.5 |
| Starter Plan, 3 workflow cards, prompt starter sheet, red list | 2.5 |
| One remote walkthrough session | 1.0 |
| 30-day check-in | 0.5 |
| **Total (price on 5 hours for buffer)** | **4.5** |

**Prices**

| Option | Scope | Non-contract | Managed client | Floor |
|---|---|---|---|---|
| Standard | Everything above | $650 | $550 | $450 |
| Lean | Deliverables only (no walkthrough, no check-in; about 3 hours) | $450 | $330 | $270 |

- Managed prices are the managed remote rate ($110) times the hours. Non-contract Standard is set
  at $650 by owner decision (an effective $130/hr, below the $150 card rate on purpose to keep
  small-client volume flowing); non-contract Lean is 3 hours at $150.
- Floors are the remote floor ($90/hr) times the hours. Below the floor needs owner sign-off,
  same as everything else.
- Lead with Standard. Offer Lean only when the client wants to run it themselves or budget is
  the blocker. Both clear the 50% margin floor. Your public AI page describes Standard
  (walkthrough and 30-day check-in included). A Lean quote must say in writing that it has no
  walkthrough and no check-in.
- Scope that grows (more users, more workflow cards, extra sessions for a team) is re-quoted
  from hours at the client's card rate, still as a fixed fee. Out-of-scope requests after
  delivery bill hourly at the card rate (remote: 30-minute minimum, then 15-minute increments).

**What is free**

- A 30 to 45 minute AI conversation is free for managed clients and for prospects in the ICP (a
  door-opener). Individuals and small clients outside the ICP get a normal short scoping call,
  but the advice itself is the paid project. Your website does not advertise this
  conversation. Website leads get the short scoping call first. Offer the free conversation
  only after that call confirms ICP fit.
- For managed clients, ongoing AI progress review folds into the QBR at no extra charge, and AI
  license administration is covered like any other SaaS. The written Starter Plan pack is not
  free; it is the managed-price project above.

**Standing rules**

- **Fixed-fee scope, never prepaid hours.** Unused hours do not carry over and the project is
  never described as a block. This keeps it clear of the no-block-hours rule on the break-fix
  card.
- **The price never changes in exchange for a review or referral.** No discounts, credits, or
  anything of value for a review (review platforms' policies and the msp-marketing rule both
  forbid it). The review and referral payoff comes from volume and a plain ask after delivery
  (msp-sales).
- **AI licenses** (Copilot, Gemini, ChatGPT business plans, Claude Team) that {{COMPANY_NAME}}
  bills follow the standing third-party license markup above: one line, markup never broken
  out. Look up current vendor pricing at the time of the quote; never quote a seat price from
  memory.
- **Paper before work** (msp-legal owns the documents): managed clients sign a short SOW under
  their existing MSA; non-managed businesses sign the MSA plus a SOW; individuals sign a one-page
  engagement letter instead. The kit does not include that letter; draft it with your attorney
  (msp-ai-adoption Setup Decision 3), and route individual projects through msp-legal until it
  exists.
- **No paid workshop product.** Group sessions run only as the free "AI basics workshop"
  (example name; msp-marketing). Your public name for the AI project always means the paid
  project, never the workshop. A client who wants their team trained gets extra walkthrough
  hours on their own project, priced from hours.
- **Marketing carries no AI adoption prices**, same as every other price.

---

## Setup Decisions

Everything above is what the example MSP settled for its own shop. Settle each of these for yours
before this skill goes anywhere near a client:

- **Labor cost basis.** The example uses a $25/hr L1 remote wage, a $32/hr field tech wage, and a
  1.30x burden, landing at $40/hr remote and $80/hr on-site loaded cost. Rebuild this from your own
  hiring market and benefits package; see `references/labor-rates.md` for the levers.
- **Margin targets.** The example uses a 60% gross margin anchor and a 50% gross margin floor, both
  measured after a 3% payment-processing fee baked into the multipliers. Decide your own margin
  targets and processing-fee assumption.
- **Engagement minimum.** The example uses $1,000/month as the smallest managed-client fee it will
  accept. Set your own based on what a client actually costs you to service.
- **Contract ladder discount.** The example removes 4% of the opening price per year of commitment
  beyond the first (never more than 5%, which would erase the buffer above the floor). Decide your
  own ladder.
- **Annual escalator.** The example raises multi-year monthly fees 3% on each anniversary after year
  one. Decide your own, and make sure it is stated plainly in your contract paper.
- **Third-party license markup.** The example bills licenses at cost plus 15%. Decide your own
  markup and whether it covers procurement and vendor liaison the same way.
- **After-hours and holiday multipliers.** The example uses 1.5x after-hours and 2x holiday. These
  multipliers should match whatever your legal paper and helpdesk practice actually promise.
  Whatever you land on, it is a single owning source, not something restated inconsistently across
  skills.
- **Break-fix and hourly rate card.** The example uses $110/$150 remote and $220 on-site (managed
  vs. non-contract). Rebuild this card from your own loaded costs in
  `references/break-fix-rates.md`.
- **On-site allowance pricing.** The example prices bundled on-site hours at the standard anchor and
  rides the contract ladder like everything else. Decide whether that is the right model for your
  service area and drive times.
- **Support-hour assumptions per device.** The example's per-block labor hours (1.0 for a
  workstation, 1.5 for a server, and so on) reflect a reactive, early-stage shop with limited
  automation. Revisit these once you have your own ticket data; see `references/support-hours.md`.
- **Website builds and Website Care.** The example builds brochure sites at $300 setup (waived
  with a one-year Care Order) plus $150 per page, and prices Website Care at $60/$58/$55/$50 on a
  1/2/3/5-year ladder with Standard, Plus, Pro, and Business tiers keyed to the hosting platform's
  plans. Decide whether you build and manage websites at all; if you do, set your own build and
  Care prices, and match them to your website paper (msp-legal document-stack entry 13). If you
  do not, follow the project-offering opt-out list in msp-setup Phase 3.
- **AI adoption project.** The example prices a 4.5-hour project on 5 hours: Standard $650
  non-contract / $550 managed / $450 floor, Lean $450 / $330 / $270 floor. Decide whether you
  offer it (msp-ai-adoption Setup Decision 1) and rebuild these from your own break-fix card.
  If you offer it, set its public name, page, and call-to-action link in msp-ai-adoption Setup
  Decision 6, and use that name on every quote.

Once you have settled these, re-run `scripts/price_quote.py` against a known client (for example
`scripts/client.template.json`) and check how far the band moved before quoting anything live.

---

## Output

For an internal decision, run the configurator and walk the user through the options in plain terms:
which to lead with, where to open, where the realistic landing sits, and where each floor is. Keep it
in the conversation; this is a working number, not a deliverable.

When a number is going into something the client will see (a quote or marketing), present the
**client-facing term ladder** the configurator produces: the 1-year price on top, clearly labeled as
the minimum term and the highest price, with 2, 3, and 5 years stepping down. Hand off to `msp-brand`
for voice and formatting and to `msp-sales` for the value framing. The client should always meet the
price wrapped in the outcome it buys, presented as options assembled for them, never as a naked
spreadsheet or a standard tier card. The internal band (floor and opening ask) stays internal.

Internal margin notes and quote rationale are Zone 1 of `msp-technical-writing` (flavored mode).
Anything the client sees follows `msp-brand`.
