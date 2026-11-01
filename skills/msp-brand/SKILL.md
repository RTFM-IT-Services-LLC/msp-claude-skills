---
name: msp-brand
description: >
  Use this skill whenever generating ANY document, marketing material, email, proposal, slide deck,
  or other customer- or internal-facing content for your MSP, so that naming, visual style, and
  voice stay consistent. Triggers include any request to create, write, design, or format content
  "for us", "for my MSP", "on brand", "branded", or anything that will carry the company's name,
  logo, colors, or voice: flyers, one-pagers, case studies, cold emails, sales scripts, proposals,
  decks, social posts, letterhead, email signatures, or web copy (content and voice only; site
  build and hosting is msp-website-setup). Always load this skill before
  producing branded output, and apply it alongside content skills like msp-sales, msp-marketing,
  msp-pricing, docx, and pptx.
---

# MSP Brand Details

This skill is the single source of truth for how your MSP looks and sounds. Apply it to every piece
of branded content. When this skill conflicts with a generic template, this skill wins.

---

## Setup: fill this in first

This skill is the one place in the whole suite where your company's identity lives. No other skill
states your name, tagline, colors, fonts, contact details, or voice; they all defer here. That
means this file is the single source of brand truth, and it is only as good as what you put in it.

Before you use any other skill in this suite:

1. **Fill in every section below completely.** Work top to bottom: identity, visual style, voice.
2. **Replace every double-brace placeholder token** (the canonical list lives in msp-setup) with
   your real value. These same tokens appear across the other skills; setting them here is what
   makes the rest of the suite speak in your name.
3. **Fill in the tables** for colors, typography, and logo files, then **delete the "Example"
   rows and any example-only guidance** so nothing ships but your own values.
4. **Drop your logo files into this folder** (`msp-brand/`) and list them in the logo table.

Until this file is filled in, treat the other skills as unbranded. Do not send anything
client-facing until every double-brace placeholder token and every example value here has been
replaced with yours.

---

## 1. Identity & Naming

**Legal entity:** {{COMPANY_LEGAL_NAME}}

**Use in content:**
- Default name in most materials: **{{COMPANY_NAME}}**.
- Use the full legal name **{{COMPANY_LEGAL_NAME}}** in contracts, proposals, invoices, footers,
  and any legal or formal document.
