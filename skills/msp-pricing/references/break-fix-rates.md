# {{COMPANY_NAME}} Pricing: Break-Fix and Hourly Rate Card

**Defaults you must review:** these are one working MSP's numbers in one market. See the "Setup
Decisions" section of `../SKILL.md` before treating any rate here as settled for your shop.

Example defaults from the source MSP. This is the owning source for every hourly rate
{{COMPANY_NAME}} charges. Rates here are what onboarding, migrations, projects, out-of-scope
requests, and non-contract work bill at. Derived from the loaded costs in `labor-rates.md` using
the same multipliers as the managed sheet, so the whole card re-costs when the levers move.

There is no retainer rate. The retainer concept (the old $120/hr on-site courtesy) is retired;
managed clients get managed rates, everyone else gets non-contract rates, and nothing bills
below the floor.

## The Card

| Rate | Managed client | Non-contract |
|---|---|---|
| Remote / bench, per hour | $110 | $150 |
| On-site, per hour | $220 | $220 |

- **Managed client** rates apply to any hourly work for a client under agreement: onboarding
  (always billed separately, per the standards), migrations, projects, on-site hours beyond a
  bundled allowance, and anything out of scope for their Order.
- **Non-contract** rates apply to pay-as-you-go callers with no agreement. The remote premium
  is deliberate: the agreement should be visibly worth having. Non-contract work is scheduled
  best-effort; response targets belong to managed clients only (msp-helpdesk).

## Multipliers (owning source: the SKILL.md standards)

- After-hours work: 1.5x the applicable rate.
- Holiday work: 2x the applicable rate.
- Multipliers stack on the client's column, never invented or waived ad hoc.

## Increments and Minimums

- Remote: 30-minute minimum, then 15-minute increments.
- On-site: 1-hour minimum, then 30-minute increments. No trip fee or mileage line; travel is
  already in the on-site cost basis (see `labor-rates.md`).

## What Is Not Offered

- **No block hours or prepaid packages.** Blocks compete with the managed agreement, which is
  the product. Break-fix stays deliberately unattractive beyond a first engagement.
- **No retainer or loyalty hourly rate.** Retired everywhere.
- **No sub-year managed pricing dressed as hourly.** A non-contract caller who needs ongoing
  help gets the managed conversation (msp-sales), not a standing hourly arrangement.

## Margin Math (why these numbers)

Costs come from `labor-rates.md`: remote $40/hr loaded, on-site $80/hr loaded. Margins are
gross margin after the 3% payment-processing skim baked into every price.

| Rate | Cost | GM after fees | Vs floor (50%) |
|---|---|---|---|
| Remote $110 | $40 | ~61% | Clear |
| Remote $150 | $40 | ~70% | Clear |
| On-site $220 | $80 | ~61% | Clear |

Floors, if a negotiation ever pushes: remote $90, on-site $180 (cost x 2.128 floor multiplier,
rounded up to $10). Anything below needs owner sign-off, same rule as the managed sheet.

## Interactions

- Quotes for one-time work state hours, rate, and increments plainly, per msp-brand.
- Website Care clients are under agreement: edit time past their monthly allowance bills at the
  managed rate. Website owners without Care bill at the non-contract rate. Build and Care prices
  live in the SKILL.md section "Websites: Builds and Website Care".
- AI adoption projects price from this card as fixed-fee projects. The scope, hours, and
  prices live in the SKILL.md section "Project Offering: AI Adoption". When this card changes,
  re-derive those project prices in the same pass.
- Bundled on-site allowances inside managed agreements are priced by the configurator at the
  standard anchor and ride the contract ladder (see `cost-model.md` section 7). Overage beyond
  the allowance bills at the managed on-site rate on this card.
- When `L1_WAGE`, `FIELD_WAGE`, `BURDEN`, or the overhead levers change in `price_quote.py`,
  re-derive this card in the same pass; it prices off the same loaded costs.
