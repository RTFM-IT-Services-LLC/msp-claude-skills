# Review Page Spec

Claude builds one review page per monthly pack. The page is not built yet. This spec is the
target for the build session.

The scheduling tool's free tier has no approval feature. Approval happens only on the review
page. Nothing goes to the scheduling tool or to the website `dev` branch until an item shows
Approve.

---

## Who Uses It

- The owner and any designated approver open the page from the same link.
- In the shipped default, either approver can approve an item alone (SKILL.md Setup
  Decision 5).
- Claude reads the decisions back and acts on them.

## Layout

- One card per topic.
- Each card shows the article summary, every channel variant, the media, and the planned date.
- Each item has an Approve button, a Change button, and a note field.
- Manual items (neighborhood platform) show a Copy button and their target date.

## Behavior

- The page saves each decision and shows who made it.
- A Change decision needs a note. Claude revises the item from that note.
- A revised item returns to the page as a new decision. The old decision stays visible.
- Original posts from the owner join the current month's page as new cards.

## Build Notes

- Build the page as an artifact with shared state, so that every approver sees the same
  decisions and Claude can read them back. Load the artifact-capabilities skill before the
  build.
- Show the media that will post. Do not link to file sync service share links, because the
  links can expire.
- Show each variant as it will post: the final text, the hashtags, the link, and the media.
- If the Owner Visibility Rules in SKILL.md apply, check the page against them before Claude
  sends the link.
