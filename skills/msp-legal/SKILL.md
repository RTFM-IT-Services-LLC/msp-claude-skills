---
name: msp-legal
description: >
  Use this skill for ANY legal or contract work for your MSP: reviewing, drafting, or revising an
  MSA, Service Order, SOW, SLA, NDA, waiver, DPA, or BAA; triaging a contract a client or vendor
  sends; assessing legal risk on a deal; or answering "what document do we need for this client".
  Always load this skill BEFORE running any generic legal skill (legal:review-contract,
  legal:triage-nda, legal:legal-risk-assessment, legal:compliance-check, etc.): it is your
  playbook and document map, the organization-specific positions those skills ask
  for. Also trigger on "is this enforceable", "what should our contract say", "the client wants
  to change a clause", or any mention of liability caps, indemnification, non-solicits, or
  contract terms for an IT services business. Apply alongside msp-brand (naming and voice),
  msp-pricing (any term or number a client could see), msp-sales (how legal terms land in the
  sales conversation), and msp-security (security waivers and attestations).
---

# {{COMPANY_NAME}} Legal Playbook

> **Defaults you must review.** The specific numbers and negotiating positions in this skill
> (liability caps, indemnification stances, notice periods, termination fees, SLA credit
> structures, and the rest) are shipped as one MSP's negotiated example defaults, not legal
> advice. Review and replace them with your own, and have your own attorney approve your
> versions, before anything goes client-facing.

This skill is the source of truth for {{COMPANY_NAME}}'s legal document stack and its standing
contract positions. It exists so that legal work is consistent: the same documents, the same
clause positions, and the same escalation rules every time, instead of re-deriving them from
scratch in each session.

**Standing disclaimer, always in force:** Claude assists with legal workflows but does not
provide legal advice. {{COMPANY_NAME}} is a small business without in-house counsel, so every
output in this domain is working analysis for {{OWNER_NAME}} (or the owner), and anything
load-bearing (a new template, a changed clause, a signed deal with modified terms) goes to an
attorney licensed in {{STATE}} before reliance. Say so in internal deliverables. Never print that
disclaimer inside a client-facing contract itself.

---

## How This Skill Divides Work With Its Siblings

- **msp-legal (this skill):** which documents exist, what each is for, how they fit together,
  {{COMPANY_NAME}}'s standing positions on contested clauses, and when to escalate to an
  attorney.
- **msp-brand:** how legal documents look and read. Full legal name in contracts, no em dashes
  anywhere, brand fonts and accent formatting for formatted templates. Load it before producing
  any formatted document.
- **msp-technical-writing:** the sentence form of contract prose, legal notes, and risk
  summaries. These use the flavored mode. Legal drafting conventions win on conflict, and the
  attorney's wording controls.
- **msp-pricing:** every number and commercial term a client could see. Term lengths, the
  discount ladder, minimums, and rate multipliers belong to that skill; contracts must match it,
  never contradict it (see "Pricing rules that bind contracts" below).
- **msp-sales:** how contract terms are explained to a prospect. The paper is protective; the
  sale is warm. When a clause needs translating into plain English at signing, that is a sales
  task informed by this skill.
- **Generic legal plugins (legal:review-contract, legal:triage-nda, legal:legal-risk-assessment,
  legal:compliance-check, legal:legal-response, legal:vendor-check, etc.):** these supply the
  method (clause-by-clause review, GREEN/YELLOW/RED triage, severity-by-likelihood risk). This
  skill supplies the organization-specific inputs those methods ask for: the playbook positions,
  the acceptable ranges, and the escalation triggers. When a plugin asks for "the organization's
  playbook," it means `references/playbook-positions.md` in this skill.

