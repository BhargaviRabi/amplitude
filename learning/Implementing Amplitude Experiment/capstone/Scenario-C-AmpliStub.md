# Scenario C - AmpliStub: highlight desirable, affordable seats

Amplitude notebook: [Open Scenario C](https://app.amplitude.com/analytics/partner-training/notebook/0p70on2d). Created in Bhargavi Devi's Space from the official template. Reviewer access remains to be confirmed.

Status: completed mock test plan; not a launched experiment. Owner: Bhargavi Devi. Proposed real-launch approvers: Product, Analytics, Backend Engineering, and Marketplace Operations.

## 1. Problem statement and supporting evidence

The supplied scenario describes a web ticket marketplace with purchase conversion below competitors and customer feedback that seat selection is cumbersome. The affected persona is a ticket shopper comparing seats and prices for an available event. Difficulty finding desirable, affordable seats may drive booking abandonment, reducing completed purchases and the ability to grow market share.

Evidence available: the qualitative Scenario C brief, including its report of negative feedback and comparative conversion. No competitor benchmark value, interviews, event logs, or measured baseline was supplied. All numeric baselines below are **illustrative assumptions**, not research findings.

Before a real launch, inspect 28 days of event-view → seat-map → seat-selected → checkout → purchase funnels; analyze abandonment by event category, price band, and device; inspect existing feedback or consented session replays for search friction. Validate any competitor benchmark's denominator and period before comparing it to the app. Confirm that inventory and price latency, rather than only navigation, are not the dominant failure.

## 2. Hypothesis and experiment type

If the seat-selection page highlights a small set of currently available seats that balance view quality and price, then purchase conversion within 24 hours will increase by at least 10% relative because users can identify suitable seats with less search effort. We also expect faster seat selection without increasing booking failures or reducing net booking revenue materially.

Use a **Hypothesis Test** with purchase conversion as the primary outcome. This test measures conversion within the marketplace; market-share growth needs separate external evidence.

## 3. Goals and metrics

Time zero is the first eligible seat-map render. One user enters once and retains the variant across events. The primary purchase must match the event ID of that first eligible seat-map view; later event browsing remains exposed consistently but is diagnostic. All metrics use exposed users, including nonbuyers, unless explicitly labeled diagnostic.

| Role | Definition and source | Assumed baseline | MDE or guardrail |
|---|---|---|---|
| Primary | Users with server-confirmed `Ticket Purchase Completed` for the index event within 24 hours / exposed users | 12% | +10% relative MDE = +1.2 points, target 13.2%; lower 95% difference bound above zero and point estimate at least +1.2 points |
| Secondary | Users selecting a valid seat for the index event within 5 minutes / exposed users | 30% | +10% relative MDE = +3 points, target 33% |
| Secondary | Restricted time to first valid seat selection: elapsed seconds, capped at 600; nonselectors receive 600 | 240 seconds | -15% relative MDE, target 204 seconds |
| Guardrail | Users with booking/inventory failure for the index event within 24 hours / exposed users | 1% | Upper 95% absolute difference bound below +0.5 points |
| Guardrail | Seven-day net booking revenue for the index event per exposed user, including refunds and zeros | $3; SD $6 | Lower 95% difference bound above -10% of baseline (-$0.30) |
| Operational | Server p95 request latency at the seat-map route | 200 ms | No sustained increase over +20 ms versus control; review two consecutive hourly windows with at least 100 requests/arm/window |

Shorter time among only purchasers can be misleading if treatment changes who purchases. The capped selection-time metric retains nonselectors in the denominator. Revenue means marketplace net revenue under a fixed accounting definition, not ticket gross merchandise value. Deduplicate purchases/refunds with order IDs. Later refunds are a follow-up measure beyond the seven-day metric.

## 4. Variants

| Variant | Experience |
|---|---|
| `control` | Existing seat map and filters, without recommended-seat highlights |
| `treatment` | The same seat map and filters with up to three available seats or seat blocks highlighted as “Recommended,” respecting party size and the shopper's existing price filter |

Freeze the recommendation rule before launch: among eligible inventory, rank a documented normalized view-quality score and all-in price score with equal weight; use a deterministic tie-break. Validate how view quality is obtained and displayed. If no price filter is set, use the lowest-priced half of available suitable inventory before ranking. Do not silently raise the user's price ceiling. Show full prices, keep all seats accessible, and avoid auto-selection. Inventory, fees, checkout, and baseline sorting remain unchanged. Hide highlights if there is insufficient inventory or recommendation failure.

The ranking policy is a proposed product specification, not an existing algorithm supplied in the brief. Confirm it with Product before production use.

## 5. Targeting and allocation

Eligible: web users reaching a seat map for events with supported inventory and sufficient data for the frozen recommendation rule. Evaluate eligibility identically before randomization; log index event ID and available inventory. Exclude staff, bots, unsupported venues, sold-out events, and conflicting booking tests.

Use one stable first-party experiment subject ID, available to both the server and Analytics as the device ID, for **50% control / 50% treatment**. Preserve this ID through login and use it as the fixed bucketing input. Because this local design lacks Amplitude identity resolution, the inference unit is a browser/device, not a cross-device person. A later cross-device account-level design requires an explicit account ID and a new identity plan. Do not switch bucketing keys halfway through the test.

Ramp the total audience 10% → 50% → 100% over three days while retaining 50:50 assignment and stable buckets. Do not alter the arm split to chase outcomes. Inspect event category, price band, and mobile/desktop web as prespecified diagnostic segments.

## 6. Integration and validation

Use a **server-side Experiment SDK with local evaluation**. The lowest-latency requirement is the deciding factor: flag evaluation occurs in the server process without a remote evaluation round trip per request. Initialize and warm flag configuration before serving experiment traffic, refresh configuration in the background, and verify assignment tracking for the chosen SDK/version. Store the server deployment key only on the server.

Proposed flag: `capstone-c-recommended-seats`, configured for local evaluation and the specified device-ID bucketing key. Target using request-supplied properties; do not depend on remote identity enrichment. Return variant metadata with the rendered page and send exposure only when the eligible seat-map container is shown. Separate automatic assignment tracking from explicit visibility exposure; deduplicate the exposure path. Performance monitoring must capture timeouts and failed renders too, since a render-only metric can hide delivery failures.

Map `Seat Map Viewed`, `Seat Selected`, `Checkout Started`, `Ticket Purchase Completed`, `Booking Failed`, and refund events to the production taxonomy. Include index event ID, order ID where applicable, experiment subject ID, variant, recommendation eligibility, price band, and route latency. Reject duplicate orders and ensure backend purchase IDs join to the same first-party subject.

QA includes deterministic repeated assignments, login continuity, cold-start and stale-config behavior, missing inventory, inaccessible highlights, keyboard navigation, order reconciliation, and latency under load. Fall back to the existing seat map on evaluation or recommendation failure; log delivery failure and its intended assignment for bias checks. Run at least a seven-day A/A for first-time integration, extending for adequate diagnostic traffic.

## 7. Statistical settings and timeline

Pre-register a fixed-horizon two-sided Welch T-test, alpha 0.05, 80% planning power, 95% intervals, and one user/device-level primary outcome. Use the same unit in metrics and randomization. Secondary metrics are exploratory. Select fixed horizon explicitly rather than silently using the platform's sequential default; monitor safety daily without declaring early efficacy.

The normal approximation for 12% → 13.2% conversion gives approximately 12,004 users/arm using the two-proportion formula in the guide. Set **13,000 users/arm** to round upward, then verify actual inputs and other safety requirements with the duration estimator. This is not a promise of significance.

| Phase | Duration and exit condition |
|---|---|
| Design, inventory/recommendation review | 1 week |
| Server integration, load testing, A/A | 1–2 weeks |
| Enrollment | At least 14 days and 13,000/arm; assume 2,000 newly eligible browser IDs/day combined; extend for ramp losses |
| Outcome maturity and ingestion | 7 days for revenue after last enrollment plus 2 days reconciliation |
| Review | 2 working days; roughly 6–7 weeks including preparation |

Maximum enrollment is 28 days. If sample is insufficient then, report inconclusive and redesign; do not extend opportunistically. Keep treatment delivery stable through the outcome windows.

## 8. Analysis and potential next steps

Check sample-ratio mismatch (investigate p < 0.001), intended assignments versus visible exposures, delivery failures, inventory mix, bot exclusions, order joins, and complete outcome windows. Ticket inventory is shared: one arm can consume seats the other could have bought. Report this interference limitation, monitor high-demand/low-inventory events, and avoid claiming an isolated-user effect where depletion dominates. Consider a future event-level cluster design with cluster-aware power if interference is material.

- **Success:** purchase improvement is statistically positive with at least +1.2 points estimated lift, revenue/booking-failure margins pass, and latency remains acceptable. Ramp gradually, retaining monitoring of inventory fairness and refunds. Faster selection supports the mechanism but is not required to claim a separate proven effect.
- **Failure:** purchases or net revenue worsen, recommended inventory is misleading, or latency/booking failures breach the limit. Roll back highlights and investigate ranking or inventory freshness.
- **Inconclusive:** retain the existing map. Diagnose recommendation visibility and relevance; test a revised ranking or larger sample under a new preregistered plan.

Save a decision memo and technical cleanup task after rollout. No conversion lift is claimed as observed.

## 9. Sources

Supplied capstone PDF Scenario C and rubric; local course summary Courses 2–4. Technical references: [local evaluation](https://amplitude.com/docs/feature-experiment/local-evaluation), [create a local evaluation flag](https://amplitude.com/docs/feature-experiment/advanced-techniques/create-a-local-evaluation-flag), [server SDK](https://www.amplitude.com/docs/sdks/experiment-sdks/experiment-node-js), and [T-test analysis](https://amplitude.com/docs/feature-experiment/experiment-theory/analyze-with-t-test). Recommendation design and numeric values are assumptions.
