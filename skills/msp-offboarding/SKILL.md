---
name: msp-offboarding
description: >
  Use this skill whenever a client relationship is ending or might end: a client
  gives notice, says they are not renewing, is switching providers, or asks to cancel; you decide
  to exit a client (see msp-metrics for that decision); or anyone mentions data return, removing
  our access, transitioning to a successor provider, a final invoice, or "offboarding" a client.
  Also trigger when drafting termination acknowledgments or closure letters. Apply alongside
  msp-legal (the signed MSA and Order govern notice, fees, and data handling; this is a
  legal-adjacent workflow), msp-brand (every message), msp-client-comms (the letters), and
  msp-metrics (log the loss and the reason).
---

# {{COMPANY_NAME}} Client Offboarding

This skill is the source of truth for how {{COMPANY_LEGAL_NAME}} exits a client relationship. A
clean exit protects {{COMPANY_NAME}} legally, protects the client operationally, and protects the
reputation that referrals are built on. The last month of a relationship is remembered longer
than the first.

Two principles govern everything below. First, **service quality holds at full standard through
the last day**. The SLA applies until the agreement ends, and a degraded exit is both a
reputation wound and a liability invitation during the one-year claim period. Second, **the
signed paper governs**. Notice periods, early-termination fees, and data obligations come from
this client's actual MSA and Order, read fresh, never asserted from memory.

Standing note per msp-legal: this is working analysis, not legal advice. Disputed exits,
early-termination fee enforcement, and anything involving regulated data goes to an attorney
licensed in {{STATE}} before {{COMPANY_NAME}} relies on it.

**Defaults you must review:** the specific numbers in this skill are shipped example defaults
from a working MSP. Review and replace them with your own before anything goes client-facing.

---

## Two Doors In

- **The client terminates.** Follow the runbook as written.
- **{{COMPANY_NAME}} terminates.** The decision itself belongs to msp-metrics (the fire-or-fix
  framework) and to the owner. Once decided, run the same runbook with a longer, more generous
  runway (60 to 90 days where practical; this ships as the example default), a referral or two to
  other providers, and extra care in tone. Exiting a client gracefully is a marketing act.

---

## First 48 Hours After Notice

1. **Read this client's signed MSA and Order.** Confirm the required notice, the effective end
   date, and any early-termination fee. If they are exiting mid-term, the fee conversation is
   the owner plus msp-legal, handled separately from the transition work and never as a surprise
   line on the final invoice.
2. **Acknowledge in writing** (template below): received, effective end date, what happens next.
   Neutral, warm, zero guilt-tripping.
3. **Freeze scope.** No new projects, pause pending Change Orders. Keep normal support running
   exactly as before.
4. **Brief the team.** Full service through the last day, neutral tone about the departure and
   about any successor, and a reminder that the mutual non-solicit runs 12 months:
   {{COMPANY_NAME}} does not recruit their staff, and if their side or a successor starts
   recruiting yours, flag it to the owner rather than engaging.
5. **Log it in your PSA (ticketing) system** with the stated reason for leaving. msp-metrics
   reviews churn reasons; an honest reason recorded now is worth more than a flattering one.

---

## The Transition Runbook

Sequence matters more than speed. The rule that prevents the worst outcome:
**{{COMPANY_NAME}}'s access is removed last, only after the client confirms their own control
works.** A client locked out of their own systems by an eager offboarding is the single most
damaging exit failure.

Write the runbook steps in the strict mode of msp-technical-writing (Zone 1). Write the
documentation package in the flavored mode, with any procedure inside it in the strict mode.

### 1. Assemble the documentation package

- Asset inventory and network map
- License inventory and software keys
- Vendor contact list with account numbers
- Backup configuration, schedule, and the date of the last verified restore
- The agreed user add and remove process, and anything else a successor needs on day one

Deliver via a secure channel. Credentials transfer through the vault's secure sharing or an
agreed secure method, never plain email.

Name and stamp each file in the package per msp-brand section 4 (Document Versioning). Example:
`acme-dental-asset-inventory-2026-11-01-v1.0.xlsx`. Then the successor knows which copy is
current.

### 2. Transfer control

- Confirm the client owns a working break-glass admin on their email and productivity platform,
  and that someone on their side (or the successor) has tested it.
- Confirm domain registrar and DNS control sits with the client or transfers per their
  instruction, in writing.
- Website clients (a site {{COMPANY_NAME}} built, or Website Care, including Care-only clients):
  follow msp-website-setup "At Offboarding". Deliver the site source or transfer the repo, and
  confirm the client controls the registrar, DNS, and hosting platform account, within the 30
  days the Care Order allows (provided undisputed amounts are paid). If the setup fee was waived
  and Care ends inside its first term, flag the clawback to msp-legal before the final invoice.
