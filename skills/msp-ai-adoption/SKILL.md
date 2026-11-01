---
name: msp-ai-adoption
description: >
  Use this skill when a client or prospect of your managed IT services (MSP) business asks a
  general AI question: "I want to use AI but don't know where to start", "how can we use AI",
  "should we be using ChatGPT", "we bought Copilot and nobody uses it", "is Gemini any good",
  or "can AI help my team". Delivers the AI adoption project. Runs a structured discovery (tools, work, data, comfort), picks
  three starter use cases, and produces platform-specific workflow cards, prompt templates,
  and a 30-day adoption plan for Copilot, Gemini, ChatGPT, or Claude. Also for preparing a
  client AI call, turning call notes into a plan, or leveling up a team already using AI.
  Apply alongside msp-security (data rules and shadow AI), msp-legal (AI use policy, DPA),
  msp-pricing (if billed), msp-brand (every client-facing page), and msp-sales (when it opens
  a deal).
---

# {{COMPANY_NAME}} AI Adoption

**Defaults you must review:** the free-versus-paid rules, deliverable set, and paper
requirements in this skill are shipped example defaults from a working MSP. Review and replace
them with your own before anything goes client-facing (see Setup Decisions at the bottom).

This skill turns the vague question "how do we use AI?" into a short, specific plan a small
business can actually follow. The client almost never needs AI explained. They need someone to
look at their actual work, their actual tools, and their actual data, and say: "start with these
three things, here is exactly how, and here is what not to put in it."

The deliverable is always concrete: named tasks, step-by-step instructions for the platform they
already pay for, copy-paste prompts, and a check-in date. Never a generic "AI can boost
productivity" overview.

---

## How This Skill Divides Work With Its Siblings

- **msp-security** owns what data may go into which AI tool, the shadow-AI risk, and tenant
  settings. Every plan from this skill passes through the Data Rules section below, which
  follows that standard.
