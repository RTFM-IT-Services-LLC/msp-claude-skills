# Monthly Pipeline

How a licensed marketing pack becomes approved, published posts. Build status lives in the
SKILL.md Build Status table.

**Defaults you must review:** the cadence, the queue slot count, and the approval rule in this
file are shipped example defaults from a working MSP. Review and replace them with your own
(SKILL.md Setup Decisions 5, 6, and 13).

The owner's monthly work is three tasks: download the pack, approve the review page, and
approve the website preview. Claude does the rest.

**Warning:** the membership's bundled posting tool may auto-import unbranded posts, sometimes
scheduled in the membership's own time zone. Keep auto-import off, and connect no social
account to it.

---

## Inputs

- **The monthly licensed marketing pack** from a paid MSP marketing content membership. Blog
  posts, social posts, images, videos, and often a bulk import file for a scheduling tool. The
  membership license typically allows adaptation (msp-marketing rewrite playbook). Do not
  import the pack's bulk import file as it is. It holds the unbranded posts, and only
  rewritten, approved items post.
- **Original posts from the owner.** A rough note, a photo, or a link, sent at any time.

## Cadence

The cadence is msp-marketing Setup Decision 1. This pipeline follows it. Example default: post
whatever the pack supplies, spread across the month, plus the original posts. Each channel gets
one post per topic.

## Intake Folder

The owner saves each pack to one fixed intake folder, named in SKILL.md Setup Decision 6.
Claude checks this folder. Pick one naming pattern and keep it (for example, one subfolder per
month, or the pack's downloaded folder name). The build session creates the folder.

---

## Pack to Published Posts

1. The owner downloads the pack and saves it to the intake folder.
2. A monthly scheduled task starts Claude. The owner can also say "process this month's pack".
3. Claude rewrites each blog post into a resources article, per the msp-marketing rewrite
   playbook.
4. Claude writes one post per active channel for each topic. Each channel gets its own length
   and format, per the msp-marketing format menu.
5. Claude picks the pack image or video for each post.
6. Claude sets the dates. Each article goes live before the posts that link to it.
7. Claude publishes the review page and sends the owner the link.
8. The owner or a designated approver marks each item Approve or Change, with a note for
   changes.
9. Claude revises the items marked Change and puts them back on the review page.
10. Claude commits the approved articles to the `dev` branch.
11. The owner checks the hosting platform's preview environment and approves the merge to
    `main`.
12. Claude attaches the media by its public URL and schedules the approved posts in the
    scheduling tool through the API (see `scheduling-tool.md`, Media).
13. On the free tier, the scheduling tool holds only a few scheduled posts per channel (10 in
    the example). Claude adds the rest as slots open.
14. Claude checks the scheduling tool for failed posts and reports them.
15. Claude logs each piece in the msp-marketing content log.
16. If the neighborhood platform is active, the owner posts its items by hand on their dates.

Rules for the pipeline:

- Nothing posts until the owner or a designated approver approves it. In the shipped default,
  either approver can approve alone (SKILL.md Setup Decision 5).
- An item marked Change goes back to Claude and returns to the review page.
- A post that links to an article waits until that article is live on `main`.
- If the Owner Visibility Rules in SKILL.md apply, check every item against them before step 7.
- Step 15 follows the msp-marketing logging rule. The installed plugin is read-only, so
  outside the source folder Claude outputs the log rows for the owner.

## Original Posts

1. The owner sends Claude a rough note, a photo, or a link.
2. Claude writes the channel versions and adds them to the current review page.
3. After approval, the items follow steps 12 to 16.

---

## Scheduled Task

Not built. The pack arrival day is a Setup Decision, and it sets the task date.

Proposal for the build session:

1. Run once a month, a few days after the pack arrives.
2. Check the intake folder for the current month's pack.
3. If the pack is there and not processed, run steps 3 to 7.
4. If the pack is missing, tell the owner.
5. In the same run, check the scheduling tool queue (step 13) and failed posts (step 14).

Queue refill on the free tier also needs a check between monthly runs. Setup Decision 6 sets
how often.
