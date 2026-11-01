---
name: msp-onboarding
description: >
  Use this skill whenever a new client signs or client onboarding comes up in any
  form: a deal hits Closed Won, someone says "we signed", "kickoff", "welcome email", "get them set
  up", "take over from their old IT guy", or names a new client that needs setting up. Also trigger
  for planning or quoting onboarding work, building a credential collection list, deploying agents
  to a new environment, or the 30-day review. This is the handoff target for msp-sales pipeline
  stage 7 (Closed Won). Apply alongside msp-legal (paper gates before work starts), msp-pricing
  (onboarding is always billed separately), msp-brand (every client-facing message), msp-security
  (the baseline assessed and hardened to), and hand off to msp-helpdesk and msp-qbr at the end.
---

# {{COMPANY_NAME}} Client Onboarding

This skill is the source of truth for how {{COMPANY_LEGAL_NAME}} takes a signed client from
"Closed Won" to steady-state managed service. The first 30 days decide whether the client feels
the relief they were sold or starts wondering what they signed. Run this the same way every time.

Onboarding is also where {{COMPANY_NAME}} protects itself: the environment gets documented
as-found before anything changes, and the paper gets verified before any work starts.

**Defaults you must review:** the specific numbers in this skill are shipped example defaults
from a working MSP. Review and replace them with your own before anything goes client-facing.

---

## How This Skill Divides Work With Its Siblings

- **msp-sales** hands off here at pipeline stage 7. Discovery notes (headcounts, device counts,
  pain points, promises made) are the onboarding inputs. Read them before the kickoff.
- **msp-legal** owns the paper gates below. If a gate fails, work does not start.
- **msp-website-setup** owns new website builds and taking over an existing site. A client
  whose only managed line is Website Care onboards through that skill, not the full process
  here.
- **msp-pricing** owns the onboarding project price. Onboarding and migration are always billed
  separately at break-fix rates, never absorbed into the monthly. If the project was not quoted
  before signature, quote it now before scheduling work.
- **msp-brand** governs every message a client sees, including the welcome email below.
- **msp-technical-writing** sets the prose form. The 30-day runbook, credential collection
  lists, and internal notes are Zone 1 (strict mode for steps). The welcome email follows
  msp-brand. Any setup steps for client users inside it are Zone 2.
- **msp-helpdesk** is where the client lands at day 30: priorities, targets, and intake.
- **msp-qbr** picks up the roadmap seeded by the 30-day review, roughly 90 days in.

---

## Gate Zero: Before Any Work Starts

Verify all of these. A missing gate is a stop, not a note.

1. **Countersigned MSA plus a signed Service Order (or SOW)** on file for this client. Verify
   against the actual signed documents, not memory. (If your Service Order template is not yet
   finalized, whatever paper this client actually signed governs.)
2. **Onboarding project approved.** Scope and price per msp-pricing, at break-fix rates. If
   the fee was waived or discounted under the bundle discount, the signed SOW must state the
   percentage and the signed Service Order must carry the clawback. A waiver that exists only
   in an email fails this gate.
3. **Regulated data check.** Education, healthcare, financial, or legal clients: the DPA or BAA
   gate applies before {{COMPANY_NAME}} touches regulated data. If regulated data is in scope
   (student records, health information, financial data, and the like) and the DPA or BAA
   addendum is not signed, or you have not yet built one, escalate to the owner and msp-legal
   before deploying anything that touches that data. State privacy law and sector-specific
   regulation may also apply; that determination runs through msp-legal.
4. **Certificate of insurance** sent if the client requested one.
5. **Discovery notes in hand** from msp-sales: the counts the price was built on.

---

## The 30-Day Runbook

Four overlapping phases. Days are targets, not law; the sequence is the law.

### Phase 1: Kickoff and Access (Days 1 to 5)

- Send the welcome email (template below) within one business day of signature.
- Create the client in your PSA (ticketing) system: contacts, sites, agreement, billing setup
  matching the Order.
- Hold the kickoff call. Agenda: introduce the team, confirm the main point of contact and an
  emergency contact, agree communication channels, walk the credential list, set expectations
  for the next four weeks, confirm any scheduled downtime windows.
- Collect credentials (checklist below). Everything goes into the password vault immediately.
  Never store credentials in tickets, email threads, or loose documents.
- Establish how their staff will reach the help desk from day one, even while setup is underway.

**Credential and access collection checklist:**

- Their email and productivity platform admin (create a {{COMPANY_NAME}}-controlled admin,
  confirm a client-owned break-glass admin exists too)
- Domain registrar and DNS host
- Website: where it is hosted and who holds the account. If {{COMPANY_NAME}} will manage it
  (Website Care), the site moves to or stays in a hosting account in the client's name per
  msp-website-setup; never into a {{COMPANY_NAME}}-owned account
- Email security or spam filter portal, if any
- Firewall and router admin
- Switches and wireless access points
- ISP account numbers and support PINs, per site
- Backup platform
- Server and NAS local admin accounts
- Line-of-business applications, plus vendor support contract details and account numbers
- VoIP portal, printer and copier vendor, alarm and camera systems, as applicable
- Software license keys and any prior password manager export
- Previous IT provider contact, if a handoff conversation is possible

### Phase 2: Deploy and Discover (Days 3 to 10)

- Deploy the RMM agent to every managed machine. Coordinate timing so nobody gets interrupted.
- Roll out your endpoint protection (EDR/AV) platform to managed computers. Account-only users
  have no managed endpoint; nothing deploys to their personal devices.