**First orientation question on any contract:** which side is {{COMPANY_NAME}} on? On
{{COMPANY_NAME}}'s own templates, {{COMPANY_NAME}} is the **Provider** and the paper is
deliberately provider-favorable; the job is to protect that posture while removing errors,
contradictions, and small-client friction. On paper someone else sends (a vendor agreement, a
client's procurement template, an inbound NDA), {{COMPANY_NAME}} is the **customer or recipient**
and the lens flips: now hunt for the same aggressive clauses {{COMPANY_NAME}} itself uses.

---

## The Document Stack

This is the map of every legal document {{COMPANY_NAME}} needs, what each one does, and how they
relate. Full per-document detail (purpose, contents, status, drafting guidance) lives in
`references/document-stack.md`. Load that file when drafting or revising any of these, or when
advising which document a situation calls for.

**How the documents fit together:**

```
NDA (optional, pre-sale)
        |
MSA  (the umbrella; every client signs it once)
 |
 +-- Service Order ......... managed services: scope, pricing, TERM, SLA targets
 +-- SOW ................... one-time projects: deliverables, price, timeline
 +-- Change Order .......... mid-flight changes to an Order or SOW
 +-- DPA / BAA addendum .... attached when the client handles regulated data
 +-- Website Services Addendum + Website Development SOW + Website Hosting
 |   and Care Service Order ... website builds and Website Care
 +-- Risk Acceptance Waiver. signed when a client declines a recommendation
     (declined security controls come from msp-security's baseline)
```

The architectural rule that governs everything: **the MSA is the umbrella and carries no term,
no pricing, and no client-specific scope.** Every client signs the same MSA, whether managed,
break-fix, or project-only. Commercial specifics (term commitments, the discount ladder, seat
and device counts, SLA response targets) live in the Order or SOW underneath it. Never "fix" the
MSA by adding term or pricing language to it.

**The stack at a glance:**

| Document | One-line purpose | Status |
|---|---|---|
| Master Services Agreement (MSA) | Umbrella legal terms every client signs once | Example template; pending attorney review |
| Service Order | Per-client managed-services scope, pricing, term, SLA targets | Example template; pending attorney review |
| Statement of Work (SOW) | Scope and price for one-time projects | Example template; pending attorney review |
| Service Level Agreement (SLA) | Response and resolution targets | Built as Schedule A of the Order template; pending same review |
| Non-Disclosure Agreement (NDA) | Confidentiality before deep discovery | Not built; low effort, worth adding |
| Risk Acceptance Waivers | Client declines a recommendation in writing | Example template; pending attorney review |
| Data Processing Agreement (DPA) | Regulated-data handling addendum (per client's applicable regime) | Example template; pending attorney review; regimes confirmed per client |
| Business Associate Agreement (BAA) | HIPAA addendum for healthcare clients | Not built; build when first healthcare client appears |
| Change Order | Amend scope/price of an existing Order or SOW | Not built |
| Website Services Addendum | Website-specific terms (content, ownership, third-party platform) for builds and Care | Not included in the kit; draft with your attorney if you build websites (document-stack entry 13) |
| Website Development SOW | Fixed-fee website build | Not included; draft with your attorney (entry 13) |
| Website Hosting and Care Service Order | Monthly Website Care: term ladder, tiers, edit allowance | Not included; draft with your attorney (entry 13) |
| Third-party terms flow-through | Pass vendor EULAs (email/productivity platform, endpoint protection, device management, and the like) to client | Not built |
| Website privacy policy + terms of use | {{DOMAIN}} compliance | Not built |
| Staff confidentiality + IP assignment | Protects client data and {{COMPANY_NAME}}'s IP as the team grows | Not built; internal corporate docs (operating agreement) exist separately |

When a client asks "what do we need for client X," walk the stack top down: MSA always; Order or
SOW depending on engagement type; DPA/BAA if regulated data; waivers as recommendations get
declined. msp-security is the source for which controls a waiver covers, what {{COMPANY_NAME}}
can truthfully attest to on a client's cyber insurance questionnaire, and the regulated-client
overlays that a DPA or BAA commitment rests on.

**A note on the templates:** example drafts of the Service Order, SOW, Risk Acceptance Waiver,
and DPA ship in the kit's `templates/` folder (msp-service-order, msp-sow,
msp-risk-acceptance-waiver, msp-dpa). The MSA, the BAA, and the three website documents are a to-do for you to draft with your own
attorney, and every shipped draft also requires that attorney review before first use. This file describes what belongs in each document and how they relate;
it is not a substitute for the signed paper.

---

## Standing Contract Positions

{{COMPANY_NAME}}'s example negotiated positions on contested clauses (liability cap, dispute
venue, the ransom clause, non-solicit, insurance, claim period, amendment mechanics, survival)
live in `references/playbook-positions.md`. These are one MSP's negotiated positions, not legal
advice. **Load that file before any contract review, redline, clause question, or negotiation
prep, and have your own attorney approve your versions before you rely on them.** It is
formatted the way legal:review-contract expects a playbook: standard position, acceptable range,
and escalation trigger per clause. It also carries the open items from that review so they are
not forgotten or silently re-decided.

Two rules from that file worth keeping in mind at all times:

