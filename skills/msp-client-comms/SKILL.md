---
name: msp-client-comms
description: >
  Use this skill whenever writing an operational message to an existing client of your MSP:
  outage or incident notices and updates, planned or emergency maintenance announcements,
  post-incident summaries, security advisories ("warn our clients about this phishing wave"),
  price change letters, new-user-ready or user-offboarded confirmations, and ticket closing
  notices. Trigger on "draft an email to the client about", "let them know", "notify clients",
  "tell the client", or any in-service client notification. Sales outreach to prospects belongs to
  msp-sales; this skill owns messages to clients already under agreement. Apply alongside
  msp-brand (voice and signature), msp-helpdesk (priorities set the cadence), msp-legal
  (anything touching breach, liability, or contract mechanics), and msp-pricing (any number).
---

# {{COMPANY_NAME}} Client Communications

> **Defaults you must review.** The specific numbers in this skill are shipped example defaults
> from a working MSP. Review and replace them with your own before anything goes client-facing.

This skill is the source of truth for the messages {{COMPANY_NAME}} sends clients during
service: routine, urgent, and awkward. Consistent, calm, plain-English communication during a
problem is the product, as much as the fix itself. A client who hears from {{COMPANY_NAME}}
quickly, in words they understand, with a promise of the next update, experiences a very
different outage than one who hears silence.

Everything here rides on msp-brand: friendly expert, plain English, outcomes not specs, the
standard signature block, and no em dashes anywhere.

---

## Global Rules

- **Plain English, always.** "Email is down for your whole office," not "we are experiencing an
  email service degradation." Per msp-brand, write to the office manager, not to IT.
- **No blame, no vendor trash talk.** "Our upstream provider is working on it," not naming and
  shaming. {{COMPANY_NAME}} owns the client experience even when a vendor owns the fault.
- **Every time reference carries the date and {{TIMEZONE}}.**
- **Incident messages always end with the next-update commitment**, and {{COMPANY_NAME}} keeps
  it even when the update is "still working on it."
- **Never speculate about cause in writing during an active incident.** Facts observed, actions
  taken, next step. Cause analysis goes in the post-incident summary, after it is known.
- **Legal gate:** anything touching a possible security breach, regulated data, an admission
  that could read as fault, or contract mechanics (like the price letter) passes through
  msp-legal before sending.
- Update cadence and severity words come from msp-helpdesk. A message about a P1 says things
  are urgent because they are; a P3 does not borrow urgency to look responsive.
- **Client steps follow msp-technical-writing (Zone 2, strict mode).** This covers the "what to
  do" list in a security advisory and any reset or setup steps. Put the steps in their own
  numbered list. The rest of the message follows msp-brand.
- **Letters as files:** a message sent as email text has no version. A letter sent as an
  attachment (for example, a price change letter as a PDF) follows msp-brand section 4
  (Document Versioning).

Placeholders appear in [brackets]. The support intake address is {{SUPPORT_EMAIL}}
({{SUPPORT_ALIAS_EMAIL}} also opens a ticket; print {{SUPPORT_EMAIL}} in anything client-facing).

---

## Templates

### 1. Planned maintenance (send 3 or more business days ahead)