- Macs in the fleet: enroll in your Mac device management (MDM) platform per what was sold.
- **Document the environment as found, before changing it.** Asset inventory (RMM sweep plus a
  manual pass for what agents cannot see), server roles, backup status, patch levels, security
  posture. This baseline is protective in two directions: it proves what {{COMPANY_NAME}}
  inherited, and the MSA's ransomware cost allocation carries a negligence carveout, so a dated
  record showing the starting condition and {{COMPANY_NAME}}'s diligence matters if anything
  ever goes wrong. Assess security against the msp-security Tier 1 baseline
  (`references/client-baseline.md` in that skill), documenting each control as found.
- Test a backup restore. "Backups are running" is not the same as "backups restore." If there
  are no working backups, that is an urgent finding: tell the client in plain terms and quote
  the fix as a project immediately.
- **Printer inventory:** record every printer (make, model, connection type). Business-class
  networked printers go on the Managed Printer line (msp-pricing). Flag consumer-grade,
  inkjet, or USB-attached units as nonstandard: excluded from the monthly, best-effort hourly
  only, with a written replacement recommendation (a ~$300 business laser costs less than
  three nightmare tickets). Confirm vendor warranty status on covered printers so the liaison
  commitment is deliverable.

### Phase 3: Stabilize and Harden (Days 8 to 20)

- Remove the previous provider's access: their RMM agents, their admin accounts, their remote
  access tools. Document what existed before removing it.
- Rotate shared and admin credentials into the vault.
- Harden to the msp-security Tier 1 baseline. Gaps that cannot close in onboarding get a
  remediation date or a signed Risk Acceptance Waiver (msp-legal).
- Enforce MFA on every user account and every admin account. Not optional and not tied to what
  was sold; a client that declines signs a Risk Acceptance Waiver (msp-legal).
- Set the patching policy and maintenance windows in the RMM.
- Check email security basics (SPF, DKIM, DMARC) and fix what is broken.
- Deploy ZTNA if it was sold.
- Remediate the backup gaps found in Phase 2.

### Phase 4: Document, Review, Hand Off (Days 20 to 30)

- Finish the documentation set: network map, license inventory, vendor contact list, and the
  agreed process for adding and removing users.
- Tune monitoring so alerts are meaningful. An alert nobody acts on trains everyone to ignore
  alerts.
- Verify billing matches reality: the user and device counts now known versus the counts on the
  Order. Deltas go to the Change Order conversation (msp-legal and msp-pricing), raised
  plainly and early. Undiscovered devices are normal; silently absorbing them breaks the margin.
- Announce the help desk to the client's staff: how to reach support, what to include, what to
  expect (per msp-helpdesk).
- Hold the 30-day review with the owner or main contact: what was found, what was fixed, what
  remains as a risk, and a first sketch of the roadmap. This meeting seeds the first QBR.
- Any document file from this phase (the 30-day review summary, the roadmap sketch, or a
  documentation export) follows msp-brand section 4 (Document Versioning).

**Definition of done:** all agents deployed and reporting, backups verified by a test restore,
prior provider access removed, credentials vaulted, documentation set complete, billing counts
verified, staff knows how to get help, 30-day review held.

---

## When Discovery Diverges From the Deal

- **Counts differ from the Order:** raise it in the 30-day review at the latest. The fix is a
  Change Order, not a quiet subsidy and not a surprise invoice.
- **Client declines a recommendation** (MFA, a backup fix, replacing an end-of-life machine):
  get the refusal in writing. If you have not yet built a Risk Acceptance Waiver template, a
  plain confirmation email ("You have asked us not to X; our recommendation remains X because
  Y") is the minimum record. Flag the pattern to msp-metrics at review time.
- **Prior provider is hostile or unreachable:** document every attempt and every finding, change
  all credentials early, and keep the client informed in neutral language. Never badmouth them
  to the client.

---

## Welcome Email Template

Apply msp-brand. Plain English, warm, no em dashes.

> **Subject: Welcome to {{COMPANY_NAME}}**
>
> Hi [First name],
>
> Welcome aboard. We are glad to have [Company] with us, and we are ready to take IT off your
> plate.
>
> Here is what happens next:
>
> 1. **Kickoff call.** [Name] will reach out today to schedule a short kickoff, ideally this
>    week.
> 2. **Getting set up.** Over the first couple of weeks we will install our management tools on
>    your computers, check your backups and security, and gather the account details we need. We
>    will coordinate timing with you so nobody gets interrupted.
> 3. **Your new help desk.** Starting [date], when something breaks or anyone has a question,
>    email {{SUPPORT_EMAIL}} or call {{PHONE}}. That is the fastest way to reach us.
>
> You do not need to prepare anything right now. We will bring a short list to the kickoff and
> walk through it together.
>
> Thanks for trusting us with this.
>
> [Name]
> {{COMPANY_NAME}}
> {{TAGLINE}}
> {{DOMAIN}} · {{INFO_EMAIL}} · {{PHONE}}

---

## Setup Decisions

Values below are the shipped example defaults from a working MSP. Decide your own before this
goes live.

- **Client-facing support intake address.** The example default is a single primary support
  address ({{SUPPORT_EMAIL}}) with an alias ({{SUPPORT_ALIAS_EMAIL}}) that also opens a ticket,
  and only the primary address gets printed in client-facing templates. Choose your own primary
  and alias addresses and update the welcome email and every other template accordingly.

Standing rule, unchanged: the 30-day arc and phase timing above are internal rhythm, not a
client promise. Do not commit dates in writing beyond what the onboarding project scope states.
