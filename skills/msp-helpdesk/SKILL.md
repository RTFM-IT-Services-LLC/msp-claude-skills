---
name: msp-helpdesk
description: >
  Use this skill for anything about how your MSP runs day-to-day support: setting or
  questioning a ticket's priority, response and resolution targets, "the client says everything is
  down", escalation, after-hours or emergency requests, security incident intake, triage order,
  your PSA (ticketing) system workflow, time entries, or ticket categories. Also trigger when
  drafting anything that describes support levels or response times to a client, and when
  training new hires on the service desk workflow (client onboarding is msp-onboarding). Apply
  alongside msp-client-comms (the messages clients receive during incidents), msp-legal (the SLA
  schedule lives in each client's Order; security incidents have contract implications),
  msp-pricing (after-hours billing multipliers), msp-maintenance (alerts that escalate into
  tickets, and the on-call rotation behind the after-hours line), and msp-metrics (ticket data
  feeds every business number).
---

# {{COMPANY_NAME}} Service Desk Operations

> **Defaults you must review.** The specific numbers in this skill are shipped example defaults
> from a working MSP. Review and replace them with your own before anything goes client-facing.

This skill is the source of truth for how {{COMPANY_NAME}} triages, works, escalates, and
closes support tickets. It exists so every ticket gets the same treatment regardless of who
touches it, and so the ticket data underneath the business stays trustworthy.

This skill owns the reactive desk. The proactive cycle (patching, backup verification,
monitoring and alert triage, the on-call rotation, change management) lives in
msp-maintenance; alerts become tickets here per that skill's triage rules, and the on-call
rotation behind the after-hours line is defined there.

One standing rule inherited from msp-pricing shapes everything here: **response time never
varies by client, option, or price.** Options differ in what they include, never in how fast
{{COMPANY_NAME}} answers. Every client gets the best response {{COMPANY_NAME}} has.

**Status caveat, important:** contractually, SLA targets live as a schedule inside each client's
Service Order (per msp-legal). Until your own Service Order template is finalized, the targets
below are policy, not yet contractual: run the desk by them regardless. They reach clients only
once msp-legal places them in the Order schedule, and whatever a signed Order says for a given
client governs for that client.

---

## Priority Matrix

Priority is about business impact and workaround, not about who is loudest.

| Priority | Definition | Example scenarios |
|---|---|---|
| **P1 Critical** | The business is stopped, or an active security incident. No workaround. | Whole office offline; server down; email down company-wide; suspected ransomware or account compromise |
| **P2 High** | A department or several people blocked, or one person fully down in a time-critical role. Core service degraded. | Accounting locked out on payroll day; the shared drive down for one team; internet crawling site-wide |
| **P3 Normal** | One person impaired but working, or an intermittent, non-blocking problem. | One user's email client misbehaving; a printer down with another nearby; a slow laptop |
| **P4 Low** | Questions, requests, routine changes, scheduled work. | New user setup; software install; how-to; equipment moves |

Two automatic rules: any suspected security compromise is P1 regardless of apparent size, and a
P3 that blocks a deadline the client names gets promoted rather than argued about.

**"Everything is down" triage, in order:** confirm scope (one user, one team, or the site), then
check the layers from outside in: power at the site, internet circuit (carrier status and modem),
firewall, switch, server or cloud service status pages. Remote diagnosis first; dispatch on-site
only once the failing layer is known or remote access is impossible. Most "everything is down"
calls are one layer, and naming it fast is what makes the 30-minute first response useful rather
than just prompt.

## Response Targets (example defaults)

Business hours: 8:00 am to 6:00 pm, Monday through Friday, {{TIMEZONE}},
excluding listed holidays (see the holiday list in Setup Decisions below).

| Priority | First response | Working rhythm | Client updates |
|---|---|---|---|
| P1 | 30 minutes | Continuously until resolved or contained | Hourly, via msp-client-comms |
| P2 | 2 business hours | Same business day | At least daily |
| P3 | 4 business hours | Resolve or schedule within 3 business days | On change of status |
| P4 | Next business day | As scheduled | On completion |

First response means a human acknowledgment with a next step, not an autoresponder.

## After Hours

- After-hours support is for P1 only, reached by phone at {{PHONE}}, which forwards to
  on-call after hours. One number, day or night; safe to print in client-facing material.
- Billing follows the client's Order and the MSA: after-hours work at 1.5x and holiday work at
  2x the hourly rate, per msp-pricing. Never invent or waive multipliers ad hoc.
- Non-P1 requests that arrive after hours get acknowledged the next business morning. Do not
  train clients that everything is an emergency by treating everything as one.

## Printer Tickets

Printer tickets: the desk resolves everything remote (drivers, queues, connectivity,
scan-to-email/folder, firmware) for managed printers. Hardware failures (jams, fusers,
dead units) are diagnosed remotely, then routed to the vendor warranty: you open and
manage the claim; the desk does not repair hardware. Physical work on site uses the
client's on-site allowance or bills at break-fix on-site rates. Consumables requests
(toner, supplies) are politely declined, not a service you offer. Printers not on
the managed line (consumer, inkjet, USB-attached) are best-effort at hourly rates.

---

## Security Incidents

Suspected compromise (ransomware, account takeover, data exposure) is its own track:

1. **Contain first, backups included.** Isolate the affected machine and, in any ransomware or
   lateral-movement scenario, verify and isolate the backup copies immediately; modern
   ransomware hunts backups before announcing itself. Preserve evidence; do not wipe and
   reimage before the picture is understood.
2. **Kill the identity, not just the account.** For account takeover: disable the account AND
   revoke active sessions and tokens, reset MFA methods, remove attacker-added inbox rules and
   forwarding, and review OAuth application grants. A disabled account with live tokens is
   still compromised. For a compromised mailbox, run the Compromised Mailbox Checklist below.
3. **Escalate to the owner immediately**, regardless of hour.
4. **Counsel early for anything significant.** For incidents with plausible data exposure,
   regulated data, or serious client impact, engage an attorney licensed in {{STATE}}
   (msp-legal) before deep forensics, so the investigation can be conducted under privilege.
   Once {{COMPANY_NAME}} carries E&O and cyber policies, carrier notification happens at the
   same moment; carriers can require notice before incident spend and may mandate their own
   response firms.
5. **Communicate** through msp-client-comms incident templates (the security incident notice
   for the affected client passes through msp-legal). During an active incident, never
   speculate in writing about cause or fault.
6. **Document contemporaneously.** Times, actions, findings, decisions. The MSA's ransomware
   cost allocation carries a negligence carveout, which means {{COMPANY_NAME}}'s protection in
   a bad scenario is a record showing it followed its own process with reasonable care. The
   notes are part of the response, not paperwork after it.
7. **Regulated-data clients** (education, healthcare, financial, legal) may carry breach
   notification duties, and {{STATE}}'s consumer notification clock may be short. That is an
   attorney conversation, early, via msp-legal.
8. **Ransom stance:** {{COMPANY_NAME}} never advises paying a ransom and never facilitates
   payment; payment decisions, sanctions exposure (OFAC), and any negotiation belong to the
   client, its insurer, and counsel. Reporting to law enforcement (FBI/IC3) is encouraged and is
   the client's call, guided by the attorney.
9. **Close the loop into msp-security.** Any control found missing or failed during the
   incident becomes an msp-security assessment finding afterwards, with a remediation date or
   a signed waiver.

**If {{COMPANY_NAME}}'s own tooling is the suspected vector** (RMM, credential vault, or
{{COMPANY_NAME}} accounts): this is the worst scenario and it spans every client at once.
Immediately isolate or disable the suspected {{COMPANY_NAME}} tool tenant-wide, rotate
{{COMPANY_NAME}} credentials from a known-clean device, communicate with clients out-of-band
(phone, not the possibly-compromised email), treat every client environment as potentially
affected until shown otherwise, and get the attorney engaged in the first hour. Contemporaneous
documentation matters most here. The RMM disable procedure, {{COMPANY_NAME}} access rules, and
the tabletop exercise for this scenario live in msp-security's house standard
(`references/msp-house-security.md` in that skill).

