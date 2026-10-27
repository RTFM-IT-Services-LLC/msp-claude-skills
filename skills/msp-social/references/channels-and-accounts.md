# Channels and Accounts

The {{COMPANY_NAME}} channel list, the example phases, the ownership rules, and the setup steps
for each platform. The setup steps and platform facts come from research checked October 2026.
Platform limits change, so check them again before a build session. Some platform help centers
blocked the research tools, so some steps come from recent third-party guides. Check each
screen as you go.

**Defaults you must review:** the channel list, the phases, the budget ceiling, and the post
counts in this file are shipped example defaults from a working MSP. Review and replace them
with your own (SKILL.md Setup Decisions 2, 4, and 10). The platform sizes and limits are
platform facts, not choices.

---

## Channel Table

| Channel | How it gets posted | Phase | Account identity | Notes |
| --- | --- | --- | --- | --- |
| {{DOMAIN}} resources | Claude commits to `dev`, the owner approves the preview, merge to `main` | 1 | Repo on your git hosting provider | Articles go live before the social posts that link to them. Mechanics: msp-website-setup. |
| Local business listing profile | Scheduling tool | 1 (free tier) | Your existing listing, or a new one. A second person added as Owner. | Text, images, or video. Video through the scheduling tool is not tested yet. |
| General social network page | Scheduling tool | 1 (free tier) | The platform's business account manager | Needs a real person's account behind it. Check what that account shows publicly. |
| Microblog platform | Scheduling tool | 1 (free tier) | Shared marketing mailbox | Check whether your scheduling tool charges extra for this channel. |
| Photo-first social platform | Scheduling tool | 2 (paid per-channel tier) | Shared marketing mailbox, linked to the general social page | Every post needs an image or video. |
| Video-sharing platform (including short-form video) | Scheduling tool | 2 (paid per-channel tier) | Brand channel | Uses the marketing pack videos. |
| Short-form video platform | Scheduling tool | 2 (paid per-channel tier) | Shared marketing mailbox | Every post needs media. Uses the marketing pack videos. |
| Conversation platform | Scheduling tool | 2 (paid per-channel tier) | Created from the photo-first account, if the platform works that way | Same handle as the photo-first account. |
| Professional network company page | Scheduling tool | 3 (paid per-channel tier) | Needs a personal profile as admin | If the Owner Visibility Rules apply, waits until the owner goes public. |
| Professional network, the owner's profile | Scheduling tool | 3 (paid per-channel tier) | The owner's personal account | If the Owner Visibility Rules apply, waits until the owner goes public. |
| Neighborhood platform | Manual | Manual | Shared marketing mailbox, business page | Manual posting only. The start date is a Setup Decision. |
| Community forum platforms | Not planned | None | None | See Community Forum Platforms, below. |

Per-platform post formats (lengths and structure) live in the msp-marketing format menu.

---

## Phases and Upgrade Triggers (example default rollout)

This is the shipped example rollout. Write your own channel list and phases here (SKILL.md
Setup Decision 2).

- **Phase 1 (free tier, no cost):** the local listing, the general social page, and the
  microblog platform. The owner reserves the phase 2 handles at the same time but connects
  nothing else.
- **Phase 2 (paid per-channel tier, 7 channels):** adds the photo-first platform, the
  video-sharing platform (including short-form video), the short-form video platform, and the
  conversation platform.
  - Trigger: the owner decides to upgrade. Example default: review after the first month of
    live posts.
  - Also consider it when the free-tier cap on scheduled posts per channel becomes a burden.
- **Phase 3 (paid per-channel tier, 9 channels):** adds the professional network company page
  and the owner's profile.
  - Trigger: the owner decides to add them. If the Owner Visibility Rules apply, the owner
    must first decide to go public. Nothing else unlocks this phase.
  - If the Owner Visibility Rules do not apply, consider adding the professional network
    earlier, because msp-marketing ranks it the priority B2B channel.

