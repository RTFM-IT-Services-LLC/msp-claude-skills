#!/usr/bin/env python3
"""
{{COMPANY_NAME}} pricing configurator.

Two ways to run it:

1) Quick single check (CLI flags) -- price one configuration and see its band:

   python3 price_quote.py --workstation 24 --mobile 5 --firewall 1 \
       --switch 2 --wap 3 --network-base 1 --users 25 --years 3 \
       --edr --onsite-hours 2 --compliance

2) Package builder (JSON) -- the main workflow. Describe one client and a few
   custom options assembled from building blocks; get a side-by-side comparison:

   python3 price_quote.py --packages client.json

   client.json:
   {
     "client": "Acme Dental",
     "users": 25,
     "years": 3,
     "options": [
       {"name": "Lean",        "workstation": 24, "mobile": 5, "firewall": 1,
        "switch": 2, "wap": 3, "network_base": 1, "agents": ["edr"],
        "onsite_hours": 0, "value_factors": []},
       {"name": "Recommended", "recommended": true, "workstation": 24, "mobile": 5,
        "server": 1, "firewall": 1, "switch": 2, "wap": 3, "network_base": 1,
        "agents": ["edr","ztna"], "onsite_hours": 2,
        "value_factors": ["compliance","downtime_sensitive"]},
       {"name": "Full",        "workstation": 24, "mobile": 5, "server": 1,
        "firewall": 1, "switch": 2, "wap": 3, "camera": 4, "network_base": 1,
        "agents": ["edr","ztna","mdm_ent"], "onsite_hours": 4,
        "value_factors": ["compliance","downtime_sensitive","security_pressure"]}
     ]
   }

Everything is monthly USD unless noted.
"""

import argparse
import json
import math

COMPANY_NAME = "{{COMPANY_NAME}}"  # Set your company name here (filled in during kit setup)

# --- Labor cost basis (market research, June 2026; see references/labor-rates.md) ----
# The original sheet used magic numbers ($40 remote / $80 on site). They are now built up
# from researched wages so the basis is transparent and tunable. The defaults reproduce
# $40 / $80 exactly, so existing prices do not move. Change a wage or a factor and the
# whole sheet re-costs from real inputs (e.g. cheaper remote labor, shorter drive times).
L1_WAGE     = 25.00   # decent L1 phone help desk tech, base wage/hr (service-area aligned)
FIELD_WAGE  = 32.00   # good field services tech, base wage/hr
BURDEN      = 1.30    # payroll taxes + workers comp + benefits + PTO (lean small-MSP)
REMOTE_OH   = 7.50    # per remote hr: tooling, supervision, escalation to higher tiers
ONSITE_UTIL = 1.65    # on-site multiplier: drive time + lower on-site utilization
ONSITE_OH   = 11.00   # per on-site hr: vehicle/mileage + field tooling

REMOTE_LABOR = round(L1_WAGE * BURDEN + REMOTE_OH)                    # ~ $40/hr
ONSITE_COST  = round(FIELD_WAGE * BURDEN * ONSITE_UTIL + ONSITE_OH)   # ~ $80/hr

# Per device: (fixed base cost, monthly labor hours)
UNITS = {
    "workstation": (10.00, 1.0), "account_only": (4.00, 0.4), "server": (15.00, 1.5),
    "mobile": (12.00, 0.5), "network_base": (0.00, 0.5), "firewall": (0.00, 0.5),
    "switch": (0.00, 0.1), "wap": (0.00, 0.1), "camera": (0.00, 0.1),
    "printer": (0.00, 0.3), "special_sw": (0.00, 1.0),
}
# A workstation line is an "account + computer" user (managed machine plus that person's support).
# account_only is a user with a managed account but no managed machine (BYOD, 1099 contractors):
# identity provisioning, password/MFA, account security monitoring, licensing. Lighter than a
# workstation because there is no machine to maintain. Endpoint agents do not apply to it.
# Server raised from 1.0 to 1.5 hrs: servers are higher-touch. See references/support-hours.md.
# printer is business-class NETWORKED printers only: remote work (connectivity, IP, drivers,
# queues, scan-to-email/folder, firmware) plus vendor liaison. No consumables; physical work
# rides on-site allowance/break-fix. Consumer/inkjet/USB units get no monthly line --
# best-effort hourly only. $40 anchor, $30 floor. See references/cost-model.md.

