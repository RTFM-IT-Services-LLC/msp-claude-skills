---
name: msp-social
description: >
  Use this skill for your MSP's social media operations: which channels the company posts to,
  setting up or securing a social account, the social scheduling tool, and the monthly pipeline
  that turns a licensed marketing pack into approved, scheduled posts. Trigger on "process this
  month's pack", "schedule these posts", "set up our social accounts", "set up our local listing,
  general social page, microblog, or professional network page", "add a channel", "upgrade the
  scheduling tool", "the review page", "a post failed", "connect the scheduling tool", or any
  question about social posting automation, account ownership, handles, or profile images.
  msp-marketing owns what posts say (voice, formats, idea bank, CTAs). This skill owns where
  they go and how they get there. Website article publishing belongs to msp-website-setup.
  Apply alongside msp-marketing, msp-brand, and msp-technical-writing.
---

# {{COMPANY_NAME}} Social Media Operations

**Defaults you must review:** the specific numbers in this skill and its reference files
(channel phases, queue slots, budget ceiling, media retention, post counts) are shipped example
defaults from a working MSP. Review and replace them with your own before anything goes
client-facing (see Setup Decisions at the bottom).

This skill runs the {{COMPANY_NAME}} social media system. Claude turns each monthly licensed
marketing pack, plus original posts from the owner, into resources articles and social posts.
The owner or a designated approver approves them on one review page. After approval, the
social scheduling tool publishes the social posts and the website pipeline publishes the
articles. Nothing posts without approval.

---

## How This Skill Divides Work With Its Siblings

- **msp-social (this skill):** where posts go and how they get there. The channel list and
  phases, account setup and ownership, the optional owner visibility rules, profile assets, the
  scheduling tool, the monthly pipeline, the review page, manual channels, and how to choose a
  scheduling tool.
- **msp-marketing:** what posts say. Voice, the rewrite playbook, the format menu (including
  the per-platform post formats), the idea bank, the CTA library, SEO, and the content log.
  Load it for every piece of content this pipeline produces.