### Compromised Mailbox Checklist

Use this checklist when a mailbox on the client's email and productivity platform is
compromised. It expands step 2 above. Steps 3 through 9 of the Security Incidents track still
apply. The order follows the major email platform vendors' published compromised-account
guidance for administrators.

Work from a known-clean device. Contact the client by phone, not through the affected mailbox.

1. Disable or suspend the account.
2. Revoke all active sessions and refresh tokens.
3. If malware is possible on the user's computer, isolate that computer.
4. Scan the isolated computer before the user signs in on it again.
5. Reset the password to a new password that the user does not use anywhere else.
6. Give the new password to the user by phone or through the vault. Never send it by email.
7. Delete the user's app passwords. A password reset does not revoke them.
8. List all inbox rules, including hidden rules. Some platforms do not show every rule in the
   mail client.
9. Remove each inbox rule and forwarding address that the user cannot explain.
10. Revoke each OAuth application grant that the client did not approve.
11. Remove each mailbox delegate and each full mailbox access, send-as, or send-on-behalf
    permission that nobody can explain.
12. Remove each MFA method, recovery phone number, and recovery email address that the user
    does not recognize.
13. Remove any admin role that the account should not hold.
14. Search the sign-in logs, audit logs, and message trace from a date before the first known
    sign of compromise.
