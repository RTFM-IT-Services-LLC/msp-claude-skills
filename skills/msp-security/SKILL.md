---
name: msp-security
description: >
  Use this skill for security standards at your managed IT services (MSP) business, in both
  directions: the baseline every managed client must meet (MFA, endpoint protection, email
  security, backups, admin access, offboarding) and how the MSP secures itself (RMM hardening,
  the credential vault, admin separation, partner-delegated admin access into client tenants,
  our own devices). Trigger on "security baseline", "security standard", "harden this tenant",
  "is this client secure enough", "security assessment", "cyber insurance questionnaire", "can
  we say we're compliant", HIPAA, FTC Safeguards, WISP, CMMC, PCI, CIS Controls, "lock down our
  RMM", or any question about what controls a client or our MSP should have. msp-helpdesk owns
  incident response; msp-maintenance owns patch and backup cadence; this skill owns the
  standard they deliver against. Apply alongside msp-onboarding, msp-qbr, msp-legal,
  msp-pricing, msp-client-comms, and msp-sales.
---

# {{COMPANY_NAME}} Security Standards

**Defaults you must review:** the specific tiers, thresholds, cadences, and review rules in this
skill and its reference files are shipped example defaults from a working MSP. Review and replace
them with your own before anything goes client-facing (see Setup Decisions at the bottom).

This skill is the source of truth for what "secure" means at {{COMPANY_NAME}}. It has two
halves, and both matter equally:

1. **The client baseline:** the controls every managed client environment must have, how
   {{COMPANY_NAME}} verifies them, and what happens when a client declines one.
2. **The house standard:** how {{COMPANY_NAME}} protects itself. An MSP holds the keys to every
   client at once, which makes {{COMPANY_NAME}} a more valuable target than any single client. A
   compromise of {{COMPANY_NAME}}'s tooling is a compromise of every client (msp-helpdesk covers
   that scenario's response).

The detail lives in three reference files. Read the one the task needs:

- `references/client-baseline.md`: the full client control checklist by domain, each control
  with its tier, how to verify it, and the evidence that proves it.
- `references/msp-house-security.md`: {{COMPANY_NAME}}'s own security standard as an MSP.
- `references/compliance-overlays.md`: extra controls and attorney flags for regulated
  verticals (accounting and tax, legal, healthcare, manufacturing and defense, card payments,
  education and childcare) plus state law touchpoints for {{STATE}}.

**Status:** controls already set elsewhere in the suite are marked as inherited; everything
else is a recommended default until you confirm it (see Setup Decisions). Run the work by these
standards once confirmed; they become contractual for a client only through that client's signed
paper (msp-legal).

---

## The Frameworks We Align To

{{COMPANY_NAME}} does not invent its own security framework. It aligns to public ones, which
makes the baseline defensible to insurers, auditors, and attorneys:

