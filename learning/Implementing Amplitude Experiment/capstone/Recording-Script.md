# Capstone recording script

Read only the paragraphs under “Say.” Stage directions and timestamps are not spoken. Target roughly 140–150 words per minute with short pauses; rehearse and adjust to an actual 8–10 minute recording. The spoken script contains approximately 1,350 words: about 9–9.6 minutes at that pace before short pauses. The timestamps are pacing guides, not a measured video duration. Replace the name placeholder in your spoken introduction.

## 0:00–0:30 - Introduction

Show: the four notebook titles.

Say:

Hello, I am [your name]. I will explain my test plans for AmpliCook, AmpliPost, AmpliStub, and AmpliCare. These are mock designs based on the customer scenarios. The brief provides qualitative problems, but no measured baselines. My numerical assumptions would therefore need validation before a real launch. For each scenario, I have defined the hypothesis, outcomes, variants, allocation, implementation approach, timeline, and decisions for success, failure, or inconclusive results.

## 0:30–2:35 - Scenario A: AmpliCook

Show: Scenario A problem and hypothesis, then metrics and variants.

Say:

AmpliCook already has strong retention, but monetization is underperforming. The customer wants to increase advertisements without damaging the experience that keeps people returning. I would first inspect home-feed engagement, retention cohorts, ad revenue, and feedback about ad load to validate this problem.

My hypothesis is that a modest increase in ad density can improve seven-day ad revenue by ten percent while keeping the retention decline below two percentage points. The proposed control shows one ad after ten organic cards, with a session cap of three. Treatment shows one after eight cards, with a cap of four. These are proposed values, not facts about the existing app. Recipe ranking and ad format stay constant.

This is a Do No Harm design centered on retention, with revenue improvement also required for rollout. At an assumed forty percent retention baseline, the unacceptable loss is two percentage points. I need the lower confidence bound of the treatment difference to stay above that margin. Simply seeing no statistically significant decline would not prove safety.

Revenue is measured per exposed user, including people who generate no revenue. That avoids selecting only successful ad viewers. I also monitor recipe engagement, crashes, and feed latency.

I would use client Experiment SDKs with remote evaluation on iOS and Android, maintaining consistent identity with Analytics. Users are assigned fifty-fifty, and exposure occurs when the home feed renders. A separate A/A validates assignments and tracking before the A/B test.

My illustrative target is ten thousand users per arm, with at least two weeks of enrollment and time for retention outcomes to mature. I would roll out only if retention safety, revenue improvement, and guardrails pass. If retention is harmed, I would roll back even if revenue increases. If evidence is inconclusive, I would retain the existing feed.

## 2:35–4:40 - Scenario B: AmpliPost

Show: Scenario B primary metric, price comparison, and timeline.

Say:

AmpliPost needs subscription revenue quickly, but its retention is fragile. The key distinction is that more sign-ups are desirable, while revenue is the higher business priority. I would validate the offer-to-purchase funnel and reconcile discounts, payments, refunds, and fees with billing before launching.

The proposed experiment compares the same unlimited monthly plan at a discounted sixteen dollars and a full price of twenty dollars. Those prices are illustrative. I assume the control is already monthly; if it is annual, the experiment also changes billing frequency, and the interpretation and revenue horizon must be redesigned.

My primary metric is thirty-day net subscription revenue per exposed eligible user. Looking only at revenue per purchaser would be misleading because a higher price could discourage many users from purchasing at all. I include nonbuyers as zeros and account for refunds and fees. The target is a ten percent relative revenue increase.

Sign-up conversion and checkout starts are secondary metrics. Retention, conversion loss, and billing complaints are safety checks. As a simple gross-revenue illustration, ten percent conversion at sixteen dollars breaks even with eight percent conversion at twenty dollars. But the actual decision still uses net revenue and all safety gates.

I would use client-side remote evaluation across web and mobile, with stable account assignment. The billing service must enforce the same offer that the user saw. Existing subscribers and outstanding promotional commitments are excluded, and accepted purchase terms remain honored.

The illustrative sample is twenty-six thousand users per arm. Although the business is under time pressure, a thirty-day metric requires thirty days of observation after the last participant enters. I would not call early revenue a final result. A win requires credible revenue improvement and acceptable safety outcomes. A billing defect or harmful retention effect triggers rollback of new offers. An uncertain result means keeping the current offer and considering a new, narrower test.

## 4:40–6:45 - Scenario C: AmpliStub