# Per endpoint agent COSTS (Agent Prices sheet). Load onto devices that use them.
AGENTS = {"edr": 1.30, "ztna": 7.00, "mdm_sb": 5.00, "mdm_ent": 7.00}

# --- Pricing standards ----------------------------------------------------------
# Payment processing (example default): clients pay however they want, with
# no surcharge, and {{COMPANY_NAME}} does not eat the fee. Card processing is ~3% of revenue, so it
# lives in the multipliers rather than in loaded costs (a fee on revenue cannot be
# modeled as a fixed cost). Margin targets are unchanged -- 60% anchor, 50% floor --
# but are now measured AFTER the fee skim. Assumes standard (free) deposits from your
# payment processor; the optional 1% instant-deposit fee stays off.
PROC_FEE         = 0.03   # payment processing, % of revenue, baked into every price
STD_MULTIPLIER   = 1 / (1 - PROC_FEE - 0.60)   # ~2.703x: 60% GM after fees (was 2.5)
FLOOR_MULTIPLIER = 1 / (1 - PROC_FEE - 0.50)   # ~2.128x: 50% GM after fees (was 2.0)
YEAR_DISCOUNT    = 0.04   # each year beyond 1 removes 4% of anchor; 5yr = 16% off, ~53% GM after fees
MIN_YEARS        = 1      # 1 year is the minimum term, so the 1-yr price is the highest shown
MAX_YEARS        = 5
PRESENT_TERMS    = [1, 2, 3, 5]   # terms to show clients: 1-yr (highest) plus longer step-downs
ENGAGEMENT_MIN   = 1000   # don't take a managed client below this $/month
START_CAP        = 1.40   # opening ask never more than 40% over anchor

VALUE_FACTORS = {
    "compliance":         (0.20, "Regulated data (HIPAA, PCI, finance, legal)"),
    "downtime_sensitive": (0.15, "An hour down is real lost revenue"),
    "security_pressure":  (0.12, "Cyber-insurance mandate or elevated risk"),
    "power_users":        (0.12, "Specialized software / heavy power users"),
    "high_pain":          (0.08, "Strong pain, weak incumbent, urgency"),
}


def round_up(x, step):
    return int(math.ceil(x / step) * step)


def device_cost(unit, agents):
    fixed, hours = UNITS[unit]
    cost = fixed + hours * REMOTE_LABOR
    if unit in ("workstation", "server"):
        cost += sum(AGENTS[a] for a in agents)
    return cost


# Small-item exception (example default): for the tiny lines ($4 cost), the
# $10 rounding step would double the price from $10 to $20 over a ~$0.30 fee. They stay
# at $10 -- 57% GM after fees, still above the 50% floor. Revisit if labor rates change.
ANCHOR_OVERRIDES = {"switch": 10, "wap": 10, "camera": 10}


def anchor(cost, unit=None):
    if unit in ANCHOR_OVERRIDES:
        return ANCHOR_OVERRIDES[unit]
    return round_up(cost * STD_MULTIPLIER, 10)


def contract(anchor_price, years):
    years = max(MIN_YEARS, min(years, MAX_YEARS))
    return round(anchor_price * (1 - YEAR_DISCOUNT * (years - 1)))


def term_ladder(year1_total):
    """Client-facing prices across PRESENT_TERMS, built off the 1-year (highest) price.
    The 1-year figure is returned exactly so it matches the opening ask shown elsewhere;
    longer terms step down by the commitment discount, rounded to the nearest $5."""
    out = []
    for t in PRESENT_TERMS:
        if t == 1:
            out.append((t, round(year1_total)))
        else:
            price = year1_total * (1 - YEAR_DISCOUNT * (t - 1))
            out.append((t, int(round(price / 5.0)) * 5))
    return out


def floor(cost):
    return round_up(cost * FLOOR_MULTIPLIER, 10)


def gm(price, cost):
    """Gross margin after the payment-processing skim, as a percent of price."""
    return (price * (1 - PROC_FEE) - cost) / price * 100 if price else 0.0