| Framework | What {{COMPANY_NAME}} uses it for |
|---|---|
| CIS Critical Security Controls v8.1, Implementation Group 1 (IG1) | The yardstick for the client baseline. IG1 is the "essential cyber hygiene" set sized for small businesses with no security staff: the typical small-MSP market. |
| CISA/NSA/FBI joint advisory AA22-131A, "Protecting Against Cyber Threats to Managed Service Providers and their Customers" (May 2022), plus CISA's MSP and SMB hardening guidance | The yardstick for the house standard. |
| NIST Cybersecurity Framework 2.0 (Govern, Identify, Protect, Detect, Respond, Recover) | Shared vocabulary for QBRs, insurers, and regulated clients. Map findings to its six functions when a client or auditor asks. |
| Vendor secure baselines (your email and productivity platform's security score or security health report, CIS Benchmarks for Windows and macOS) | Configuration detail for specific platforms. |

**Language rule (non-negotiable in anything a client or prospect sees):** {{COMPANY_NAME}}'s
controls are "aligned with" or "based on" these frameworks. Never write or say that
{{COMPANY_NAME}} or a client is "compliant", "certified", "HIPAA certified", "fully secure",
"hack-proof", or "guaranteed". No one can certify HIPAA compliance, and a security guarantee is
a warranty {{COMPANY_NAME}} cannot keep and the MSA does not give. Say what is in place and how
it is verified. Voice per msp-brand.

---

## The Client Baseline: The Short Version

Every managed client gets these. They are what the managed fee delivers. Full detail, verify
steps, and evidence for each are in `references/client-baseline.md`.

**Tier 1, Baseline (every managed client, included in the managed service):**

1. **MFA on every user account** in the client's email and productivity platform, and on every
   admin console {{COMPANY_NAME}} manages. Legacy authentication blocked. No exceptions
   without a signed Risk Acceptance Waiver (inherited from msp-onboarding).
2. **Separate, named admin accounts.** No daily-driver account holds admin rights. No shared
   admin logins. A client-owned break-glass admin exists and is documented (inherited from
   msp-onboarding).
3. **Endpoint protection (your EDR/AV platform) on every managed computer and server**,
   reporting to {{COMPANY_NAME}}, tamper protection on (inherited from msp-pricing and
   msp-onboarding).
4. **Supported operating systems and software only.** Anything past end of support is a
   finding with a replacement date or a signed waiver.
5. **Patching on the msp-maintenance cadence**, including firmware on firewalls, switches,
   and access points (inherited).
6. **Backups with a copy the attacker cannot reach:** 3-2-1 with at least one immutable or
   offline copy, cloud mailboxes and files included, test restores on the msp-maintenance
   cadence (cadence inherited; immutability is the recommended default).
7. **Email authentication and filtering:** SPF, DKIM, and DMARC published and passing, with
   DMARC moving toward enforcement; external-sender tagging; auto-forwarding to outside
   domains blocked by default.
8. **Disk encryption** (the operating system's built-in full-disk encryption) on every managed
   laptop, keys escrowed where {{COMPANY_NAME}} can retrieve them.
9. **Firewall with no unnecessary inbound exposure:** no RDP or admin interfaces open to the
   internet, default passwords changed, remote access only through an approved path (ZTNA if
   sold, otherwise MFA-protected VPN).
10. **Same-day offboarding:** departing staff lose access the day they leave, including
    sessions, tokens, and mobile devices (process in `references/client-baseline.md`).
11. **Security awareness basics:** new-staff security orientation at onboarding and
    {{COMPANY_NAME}} security advisories when an active threat is relevant (msp-client-comms).
12. **Documented:** every control above recorded in the client's documentation with its last
    verified date.

**Tier 2, Recommended (quoted per client through msp-pricing, strongly advised):**
phishing-resistant MFA for admins and finance staff, conditional access or device-compliance
policies, DNS filtering, advanced email threat protection, a formal phishing-simulation and
training program, mobile device management for company phones, dark-web credential monitoring,
and an annual written risk assessment.

**Not offered (shipped default):** EDR, SIEM, and 24/7 managed detection and response. The
default assumes {{COMPANY_NAME}} does not operate a SOC and has no MDR partner. If a client or
its insurer requires these, scope it case by case at that point; never promise it in a
proposal. If you do offer them, see Setup Decision 1.

**Tier 3, Regulated overlays:** whatever the client's regulatory regime adds on top. See
`references/compliance-overlays.md`. Always an msp-legal conversation; an attorney licensed in
{{STATE}} confirms which regime applies.

**When a client declines a Tier 1 control:** {{COMPANY_NAME}} does not quietly skip it. Explain
the risk in plain English, then get the Risk Acceptance Waiver signed
(`templates/msp-risk-acceptance-waiver-template.docx`, msp-legal). A declined control stays on
the QBR scorecard as a red or yellow item with the waiver noted. A client who declines several
Tier 1 controls is a fit conversation for msp-metrics, because {{COMPANY_NAME}} carries the
reputational and practical risk of an environment it cannot protect.

---

## The House Standard: The Short Version

Full detail in `references/msp-house-security.md`. The rules that matter most:

1. **Phishing-resistant MFA** (FIDO2 security keys or passkeys) on every {{COMPANY_NAME}}
   account that can touch a client: your PSA and RMM, the credential vault, the partner or
   delegated-admin portals for client email and productivity tenants, your own email and
   productivity admin, your endpoint protection console, your Mac MDM, your DNS and hosting
   provider, backup consoles, registrars, and {{COMPANY_NAME}}'s own email.
2. **The credential vault is the only home for client credentials.** Per-client separation,
   MFA on the vault, no credentials in tickets, email, chat, notes, or AI prompts (inherited
   rule from msp-onboarding, extended here).
3. **Least privilege and just-in-time access into clients.** Where the client's platform offers
   partner-delegated admin with granular, time-bound roles, use it with the narrowest roles,
   never a legacy broad delegation or standing global admin. Named {{COMPANY_NAME}} accounts,
   never shared ones, so every action traces to a person.
4. **The RMM is hardened like the crown jewel it is:** MFA enforced, minimum users with script
   rights, scripts reviewed before they run fleet-wide, audit logs reviewed, and remote-access
   sessions logged.
5. **{{COMPANY_NAME}} devices are managed to a higher bar than client devices:** encrypted,
   patched, endpoint-protected, and used for {{COMPANY_NAME}} work only.
6. **Logs kept long enough to investigate:** {{COMPANY_NAME}} tooling audit logs retained and
   exportable, at least 90 days searchable, longer where the platform allows.
7. **Vendor security reviewed** before {{COMPANY_NAME}} adopts a tool that touches client
   environments.
8. **{{COMPANY_NAME}}'s own incident plan is rehearsed:** the "our tooling is the vector"
   scenario in msp-helpdesk gets a tabletop walk-through at least once a year.
9. **AI tooling rule:** client credentials, secrets, and regulated data (ePHI, tax data,
   privileged legal material, card data) never go into AI tools. Anonymize client details
   where practical. The DPA names AI tooling as a subprocessor; stay inside what it allows.
10. **Insurance gate** (inherited from msp-legal): E&O plus cyber must bind before the first
    MSA signing.

---

## Security Assessments

**When:** during onboarding Phase 2 (document as found, before changing anything), again at
the 30-day review (what was fixed), and then annually for every managed client, timed to feed
a QBR. Also on request before a cyber insurance renewal.

**How:** walk `references/client-baseline.md` domain by domain. For each control record: in
place / partial / missing / waived, the evidence (screenshot, export, report, or log entry),
and the date checked. Pull the email and productivity platform's security score or security
health report as a supporting number, never as the whole assessment.

**Output:** an internal findings list (in the client's documentation) and a client-facing
summary in plain English, branded per msp-brand, with each gap stated as risk, fix, and rough
cost band from msp-pricing. Remediation inside the baseline is part of the managed service;
anything new (a project, a Tier 2 add-on) is quoted. When either output is a file, it follows
msp-brand section 4 (Document Versioning). Example:
`acme-dental-security-assessment-2026-11-01-v1.0.docx`.

**The QBR Security row (msp-qbr), scored from the assessment:**

| Score | Meaning |
|---|---|
| Green | Every Tier 1 control in place and verified within the last quarter; no open security incidents; no waivers. |
| Yellow | One or two Tier 1 gaps with a remediation date inside 90 days, or any Tier 1 control covered only by a signed waiver. |
| Red | MFA missing for any user, backups without a tested restore or without an unreachable copy, unsupported systems with no plan, or any Tier 1 gap with no remediation date and no waiver. |

Score honestly, per msp-qbr: a yellow {{COMPANY_NAME}} flags first builds more trust than a
green that should not be.

---

## Cyber Insurance Questionnaires

Clients will hand {{COMPANY_NAME}} their cyber insurance application and ask for help. This is
a high-stakes document: a materially false answer on an insurance application can give the
carrier grounds to deny a claim or rescind the policy.

- **The client signs the application, not {{COMPANY_NAME}}.** {{COMPANY_NAME}} supplies facts
  about the environment it manages; the client (with its broker) owns the answers.
- **Answer only from evidence.** Every "yes" {{COMPANY_NAME}} supports needs current evidence
  from the assessment. If a control is partial (MFA on email but not on the VPN), say exactly
  that. Never round a partial up to yes.
- **Questions outside {{COMPANY_NAME}}'s scope** (HR policies, wire-transfer verification
  procedures, vendor contracts) go back to the client; {{COMPANY_NAME}} does not guess.
- **Log what {{COMPANY_NAME}} provided** and when, in the client's documentation.
- **Turn gaps into a plan:** the questions a client cannot answer yes to are the best Tier 2
  conversation {{COMPANY_NAME}} will ever get, and they are why msp-sales leans on the
  insurance angle. Quote the fix through msp-pricing.
- Anything that looks like {{COMPANY_NAME}} attesting to a control in writing on the insurer's
  form, or a request for {{COMPANY_NAME}} to sign, goes to msp-legal first.

---

## Security Advisories to Clients

When an active threat is relevant to {{COMPANY_NAME}}'s clients (a phishing wave, a critical
vulnerability in software they run, a vendor breach), send the security advisory through
msp-client-comms. Rules: specific and actionable, no fear-mongering, no speculation, and say
what {{COMPANY_NAME}} has already done. If a client is actually affected, it is an incident,
not an advisory: msp-helpdesk's security track takes over.

---

## How This Skill Connects to the Suite

| Skill | What it takes from this one |
|---|---|
| msp-onboarding | Phase 2 assessment and Phase 3 hardening target the Tier 1 baseline here. |
| msp-maintenance | Delivers the recurring controls (patching, backups, monitoring) on its cadence; this skill defines what "done" means. |
| msp-helpdesk | Owns incident response. A failed control discovered during an incident becomes an assessment finding afterwards. |
| msp-qbr | Security row scored with the table above. |
| msp-legal | Waivers for declined controls, DPA and BAA gates, regulatory questions, insurance attestations. |
| msp-pricing | Every Tier 2 add-on and remediation project price. No prices in this skill. |
| msp-sales | Uses the baseline as a selling point, in "aligned with" language only. |
| msp-client-comms | Security advisories and anything client-facing about a control change. |
| msp-offboarding | {{COMPANY_NAME}} access removal at exit follows the house standard's access rules. |
| msp-technical-writing | Sets the prose form. Security standards, internal assessment findings, and hardening or incident procedures are Zone 1 (strict mode for steps). The client-facing assessment summary follows msp-brand. The fix for each gap is Zone 2. |

---

## Inherited Defaults (already set in sibling skills)

These are settled in other skills. If you change one there, keep this skill consistent.

- MFA enforced on every user and admin account, waiver if declined; client-owned break-glass
  admin; credentials only in the vault (msp-onboarding).
- Endpoint protection on essentially every managed computer; your Mac MDM platform for Macs;
  ZTNA where sold (msp-pricing, msp-onboarding).
- Patching and backup verification cadence (msp-maintenance).
- Security incident track, ransom stance, and the "our own tooling is the vector" scenario
  (msp-helpdesk).
- Declined recommendations get a signed Risk Acceptance Waiver (msp-legal).
- Insurance gate: E&O plus cyber bind before first MSA signing (msp-legal).
- Endpoint protection stays on the platform's plain (non-EDR) tier; no EDR tier (see Setup
  Decision 1).
