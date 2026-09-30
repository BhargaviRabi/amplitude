# Scenario A - AmpliCook: more ad revenue while protecting retention

Amplitude notebook: [Open Scenario A](https://app.amplitude.com/analytics/partner-training/notebook/s92ecypn). Created in Bhargavi Devi's Space from the official template. Reviewer access remains to be confirmed.

Status: completed mock test plan; not a launched experiment. Owner: Bhargavi Devi. Proposed approvers for a real launch: Product, Analytics, Mobile Engineering, and Ad Operations.

## 1. Problem statement and supporting evidence

The supplied scenario describes an iOS/Android meal-prep app with strong retention but underperforming monetization. The affected persona is an active, ad-supported home-feed user who wants to discover recipes and plan meals without excessive interruption. Increasing ads could grow revenue but make this core experience less useful, putting retention and sustainable user-base growth at risk.

Evidence actually available: the qualitative customer brief in the capstone PDF, Scenario A. No historical events, revenue exports, interviews, or measured rates were supplied. The following numbers are **illustrative planning assumptions, not customer findings**.

Before a real launch, inspect the preceding 28 days of Amplitude home-feed and recipe funnels, retention cohorts split by platform and tenure, ad-provider reconciled revenue, and support feedback concerning ads. Compare revenue per eligible user and retention by existing ad load; treat these correlations as problem validation, not causal evidence. Confirm the baseline and traffic assumptions below with the customer.

## 2. Hypothesis and experiment type

If we increase home-feed ad density modestly, then seven-day ad revenue per eligible exposed user will increase by at least 10% because more viewable inventory creates more monetization opportunities, while seven-day return retention will decline by less than 2 percentage points because recipe access and feed usability remain intact.

Use a **Do No Harm** design centered on retention, with revenue improvement required as a separate business gate. An absence of statistically significant harm does not establish safety; the retention interval must exclude the agreed unacceptable loss.

## 3. Goals and metrics

Time zero is the first eligible home-feed render. The denominator includes every eligible exposed user, including users with no subsequent activity or revenue. Each user enters once. Windows are elapsed time from that first exposure, using UTC timestamps.

| Role | Exact metric and source | Assumed baseline | Target or safety margin |
|---|---|---|---|
| Primary safety metric | Seven-day return retention: users with a qualifying `Recipe Viewed` or `Meal Plan Saved` event during hours 24–192, divided by exposed users | 40% | Non-inferiority margin: -2 percentage points (5% relative loss); treatment-control lower 95% confidence bound must exceed -0.02 |
| Required business metric | Seven-day ad revenue per exposed user: sum of reconciled `Ad Revenue Recorded.net_revenue_usd` during hours 0–168 / exposed users; include zeros | $0.70; user-level SD $1.40 | +10% relative MDE = +$0.07, target $0.77; require positive lower 95% bound and estimated lift at least 10% |
| Secondary | Seven-day recipe engagement: users with `Recipe Viewed` within 168 hours / exposed users | 60% | +5% relative MDE = +3 points, target 63% |
| Secondary | Viewable ad impressions per exposed user in 168 hours, from unique `Ad Impression` records | 14 | +15% relative MDE, target 16.1 |
| Guardrail | Crash-affected exposed users within 168 hours / exposed users | 1% | Upper 95% bound on absolute increase below +0.5 points |
| Operational guardrail | Home-feed p95 render latency, from performance telemetry | 800 ms | No sustained increase above +100 ms versus control; incident review if exceeded for two consecutive hourly windows with at least 100 renders/arm/window |

Revenue must represent actual monetization, not ad requests or estimated impressions alone. Freeze currency conversion and late-ad-revenue reconciliation rules before launch; wait 48 hours after outcome maturity for delayed ingestion. Growth of the overall user base is a long-term business KPI, not a direct causal claim from this existing-user test.

## 4. Variants

All ad-density values are proposed mock values to validate against the real app.

| Variant | User experience | Proposed payload |
|---|---|---|
| `control` | Current feed, assumed one clearly labeled ad after every 10 organic cards, maximum 3 ads per session | `{"organic_cards_between_ads":10,"max_ads_per_session":3}` |
| `treatment` | One clearly labeled ad after every 8 organic cards, maximum 4 ads per session | `{"organic_cards_between_ads":8,"max_ads_per_session":4}` |

Keep ad format, demand partners, recipe ranking, notifications, and ad-free entitlement unchanged. Never place an ad ahead of the first recipe. Honor the app's existing advertising eligibility and consent rules. Unknown flags or fetch failures render the current feed; do not label fallback users as successfully exposed treatment users.

## 5. Targeting and allocation

Eligible: signed-in, ad-supported users on supported iOS/Android versions who reach the home feed and are eligible to receive ads. Exclude staff, QA devices, known bots, ad-free subscribers, and users in competing feed/ad experiments before randomization.

Randomize persistently at user level, with the same application user ID supplied to Analytics and Experiment. Use 50% control / 50% treatment inside each platform segment. Users moving between devices retain their assignment; verify this in QA. Do not rerandomize each session. Report that this initial test applies to signed-in users, with anonymous users requiring separate validation.

A separate QA flag receives internal traffic. After QA, ramp the analysis experiment's eligible audience from 10% to 50% to 100% over three days, retaining a 50:50 arm split throughout. Keep assignment stable during ramp, record ramp dates, and include all valid first exposures in the preregistered analysis. Users outside the rollout receive normal production behavior and are not the experiment's control denominator.

## 6. Integration and validation

Use mobile **Feature Experiment client SDKs with remote evaluation**, integrated with the existing Analytics identity. Create separate iOS/Android deployments per environment in the same intended Analytics project. Fetch after identity is ready and before the home-feed decision; record exposure when the selected feed is actually rendered, not on background prefetch. Verify the SDK's automatic-exposure behavior so there is exactly one tracking mechanism per exposure.

Proposed flag: `capstone-a-home-feed-ad-density`. Proposed events are specifications to map to the existing taxonomy, not claims that they already exist. Check flag key, variant, user/device identity, timestamps, app version, platform, ad impression ID, and revenue transaction ID. Deduplicate ad callbacks; reconcile revenue against the ad provider. Keep keys out of the test-plan notebook.

For a first Experiment integration, run an A/A with identical feed payloads for at least seven days and adequate diagnostic traffic. Confirm stable assignments, expected 50:50 allocation, event joins, no duplicate revenue, and no unexplained platform differences. An A/A is pipeline validation, not proof that every metric must have a nonsignificant p-value.

## 7. Statistical settings and timeline

Pre-register a fixed-horizon analysis using a two-sided Welch T-test at alpha 0.05, 80% planning power, user-level observations, and 95% confidence intervals. This deliberately differs from the usual sequential default so the mock sample-size calculation and final decision are auditable. Use the retention difference interval against -0.02; use a validated external analysis if the workspace cannot express this margin directly. Do not change methods after seeing results. Secondary metrics are exploratory and cannot rescue a failed primary gate.

Approximate normal planning gives 9,419 users/arm for retention non-inferiority at a true difference of zero, and 6,280/arm for revenue under the stated SD. Set a rounded minimum of **10,000 users per arm**, subject to recalculation using actual variance and safety metrics. The sample-size note in the submission guide explains the method. The revenue MDE powers detection versus zero, not an 80% chance of clearing the additional point-estimate threshold exactly at 10%.

| Phase | Proposed duration and exit condition |
|---|---|
| Design and baseline validation | 1 week; metric definitions, harm margins, sample size signed off |
| Integration, QA, A/A | 1–2 weeks; extend if diagnostic traffic is inadequate |
| A/B enrollment | At least 14 days; planning assumption 2,000 newly eligible users/day combined, around 28,000 before ramp losses; reach 10,000/arm |
| Outcome maturity and ingestion | 8 days after last enrollment plus 2 days ingestion/reconciliation |
| Analysis and decision | 2 working days; about 6–7 weeks end to end including preparation |

If enrollment is short, continue only to the preregistered maximum of 28 enrollment days, then mature all outcomes. Do not repeatedly extend until significance appears. Low traffic at that cap means inconclusive or a newly designed experiment.

## 8. Analysis and potential next steps

Before interpreting effects, check sample-ratio mismatch (investigate p < 0.001), identity consistency, missing exposure joins, revenue reconciliation, and completion of all observation windows. Diagnose assignment and exposure counts separately. A tracking failure blocks inference. Inspect prespecified iOS/Android and new/returning-user splits diagnostically; do not declare segment winners without a new confirmatory plan.

- **Success:** retention lower bound exceeds -2 points, revenue lower bound exceeds zero with at least 10% estimated lift, and guardrails pass. Roll out 25%, 50%, then 100%, reviewing each stage; monitor 28-day retention before making a long-term retention claim.
- **Failure or harm:** roll back on a safety incident or credible guardrail breach, even if ad revenue rises. Investigate placement, latency, and user feedback; propose a lower-density treatment.
- **Inconclusive:** an interval crossing the harm margin or zero is not a win. Keep the current experience; report the interval and achieved sample, then consider a better-powered test or a more differentiated treatment.

Record the final decision, evidence, owner, and follow-up date. No experiment results are claimed in this mock plan.

## 9. Sources

Scenario and required deliverables: supplied capstone PDF, pages 1–3 and rubric page 5; local course summary, Courses 2–4. Technical choices checked against [remote evaluation](https://www.amplitude.com/docs/feature-experiment/remote-evaluation), [event tracking](https://www.amplitude.com/docs/feature-experiment/under-the-hood/event-tracking), and [T-test analysis](https://amplitude.com/docs/feature-experiment/experiment-theory/analyze-with-t-test). Numerical assumptions and rollout choices are proposed design decisions.