- **msp-website-setup:** the website publishing mechanics (repo, `dev` and `main` branches,
  the hosting platform's preview environment). This skill only sets the order: an article goes
  live before the posts that link to it.
- **msp-brand:** naming, logos, colors, and voice. The profile assets in this skill come from
  the msp-brand logo files.
- **msp-technical-writing:** the prose form of this skill and of all internal pipeline notes.
- **msp-metrics:** results tracking. Post and channel results feed the monthly owner review
  when the company starts to measure them.
- **msp-pricing:** client prices. The scheduling tool and media host costs in this skill are
  vendor costs that the company pays. They are internal numbers and never appear in client
  content.

---

## Build Status

**Phase:** not started. The shipped example rollout starts with phase 1 (see
`references/channels-and-accounts.md`).

**Active channels:** none yet. List each channel here as it connects. The example phase 1
channels are the local business listing profile, the general social network page, and the
microblog platform, on the scheduling tool's free tier.

| Part | Status |
| --- | --- |
| Scheduling tool account (free tier) and API key | Not built |
| Scheduling tool security check | Not done |
| Media bucket on the media subdomain (for example media.{{DOMAIN}}) | Not built |
| Media upload test (from each place that runs uploads) | Not done |
| Video post to the local listing through the scheduling tool (test) | Not done |
| Phase 1 accounts (local listing, general social page, microblog) | Not built |
| Phase 2 handles reserved | Not done |
| Phase 1 profile assets | Not built |
| Intake folder | Not built |
| Review page | Not built |
| Scheduling tool API connection | Not built |
| Monthly scheduled task | Not built |

Update this table as each build step finishes.

---

## Owner Visibility Rules (optional)

Some owners do not want to be public as the owner of the company yet. Setup Decision 1 records
your choice. If the owner does not want to be public yet, apply these rules. While they apply,
they are hard rules:

- Do not create or connect a personal profile on any public channel.
- Do not publish content that names {{OWNER_NAME}} as the owner.
- Do not set up the professional network. The professional network company page and the
  owner's profile (phase 3 in the example rollout) wait until the owner decides to go public.
- Check the general social page as a visitor before the first post. Confirm that no personal
  name shows in its transparency panel.
- Use the display name {{COMPANY_NAME}} and the shared marketing mailbox on {{DOMAIN}}
  wherever a platform allows a business login.

If a request would break these rules, stop and ask the owner. Do not find a workaround.

If the owner is already public, skip this section. The ownership rules in
`references/channels-and-accounts.md` still apply.

---

## Core Workflows

### 1. Process a monthly pack

**When:** "process this month's pack", or the monthly scheduled task starts.

1. Open `references/monthly-pipeline.md` and follow the pipeline steps.
2. Load msp-marketing for the rewrite, the formats, and the CTAs.
3. Build the review page per `references/review-page.md`.
4. Schedule only the approved items in the scheduling tool per
   `references/scheduling-tool.md`.

### 2. Add an original post

**When:** the owner sends a note, a photo, or a link to post.

1. Write one version per active channel with msp-marketing.
2. Add the items to the current review page.
3. After approval, schedule them per pipeline steps 12 to 16.

### 3. Upgrade a phase

**When:** the owner decides to move to the next phase.

1. Confirm the decision with the owner. A phase change costs money and changes the channel
   list.
2. Tell the owner to change the scheduling tool plan. The owner owns the billing.
3. Set up and connect the new accounts per `references/channels-and-accounts.md`.
4. Make the profile assets for the new phase.
5. Update the Build Status table and the active channel list in this skill.
6. Record the decision where your shop keeps settled decisions.

If the Owner Visibility Rules apply, the professional network phase also needs the owner to
end them. Do not start that phase without that decision.

### 4. Set up an account

1. Open `references/channels-and-accounts.md`.
2. Follow the ownership rules and the setup steps for that platform.
3. Store every login, recovery code, and key in the company password vault.
4. Update the Build Status table.

### 5. Handle a failed post

1. Find the failed post and its error in the scheduling tool (see
   `references/scheduling-tool.md`, Failure Checks).
2. Tell the owner which post failed, on which channel, and why.
3. Fix the cause. Examples: reconnect the channel, or replace the media.
4. If the post text and media are the same as approved, schedule it again.
5. If the text or media changed, put the item back on the review page for approval.

---

## Reference Files

- **`references/channels-and-accounts.md`**: the channel table, the example phases, the upgrade
  triggers, ownership rules, setup steps per platform, and profile asset sizes.
- **`references/scheduling-tool.md`**: scheduling tool tiers and cost logic, free-tier limits,
  setup, the security check, API use, the media host, queue refill, and failure checks.
- **`references/monthly-pipeline.md`**: the 16-step pipeline from pack to published post, the
  intake folder, the scheduled task, and original posts.
- **`references/review-page.md`**: the review page spec.
- **`references/choosing-a-scheduling-tool.md`**: the evaluation criteria for a scheduling
  tool, the tool categories to compare, and when to look at the choice again.

---

## Risks

| Risk | Effect | Mitigation |
| --- | --- | --- |
| The scheduling tool's security is not checked | Unknown exposure for the connected accounts | Claude checks it before the accounts connect. |
| The general social page shows a personal name (if the Owner Visibility Rules apply) | The public can identify the owner | Check the page's transparency panel as a visitor before the first post. |
| The free tier holds only a few scheduled posts per channel (10 in the example) | Posts past the cap wait | Claude refills the queue as slots open. Upgrade if this becomes a burden. |
| The free tier allows 1 user | The second approver has no scheduling tool login | The login is in the vault. The team tier adds extra logins. |
| The membership's bundled posting tool may auto-import unbranded posts | Unbranded posts could publish | Keep auto-import off. Connect no social account to the membership's bundled posting tool. |
| A media link breaks before the post publishes | The post fails or loses its image | Some scheduling APIs have no media upload. Host media in your object storage bucket on a media subdomain of {{DOMAIN}}. Never use file sync service share links. |

---

## Setup Decisions

Settle these before this skill goes live for your shop. Each is shipped with an example
default; accept it, change it, or log a deferral.

1. **Owner visibility.** Whether the owner is public as the owner of the company. Shipped
   default: none (the owner is public, and the Owner Visibility Rules do not apply). If the
   owner does not want to be public yet, turn the rules on, and record what ends them.
2. **Channel list and phases.** Shipped example rollout: phase 1 is the local listing, the
   general social page, and the microblog platform on the free tier. Phase 2 adds the
   photo-first platform, the video-sharing platform (including short-form video), the
   short-form video platform, and the conversation platform. Phase 3 adds the professional
   network company page and the owner's profile. The example puts the professional network
   in phase 3 only for an owner who is not public. If the Owner Visibility Rules do not apply,
   consider adding both professional network channels earlier, because msp-marketing ranks it
   the priority B2B channel. Write your own channel list and phases into
   `references/channels-and-accounts.md`.
3. **Scheduling tool and upgrade timing.** Pick a tool with
   `references/choosing-a-scheduling-tool.md`. Shipped default: start on the free tier, then
   pay per channel as the process grows, with a review after the first month of live posts.
4. **Budget ceiling.** Example default budget ceiling: $200 per month (shipped example default;
   set your own). It covers the scheduling tool and any paid platform features.
5. **Approvers and approval scope.** Shipped default: the owner or a designated approver, and
   either one can approve alone. The owner may instead want to see everything before it posts.
6. **Intake folder and pack arrival day.** Name one fixed folder where the owner saves each
   pack, and record the day of the month the pack arrives. The arrival day sets the scheduled
   task date. Also decide how often the queue refill check runs between monthly runs.
7. **Business login.** Shipped default: a shared marketing mailbox on {{DOMAIN}}, used wherever
   a platform allows a business login. It must be a licensed user mailbox, not a group.
8. **Media host.** Shipped default: an object storage bucket served on a media subdomain of
   {{DOMAIN}} (for example media.{{DOMAIN}}), with each object deleted 60 days after upload
   (example default).
9. **Handle and display name.** One handle everywhere, based on {{COMPANY_NAME}} or
   {{DOMAIN}}, plus fallbacks in order. Check availability before setup.
10. **Neighborhood platform.** Whether to start it, and how many posts per month. Example
    default: 2 to 4. It is manual posting only.
11. **More channels.** Whether to add other networks later. Check that your scheduling tool
    supports them first.
12. **General social page owner account.** Which person's personal account sits behind the
    general social page, and whether that account shows publicly.
13. **Cadence.** Cadence is msp-marketing Setup Decision 1. This skill follows it. Each
    channel gets one post per topic.