- No EDR, SIEM, SOC, or MDR services offered; scope case by case when a client requires them
  (msp-sales service descriptions; change there first if you offer them).

## Setup Decisions

Settle these before this skill goes live for your shop. Each is shipped with a recommended
default; accept it, change it, or log a deferral.

1. **EDR, SIEM, and MDR offering.** Shipped default: none offered, endpoint protection stays on
   the platform's plain (non-EDR) tier, and a client that requires them is scoped case by case.
   Insurers increasingly ask for EDR by name, and most small MSPs have no after-hours human
   watching security alerts, so many shops will choose to standardize on an EDR-capable tier
   and offer MDR through a partner as Tier 2 (possibly Tier 1 for regulated clients). If you do,
   update the Tier 2 list and the "Not offered" paragraph here, the matching rows in
   `references/client-baseline.md`, msp-sales (service descriptions), and the msp-pricing cost
   model.
2. **Immutable backup copy as Tier 1.** Depends on your backup platform's capability; confirm
   the platform and whether every client's plan includes it.
3. **Named products for each layer:** credential vault, documentation system, backup platform,
   email security, DNS filtering, security awareness training. The skill names categories until
   you record your products (internally; keep them out of client-facing text unless you want
   them there).
4. **Security awareness in Tier 1 versus Tier 2.** Recommended default: orientation plus
   advisories in Tier 1, a formal training and phishing-simulation program in Tier 2.
5. **Annual assessment cadence and deliverable format.** Recommended default: annual, one-page
   summary plus internal findings list, feeding the next QBR.
6. **House standard specifics:** security key model and count per person with privileged
   access, the RMM script approval rule (recommended default: a second qualified person, the
   owner or a designated senior tech, reviews any script before a fleet-wide run; a one-person
   shop records its own rule here), and the log retention target.
7. **Healthcare, CUI, and card-data scope:** whether you take clients whose regimes need
   controls beyond your delivery model (see `references/compliance-overlays.md` for the
   recommended stance per vertical).
8. **{{STATE}} law touchpoints.** With your attorney, fill in the state law section of
   `references/compliance-overlays.md`: your state's reasonable-security and secure-disposal
   rules, breach notification deadline and attorney general threshold, consumer privacy law
   thresholds, and any service-provider requirements.