- **msp-legal** owns the client's AI Acceptable Use Policy wording, anything touching a DPA or
  BAA, and professional-rules questions (for law firms, ABA Formal Opinion 512 territory; the
  firm's own counsel decides ethics questions, not {{COMPANY_NAME}}).
- **msp-pricing** owns any number: license costs quoted to the client, and the price of
  this engagement (its "Project Offering: AI Adoption" section). This skill never states a
  price.
- **msp-legal** also owns the paper that must be signed before a paid project starts
  (SOW, MSA plus SOW, or the individual engagement letter; see Inherited Defaults).
- **msp-brand** governs every page the client sees. No em dashes.
- **msp-technical-writing** sets the sentence form. The Workflow Cards, how-to steps, and the
  30-day plan steps are Zone 2 (strict mode). msp-brand still governs the framing around them.
  The prompt text a client pastes into an AI tool is out of scope.
- **msp-sales** picks up when the conversation reveals a bigger need (no managed IT, messy
  tenant, a licensing upgrade). Record it as a sales note; do not pitch mid-discovery.
- **msp-qbr** is where an existing client's AI progress gets reviewed after the first 30 days.

---

## Modes: Figure Out Which One You're In

1. **Prep mode.** The owner or a tech has a call coming up. Produce a one-page question sheet
   (the Core Discovery below, trimmed to fit the time) plus any vertical-specific questions.
2. **Live mode.** Claude is talking to the client directly. Ask the discovery questions in
   small batches (two or three at a time, plain language, no jargon), and adapt based on the
   answers. Do not dump all questions at once.
3. **Notes mode.** Someone pastes call notes or a transcript. Extract answers against the
   discovery blocks, list what is still missing, then build the plan with gaps labeled.
4. **Level-up mode.** The client already uses AI. Skip the basics, run the Maturity Check,
   and build the next-step plan.

If the mode is unclear, ask one question: "Are we prepping for a conversation, or do you have
answers from the client already?"

---

## The Process

### Step 1: Triage (always first, two minutes)

Before any use-case talk, establish:

- **Who is asking?** Owner or manager (company-wide plan, policy needed) versus one employee
  (personal starter plan, but flag that the company needs a policy).
- **Which AI tools do they already have access to, and under what account type?** This is the
  single most important fact. See Platform Notes. Having Microsoft's productivity suite does not
  mean they have paid Copilot; "people use ChatGPT" usually means personal free accounts.
- **Regulated data?** Accounting (taxpayer data, FTC Safeguards), legal (privileged material),
  healthcare (ePHI), childcare or education (children's records), anything with card data. If
  yes, the Data Rules section governs every recommendation, and the plan starts with the
  low-risk use cases.
- **Is anyone already using AI without approval?** Assume yes. Shadow AI is the norm in
  small businesses, and discovering it is a finding, not an accusation.

### Step 2: Core Discovery

Four blocks. In live mode, pick the questions that matter; in prep mode, include all of block A
and B and the best of C and D.

**A. Tools and access**
1. Which email and productivity platform are you on (Microsoft's, Google's, or something
   else)? Which plan?
2. Does anyone have a paid AI license today (Copilot, Gemini, ChatGPT Plus/Team/Business,
   Claude Pro/Team)? Company-paid or personal?
3. Which free AI tools have people tried? What did they use it for?
4. What are your main business applications (accounting, practice management, EHR, ERP, CRM)?
   Do any of them have AI features built in already?
5. Where do your files live (cloud file storage, team sites and shared drives, a file server,
   the app itself)?

**B. The work (this is where the use cases come from)**
1. Walk me through a normal week. What eats the most time?
2. What do you write over and over? (Emails, proposals, client letters, reports, job
   descriptions, policies.)
3. What do you read too much of? (Long emails, contracts, regulations, vendor documents,
   meeting notes.)
4. How many meetings a week, and does anyone take notes or send follow-ups?
5. Where does information get copied from one place to another by hand?
6. What questions do new staff ask that someone always has to stop and answer?
7. If you had an extra person for ten hours a week, what would you hand them first?

**C. People and comfort**
1. Who is curious about AI, and who is skeptical or worried about it?
2. Has anyone had a bad experience (wrong answer, embarrassing output)?
3. How comfortable is the team with new software generally? Who learns fast?
4. Who would own this internally? (One champion beats a company-wide rollout.)

**D. Data and risk**
1. What information would be a disaster if it leaked? (This defines the red list.)
2. Do you have client contracts, regulators, or insurers that say anything about AI or data
   handling?
3. Do you have an AI policy, or any written rule about it today?
4. Do you want AI touching client-facing output, or internal work only for now?

### Step 3: Pick Three Starter Use Cases

From block B, list every candidate task, then score each 1 to 3 on:

- **Value:** hours saved per week, or pain removed.
- **Ease:** can it be done in the tool they already have, with no integration?
- **Safety:** can it be done without red-list data? (3 = no sensitive data at all.)

Pick the top three by total, with at least one "quick win" a skeptic will notice within a week
(meeting recap, email drafting, summarizing a long document). Never start with a use case that
scores 1 on Safety. Record the runners-up as a "next wave" list.

**Reliable starter use cases for the example ICP verticals (msp-sales)** (use as prompts for
discussion, not a menu to recite):

- **Everyone:** drafting and tone-fixing emails, summarizing long threads, meeting recaps and
  action items, first drafts of policies and SOPs, turning notes into a formatted document,
  explaining a spreadsheet formula, rewriting technical text for a customer.
- **Accounting:** client engagement letter and reminder drafts, explaining tax notices in plain
  language (with identifiers removed), month-end checklist drafts, summarizing IRS or state
  guidance. Taxpayer data stays out unless the tool is approved for it.
- **Legal:** first drafts of routine correspondence, summarizing non-privileged public
  documents, research starting points (always verified; courts have sanctioned fabricated
  citations), marketing content. Privileged material only in a firm-approved, business-tier
  tool, and only if the firm's counsel has signed off.
- **Healthcare:** patient-facing education handouts, staff policy drafts, scheduling and
  front-desk scripts, job postings. No ePHI unless the tool is covered by a BAA and the practice
  has approved it.
- **Manufacturing:** SOP and work instruction drafts, turning a supervisor's voice notes into a
  procedure, supplier email drafting, summarizing spec sheets, safety training quizzes.
- **Professional services:** proposal first drafts, meeting recaps, client update emails,
  repurposing one piece of content into several.

### Step 4: Build the Deliverables

Produce these, in this order. Load msp-brand before formatting anything the client sees.

1. **AI Starter Plan (one to two pages).** What we heard, the three starter use cases and why,
   the red list (what never goes into AI), who owns it internally, the 30-day plan, and the
   check-in date.
2. **Workflow Cards, one per use case.** Written for the platform the client has. Each card:
   - The task, in the client's own words.
   - When to use it and when not to.
   - Where to click (the exact app and entry point, per Platform Notes).
   - The prompt, copy-paste ready, with [brackets] for what they fill in.
   - How to check the output (what to verify every time).
   - A "make it better" follow-up prompt.
3. **Prompt Starter Sheet.** Five to ten reusable prompts built on the pattern below, tailored
   to their work.
4. **AI Use Policy recommendation.** A short list of rules drawn from Data Rules. If the client
   wants a formal written policy, hand off to msp-legal for the wording.
5. **Next-wave list and sales notes** (internal only): licensing gaps, tenant cleanup, security
   gaps, bigger opportunities.

**Public names for the deliverables.** Client-facing pages use these public names. Match them
to your public AI page (Setup Decision 6). Internal notes may use either name.

| Public name (client-facing) | Internal name |
|---|---|
| Your AI starter plan | AI Starter Plan |
| Three step-by-step guides | Workflow Cards |
| A prompt starter sheet | Prompt Starter Sheet |
| Clear rules for your data | Red list, plus the AI Use Policy recommendation |
| A walkthrough with your team | Remote walkthrough session |
| A 30-day check-in | 30-day check-in |

**The prompt pattern to teach every client** (simple enough to remember):

- **Role:** who the AI should act as ("You are an office manager at a 30-person CPA firm").
- **Task:** what to produce ("Draft a reminder email to clients who haven't sent documents").
- **Context:** the facts it needs, pasted in or attached (minus red-list data).
- **Format:** length, tone, structure ("Under 120 words, friendly but firm, bullet the list").
- **Check:** ask it to flag what it's unsure of ("List any assumptions you made").

Then iterate: the first answer is a draft. Teach "make it shorter", "more formal", "what did
you leave out?" as normal next steps.

### Step 5: The 30-Day Adoption Plan

- **Week 1:** champion (and owner) use the three workflow cards daily. Confirm account type and
  settings are correct before anyone starts.
- **Week 2:** champion shows two or three coworkers; collect what worked and what didn't.
- **Week 3:** refine prompts, add one use case from the next-wave list, save the best prompts
  somewhere shared (a team document, or the platform's saved prompts, projects, custom GPTs,
  Gems, or agents where the plan supports it).
- **Week 4:** check-in with {{COMPANY_NAME}}. Measure against what we heard in discovery: hours
  saved, tasks now routine, problems. Decide the next wave. Existing managed clients roll this
  into the next QBR. For a client who is not managed, this check-in is where {{COMPANY_NAME}}
  makes the managed offer that fits them (msp-sales section 10). For a Lean sale,
  {{COMPANY_NAME}} sends a short, free follow-up email at 30 days with that offer instead.

Adoption fails from disuse, not from bad AI. One champion using it daily beats a company-wide
announcement.

---

## Level-Up Mode: Maturity Check

For clients already using AI, place them on this ladder and build toward the next rung only:

- **Level 0, None or banned:** start at Step 1.
- **Level 1, Ad hoc chat:** people type questions into a chatbot, often personal accounts.
  Next: move to a company-controlled account, write the red list, build prompt templates.
- **Level 2, Repeatable prompts:** the team reuses prompts for known tasks. Next: saved
  prompts and shared instructions (Claude Projects, custom GPTs, Gemini Gems, Copilot agents
  or notebooks), grounded in their own reference documents.
- **Level 3, Connected to their data:** the AI can read their email, calendar, files, or
  business apps through the platform's built-in connections. Next: permissions review first
  (AI surfaces whatever a user can access, so overshared files become a real exposure; this is
  an msp-security task), then multi-step workflows.
- **Level 4, Automated workflows:** AI runs recurring tasks or agents with little prompting.
  Next: governance, logging, human review of anything client-facing, and cost control.

Level-up questions to add to discovery: What do you use it for most? What have you given up
on? Who uses it and who doesn't? Is anyone paying for it personally? What do you wish it could
reach (files, email, the accounting system)?

---

## Platform Notes

AI products, plan names, and features change monthly. **Before telling a client what their plan
includes, verify it against the vendor's current documentation or the client's admin portal.**
Do not state a feature or license detail from memory as fact. What follows is how to think
about each, not a spec sheet.

- **Copilot (including the free Copilot Chat).** Best fit for clients already on Microsoft's
  email and productivity platform. Key question: do they have free Copilot Chat only, or paid
  Copilot licenses that work inside their email, documents, spreadsheets, team chat, and their
  cloud file storage and team sites? Paid Copilot sees whatever the user can see, so a file
  permissions cleanup (team sites and cloud file storage) comes before rollout. You can check
  licensing and settings in the client's admin console directly for managed clients.
- **Gemini.** Best fit for clients on Google's email and productivity platform. Check what
  their edition includes and whether Gemini in email, documents, spreadsheets, meetings, and
  shared drives is turned on by the admin. Same oversharing caution applies to shared drives.
- **ChatGPT.** Very common as shadow AI on personal accounts. Distinguish free and personal
  paid plans from business plans (Team, Business, or Enterprise tiers), which add admin
  control and different data-use terms. If staff already love it, moving them to a business
  plan is often the fastest safe win.
- **Claude.** Strong at writing, long documents, and analysis. Distinguish personal plans from
  Team or Enterprise plans for business data. Projects give a team shared instructions and
  reference files; connectors can reach business apps.

**Which platform to recommend when they have none:** default to the one that matches their
productivity platform (Copilot for Microsoft shops, Gemini for Google shops), because it lives
where their files and email already are and the admin controls sit in a console you already
manage. Recommend a standalone tool when the use cases are mainly writing and analysis and the
suite option doesn't fit the budget or the work. Any cost comparison goes through msp-pricing
and uses current vendor pricing, looked up at the time.

---

## Data Rules (apply to every plan)

Follows msp-security. In plain language for the client:

1. **Business accounts only for business data.** Personal and free accounts may use what you
   type to improve the vendor's models and give the company no control. Check each vendor's
   current terms for the plan in use.
2. **The red list never goes in** unless the specific tool and plan are approved for it in
   writing: passwords and credentials, Social Security and account numbers, patient health
   information, privileged legal material, taxpayer data, children's records, card data.
3. **Remove identifiers when practical.** "Client A" works as well as a real name for most
   drafting tasks.
4. **A human checks everything before it leaves the building.** AI states wrong things with
   confidence. Numbers, citations, names, and legal or medical statements get verified every
   time.
5. **Connected AI inherits permissions.** Before turning on AI that can read company files,
   clean up who can see what.
6. **Regulated clients:** confirm the vendor offers the needed agreement (BAA for HIPAA, for
   example) on the plan in question, and route the decision through msp-legal and
   msp-security. {{COMPANY_NAME}} does not declare a client compliant.

---

## Output and Tone

- Plain language. The client asked because they don't know where to start; no acronyms
  without a definition, no hype.
- Honest about limits: say what AI is bad at for their use case, not just what it's good at.
- Specific over complete: three things done well beats a list of twenty ideas.
- Starter Plan and Workflow Cards are client-facing and follow msp-brand. Sales notes and
  the next-wave list are internal and never go to the client.
- Per msp-technical-writing, sales notes and the next-wave list are Zone 1 (flavored mode).
- Use fictional names (Acme convention) in any example saved into the kit.
- Every deliverable file follows msp-brand section 4 (Document Versioning). Example:
  `acme-dental-ai-starter-plan-2026-11-01-v1.0.docx`.

---

## Quick Clarifying Questions

If a request is thin, ask no more than these before starting:

1. What AI tools, if any, does the client already have, and are they business or personal
   accounts?
2. What industry, and roughly how many people?
3. Are we prepping for a call, or do we already have their answers?

---

## Inherited Defaults (shipped example defaults)

Clients see this project under your public name for the AI project (Setup Decision 6), and
it is marketed to any small business through your public AI page. It is a one-time project,
and like every {{COMPANY_NAME}} offering it is a path to managed services. Numbers live in
msp-pricing ("Project Offering: AI Adoption"). How and when to offer it, and when to raise
managed services, live in msp-sales (section 10). If you change one of these there, keep this
skill consistent.

1. **Free vs billable.** The 30 to 45 minute AI conversation is free for managed clients and
   for prospects in the ICP. Your website does not advertise it. Website leads get a short
   scoping call first, and the free conversation only after that call confirms ICP fit. For
   individuals and small clients outside the ICP, the advice is
   the paid project. The written pack (Starter Plan, three workflow cards, prompt starter sheet,
   red list, walkthrough, 30-day check-in) is a fixed-fee project for everyone, managed clients
   included, at their card rate. A Lean option (deliverables only, no walkthrough or check-in)
   exists; when Lean is sold, the Week 4 check-in in the 30-day plan becomes the client's own
   review unless they add it back.
2. **Managed clients.** Ongoing AI progress review folds into the QBR at no extra charge, and
   AI license administration is covered like any other SaaS.
3. **License resale** on Copilot, Gemini, ChatGPT, or Claude business seats follows the
   standing third-party license markup in msp-pricing.
4. **Paper before work.** Managed clients: a short SOW under their MSA. Non-managed businesses:
   MSA plus SOW. Individuals: a one-page engagement letter (see Setup Decisions). No
   deliverables are built for a paid project until the paper is signed.
5. **Workshops.** Group sessions run only as the free "AI basics workshop" (example name;
   msp-marketing). Your public name for the AI project always means the paid project, never
   the workshop. There is no paid workshop product. A client who wants their team trained gets
   extra walkthrough hours on their own project.
6. **Reviews and referrals.** Never traded for a price change. The payoff comes from volume and
   a plain ask after delivery (msp-sales section 10).

## Setup Decisions

Settle these before this skill goes live for your shop. Accept the shipped default, change it,
or log a deferral.

1. **Whether you offer AI adoption at all, and to whom.** Shipped default: offered to managed
   clients who ask, to any small business that comes in through your public AI page, and, as
   a volume play, to small clients and individuals outside the ICP. Every project client gets
   a managed offer that fits them (msp-sales section 10). If you do not offer it, keep this
   skill for internal use and remove the AI adoption parts of the other skills (the
   project-offering opt-out list in msp-setup Phase 3).
2. **Free conversation rule.** Shipped default: free for managed clients and ICP prospects,
   paid for everyone else (Inherited Default 1). Decide your own line.
3. **Individual engagement letter.** Shipped as a requirement but not included in the kit.
   Draft a one-page engagement letter with an attorney licensed in {{STATE}} before taking an
   individual AI adoption project; until it exists, route individual projects through
   msp-legal.
4. **Standard AI Use Policy template.** Not included in the kit. Draft one with an attorney
   licensed in {{STATE}} (through msp-legal) when the first client asks for a formal policy; the
   Data Rules above are the starting list.
5. **Workshops.** Shipped default: free marketing workshops only, no paid workshop product.
   Decide whether you want a paid training product instead; if so, price it in msp-pricing.
6. **Public name and page for the AI project.** Pick the name clients will see (example: a
   short, plain name such as "AI Quick Start"), the public page on {{DOMAIN}}, and the
   call-to-action link. Use the public name in all client-facing text and quotes; internal
   notes may use either. Never give the free group workshop the same name.