Cost logic per phase is in `scheduling-tool.md`. Example default budget ceiling: $200 per month
(shipped example default; set your own).

---

## Ownership Rules

1. If the Owner Visibility Rules apply (SKILL.md), keep the owner's name off every public
   profile until the owner decides to go public.
2. Use the shared marketing mailbox on {{DOMAIN}} as the login wherever a platform allows a
   business login: the scheduling tool, the photo-first platform, the short-form video
   platform, the microblog platform, and the neighborhood platform.
3. Make sure that the shared marketing mailbox is a licensed user mailbox in your email and
   productivity platform, not a group or distribution list. A group cannot own or manage a
   local listing profile.
4. The general social network and the professional network need a real person's account behind
   each page. Check what that person's account shows publicly before launch.
5. Turn on MFA for every account. Use a passkey or an authenticator app.
6. Store every login, recovery code, and the scheduling tool API key in the company password
   vault.
7. Use {{DOMAIN}} addresses for recovery email. Never use a personal email address.
8. Use one handle everywhere, based on {{COMPANY_NAME}} or {{DOMAIN}} (for example, the domain
   name without its extension). Pick fallbacks in order before setup (for example, add an
   underscore before a word, add "services", or add "_co"). Check handle availability before
   you set up any account.
9. Use the display name **{{COMPANY_NAME}}** everywhere.
10. Do not connect any social account to the membership's bundled posting tool.

---

## Setup Order

1. Confirm that the shared marketing mailbox is a licensed user with MFA. Add it to the vault.
2. In the membership's bundled posting tool, confirm that auto-import is off.
3. Add a second person to the local listing profile as an Owner.
4. Create the general social network's business account and the general social page.
5. Create the microblog account.
6. Reserve the handle on the photo-first platform, the short-form video platform, the
   video-sharing platform, and the conversation platform. Do not post yet.
7. Create the scheduling tool account and connect the local listing, the general social page,
   and the microblog platform (see `scheduling-tool.md`).
8. At the phase 2 upgrade, complete the phase 2 accounts and connect them to the scheduling
   tool.
9. At phase 3 (and, if the Owner Visibility Rules apply, only after the owner goes public), set
   up the professional network and connect both professional network channels to the
   scheduling tool.

---

## Setup Steps per Platform

### Local business listing profile

If the listing does not exist yet, create it as a service-area business with a hidden address.
Then:

1. Open the listing's settings, then its people and access page, then add a user.
2. Add the second person as an **Owner**, not a Manager. Managers cannot add or remove users.
3. Wait 7 days. New users cannot transfer primary ownership before then.

Platform facts (checked October 2026; platform limits change, check them again before a build
session):

- A post holds up to 1,500 characters of text, plus images or video. Whether your scheduling
  tool can send video to the local listing is not confirmed. Use one image until the build
  session tests a video post through the scheduling tool.
- The platform archives posts older than 6 months.
- The platform can reject a post that contains an unverified phone number.
- A group or distribution list cannot own or manage a profile.

### General social network page

1. Use an existing personal account on the platform, or create one. Turn on two-factor
   authentication.
2. In the platform's business account manager, create a business account.
3. Enter {{COMPANY_LEGAL_NAME}} and the shared marketing mailbox. Confirm the email.
4. Create the page inside the business account. Pick an IT services category. Use a service
   area, not a street address.
5. Add the second person as a full-control admin.
6. In the business account's security settings, require two-factor authentication.
7. Before the first post, view the page as a visitor. Open the page's transparency panel and
   confirm what it shows. If the Owner Visibility Rules apply, confirm that no personal name
   shows.

Not confirmed: whether the platform shows page admins publicly. Step 7 checks it directly.
Which person's account sits behind the page is a Setup Decision.

### Microblog platform

1. Sign up with the shared marketing mailbox.
2. Claim the handle.
3. Turn on two-factor authentication.
4. Complete the profile with the brand name and logo.

Do not buy the platform's paid organization verification. At the October 2026 check, it cost
as much as the whole example budget ceiling.