15. Check the Sent, Deleted, Drafts, and Archive folders for messages the user did not write.
16. If the account sent fraudulent messages, give the client the list of recipients to call.
17. If a message changed payment details, tell the client to call its bank at once.
18. Keep the account. Do not delete it, because it holds the evidence.
19. Confirm that MFA is enforced on the account.
20. Re-enable the account and return it to the user.
21. Record each step, its time, and its result in the ticket.

If you publish a client-facing version of this process (for example a resources article through
msp-marketing), keep its steps in the same order as this checklist.

---

## Escalation

The ladder: assigned tech, then the owner or a designated senior tech, then vendor support using
the client's support contract.

Time triggers, so nothing ages silently:

- A P1 with no clear path forward at 60 minutes: the owner or a designated senior tech engaged.
- A P2 stuck at 4 hours: owner or designated senior tech review.
- Any ticket about to blow its target: escalate before it blows, not after.

Escalating early is professionalism, not failure. The expensive mistake in a small shop is a
ticket one person quietly wrestles with for a day.

---

## Ticket Hygiene

The pricing model, the margin math, and every number in msp-metrics stand on ticket time data.
The support-hour estimates behind the price sheet get revisited against real ticket data about a
year in (per msp-pricing's research); sloppy entries now mean repricing blind later.

- **No work without a ticket.** Hallway requests, texts to the owner, drive-by asks: ticket
  first.
- **Every touch gets a note and a time entry, entered the same day.** Reconstructed time is
  fiction.
- **Consistent categories.** Standing set: hardware, software, email and accounts, network,
  security, backup, printer and peripheral, how-to and training, adds-moves-changes, vendor,
  website (Website Care edits count against the client's 30-minute monthly allowance).
  Amend the list deliberately, not per mood.
- **Resolution notes in plain English** a client could read, because sometimes they will.
- **Note form follows msp-technical-writing.** Ticket notes, time entry notes, and resolution
  notes use flavored mode. Any procedure or step list in a ticket uses strict mode. The
  plain-English rule above still applies.

**Closing the loop:** confirm the fix with the requester. If a resolved ticket gets no reply for
5 business days, send the closing notice (template in msp-client-comms) and close it. For every
P1, closing also means scheduling the post-incident summary (msp-client-comms template 5),
standing practice within 3 business days of resolution, no exceptions; a P1 is not done until
the summary is sent.

---

## Client Intake

Clients reach the desk by email to {{SUPPORT_EMAIL}} ({{SUPPORT_ALIAS_EMAIL}} also works and
opens a ticket; {{SUPPORT_EMAIL}} is the address printed in client-facing material), by phone at
{{PHONE}}, or through the portal if enabled for them. msp-onboarding gives the main contact this
channel on day one and teaches the client's full staff at the staff-wide announcement (days
20-30 of onboarding), including what a useful report looks like: what is broken, since when, how
many people affected, and what changed recently. Coach gently on tickets that arrive as "nothing
works"; never mock them.

---

## Setup Decisions

The values below shipped as example defaults from a working MSP. Confirm each for your own shop,
or replace it, before anything here reaches a client:

- Business hours: shipped default is 8am-6pm, Monday through Friday, {{TIMEZONE}},
  excluding your own holiday list; the response target table above is the shipped
  default.
- Holiday list: define your observed holiday list; shipped example default (bracketed, replace
  with your own): [New Year's Day, Memorial Day, Independence Day, Labor Day, Thanksgiving and
  the day after, Christmas Eve and Christmas Day].
- Emergency number: shipped as a single phone line ({{PHONE}}) that forwards to on-call after
  hours; decide your own after-hours number and forwarding path.
- Support intake: shipped as {{SUPPORT_EMAIL}} (printed) with {{SUPPORT_ALIAS_EMAIL}} as a
  working alias; set your own addresses.
- Quiet-close window: shipped default is 5 business days.

Nothing else is open here. The one real dependency is the Service Order template (msp-legal),
which is where these targets become contractual per client; build that before promising these
targets in writing.
