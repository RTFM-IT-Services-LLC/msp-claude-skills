# Your Social Scheduling Tool

The social scheduling tool is the {{COMPANY_NAME}} posting tool. Pick it with
`choosing-a-scheduling-tool.md`. The shipped default: start on the free tier, then pay per
channel as the process grows. This file lists what to check and how to run the tool. Vendor
plans and API fields change, so check them again before a build session.

**Defaults you must review:** the queue slot count, the budget ceiling, the media retention
period, and the phase channel counts in this file are shipped example defaults from a working
MSP. Review and replace them with your own (SKILL.md Setup Decisions 2, 3, 4, and 8). Record your
own tool's real limits and prices where this file says "Record".

The scheduling tool prices are vendor costs that the company pays. They are internal numbers.
They never appear in client content, and they are not msp-pricing numbers.

---

## Tiers and Cost Logic

| Phase | Tier | Channels | Monthly cost |
| --- | --- | --- | --- |
| 1 | Free tier | 3: local listing, general social page, microblog | $0 |
| 2 | Paid per-channel tier | 7: adds photo-first, video-sharing, short-form video, conversation | Record (per-channel price x 7) |
| 3 | Paid per-channel tier | 9: adds both professional network channels | Record (per-channel price x 9) |
| Optional | Team tier with extra logins and in-app approval | Same channels | Record (usually priced per channel) |

A channel is one connected account. The owner's professional network profile and the company
page count as 2. Example default budget ceiling: $200 per month (shipped example default; set
your own). Annual billing is often cheaper than monthly billing; check both. Do not buy a
platform's paid organization verification if it eats the budget ceiling.

## Free Tier Limits

Check these on your tool's pricing page. The example values are the shape the shipped rollout
assumes:

- A small channel cap (3 in the example). Extra channels lock until the upgrade.
- A cap on scheduled posts per channel at a time (10 in the example). A slot opens again after
  a post publishes.
- 1 user. The second approver approves on the review page and has no scheduling tool login.
- API: 1 key or app client, with request limits per 15 minutes, per 24 hours, and per 30 days.
- Limited ideas, tags, and analytics history.
- Check whether the free tier has a time limit.
- No approval feature. Approval happens only on the {{COMPANY_NAME}} review page.

API limits by tier (record your tool's values):

| Limit | Free tier | Paid per-channel tier | Team tier |
| --- | --- | --- | --- |
| Requests per 15 minutes | Record | Record | Record |
| Requests per 24 hours | Record | Record | Record |
| Requests per 30 days | Record | Record | Record |
| API keys or app clients | Record (1 in the example) | Record | Record |

Make sure the monthly run, the queue refills, and the failure checks fit inside the daily and
30-day limits. A 429 response carries a Retry-After header. Wait that long before the next
call.

---

## Setup

1. Sign up with the shared marketing mailbox on {{DOMAIN}} on the free tier.
2. Turn on two-factor authentication. If the tool offers codes by email or from an
   authenticator app, use the authenticator app.
3. Store the recovery codes in the company password vault.
4. Connect the local listing, the general social page, and the microblog platform.
5. In the tool's API settings, create one API key for Claude.
6. Store the API key in the vault.

API key rules (the owner owns the key):

- Store the key in the company password vault.
- The scheduled task also needs a copy where it runs. The build session sets that location
  with the owner. Never put the key in the repo, a skill file, a ticket, or chat.
- If the key leaks, revoke it in the tool at once and create a new one.

API key checks (record the answers):

- Who can create an API key. Some tools let only an organization owner create one.
- What the key covers. Some keys cover the whole account, with no per-organization scope.
- Whether the key expires. Some tools do not document key expiry.

---

## Security Check (not done)

Claude checks the scheduling tool before the accounts connect. Check each item on the vendor's
own pages:

- **Two-factor login:** confirm it, and confirm single-use recovery codes. Check on which tiers
  owners can require 2FA for all members. On a one-user free tier, this does not matter yet.
- **SOC 2:** look for a SOC 2 report or statement on the vendor's site and support pages.
- **Security page:** read it in full. Look for encryption, issue reporting, and a bug bounty
  or rewards program.
- **Advisory history:** check for past security advisories and incidents.

The check is complete only when every item has an answer and the owner accepts the result.

---

## API Use

**Status of this section:** nobody has connected to the API yet. The build session reads the
tool's developer docs, records the real operations, and tests each call before the pipeline
uses it.

- **Style:** record whether the API is REST or GraphQL, and its endpoint.
- **Auth:** usually a header such as `Authorization: Bearer <API key>`. A bad key returns 401.
- **Errors:** a GraphQL API can return HTTP 200 even on an error. Read the error code in the
  response body, not only the HTTP status. Record the tool's error codes (for example
  unauthorized, forbidden, not found, unexpected, and rate limit exceeded).

The pipeline needs these operations. Record the tool's name for each one:

| Task | What the operation must do |
| --- | --- |
| Get the organization ID | Return the account's organizations with their IDs. |
| List channels | Return each channel's ID, name, service, and whether its queue is paused. |
| Read one channel | Return one channel by ID. |
| Schedule a post at a set time | Create a post on one channel with text, media, and a due time in ISO 8601 UTC. |
| Add a post to the next queue slot | Create a post in the channel's next open queue slot. |
| List scheduled posts | Return scheduled posts per channel, sorted by due time, with paging. |
| Read one post | Return one post by ID. |
| Edit a scheduled post | Change the text, due time, or media. Check how to keep the media and how to clear it. |
| Delete a post | Delete one post. A delete cannot be undone. |