def price_option(opt, users, years):
    """Return per-line rows and monthly totals for one assembled option."""
    agents = opt.get("agents", [])
    value_uplift = sum(VALUE_FACTORS[f][0] for f in opt.get("value_factors", [])
                       if f in VALUE_FACTORS)
    value_mult = min(1 + value_uplift, START_CAP)

    rows = []
    tot = dict(cost=0.0, floor=0.0, anchor=0.0, contract=0.0, start=0.0)

    for unit in UNITS:
        n = opt.get(unit, 0)
        if n <= 0:
            continue
        c = device_cost(unit, agents)
        a = anchor(c, unit)
        rows.append(dict(line=unit, qty=n, cost=c, floor=floor(c), anchor=a,
                         contract=contract(a, years),
                         start=round_up(a * value_mult, 5), gm=gm(contract(a, years), c)))

    onsite = opt.get("onsite_hours", 0)
    if onsite > 0:
        a = anchor(ONSITE_COST)             # $80 cost -> $220/hr anchor (60% GM after fees)
        rows.append(dict(line=f"onsite ({onsite}h)", qty=onsite, cost=ONSITE_COST,
                         floor=floor(ONSITE_COST), anchor=a, contract=contract(a, years),
                         start=round_up(a * value_mult, 5), gm=gm(contract(a, years), ONSITE_COST)))

    for r in rows:
        for k in ("cost", "floor", "anchor", "contract", "start"):
            tot[k] += r[k] * r["qty"]

    tot.update(value_mult=value_mult, value_uplift=value_uplift, agents=agents,
               users=users, years=years, onsite=onsite,
               name=opt.get("name", "Option"), recommended=opt.get("recommended", False),
               value_factors=opt.get("value_factors", []))
    return rows, tot


def detail_block(rows, t):
    yr_hdr = f"{t['years']}yr"
    L = [f"{'Line':16}{'Qty':>4}{'Cost':>8}{'Floor':>8}{'Anchor':>8}"
         f"{yr_hdr:>8}{'Start':>8}{'GM':>6}", "-" * 66]
    for r in rows:
        L.append(f"{r['line']:16}{r['qty']:>4}{r['cost']:>8.0f}{r['floor']:>8.0f}"
                 f"{r['anchor']:>8.0f}{r['contract']:>8.0f}{r['start']:>8.0f}{r['gm']:>5.0f}%")
    L.append("-" * 66)
    L.append(f"{'MONTHLY':16}{'':>4}{t['cost']:>8.0f}{t['floor']:>8.0f}"
             f"{t['anchor']:>8.0f}{t['contract']:>8.0f}{t['start']:>8.0f}")
    return "\n".join(L)


def guardrails(t):
    g = []
    if t["contract"] < ENGAGEMENT_MIN:
        g.append(f"  ! Under the ${ENGAGEMENT_MIN:,}/mo engagement minimum. Re-scope, or offer projects and Website Care.")
    if t["contract"] < t["floor"]:
        g.append("  ! Contract price is UNDER the 50% floor. Owner sign-off required.")
    return g


def term_ladder_lines(start_total, users, indent="  "):
    L = ["CLIENT-FACING TERM LADDER (monthly):",
         f"{indent}1 year is the minimum term and the highest price; longer terms lock in a lower rate."]
    for t, price in term_ladder(start_total):
        unit = "year " if t == 1 else "years"
        pu = f"   (${price/users:,.0f}/user)" if users else ""
        tag = "   <- minimum term, highest price" if t == 1 else ""
        L.append(f"{indent}{t} {unit}  ${price:,.0f}{pu}{tag}")
    return L


def single_report(rows, t):
    L = ["=" * 66, "{{COMPANY_NAME}}  -  PRICING WORKSHEET (internal)", "=" * 66]
    L.append(detail_block(rows, t))
    if t["agents"]:
        L.append(f"Agents loaded into device cost: {', '.join(t['agents'])}")
    L.append("")
    L.append("THE BAND (internal, monthly):")
    L.append(f"  Floor (walk-away)      ${t['floor']:,.0f}")
    L.append(f"  Anchor (1-yr standard) ${t['anchor']:,.0f}")
    cap = " (capped)" if t["value_mult"] >= START_CAP else ""
    note = f"+{(t['value_mult']-1)*100:.0f}% value{cap}" if t["value_uplift"] else "no value factors"
    L.append(f"  START (opening ask)    ${t['start']:,.0f}   ({note})")
    L.append("")
    L.extend(term_ladder_lines(t["start"], t["users"]))
    if t["users"]:
        L.append("  Benchmark: $75-200 fully managed; $150-300 security/compliance heavy.")
    gr = guardrails(t)
    if gr:
        L.append("")
        L.append("FLAGS:")
        L.extend(gr)
    return "\n".join(L)