### Phase 2 accounts

Reserve these in phase 1. Complete and connect them at the upgrade.

1. Photo-first platform: sign up with the shared marketing mailbox and the handle. In the
   account settings, switch to a professional account, then a business account. Connect it to
   the general social page.
2. Conversation platform: if the platform builds profiles from the photo-first account, create
   the profile from there.
3. Short-form video platform: sign up with the shared marketing mailbox. In the account
   settings, switch to a business account.
4. Video-sharing platform: create a channel with the business name. This creates a brand
   account. In the channel's permission settings, invite the second person as an Owner.

If the video-sharing platform blocks the channel creation, check the brand account settings in
your email and productivity platform's admin console.

Photo-first and short-form video posts always need media.

### Professional network (phase 3)

If the Owner Visibility Rules apply, do these steps only after the owner decides to go public.

1. Complete the owner's profile: photo, headline, the {{COMPANY_NAME}} position, and the About
   section.
2. Connect with 10 to 30 real contacts.
3. Wait 7 days. The platform needs a profile at least 7 days old to create a company page.
4. From the profile menu, create a company page.
5. Enter {{COMPANY_NAME}}, a page URL that matches the handle, {{DOMAIN}}, the industry, the
   company size, the logo, and the tagline.
6. Add the second person as a super admin.
7. Turn on two-step verification for both people.

### Neighborhood platform (manual)

1. Create a business-only account with the shared marketing mailbox.
2. Claim or create the {{COMPANY_NAME}} page.
3. Leave the show-address option unchecked. This keeps a home address private.
4. Use the logo as the profile image.

Verify the page before you make business posts. Free posts reach neighbors within about 2
miles (checked October 2026).

---

## Manual Channels

The neighborhood platform is the only manual channel. No scheduler supports it. The start date
is a Setup Decision.

- Post local, useful items: a scam warning in your town, a power-outage tip, a free workshop.
- Example default: 2 to 4 posts per month. The review page lists them with their dates and a
  Copy button.
- The owner posts each approved item by hand on its date.
- The platform may have a publishing API that needs a developer token application. Look at it
  again only if the platform brings leads.

## Community Forum Platforms

Community forum platforms are not planned in the example default. A presence there needs a
personal account, which identifies the person behind it. If the Owner Visibility Rules apply,
that would identify the owner. Automated promotion on these platforms also risks bans. Look at
them again only if the owner asks.

---

## Profile Assets

Make these from the msp-brand logo files. Phase 1 needs only the square logo, the general
social page cover, and the microblog header.

| Asset | Size in pixels | Used on | Phase |
| --- | --- | --- | --- |
| Square logo | 800 x 800 | General social page, photo-first, video-sharing, short-form video, conversation, neighborhood | 1 |
| General social page cover | 851 x 315 (keep content inside the center 640 x 312) | General social page | 1 |
| Microblog header | 1500 x 500 | Microblog platform | 1 |
| Video-sharing banner | 2560 x 1440 (safe area 1235 x 338, max 6 MB) | Video-sharing platform | 2 |
| Professional network page logo | 300 x 300 | Professional network company page | 3 |
| Professional network page cover | 1128 x 191 | Professional network company page | 3 |
| Professional network personal banner | 1584 x 396 | The owner's profile | 3 |

Check the pixel size of your msp-brand icon files. If they are smaller than 800 x 800, the
square logo needs a larger source file or a clean upscale. Check the result at full size before
upload.

Bio limits: microblog platform 160 characters (official), photo-first platform 150 characters
(third-party), short-form video platform 80 characters (third-party), professional network
tagline 120 characters (third-party).

Size sources, checked October 2026 (platform limits change, check them again before a build
session): the microblog header, the general social page cover, and the video-sharing banner are
official. The video-sharing banner minimum is 2048 x 1152. The professional network sizes are
third-party, because its help center blocked the research tools. Post length limits live in the
msp-marketing format menu.