> **Subject: Scheduled maintenance [day, date]**
>
> Hi [name],
>
> We will be doing scheduled maintenance on [what, in plain terms] on [day, date] from [start]
> to [end], {{TIMEZONE}}.
>
> What this means for you: [impact, e.g. "email will be unavailable for up to 30 minutes during
> this window"]. You do not need to do anything.
>
> If anything seems off after [end time], let us know at {{SUPPORT_EMAIL}} or {{PHONE}}.
>
> [Signature block]

For emergency maintenance, same structure plus one honest sentence on why it cannot wait, and an
apology for the short notice. Send a two-line "complete, all clear" when done.

### 2. Incident: initial notice (within 30 minutes of confirming a P1)

> **Subject: [Company] service issue: [system]**
>
> Hi [name],
>
> We are aware that [plain-English symptom, e.g. "email is down for your office"] and we are on
> it now.
>
> What we know so far: [one or two observed facts]. In the meantime: [workaround, or "no action
> needed on your end". A workaround with more than one step goes in a numbered list].
>
> Next update: by [time], {{TIMEZONE}}, sooner if it is resolved.
>
> [Signature block]

### 3. Incident: progress update (hourly for P1, per msp-helpdesk)

> **Subject: Update: [system]**
>
> Quick update on [issue]: [what has been done or learned since the last note]. [Current state.]
>
> Next update by [time], {{TIMEZONE}}.
>
> [Signature block]

### 4. Incident: resolved

> **Subject: Resolved: [system]**
>
> [What was affected] is back up as of [time], {{TIMEZONE}}, on [date].
>
> If anything still is not working right on your end, reply here or call us at {{PHONE}}.
> [For P1s: We will send a short summary of what happened and what we are changing, within 3
> business days.]
>
> Thanks for your patience.
>
> [Signature block]

### 5. Post-incident summary (every P1, standing practice, within 3 business days; through
msp-legal if security or liability adjacent)

> **Subject: What happened on [date], and what we are changing**
>
> Hi [name],
>
> Here is the plain-English summary of [date]'s [issue], as promised.
>
> **What happened:** [cause in one or two non-technical sentences, stated as fact only once
> established].
>
> **Timeline:** [detected time] we spotted it, [milestones], [resolved time] everything was back
> to normal. Total impact: [duration and who was affected].
>
> **What we are changing:** [one to three concrete steps, e.g. "we added monitoring that
> catches this earlier" or "we scheduled the replacement of the aging switch that caused it"].
>
> Questions are welcome. Thanks again for your patience while we worked through it.
>
> [Signature block]

### 6. Security advisory (e.g. a phishing wave)

Advisory rules per msp-security: specific, actionable, no fear-mongering, and say what
{{COMPANY_NAME}} has already done on its side.

> **Subject: Heads up: [scam type] emails going around**
>
> Hi [name],
>
> We are seeing [plain description, e.g. "fake invoice emails that look like they come from
> your accounting system"] hitting businesses like yours this week. Feel free to forward this to
> your team.
>
> What to watch for: [two or three concrete tells].
>
> What to do:
>
> 1. Do not click links in the email.
> 2. Do not reply to the email.
> 3. Forward anything suspicious to {{SUPPORT_EMAIL}}. We will check it, usually within the hour.
> 4. If someone already clicked, call us right away at {{PHONE}}.
>
> Nobody is in trouble; fast beats embarrassed.
>
> We are watching for this on our side as well.
>
> [Signature block]

### 7. Price change letter

Mechanics come from msp-legal (the MSA's amendment process: 30-day notice, and the client's
review window is real, so never obscure it). The number comes from msp-pricing. The delivery
belongs in or right after a QBR (msp-qbr) whenever possible; a cold price letter is the last
resort. Per the sales philosophy: state the number plainly, wrap it in the value, and never
apologize for it.

> **Subject: An update to your service agreement**
>
> Hi [name],
>
> [Two or three specific sentences of value delivered: "This past year we handled [n] requests
> for your team, verified your backups with a monthly test restore, and got you through the
> [project] upgrade with no downtime." Pull real numbers from QBR prep, and claim only what
> actually happened for this client; the monthly restore cadence is established in
> msp-maintenance, so confirm this client's restore log backs the claim.]
>
> Starting [effective date, 30 or more days out], your monthly rate will change from
> $[current] to $[new]. [One plain sentence on why: costs of delivering the service, growth of
> the team we support, expanded scope.]
>
> Per our agreement, this change takes effect after a 30-day notice period, and I am glad to
> walk through it with you before then. Call me at {{PHONE}} or reply here and we will find a
> time.
>
> [Warm close.]
>
> [Signature block]

### 8. New user ready / user offboarded

> **Subject: [New person]'s setup is ready**
>
> Hi [name],
>
> [New person] is all set: account created, email working, [computer] configured, and access to
> [systems] in place. [Anything they need on day one, e.g. sign-in steps sent to their personal
> email.]
>
> [Signature block]

For departures, confirm the reverse: account disabled as of [time], mail routed to [person],
files preserved at [location], per your instructions. The written confirmation matters; access
removal is the kind of thing people later need proof of.

### 9. Ticket closing notice (no response for 5 business days)

> **Subject: Closing out: [issue]**
>
> Hi [name], we have not heard back, so we are marking [issue] resolved. If it is still acting
> up, just reply and this reopens; no need for a new request.
>
> [Signature block]

### 10. Security incident notice, affected client (ALWAYS through msp-legal before sending)

For a suspected or confirmed compromise affecting this client specifically. Facts observed
only, no cause speculation, no admissions, no scope guesses. The attorney reviews before it
goes out, every time; if regulated data may be involved, the attorney may direct different or
additional notice.

> **Subject: Security issue affecting [system/account], and what we are doing**
>
> Hi [name],
>
> We identified [plain factual description, e.g. "unusual sign-in activity on one of your
> email accounts"] at [time], {{TIMEZONE}}, today. We have [containment steps
> taken, e.g. "secured the account and signed out all active sessions"] and we are
> investigating.
>
> What we need from you right now:
>
> 1. [First specific ask, e.g. "Do not click anything unusual in your email today."]
> 2. [Next ask, e.g. "Call us about this issue. Do not email about it."]
>
> Next update: by [time], {{TIMEZONE}}. If you have questions before then, call
> me directly at {{PHONE}}.
>
> [Signature block]

---

## Setup Decisions

The values below shipped as example defaults from a working MSP. Confirm each for your own shop
before anything here reaches a client:

- Support intake: shipped as {{SUPPORT_EMAIL}}, with {{SUPPORT_ALIAS_EMAIL}} as a working
  alias.
- Post-incident summaries: shipped as standing practice for every P1, no exceptions; decide
  whether that stays absolute for your shop.
- Quiet-close window (template 9): shipped default is 5 business days, matching msp-helpdesk.