Show: Scenario C integration choice, variants, and purchase metric.

Say:

AmpliStub's customers struggle to find desirable and affordable seats. That may explain low purchase conversion, but I would validate it using the booking funnel, existing feedback, and seat-selection behavior. I would also investigate inventory errors and latency so the test addresses the right problem.

The treatment highlights up to three suitable seats or seat blocks while preserving the existing seat map and filters. Recommendations respect party size and the user's price filter. The control has no highlights. The ranking rule is frozen before launch, and users can still choose any available seat.

The hypothesis is that easier comparison increases purchase conversion by ten percent relative. With an assumed twelve percent baseline, the target becomes thirteen point two percent, an increase of one point two percentage points. I measure confirmed purchases for the first eligible event within twenty-four hours of exposure.

I also measure quick seat selection and capped time to selection. Including nonselectors in the time metric avoids making the experience look faster simply because slower users abandoned it. Booking failures, net revenue, and server latency are guardrails.

This scenario explicitly requires the lowest evaluation latency, so I choose server-side local evaluation. The server evaluates warmed flag configurations without a remote evaluation call on each request. The tradeoff is that this design cannot rely on Amplitude's remote identity resolution. I therefore specify a stable browser identifier and clearly limit the inference unit to that browser or device.

The plan uses fifty-fifty allocation, approximately thirteen thousand users per arm, and at least two weeks of enrollment. I also acknowledge that both arms share ticket inventory: one shopper can consume a seat another might buy. If that interference is substantial, I would redesign around event-level randomization. Successful conversion improvement with safe revenue and latency supports rollout. Booking failures or misleading recommendations trigger rollback; uncertain results lead to another design iteration.

## 6:45–8:50 - Scenario D: AmpliCare

Show: Scenario D role-specific metrics, dropdown variants, and identity approach.

Say:

AmpliCare has two related problems: caregivers do not finish profiles, and clients often do not start them. Both groups struggle to find profile editing. I would validate separate role funnels and usability feedback to distinguish navigation friction from difficult forms.

The treatment adds a clearly labeled SmartProfile dropdown with completion status and direct view or edit actions. I keep the forms and completion requirements unchanged, so the test isolates discoverability. The control retains the existing navigation.

My primary outcome is server-validated profile completion within seven days among users whose profiles were incomplete at enrollment. People count as exposed when the navigation appears, not only after clicking the dropdown. Otherwise the denominator would exclude precisely the users who could not find the feature.

The mock baseline is thirty percent completion for caregivers and ten percent for clients. I give the two roles equal predefined weight in the primary estimate and target a fifteen percent relative improvement. I also inspect each role separately and require safety in both, so a pooled improvement cannot conceal harm to one persona. Client profile starts and caregiver contacts are secondary outcomes; more completed profiles do not automatically prove more meaningful contacts.

Unlike AmpliStub, this scenario explicitly requires Amplitude identity resolution. I therefore choose server-side remote evaluation and validate account and device identity across sessions. I also test timeout fallbacks, role routing, profile-save errors, and accessibility.

The illustrative enrollment target is seven thousand users per arm per role, or twenty-eight thousand overall. Follow-up lasts fourteen days for the contact outcome. If the combined completion result improves and both roles remain safe, I would roll out gradually. If users open profiles more often but still do not complete them, the next experiment should address form friction. Harm requires rollback; insufficient evidence means retaining the current navigation.

## 8:50–9:15 - Closing

Show: four notebook links or the scenario titles, not private account settings.

Say:

Across all four plans, I would validate assumptions, preregister decisions, check assignment and exposure quality, and wait for complete outcome windows. I use a fixed-horizon analysis consistently with the sample planning and do not treat daily safety monitoring as permission to declare an early winner. Each plan defines success, failure, and inconclusive next steps. My submission includes four separate test-plan links and this explanation of the reasoning behind them.

## Rehearsal notes

- The numerical inputs are mock assumptions; avoid saying “our data showed” or “the experiment increased” anything.
- Expand A/A verbally as “A against A,” a pipeline check with identical experiences.
- Explain SDK once if useful: the software library connecting the application to Experiment.
- If you exceed ten minutes, shorten implementation examples rather than removing a scenario or its decision criteria.
- If you finish under eight minutes, explain one metric denominator and one safety decision with an example; do not add invented results.
- This script explains rationale, as the brief requests. The detailed notebook carries definitions and calculations for the reviewer to inspect afterward.