When you create a post, read both the success result (the post ID and due time) and the error
result. Never use a "share now" or "share next" mode, because a post must wait for its approved
date.

Do not invent other operations. If a task needs one that is not in this table, read the tool's
API reference first.

### Media

Some scheduling APIs have no media upload. A post then takes media only as a URL (an image URL
or a video URL). The tool fetches the file at publish time, so the URL must be public, direct,
HTTPS, and stable until the post publishes. Check whether your tool has an upload endpoint. If
it does not, follow this section.

- Never use file sync service share links for post media. Share links are not direct and can
  expire.
- Host post media in an object storage bucket served on a media subdomain of {{DOMAIN}} (for
  example media.{{DOMAIN}}). See Media Host, below.
- Upload a file only after the owner or a designated approver approves its post. Drafts never
  sit at a public URL.
- Check whether the tool documents media file types or size limits.

### Media Host

**Status:** not built. Shipped default: an object storage bucket, served on a media subdomain
of {{DOMAIN}} (for example media.{{DOMAIN}}), with each object deleted 60 days after upload
(example default).

Object storage checks (record the answers from your storage provider's docs):

- **Cost:** check the free allowance for storage and operations, and whether egress
  (downloads) costs money. These are vendor costs that the company pays, not client prices.
- **Public access:** confirm that a bucket stays private until you connect a custom domain or
  turn on a provider development URL. A development URL is often rate-limited and is for
  development only. Use a custom domain.
- **Custom domain rule:** check what the provider needs before it serves a bucket on your
  domain. Some providers need the domain's DNS in the same account as the bucket. A domain
  with DNS elsewhere may need a partial (CNAME) setup.
- **No listing:** confirm that a public bucket does not list its contents at the root of the
  domain.
- **Upload limits:** record the maximum size for a single upload and for the provider's
  command-line tool.
- **Upload endpoint:** many providers offer an S3-compatible endpoint, so any S3 client works.
- **Tokens:** scope a read and write token to this one bucket. Store the access key ID and the
  secret. A secret often shows only once.
- **Lifecycle rules:** confirm that a rule can delete objects a set number of days after upload,
  with an optional prefix filter. Expired objects can take up to a day to disappear.

Example defaults:

- One bucket for social media, standard storage.
- Custom domain: a media subdomain of {{DOMAIN}} (for example media.{{DOMAIN}}).
- Cleanup: delete each object 60 days after upload. A post can wait up to a month in the queue,
  so 60 days leaves margin. After the scheduling tool sends a post, the platform holds its own
  copy.

Proposal for the build session:

- Object keys: `YYYY-MM/<random-id>.<ext>`, so that nobody can guess a file name.

Setup:

1. In your storage provider account, create the bucket with standard storage. If the provider
   needs the domain's DNS in the same account, use the account that holds the {{DOMAIN}} DNS.
2. In the bucket settings, connect the media subdomain as a custom domain. Do not turn on a
   development URL.
3. Add a lifecycle rule that deletes objects 60 days after upload.
4. Create an API token with object read and write, scoped to this bucket only.
5. Store the access key ID, the secret, and the endpoint in the company password vault.
6. Upload one test image. Open its public URL in a browser and confirm that the image loads.
7. Send one test post through the scheduling tool with that URL. Delete the test post after it
   publishes.

**Reachability:** test the upload endpoint from each place that runs uploads (the cloud
workspace and the owner's computer). A cloud workspace with a network proxy may fail where a
computer without a proxy works. If the cloud workspace cannot reach the endpoint, run the
upload step from the owner's computer. Also test that the scheduling tool API and the storage
provider's API answer from both places.

### MCP Connector

Some scheduling tools offer an official MCP server, sometimes on every tier, including free.
It usually connects over OAuth. Its calls count against the same API limits.

Use the API with a key, not an MCP connector, for unattended runs. The queue refill and the
failure checks run without anyone present, and MCP tool calls stop for approval prompts. Leave
MCP unconnected. If the owner asks for it later, keep the approval prompts on: a create-post
tool can publish at once, and a delete cannot be undone.

---

## Queue Refill

On the free tier, each channel holds only a few scheduled posts (10 in the example). Approved
posts past the cap wait in the pipeline.

1. List the scheduled posts for each channel.
2. Count the open slots (the cap minus the scheduled posts on that channel).
3. Schedule the next approved posts, oldest planned date first, up to the open slots.
4. Never schedule an item that is not approved on the review page.

## Failure Checks

1. List the posts with the tool's failed status. Some tools have no "failed" status and use
   "error" instead. Record your tool's status values (for example draft, error, needs approval,
   scheduled, sending, and sent).
2. For each failure, read the error message, the raw platform error, and any support link the
   tool returns.
3. Check each channel for a paused queue. A paused queue does not publish.
4. Report each failure to the owner: the post, the channel, and the error.
5. Follow SKILL.md Core Workflow 5 to fix and reschedule.

## Bulk Import Files

A licensed marketing pack may ship a bulk import file (often a CSV) for a scheduling tool.
Check what the tool's bulk upload takes. Bulk uploads often take a single image per post, with
no video, no carousels, and no video-sharing posts. Photo-first posts need an image. The
pipeline does not import the pack file as it is, because its posts are not rewritten or
approved.

## API Stability

- Check whether the vendor publishes a versioning policy for the API.
- Do not build the pipeline on features the vendor marks experimental or preview.
- Watch the vendor's changelog for removed fields and their dates.
- If the vendor has an older API version with a migration guide, do not use the old version.
