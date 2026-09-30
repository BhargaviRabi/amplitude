# Scenario B - AmpliPost: undiscounted monthly subscription

Amplitude notebook: [Open Scenario B](https://app.amplitude.com/analytics/partner-training/notebook/a5r7idjc). Created in Bhargavi Devi's Space from the official template. Reviewer access remains to be confirmed.

Status: completed mock test plan; not a launched experiment. Owner: Bhargavi Devi. Proposed real-launch approvers: Product, Analytics, Billing Engineering, and Finance.

## 1. Problem statement and supporting evidence

The supplied brief describes a web/mobile social application with insufficient unlimited-plan revenue, tenuous retention, and an urgent need for revenue. The affected persona is a signed-in free user considering an unlimited subscription. A discounted offer may increase purchases without generating enough revenue; removing the discount may improve revenue per buyer but reduce conversion or retention.

Evidence available is the qualitative capstone Scenario B. There are no supplied billing records, measured conversion rates, or customer interview findings. All numbers below are **illustrative planning assumptions**.

Before launch, examine 28 days of Amplitude offer-to-payment funnels by platform and acquisition source; reconcile payments, refunds, and discounts with billing; review cancellation reasons and retention by tenure. Check the actual discounted plan's billing interval. This mock design assumes both offers are monthly so price is the only intended change. If the actual control is annual, document that this is a bundle of price and billing-frequency changes and compare an appropriate revenue horizon before proceeding.

## 2. Hypothesis and experiment type

If we replace the discounted unlimited monthly offer with the same plan at full monthly price, then 30-day net subscription revenue per exposed eligible user will increase by at least 10%, because the higher realized price will outweigh any acceptable conversion loss, without an unacceptable reduction in retention.

Use a **Hypothesis Test** with revenue as the primary outcome. Increased sign-ups remain desirable but are subordinate to revenue in the brief; this plan makes that tradeoff explicit rather than promising both will improve.

## 3. Goals and metrics

First valid subscription-offer render is time zero. Include all eligible exposed users in the primary denominator, including nonbuyers with zero revenue. Use user-level totals, not transaction-level averages or revenue per purchaser alone.

| Role | Definition and source | Assumed baseline | MDE or safety threshold |
|---|---|---|---|
| Primary | Net subscription revenue per exposed user within 720 hours: attributable collected subscription payments less refunds, taxes, and payment/store fees, converted to USD using a frozen rule | $1.60; SD $6.40 | +10% relative = +$0.16, target $1.76; lower 95% bound above zero and estimated lift at least 10% |
| Secondary and safety | Users with first successful `Subscription Purchased` within 168 hours / exposed users | 10% | Improvement MDE +10% relative, target 11%; safety margin -2 percentage points, lower 95% difference bound above -0.02 |
| Secondary | Users with `Checkout Started` within 168 hours / exposed users | 20% | +10% relative MDE, target 22% |
| Guardrail | Users with core social activity during hours 24–192 / exposed users | 35% | Lower 95% difference bound above -2 points |
| Guardrail | Users with a subscription refund or billing complaint within 720 hours / exposed users | 0.5% | Upper 95% difference bound below +0.5 points |
| Diagnostic | Renewal, cancellation, refund rate among purchasers, and payment success among checkout attempts | Not supplied | Describe with intervals; these condition on post-treatment actions and are not substitutes for the primary causal comparison |

Use server-authoritative billing events with unique transaction IDs; deduplicate webhooks and link refunds to the originating purchase. Include refunds received within the defined 30-day outcome window and freeze the extract after a further 72-hour ingestion allowance. Report later refunds separately. Never call 30-day revenue lifetime value.

## 4. Variants

Mock price assumptions: control is $16/month after a 20% discount on a $20 list price; treatment is $20/month with no discount. Replace these with actual prices before a real launch.

| Variant | Experience |
|---|---|
| `control` | Existing discounted unlimited monthly plan; show $16/month and accurate discount copy |
| `treatment` | Same unlimited features and monthly billing, $20/month, no discount messaging |

Keep trial policy, placement, benefits, billing interval, cancellation process, and purchase flow constant. Show the same assigned price at offer, checkout, and payment confirmation. Exclude existing paid subscribers and users with outstanding quotes/promotions that must be honored. Preserve accepted terms after purchase; never reprice an existing subscriber when the flag changes. On evaluation failure, serve the established offer through the normal authoritative pricing service.

At the assumed control conversion, $16 × 10% = $1.60 gross revenue per exposed user. At $20, 8% conversion is the gross break-even point; 8.8% produces $1.76. These are intuition only: the primary net-revenue metric still determines the outcome after fees and refunds. The $1.60 net baseline is a separate illustrative assumption to validate, not derived from that gross illustration.

## 5. Targeting and allocation

Eligible: signed-in free users eligible to buy the monthly plan who reach the offer on web, iOS, or Android in a single supported currency/market. Exclude staff, bots, existing subscribers, conflicting pricing tests, and entitlement/promotion exceptions before assignment. Expansion to other currencies follows a separate test.

Use stable account-level assignment, 50% control / 50% treatment in each platform segment. Pass the same account ID across devices and Analytics/Experiment; record platform at first exposure for analysis. Ramp total eligible traffic 10% → 50% → 100% over three days with the arm ratio unchanged. Nonenrolled users receive the existing offer outside the analysis.

## 6. Integration and validation

Use **client-side Feature Experiment with remote evaluation**, with web, iOS, and Android client deployments per environment. This covers both web and native experiences and preserves one coordinated experiment. The backend remains authoritative for the offer and charge; do not trust a browser-provided price or put a server deployment key in client code.

Proposed flag: `capstone-b-unlimited-monthly-price`. Fetch after identity initialization. Record exposure only when the assigned offer is rendered, and pass the approved offer ID into the billing workflow. Validate web-to-mobile journeys, login/logout, repeated visits, price consistency, eligibility, billing failures, refunds, and fallback. Retain existing Analytics instrumentation and map proposed `Offer Viewed`, `Checkout Started`, `Subscription Purchased`, `Subscription Refunded`, and core activity events to actual names.

Run A/A with the same price in both arms if Experiment is newly integrated; use at least seven days plus adequate traffic to validate identity, allocation, exposure joins, and revenue reconciliation. A/A does not prove price changes are safe.

## 7. Statistical settings and timeline

Pre-register a fixed-horizon two-sided Welch T-test, alpha 0.05, 80% power, 95% confidence intervals, one primary metric, and user-level outcomes. Use a validated external margin comparison for guardrails if unavailable in the workspace. A fixed horizon is chosen deliberately; daily safety monitoring must not become daily efficacy decisions. Secondary improvement targets are exploratory; no multiple-metric winner selection.

Using assumed revenue SD $6.40 and a $0.16 absolute MDE gives approximately 25,117 users/arm. Plan **26,000 users per arm** and recalculate from actual revenue variance and safety requirements before launch. Heavy revenue tails or heterogeneous fees can require more. Achieving this sample powers a test against zero; it does not guarantee clearing every business gate.

| Phase | Duration and exit condition |
|---|---|
| Design, pricing confirmation, baseline validation | 1 week |
| Integration, billing QA, A/A | 1–2 weeks, longer if unresolved tracking issues |
| Enrollment | Minimum 14 days and 26,000/arm; assume 4,000 newly eligible users/day combined, with ramp losses allowed for |
| Maturity | 30 days after the last enrolled user; keep accepted pricing terms consistent |
| Reconciliation and decision | 3 days ingestion plus 2 working days review |

Allow roughly 10–12 weeks including preparation. If ramp losses prevent reaching the sample in 14 days, enroll longer up to a fixed 28-day cap; mature all users afterward. Revenue urgency does not justify claiming a 30-day result after one week. Early seven-day revenue is descriptive only. If this schedule is too slow, redesign and preregister a shorter primary horizon before launch, with explicitly narrower claims.

## 8. Analysis and potential next steps

Check assignment and exposure sample-ratio mismatch, identity consistency, billing-event deduplication, complete 30-day windows, and parity between displayed and charged prices. Investigate SRM p < 0.001 before interpreting results. Inspect platform, tenure, and acquisition-source differences diagnostically; avoid post hoc targeting based on chance findings.

- **Success:** net revenue lower bound is positive with at least 10% estimated lift, all safety margins pass, and no pricing defect exists. Expand gradually while monitoring longer-term renewal and refunds. Report any lower sign-up conversion candidly.
- **Failure:** revenue declines, safety margins fail with convincing evidence, or a billing defect occurs. Stop new treatment offers, restore the existing offer, and honor purchases already made. Investigate value perception and consider an intermediate discount in a new test.
- **Inconclusive:** if revenue is promising but uncertain or retention safety is unresolved, retain control. At the enrollment cap, report insufficient evidence; do not choose full price solely because per-purchaser revenue rose.

Document decision ownership and a 60-day renewal follow-up. No mock values are experimental results.

## 9. Sources

Supplied capstone PDF Scenario B and rubric; course summary Courses 2–4. Implementation references: [remote evaluation](https://www.amplitude.com/docs/feature-experiment/remote-evaluation), [event tracking](https://www.amplitude.com/docs/feature-experiment/under-the-hood/event-tracking), and [T-test analysis](https://amplitude.com/docs/feature-experiment/experiment-theory/analyze-with-t-test). Prices, thresholds, and traffic are explicit mock assumptions.