def packages_report(client):
    users = client.get("users", 0)
    years = client.get("years", 1)
    name = client.get("client", "Client")
    priced = [price_option(o, users, years) for o in client["options"]]

    L = ["=" * 78, f"{COMPANY_NAME}  -  PROPOSAL OPTIONS for {name}  (internal)",
         f"{len(priced)} options assembled from building blocks | terms 1/2/3/5 yr | "
         f"{users} users", "=" * 78, ""]

    # Per-option detail
    for rows, t in priced:
        tag = "  << recommended" if t["recommended"] else ""
        L.append(f"### {t['name']}{tag}")
        if t["value_factors"]:
            L.append(f"value factors: {', '.join(t['value_factors'])}")
        L.append(detail_block(rows, t))
        for gline in guardrails(t):
            L.append(gline)
        L.append("")

    # Internal band
    L.append("=" * 78)
    L.append("INTERNAL  -  band per option (monthly):")
    hdr = f"{'':22}" + "".join(f"{t['name'][:13]:>14}" for _, t in priced)
    L.append(hdr)
    def money(v):
        return f"{'$' + format(v, ',.0f'):>14}"
    for label, key in [("Floor (walk-away)", "floor"), ("Anchor (1-yr standard)", "anchor"),
                       ("START (open here)", "start")]:
        L.append(f"{label:22}" + "".join(money(t[key]) for _, t in priced))
    if users:
        L.append(f"{'START $/user':22}" + "".join(money(t['start']/users) for _, t in priced))

    # Client-facing term ladder matrix
    L.append("")
    L.append("=" * 78)
    L.append("CLIENT-FACING TERM LADDER (monthly)  -  1-yr is the minimum term and highest price")
    L.append(hdr)
    ladders = [dict(term_ladder(t['start'])) for _, t in priced]
    for term in PRESENT_TERMS:
        label = f"{term} year" + ("s" if term > 1 else "") + (" (highest)" if term == 1 else "")
        L.append(f"{label:22}" + "".join(money(lad[term]) for lad in ladders))
    L.append("=" * 78)

    rec = next((t for _, t in priced if t["recommended"]), None)
    if not rec and priced:
        rec = priced[len(priced) // 2][1]   # default to the middle option
    if rec:
        rl = dict(term_ladder(rec["start"]))
        if users:
            pu = " | ".join(f"{term}yr ${rl[term]/users:,.0f}" for term in PRESENT_TERMS)
            L.append(f"{rec['name']} per user: {pu}")
        L.append("")
        L.append(f"Lead with '{rec['name']}'. Present the term ladder: the 1-year (${rl[1]:,.0f}) is the "
                 f"highest and the minimum term;")
        L.append(f"2, 3, and 5 years step down to ${rl[5]:,.0f}. Say plainly that the 1-year is the highest "
                 f"price. Never cross any option's floor.")
    L.append("Present these as options you built for THIS client, not as standard tiers.")
    L.append("Response time is identical across every option. Onboarding is billed separately.")
    return "\n".join(L)


def main():
    p = argparse.ArgumentParser(description="{{COMPANY_NAME}} pricing configurator")
    p.add_argument("--packages", help="path to a client packages JSON file")
    for u in UNITS:
        p.add_argument(f"--{u.replace('_','-')}", type=int, default=0, dest=u)
    p.add_argument("--onsite-hours", type=int, default=0, dest="onsite_hours")
    p.add_argument("--users", type=int, default=0)
    p.add_argument("--years", type=int, default=1)
    for a in AGENTS:
        p.add_argument(f"--{a.replace('_','-')}", action="store_true", dest=a)
    for f in VALUE_FACTORS:
        p.add_argument(f"--{f.replace('_','-')}", action="store_true", dest=f,
                       help=VALUE_FACTORS[f][1])
    args = p.parse_args()

    if args.packages:
        with open(args.packages) as fh:
            print(packages_report(json.load(fh)))
        return

    opt = {u: getattr(args, u) for u in UNITS}
    opt["onsite_hours"] = args.onsite_hours
    opt["agents"] = [a for a in AGENTS if getattr(args, a)]
    opt["value_factors"] = [f for f in VALUE_FACTORS if getattr(args, f)]
    rows, totals = price_option(opt, args.users, args.years)
    print(single_report(rows, totals))


if __name__ == "__main__":
    main()