- Decide on one short form of your name and use it consistently once the full name has appeared, or
  in casual/internal contexts. Pick a short form that reads cleanly and does not accidentally
  repeat a word (for example, do not let a short name that already contains "IT" turn into "IT IT
  Services" when you append "IT Services").

**Naming rules (write your own here, then keep them):**
- If your company name is an acronym or initialism, decide once whether you ever spell it out in
  customer-facing materials, and write that rule here. Many strong brands never expand the acronym
  and let the name and tagline carry the meaning; others always expand it. Either is fine, but be
  consistent, and if any expansion of the acronym is off-brand or off-color, state plainly that it
  is never used.
- Note any other hard naming rules that protect the brand (capitalization, spacing, what never to
  abbreviate). Keep this list short and absolute so there is no ambiguity later.

**Tagline / slogan:** {{TAGLINE}}
- A good tagline is short, plain, and says what the client gets, not what you do technically. Aim
  for something a non-technical owner would repeat back to you. Test it by reading it aloud: if it
  sounds like a slogan a real person would say, keep it; if it sounds like ad copy, cut it down.
- Use it as a headline, an email sign-off line, a footer, or a hero statement.
- Capitalize it as a title when used as a tagline; sentence case is fine in running copy.

**Contact details (use exactly as written):**
- Website: **{{DOMAIN}}**
- Email: **{{INFO_EMAIL}}**
- Phone: **{{PHONE}}**
- Location: **{{STATE}}.** Decide how specific to be. Keeping it to a state or region (for example
  "Serving businesses {{SERVICE_AREA}}") reads well before you want to publish a street address.

**Standard email signature (the standing format):**

```
[Name]
{{COMPANY_NAME}}
{{TAGLINE}}
{{DOMAIN}} · {{INFO_EMAIL}} · {{PHONE}}
```

Use this block for email signatures and as the default contact footer pattern in documents.
The middot-separated contact line (`{{DOMAIN}} · {{INFO_EMAIL}} · {{PHONE}}`) is the standard
one-line contact format anywhere contact details appear.

---

## 2. Visual Style

### Color palette

Fill in your own palette below. A good starting point is one signature primary color, a darker
shade of it for hover/pressed states, one secondary accent that supports the primary without
competing with it, a soft tint for backgrounds, and a set of neutrals for text, surfaces, and
lines. Pick a primary and secondary that are clearly different in hue so they never read as "almost
the same color." For accessibility, make sure body text meets a contrast ratio of at least 4.5:1
against its background (large headings can go to 3:1); check your text-on-primary and
text-on-tint pairs specifically, since those are the ones that usually fail. Avoid pure black
(`#000000`) for text; a near-black reads softer.

The **Example** column below shows the shape of a finished palette only. Replace every HEX with
your own value and delete the Example column before shipping.

| Role | Your name | Your HEX | Example (delete) | Use for |
|------|-----------|----------|------------------|---------|
| Primary |  |  | `#E57D31` | Logo background, primary buttons, headers, links, highlights, accent rules |
| Primary (dark) |  |  | `#C96A20` | Hover/pressed states, darker accents |
| Secondary |  |  | `#369EC9` | Secondary accents, icons, supporting highlights |
| Tint |  |  | `#FDF0E6` | Page/section backgrounds, callout boxes, soft fills behind text |
| Text |  |  | `#1A1A1A` | Body text and headings |
| Text (muted) |  |  | `#555555` | Secondary/supporting text, captions |
| Surface |  |  | `#FFFFFF` | Default background |
| Line |  |  | `#E8E8E8` | Dividers, card borders, rules |

**Usage guidance:**
- Lead with your **primary** as the signature color; use it deliberately for emphasis (buttons, key
  headers, accents), not as large fill areas. Use the **darker primary** for hover/active states.
- Your **secondary** is an accent; use it sparingly alongside the primary, not as a co-lead.
- Use your **tint** for soft section backgrounds to keep materials warm rather than stark white.
- Use your **text** color for body copy and your **muted text** color for secondary text.
- Keep contrast accessible: dark text on tint/white; white or light text on your primary or on
  near-black.

### Typography

Fill in your own type choices below. A common, safe pattern is one sans-serif for headings and one
for body, plus a widely installed system font as a fallback for Word and email where web fonts do
not load. Pick fonts that are legible at small sizes and that you have the license to use. Note the
weights you use for headings, sub-headings, and body so documents stay consistent.

The **Example** column shows the shape only. Replace with your own and delete the Example column
before shipping.

| Role | Your font | Weights | Example (delete) |
|------|-----------|---------|------------------|
| Headings |  |  | Poppins, 700 for h1/h2, 600 for sub-headings and buttons |
| Body |  |  | Inter, 400 for body, 500 for emphasis |
| Document fallback |  |  | Calibri or Arial where web fonts are unavailable |

Use the document fallback in Word, email, and anywhere your web fonts cannot load, so layouts stay
clean.

### Logo

Drop your logo files into this folder (`msp-brand/`) and list them in the table below. Ship, at a
minimum, a **full lockup** (your mark plus your wordmark), an **icon/logomark** (the mark alone for
small spaces), and a **single-color or grayscale** variant for black-and-white printing. If your
logo reads better on different surfaces with different backgrounds (for example a badged version
for light pages and a dark-tile icon for light backgrounds), include those variants too.

Fill in the filenames you actually add. The **Example** column shows the shape only; delete it once
you have listed your own files.

| Your filename | What it is | Example filename (delete) | Use for |
|---------------|-----------|---------------------------|---------|
|  | Full lockup, color, mark + wordmark | `logo-full-color.png` | **Primary logo.** Most documents, decks, email signatures, headers |
|  | Full lockup, color, no badge, on light | `logo-full-nobadge.png` | Placing the logo directly on a light background without a badge |
|  | Full lockup, grayscale + wordmark | `logo-full-bw.png` | Black-and-white printing, single-color contexts |
|  | Logomark only, on primary-color tile | `icon-primary.png` | App icon, avatar, favicon, social profile picture, small spaces |
|  | Logomark only, on dark tile | `icon-dark.png` | Avatar/icon on light backgrounds where a dark tile reads better |

**File specs to record (fill in for your files):**
- Note the pixel dimensions of each file so anyone placing them knows what they are working with.
- Note whether files are flattened (solid background) or transparent PNGs. If you need to overlay
  your mark on a photo, keep a transparent-background cutout on hand.

**Usage rules:**
- Default to your **full color lockup** wherever space allows.
- Use the **icon** variants only where the full wordmark will not fit or is not needed (favicons,
  avatars, watermarks).
- Pick the variant whose background suits the surface: a badged or dark-tile icon on light pages;
  the no-badge lockup directly on light or tinted backgrounds.
- Maintain clear space around the logo equal to a consistent unit you define (a common choice is
  the height of the first letter of the wordmark).
- Do not stretch, squash, rotate, recolor, add shadows or effects, or alter the mark's elements.
- Do not place the color logo on a busy photo or a background that clashes with your primary color.
  Use a solid neutral, tinted, or dark panel behind it.

### Imagery
- Prefer clean, approachable imagery: real small-business settings, friendly team/people, simple
  iconography. Avoid clichéd "hacker in a hoodie" or overly corporate stock photos.
- Keep visuals warm and human, matching a customer-service-first positioning.

---

## 3. Voice & Tone

*(This section is the source of truth for your brand voice. msp-sales and msp-pricing defer to it.)*

**Brand personality in a phrase:** the friendly expert who handles the hard stuff so the client
does not have to. Plain-spoken, reassuring, confident, never condescending. Selling and serving are
the same thing. (Adjust this phrase to fit your own positioning, but keep it to one sentence a new
hire could act on.)

**Two registers:**

- **Customer-facing content** (emails, proposals, web, case studies, flyers): Friendly, warm, and
  **jargon-free**. Speak to business owners, not IT people. Focus on **outcomes** (save time,
  reduce risk, stay focused on your business), not on tech specs.
- **Internal / salesperson-facing content** (scripts, playbooks, enablement): Motivating,
  action-oriented, and clear. Help the reader feel confident and know exactly what to do next.

**Prose form (msp-technical-writing):** Everything that is not marketing or direct customer
communication follows msp-technical-writing. Its rules set the sentence form, and the internal
register above sets the tone for internal content. In customer-facing
content, this section owns the voice. msp-technical-writing applies there only to the
technical parts: step-by-step instructions, troubleshooting steps, and descriptions of a
technical process. Those parts still use the plain-English words below.

**Punctuation, no em dashes:** Do not use the em dash in your content. Overusing it is a strong tell
that text was AI-generated, and it turns readers off. Default to commas, periods, parentheses, a
colon, or restructuring the sentence instead. Only use an em dash in the rare case where a human
would genuinely and naturally write one. This applies to all content, customer-facing and internal.

**Plain-English rule (use these, not those):**
- "IT problems" (not "infrastructure incidents")
- "your computers and phones" (not "endpoints" or "devices")
- "keep your data safe / back up your files" (not "data resiliency posture")
- "someone to call when something breaks" (not "incident response SLA")

**Do:**
- Lead with the customer's problem or goal, in their words.
- Keep sentences short and concrete. One idea per sentence.
- Be specific about benefits ("get back the hours you lose when computers crash").
- Sound like a helpful neighbor recommending a service, not a polished ad.

**Avoid:**
- Tech jargon and acronyms in customer materials (define or replace them).
- Fear-based or pushy selling. Sell through empathy and trust.
- Hype words and filler ("cutting-edge," "synergy," "world-class," "leverage").
- Em dashes (see the punctuation rule above).
- Overstated service-area claims: never claim statewide or wider coverage than you actually
  serve. Name the area you truly cover ({{SERVICE_AREA}}) and keep marketing copy inside it.

**Audience (describe your target client):** Write to your actual buyer. As a labeled example, one
working MSP defines its audience as: *small to medium-sized businesses, owners and office managers
at companies of roughly 25 to 75 employees with no dedicated IT staff, often currently
reactive/break-fix, and the message is written to the non-technical decision-maker.* Replace that
with your own client profile: who they are, roughly how big, whether they have any internal IT, and
which person actually makes the buying decision.

---

## 4. Document Versioning

Claude often revises one document several times. Without a version system, the revisions share
one name and people confuse them. This section gives every generated file a version in its file
name and a matching stamp on the document. Every skill that produces a file follows it.

### Scope

The standard applies to every document Claude generates for {{COMPANY_NAME}}, internal or
client-facing:

- Office files and PDFs: .docx, .xlsx, .pptx, and .pdf
- Markdown and text files: .md and .txt (for example, dossiers, runbooks, and plans)
- Claude artifacts that are documents: Docs, Slides, and Sheets artifacts, and hand-built pages
- Client-facing documents: proposals, quotes, contracts, QBR scorecards, and letters

It does not apply to:

- Text that Claude writes only in the chat (emails, social posts, and scripts to paste)
- Files in a git repo, such as a client website's `COMPANY-INFO.md`, a skill file, or a master
  template in the kit's `templates/` folder. Git keeps their versions. A document filled from a
  template follows this standard.
- A file whose name a system sets (for example, `index.html` or `SKILL.md`)
- Artifacts that are working tools, not documents (for example, the msp-social review page)

### File name

Pattern: `<subject>-<doc-type>-<yyyy-mm-dd>-v<major>.<minor>.<ext>`

| Part | Rule | Examples |
|------|------|----------|
| `<subject>` | The client or prospect, as a short slug. Use `{{COMPANY_SLUG}}` for internal documents about {{COMPANY_NAME}} itself. | `acme-dental`, `{{COMPANY_SLUG}}` |
| `<doc-type>` | One to three words for the document type. If the document covers a period, add the period as a word. | `proposal`, `service-order`, `qbr-scorecard-q4`, `monthly-review-october` |
| `<yyyy-mm-dd>` | The date of this revision (the day Claude generated the file), in {{TIMEZONE}}. It changes with each revision. | `2026-11-03` |
| `v<major>.<minor>` | The version number. See Version Number below. | `v1.0`, `v1.1`, `v2.0` |

- Use lowercase letters, numbers, hyphens, and the dot in the version only. No spaces and no
  underscores.
- Keep `<subject>` and `<doc-type>` the same for every revision of one document. Then all the
  revisions sort together in a folder.
- The revision date is the only numeric date in the name.

The history of one proposal:

```
acme-dental-proposal-2026-11-01-v1.0.docx   first draft
acme-dental-proposal-2026-11-01-v1.1.docx   typo and layout fixes
acme-dental-proposal-2026-11-02-v1.2.docx   reworded the summary
acme-dental-proposal-2026-11-05-v2.0.docx   v1.2 went to the client, then the price changed
```

Exception: msp-leadgen puts the type first (`prospects-springfield-2026-08-01-v1.0.xlsx` and
`dossier-acme-dental-2026-08-01-v1.0.md`), so that all prospect lists sort together.

### Version Number

- A new document starts at v1.0.
- Raise the major number (v1.3 to v2.0) if one or both of these conditions are true:
  - The content changed: a price, scope, term, date, recommendation, or structure (a section
    added or removed).
  - The previous version went to someone outside {{COMPANY_NAME}} (a client, a prospect, or a
    referral partner).
- Otherwise, raise the minor number (v1.3 to v1.4). Minor changes are wording, typos,
  formatting, and layout.
- If the change is minor and you do not know whether the previous version was sent, ask the user.
- After v1.9 comes v1.10, not v2.0.
- Never reuse a number. Save each revision as a new file and leave the earlier files in place.

### The Stamp

- The stamp text is the exact file name without the extension. Example:
  `acme-dental-proposal-2026-11-03-v1.1`.
- Style: 8 pt, your muted text color from the palette table, in your body font (or the document
  fallback). No label and no bold.
- The stamp and the file name always match. When the name changes, change the stamp.
- In Office files, also set the document Title property to the stamp text.

| Format | Where the stamp goes |
|--------|----------------------|
| .docx | The footer of every page, left aligned, on its own line below any page number or contact line |
| .pdf | The same place as in .docx. A PDF exported from a stamped .docx already has it. |
| .pptx | A small text box at the bottom left of every slide, including the title slide |
| .xlsx | The left section of the print footer on every sheet |
| .md | The last line, after a blank line, in italics: `*dossier-acme-dental-2026-11-01-v1.0*` |
| Published .md (for example, a resources article for {{DOMAIN}}) | The last line as an HTML comment, so that the stamp never shows on the site: `<!-- {{COMPANY_SLUG}}-article-phishing-2026-11-01-v1.0 -->` |
| .txt | The last line, after a blank line, as plain text |
| Artifact | Add the version to the end of the title ("Acme Dental Proposal v1.1"). Docs: put the stamp on the last line. Slides: bottom left of every slide. Sheets: a note below the data. |

For an artifact, revise the same artifact. Its history keeps the earlier versions. Change the
title and the stamp on every revision.

### Before You Make a Revision

1. Find the latest version. Look at the files in this conversation: the files you made and the
   files the user attached.
2. If you find it, read its version from the file name.
3. If the file name and the stamp do not match, ask the user which one is correct.
4. If you cannot find an earlier file (for example, in a new chat), ask the user to attach the
   latest file or to tell you its version. Do not guess.
5. Do not search folders or file sync services for the file unless the user points to a
   location.
6. Pick the next number with the Version Number rules.
7. Save the revision as a new file with the new name and the new stamp.
8. In your reply, give the new version and one line about what changed. Example: "v1.1: fixed
   two typos and the table layout."

---

## Quick Reference (paste-ready)

- **Name:** {{COMPANY_NAME}} (legal: {{COMPANY_LEGAL_NAME}})
- **Tagline:** {{TAGLINE}}
- **Web / Email / Phone:** {{DOMAIN}} · {{INFO_EMAIL}} · {{PHONE}} · {{STATE}}
- **Signature:** Name / {{COMPANY_NAME}} / tagline / contact line
- **Colors:** fill in your primary, dark primary, secondary, tint, and near-black from the palette table
- **Fonts:** fill in your heading font, body font, and document fallback from the typography table
- **Logo:** your full color lockup is the default; icons for small spaces; grayscale for single-color
- **Voice:** Friendly expert. Plain English. Outcomes over specs. Empathy over fear.
- **Files:** `<subject>-<doc-type>-<yyyy-mm-dd>-v1.0.<ext>`, a footer stamp that matches the file
  name (8 pt, muted text color), and a new file for every revision (section 4).
- **Prose form:** msp-technical-writing for everything except marketing and direct customer
  communication, and for steps or instructions inside those.
- **Never:** jargon in client copy; fear-based selling; em dashes.
