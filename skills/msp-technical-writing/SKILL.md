---
name: msp-technical-writing
description: >
  Use this skill for the prose form of all writing for your MSP that is not marketing or
  direct customer communication: runbooks, procedures, checklists, change plans, PSA ticket
  and resolution notes, internal docs and reports, decisions logs, research briefs, sales
  enablement notes, the monthly owner review, contracts and legal notes, skill files, README text,
  commit messages, and internal email or chat. Inside marketing and customer messages, use it
  only for the technical parts: step-by-step instructions, troubleshooting steps, how-to
  sections, and descriptions of a technical process. Based on ASD-STE100 Simplified Technical
  English: short active sentences, one action per step, plain words, no semicolons, zero em
  dashes. msp-brand still owns voice and naming in customer-facing content, and msp-legal
  drafting conventions win in contracts. Apply alongside the skill that owns the content.
---

# {{COMPANY_NAME}} Technical Writing

This skill sets the prose form for {{COMPANY_NAME}} writing. It adapts ASD-STE100 Simplified
Technical English (STE) to this skill kit. It removes the marks of AI slop: long run-on
sentences, passive voice, marketing adjectives, filler transitions, and em dashes.

Tested result: the source style cut anti-slop linter violations by 74% versus baseline Claude
output (1.12 versus 4.36 violations per 100 words).

This skill controls form only. The skill that owns the content still controls the facts, the
process, and the numbers. All client-visible numbers still come from msp-pricing.

---

## Where This Skill Applies

The suite has three zones. Find the zone before you write.

### Zone 1: Full scope

This skill governs the prose of everything that is not marketing or direct customer
communication:

- Runbooks, procedures, and checklists (msp-onboarding, msp-offboarding, msp-maintenance,
  msp-helpdesk, msp-website-setup)
- Change plans, maintenance plans, and security incident steps
- PSA tickets: internal notes, time entry notes, and resolution notes
- Internal docs: decisions logs, audits, handoff notes, eval write-ups, README, skill files,
  and reference files
- Business reports: the monthly owner review, client health notes, and QBR prep notes
- Lead research briefs and prospect notes (msp-leadgen)
- Sales enablement: coaching notes in scripts, objection guides, pipeline docs, and playbooks
- Legal: contract prose, legal notes, and risk summaries (see Contracts and Legal Documents)
- Security standards, internal assessment findings, and hardening procedures
- Commit messages, pull request descriptions, internal email, and team chat

### Zone 2: Technical parts of customer-facing content

In marketing and direct customer communication, msp-brand owns the voice. This skill applies
only to the technical parts:

- Step-by-step instructions (for example, "set up MFA on your phone")
- Troubleshooting steps the client follows
- Descriptions of a technical process (for example, what happens in a maintenance window)
- Workflow cards and how-to pages in msp-ai-adoption deliverables
- The "what to do" list in a security advisory
- The fix description for each gap in a client-facing security assessment or QBR scorecard

The rest of the piece follows msp-brand: greeting, empathy, reassurance, outcomes, calls to
action, and the signature block.

### Zone 3: Out of scope

- Marketing copy: articles, social posts, newsletters, web copy, and flyers (msp-marketing)
- Direct customer communication: outreach emails, the spoken lines of a call script, proposal
  narrative, case studies, the welcome email, and client notices and letters (msp-sales,
  msp-client-comms, msp-onboarding, msp-offboarding)
- Copy for a client's own website (the client's voice, per msp-website-setup)
- Code, identifiers, config, and command syntax
- Verbatim quotes: client quotes, testimonials, and quoted contract clauses
- Prompt text in AI prompt templates (the text a client pastes into an AI tool). The
  instructions around the prompt are Zone 2.
- Any text where the owner asks for a different style

### Mixed pieces

One piece often holds two zones. A security advisory has a warm opening (Zone 3) and a list of
actions (Zone 2). Separate the zones with structure. Put the technical part in its own numbered
list or section. Write that part to this skill. Write the rest to msp-brand.

---

## Precedence

1. An explicit style request from the owner wins over this skill.
2. In Zone 2, msp-brand controls tone, warmth, naming, and vocabulary. Use the msp-brand
   plain-English words inside the steps too ("your computer", not "the endpoint"). This skill
   controls the sentence form: one action per step, imperative verbs, condition first, and the
   length caps.
3. In contracts, msp-legal drafting conventions win on conflict.
4. The owning skill controls facts, process, and numbers. This skill never changes the meaning
   of a statement to satisfy a style rule.
5. Em dashes and en dashes: zero, in every zone this skill touches. This rule is stricter than
   the msp-brand allowance for a rare human em dash. The suite ground rule already bans them.

---

## Contracts and Legal Documents

Use the flavored mode for the MSA, Service Order, SOW, DPA, BAA, waivers, and addenda. Legal
drafting conventions win on conflict:

- Defined terms keep their capitalized form and exact wording ("Provider", "Client", "Service
  Order"). This matches the rule "one name for one thing".
- A clause can run past 25 words when a shorter form loses precision.
- Semicolons can separate the items of an enumerated clause list.
- Terms of art stay ("indemnify", "liquidated damages", "notwithstanding"). Do not replace a
  legal term with a short common word.
- Keep the modal verb convention of the existing template.
- Review by an attorney licensed in {{STATE}} controls the final wording.

Apply the rules where they cost no precision:

- Use the active voice with a named party. "Provider will notify Client", not "Client will be
  notified".
- Use no marketing adjectives, no filler, and no em dashes.

---

## Modes

- **Strict:** text that tells someone what actions to take. Apply every rule and both length
  caps without exception. Examples: runbook steps, change plans, patch and test-restore
  procedures, security incident steps, website deployment steps, credential collection lists,
  and all Zone 2 instructions and troubleshooting steps.
- **Flavored (default):** everything else in Zone 1. Apply the sentence, paragraph, active
  voice, no-em-dash, and no-phrasal-verb rules. Relax the restricted dictionary so the text
  keeps enough range to read naturally.

Pick the mode from the text. Do not ask which mode to use.

---

## Rules

### Words

- Use one name for one thing. Do not call the same item by two different names. Use the term
  the owning skill uses:
  - "client" for a business under agreement, "prospect" for a business not yet signed
  - "Service Order" (then "Order"), per msp-legal
  - "Website Care", per msp-website-setup and msp-pricing
  - "P1" through "P4" for ticket priority, per msp-helpdesk
  - The company name per msp-brand: "{{COMPANY_LEGAL_NAME}}" in contracts and
    "{{COMPANY_NAME}}" in other documents and internal text
- Use the short common word: start (not begin, commence, or initiate), use (not utilize or
  leverage), help (not facilitate), make sure (not ensure), before (not prior to), after (not
  subsequent to), about (not regarding or concerning), get (not obtain or acquire), show (not
  demonstrate), also (not additionally, furthermore, or moreover).
- Give each word one meaning. "Fall" means to move down, not to decrease.
- No marketing adjectives: seamless, robust, powerful, cutting-edge, effortless, world-class,
  next-generation, revolutionary, battle-tested, enterprise-grade.
- Use American spelling.
- Internal text can use technical terms ("endpoint", "tenant", "RMM"). Zone 2 text uses the
  msp-brand plain-English list instead.

### Verbs

- Use the active voice. "The technician restarts the service", not "the service is restarted".
- Use a verb for an action. "Analyze the log", not "perform an analysis of the log".
- No stacked auxiliaries. Not "it is important to note that this may help to improve". Write
  "this improves X".
- No "-ing" main verb where a simple tense works.
- No phrasal verbs where a plain verb exists: create (not spin up), contact (not reach out),
  examine (not dive into), start (not kick off), deploy (not roll out).

### Sentences

- One instruction per sentence. Use a maximum of 20 words for an instruction and 25 words for a
  descriptive sentence.
- No contractions in documents, tickets, runbooks, contracts, or Zone 2 steps. Contractions
  are acceptable in internal chat.
- Use articles: a, an, the, this, these.

### Punctuation

- No em dashes and no en dashes, ever. Use a period, a comma, a colon, or parentheses instead.
  For a range, write "to" or "through" ("Days 1 to 5", "P1 through P4").
- No semicolons. Write two sentences. The only exception is an enumerated list inside a
  contract clause.

### Structure

- One topic per paragraph, with a maximum of six sentences.
- For steps, use a numbered vertical list. Give one action per item, in the imperative form.
- Put a condition before its command. "If the backup job failed, run it again", not "Run the
  backup job again if it failed".

### Output

- Write only the requested text. No preamble, no summary of what you wrote, and no closing
  remarks.
- When the text goes into a file, name and stamp the file per
  msp-brand section 4 (Document Versioning).

---

## Editing the Skill Kit

New or changed text in the kit's skill files uses the flavored mode. Step lists in skills use
the strict mode. Existing sections stay as written until the owner asks for a rewrite. The kit
ground rules in README.md still apply: numbers from msp-pricing and naming from msp-brand. Keep
every skill description under the 1,024 character limit.

---

## Self-Lint (run before you return text)

1. Is there an em dash or an en dash? Remove it. Zero tolerance.
2. Is a sentence over 20 words (instruction) or 25 words (descriptive)? Split it.
3. Is there a semicolon outside a contract clause list? Replace it with a period.
4. Is there a contraction in a formal document or a step? Expand it.
5. Is there a passive verb with a known actor? Make it active.
6. Is there an "-ing" main verb, a nominalization ("perform an analysis"), or a phrasal verb
   ("spin up")? Replace it with a plain verb.
7. Does one thing have two names? Pick one name.
8. Is there a marketing adjective or a filler transition (furthermore, additionally,
   moreover)? Delete or replace it.

For long documents, run the bundled linter from this skill folder:

```
python3 scripts/ste-lint.py draft.md
```

The score is violations per 100 words. A lower score is cleaner. The target is under 1.5 for
the flavored mode and under 0.5 for the strict mode. The `em_dash` count must be 0. The linter
checks only the mechanical subset of STE. It does not check judgment rules. In contracts and in
the msp-brand parts of a mixed piece, read the score as advice only. The `em_dash` count must
still be 0.

---

## Limits

This skill fixes the form of slop. It cannot make a hollow paragraph true. Say only things that
are accurate and necessary, then apply the form.

The full ASD-STE100 standard (Issue 9) is free at https://asd-ste100.org. It is copyrighted.
Do not paste it in full.