1. **Do not weaken the core protections to make a deal feel friendlier.** The limitation of
   liability, disclaimers, client responsibilities, IP ownership, and remote-access rights are
   working as designed. Friction gets solved in the Order, in the conversation, or in the small
   set of clauses marked flexible, not by editing the MSA per client.
2. **Some things are attorney-only.** The non-solicit liquidated-damages figure, the overall
   enforceability of the liability cap, and any client-demanded change to indemnification go to
   an attorney licensed in {{STATE}}, full stop. Flag, do not freelance.

---

## Rules That Bind Every Legal Document

**Brand rules (from msp-brand, restated because contracts are where they bite):**
- Full legal name **{{COMPANY_LEGAL_NAME}}** in contracts, signature blocks, and formal
  documents. Signature block reads "{{COMPANY_LEGAL_NAME}} (Provider)".
- No em dashes anywhere, including inside contract prose.
- Prose form follows the "Contracts and Legal Documents" section of msp-technical-writing.
- Governing law is {{STATE}}.

**Pricing rules that bind contracts (from msp-pricing; contracts must match the sheet):**
- One year is the minimum managed-services term and the highest price shown; longer terms step
  down a 4% per year ladder. This lives in the **Order**, never the MSA. (Example default; set
  your own.)
- $1,000/month engagement minimum. (Example default; set your own.)
- After-hours work at 1.5x and holiday work at 2x the hourly rate. The MSA states both
  multipliers; any rate that appears in a contract must match the price sheet. (Example default;
  set your own.)
- If a contract needs a number and the number is not in msp-pricing, that is a pricing task
  first. Load msp-pricing; do not invent figures in legal documents.

**The relationship lens (from msp-sales):** {{COMPANY_NAME}} sells through trust to small
clients. Provider-favorable paper and a warm sale coexist, but the clauses most likely to spook a
small owner or their insurance broker (insurance burden, ransom wording, unilateral amendment,
short claim windows) are exactly the ones the playbook has already right-sized. When reviewing or
drafting, keep asking: would this clause survive being read aloud to the owner of a 10-person
business? If not, is the protection worth the friction, and can the Order flex it instead?

---

## Workflow Notes

- **Reviewing a contract:** load `references/playbook-positions.md`, then run the
  legal:review-contract method against it. Classify findings: outright errors, internal
  contradictions, {{STATE}} enforceability questions, conflicts with msp-pricing, and
  small-client friction.
- **Inbound NDA:** load the playbook file, then run legal:triage-nda. {{COMPANY_NAME}}'s red
  flags for inbound paper mirror what it right-sized in its own: embedded no-hire clauses
  broader than a targeted non-solicit, missing standard carveouts, exclusive venue outside
  {{STATE}}.
- **Drafting a new template:** read the relevant entry in `references/document-stack.md` first;
  it carries the standing decisions about what goes in that document and what stays out of it.
  Apply msp-brand formatting. Deliver clean text plus, if requested, a tracked-changes version
  for the attorney.
- **Risk or compliance questions:** legal:legal-risk-assessment and legal:compliance-check
  supply the framework; this skill supplies {{COMPANY_NAME}}'s escalation reality, which is
  simple: the escalation path is always "an attorney licensed in {{STATE}}," because there is no
  senior counsel.
- **Formatted output:** consult the `docx` skill for Word deliverables, save to the session's
  outputs or working folder (wherever the current environment delivers files to the user), and
  present the file. Verify zero em dashes before delivering.
  Name and stamp the file per msp-brand section 4 (Document Versioning). Example:
  `acme-dental-service-order-2026-11-01-v1.0.docx`. The stamp goes on its own line below the
  page number. A changed term, or a revision after the client saw the document, makes a new
  major version. The DRAFT banner for attorney review is separate from the version and stays
  until the attorney signs off.

---

## Setup Decisions

The positions in `references/playbook-positions.md` shipped as example defaults from a working
MSP, and the items below are still genuinely open. Settle all of it for your own shop, with your
own attorney, before this playbook goes client-facing:

- Attorney review of the whole document stack before anything goes live. Priorities: the
  non-solicit liquidated-damages figure, the liability cap's overall enforceability, and a full
  pass on every template.
- Your own Service Order template, carrying your own minimum term and discount ladder.
- Your own DPA, if you have or expect any regulated-data client (education, healthcare-adjacent,
  financial, or legal). Confirm with your attorney which regimes actually apply to each such
  client before attaching it.
- Your own governing law, venue, and county for dispute resolution.
- Your "client's insurance primary over Provider's" flex policy: decide whether to soften it by
  default for small accounts or only on request, and document your choice.
