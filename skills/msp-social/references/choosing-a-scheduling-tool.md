# Choosing a Scheduling Tool

How to pick the social scheduling tool, the categories of tool to compare, and when to look at
the choice again. Record the tools you rejected and why, so that nobody suggests them again
unless a revisit condition is true.

**Defaults you must review:** the budget ceiling and the upkeep estimates in this file are
shipped example defaults from a working MSP. Review and replace them with your own (SKILL.md
Setup Decisions 3 and 4).

The review page and all content stay outside the posting tool. If you switch tools, only the
last pipeline step changes.

---

## Evaluation Criteria

Check each candidate against these:

1. **API:** an official, documented API that works with a key, so that unattended runs (queue
   refill, failure checks) do not stop for approval prompts. An official MCP connector is a
   bonus, not a requirement.
2. **Channel coverage:** every channel in your phases, with no extra fee per channel type.
   Check whether one account (one brand) can hold both the owner's professional network
   profile and the company page.
3. **Billing model:** per-channel billing lets the cost grow only as you add channels.
4. **Fit with your content source:** whether your marketing membership already ships a bulk
   import file for the tool.
5. **Media handling:** an upload endpoint, or media by URL only (then you need the media host
   in `scheduling-tool.md`).
6. **Approval:** whether the tool has in-app approval, and on which tier. The review page covers
   approval if it does not.
7. **Limits:** queue slots per channel, users, API keys, and request limits per tier.
8. **Security:**
   - Two-factor login, with recovery codes.
   - A SOC 2 report.
   - Security advisory history, with no open critical advisories.
   - Founder and bus-factor risk (a solo founder or a very small team).
9. **Cost:** inside the budget ceiling at your last phase. Example default budget ceiling: $200
   per month (shipped example default; set your own).

---

## Tool Categories

| Option | What to weigh |
| --- | --- |
| Membership-bundled posting tool | Costs nothing extra. It may not support every channel you need. Claude access may not be confirmed (no official, documented API). It stops if the membership ends. It may auto-import unbranded posts. |
| Hosted open-source scheduler | Check two-factor login, SOC 2, the advisory history, and founder risk with care. Some have had critical advisories and a solo founder. |
| Analytics-first scheduler | Some channels can cost extra. Both professional network channels may need two separate brands. |
| Self-hosted scheduler | Server cost, patching, and every platform's developer app approval fall on you. |
| Self-written tool (Claude builds it) | About $0 plus any platform API fees, but several Claude build sessions (example estimate: 6 to 10). The professional network page, the local listing, the short-form video platform, and the video-sharing platform need platform approval first. Example upkeep: 1 to 2 hours per month. |
| Per-channel scheduling tool | The shipped default category. Pick one with an official API (and ideally an official MCP connector), no extra fee for the microblog channel, an import file from your membership pack, and per-channel billing. |

---

## Revisit Conditions (standing proposal)

These are example defaults. Confirm your own.

- **Membership-bundled posting tool:** if it adds the channels you need and an official,
  documented API that Claude can use. Keep auto-import off until then.
- **Hosted or self-hosted open-source scheduler:** if it confirms two-factor login, gets SOC 2,
  and has no open critical advisories.
- **Analytics-first scheduler:** if the extra-cost channels become included and one brand can
  hold both professional network channels.
- **Self-written tool:** only if no hosted tool fits the budget ceiling and the platform
  approvals are in place.
- **Any tool:** if your current tool fails the security check, raises prices past the budget
  ceiling, or drops a channel you use.

When you switch tools or reject one, record the decision where your shop keeps settled
decisions.