- Walk the successor through the environment if the client asks. Courteous and professional;
  factual about the environment, quiet about {{COMPANY_NAME}}'s internal matters and pricing.

### 3. Remove the stack, on the last day, in order

1. Silence monitoring and alerting for the client.
2. Remove RMM agents.
3. Unenroll endpoint protection, ZTNA, and MDM as applicable.
4. Remove {{COMPANY_NAME}} admin accounts (including {{COMPANY_NAME}}'s administrator seat on
   the client's hosting platform account and git repo access), last, after client-confirmed
   control.
5. Recover any {{COMPANY_NAME}}-owned loaner hardware.

{{COMPANY_NAME}} access removal follows msp-security's house standard: partner-delegated admin
relationships ended, named {{COMPANY_NAME}} accounts removed, and the client's vault entries
rotated or handed over.

Keep a dated record of each removal. The closure letter will attest to it.

### 4. Data retention

Standing policy (example default): {{COMPANY_NAME}} retains client data and backup copies for
60 days after offboarding completes, then deletes them and sends written confirmation of the
deletion to the client. State this in the closure letter and calendar the deletion date before
the exit closes. A signed DPA or the client's Order can override this per client, and for
regulated-data clients retention and deletion remain an attorney question via msp-legal, not a
default.

As a floor, {{COMPANY_NAME}}'s own engagement records (tickets, invoices, the signed agreements,
the offboarding evidence) are retained through the one-year claim period in the MSA, then
reviewed for destruction.

### 5. Final billing

Service through the end date, unreturned hardware, open project balances, and any
early-termination amount already agreed through the owner and msp-legal path. No surprises: the
final invoice should contain nothing the client has not already heard about.

---

## Never Do These

- Never hold data, credentials, or access hostage over unpaid invoices. Collection runs through
  the attorney path; hostage-taking creates liability and torches the referral reputation in one
  move.
- Never remove {{COMPANY_NAME}} access before the client has confirmed their own.
- Never criticize the successor provider or the client's decision, in writing or aloud.
- Never let quality visibly sag during the notice period. That story gets retold.

---

## Templates

Apply msp-brand. Plain English, warm, no em dashes.

The letters follow msp-brand. Any steps the client must take inside a letter are Zone 2 of
msp-technical-writing. Put them in a numbered list and write them in the strict mode.

**Acknowledgment (within 2 business days of notice):**

> **Subject: Confirming your transition plan**
>
> Hi [First name],
>
> Thanks for letting us know. We have received your notice, and your services with us will run
> through [end date].
>
> Between now and then, nothing changes day to day: your team can reach us the same ways for
> anything they need. In the background we will prepare a full handoff package (your asset list,
> network map, account details, and vendor contacts) and coordinate the transfer of access with
> [you / your new provider] so the switch is smooth.
>
> I will follow up with a short transition checklist this week. If anything about the timing
> needs to move, just tell us.
>
> [Signature block per msp-brand]

**Closure letter (after the last removal step; this is the liability shield, send it every
time):**

> **Subject: [Company] transition complete**
>
> Hi [First name],
>
> As of [date], we have completed the transition of [Company]'s IT services.
>
> Where everything stands:
>
> - Our management and security tools have been removed from your computers and servers.
> - Administrator access has been transferred to [name or successor], and our accounts have been
>   removed.
> - Your documentation package was delivered to [name] on [date].
> - Backup copies of your data will be retained for 60 days as a safety net for your new
>   provider, then deleted on [date]. We will confirm the deletion in writing. [Adjust only if
>   this client's DPA or Order says otherwise.]
>
> Final invoice [number] covers service through [end date].
>
> Thank you for the time we spent working together. If anything comes up during the transition
> that we can help clarify, reach out any time. We wish you and the team the best.
>
> [Signature block per msp-brand]

---

## After the Exit

- Store the offboarding evidence (checklists, removal dates, delivery confirmations, the closure
  letter) with the client record.
- Record the loss reason and the final numbers for the msp-metrics monthly review.
- A polite check-in about 90 days later is fine, and sometimes wins the client back. Anything
  that smells like told-you-so is not.

## Setup Decisions

Values below are the shipped example defaults from a working MSP. Decide your own before this
goes live.

- **Post-exit retention:** 60 days for client data and backups, then deletion with written
  confirmation, ships as the example default. DPA or Order terms override per client; regulated
  data goes through msp-legal.
- **Runway for company-initiated exits:** 60 to 90 days ships as the standing default.
