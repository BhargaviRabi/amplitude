# Scenario D - AmpliCare: make SmartProfiles easy to find and complete

Amplitude notebook: [Open Scenario D](https://app.amplitude.com/analytics/partner-training/notebook/m22c35p0). Created in Bhargavi Devi's Space from the official template. Reviewer access remains to be confirmed.

Status: completed mock test plan; not a launched experiment. Owner: Bhargavi Devi. Proposed real-launch approvers: Product, Analytics, Backend Engineering, and Customer Experience.

## 1. Problem statement and supporting evidence

The supplied scenario describes a web caregiving marketplace where too few caregivers finish profiles and too few clients begin them. Both personas struggle to find and edit profiles because of the current UX. Incomplete caregiver profiles may limit useful supply; incomplete client profiles may hinder family-caregiver engagement.

The evidence is the qualitative customer brief in Scenario D. No measured funnel, interview notes, or analytics access was supplied. All numbers below are **illustrative planning assumptions**, not real customer results.

Before a real launch, examine 28 days of navigation → profile start → save → completion funnels separately for caregivers and clients. Review support issues and usability observations concerning profile discoverability. Distinguish navigation difficulty from burdensome fields or validation defects. Validate the definition of a completed SmartProfile with Product and verify that a saved-but-incomplete profile does not emit completion.

## 2. Hypothesis and experiment type

If the main navigation offers a clearly labeled SmartProfile dropdown with a direct edit action and completion status, then seven-day SmartProfile completion will increase by at least 15% relative because caregivers and clients can locate and resume their profile tasks more easily. More complete profiles should support family-caregiver engagement, which remains a downstream metric rather than a guaranteed consequence.

Use a **Hypothesis Test** for completion, with explicit safety checks for each persona so pooled success cannot hide a harmed group.

## 3. Goals and metrics

First eligible navigation render is time zero. Include signed-in users whose relevant profile is incomplete at that moment, including people who never open the dropdown. Record role and completion state at enrollment; never reclassify based on treatment-driven behavior. For dual-role accounts, assign one preexisting primary role at enrollment and keep one account-level assignment.

| Role | Definition and source | Assumed baseline | MDE or safety threshold |
|---|---|---|---|
| Primary | Users whose server-validated SmartProfile first becomes complete within 168 hours / exposed users, pooled with a preregistered 50:50 caregiver/client standardization | 20% (30% caregiver; 10% client) | +15% relative = +3 points, target 23%; lower 95% difference bound above zero and point estimate at least +3 points |
| Secondary | Caregiver completion within 168 hours / exposed caregivers | 30% | +15% relative MDE = +4.5 points, target 34.5%; also safety lower bound above -3 points |
| Secondary | Client completion within 168 hours / exposed clients | 10% | +15% relative MDE = +1.5 points, target 11.5%; also safety lower bound above -1.5 points |
| Secondary | Clients with `Profile Started` within 168 hours / exposed clients | 20% | +20% relative MDE = +4 points, target 24% |
| Secondary | Clients initiating a genuine caregiver contact within 336 hours / exposed clients | 8% | +10% relative MDE = +0.8 points, target 8.8%; exploratory, not independently powered by this plan |
| Guardrail | Users encountering a profile-save error within 168 hours / exposed users | 2% | Upper 95% difference bound below +1 point |
| Operational | Navigation/server p95 latency | 300 ms | No sustained increase over +50 ms; review two consecutive hourly windows with at least 100 requests/arm/window |

Use `SmartProfile Completed` only on an incomplete-to-complete transition validated by the backend; count each account once. Contact events must exclude spam/test traffic using rules fixed before randomization. Use backend IDs, role, completion version, and event timestamps, without logging profile contents or family details.

The 50:50 standardization gives both personas equal decision weight. It is a design choice, not a claim about actual business composition. Freeze these weights before launch; report the observed-mix business impact separately. Compute weighted arm means and a stratified variance using role-level estimates in a validated analysis if the notebook's built-in chart cannot express them.

## 4. Variants

| Variant | Experience |
|---|---|
| `control` | Existing navigation and current route to viewing/editing SmartProfile |
| `treatment` | Persistent “SmartProfile” dropdown in main navigation, showing completion status plus “View profile” and “Complete your profile”/“Edit profile,” linked directly to the appropriate role-specific form |

Keep form fields, validation requirements, matchmaking, caregiver ranking, contact flow, and notifications unchanged. Do not bundle a form redesign into this first test; otherwise the cause is ambiguous. Validate screen-reader labels, keyboard focus, narrow-screen usability, and correct role routing. On evaluation failure render current navigation.

## 5. Targeting and allocation

Eligible: signed-in caregivers or clients on supported web browsers, with an incomplete SmartProfile and access to the shared navigation. Exclude staff, bots, suspended/test accounts, completed profiles, and users enrolled in overlapping onboarding experiments before randomization.

Use **50% control / 50% treatment within each enrollment role**, with stable account identity and Amplitude ID resolution. One person/account must not receive separate variants for their two roles. Pass consistent application user ID and first-party device ID into server evaluation and Analytics; verify multi-device login and identity transitions before launch. Do not claim identity resolution automatically prevents every assignment jump.

Ramp the eligible audience 10% → 50% → 100% over three days, keeping 50:50 arms. Users outside the rollout remain outside the exposed analysis population. Stop new enrollment at the fixed endpoint; retain assignments through follow-up.

## 6. Integration and validation

Use a **server-side Experiment SDK with remote evaluation**, because Amplitude identity resolution is an explicit requirement. Local evaluation would reduce evaluation latency but does not satisfy that requirement. Use environment-specific server deployments linked to the correct Analytics project, and keep server deployment keys off the browser.

Proposed flag: `capstone-d-smartprofile-navigation`. Resolve the signed-in identity before requesting evaluation. Apply an agreed server timeout and fallback to current navigation. Cache only according to the selected SDK's documented behavior; never reuse one user's result for another. Log intended assignment, fallback, route latency, and actual rendered variant. Record exposure at navigation render, not dropdown click, so people who fail to discover the control navigation still count.

Map `Navigation Rendered`, `Profile Started`, `Profile Saved`, `SmartProfile Completed`, `Profile Save Failed`, and `Caregiver Contact Initiated` to actual taxonomy. Join server completion to the same user as exposure. Test repeat visits, two devices, guest-to-login transitions, role switching, already-complete exclusion, event deduplication, timeout fallback, and accessibility.

For first-time Experiment instrumentation, run an A/A with identical navigation for at least seven days and adequate traffic. Inspect role-specific 50:50 assignment and exposure balance, merged identities, completion counts, and remote-call latency before A/B.

## 7. Statistical settings and timeline

Pre-register fixed-horizon analysis at alpha 0.05, 80% planning power, and 95% intervals. Use a stratified difference in user-level binary means for the standardized primary. Configure the platform's fixed-horizon T-test for supporting per-role charts; do not present an unweighted pooled chart as the standardized primary. Use a validated external analysis for the weighted estimate and safety margins when needed. Secondary uplift claims remain exploratory.

Plan **7,000 users per arm per role**: 28,000 total users, equally divided across the two arms and two roles. At the assumed rates, approximate role safety requirements are 3,663/arm for caregivers (-3 points) and 6,280/arm for clients (-1.5 points); the client superiority target of 10% → 11.5% needs about 6,693/arm. The rounded target also exceeds the pooled primary requirement. Recalculate actual variance, role mix, and all guardrails before launch; this sample does not independently power the 0.8-point contact-rate target.

| Phase | Duration and exit condition |
|---|---|
| Design, funnel baseline, completion rules | 1 week |
| Backend integration, identity/accessibility QA, A/A | 1–2 weeks |
| Enrollment | At least 14 days and 7,000/arm/role; assume 1,000 newly eligible users/day, half per role; about 28 days before ramp losses |
| Maturity and ingestion | 14 days after final enrollment for downstream contact, then 2 days ingestion |
| Review | 2 working days; roughly 9–11 weeks including preparation |

Set a maximum enrollment of 42 days to accommodate ramp losses and uneven role traffic. If one role remains undersampled, do not ship to both based on the other role's success. Report inconclusive or preregister a narrower follow-up. Stop based on the predefined sample and duration rules, not a favorable p-value.

## 8. Analysis and potential next steps

Check sample-ratio mismatch within each role (investigate p < 0.001), identity merges, missing exposure/completion joins, role routing, complete windows, and the weighted primary calculation. Audit fallbacks and failed renders by intended assignment to detect selection bias. Report role estimates alongside the standardized primary; do not cherry-pick whichever aggregation looks better.

- **Success:** standardized completion improves with positive lower bound and at least +3 points estimated lift, both role safety bounds pass, and operational/save-error guardrails pass. Roll out gradually, monitor contact quality, and test form simplification separately if needed.
- **Failure:** completion worsens, either persona shows unacceptable harm, errors rise, or role routing breaks. Restore current navigation and use role-specific usability research to diagnose the issue.
- **Inconclusive:** retain control. If profiles are opened more often without completion improving, investigate form friction in a new experiment. If completion rises but family contacts are uncertain, report only completion success and continue downstream measurement without claiming proven engagement lift.

Record the release owner, final decision, and follow-up review date. No customer results or identity QA outcomes have been fabricated.

## 9. Sources

Supplied capstone PDF Scenario D and rubric; local course summary Courses 2–4. Technical references: [remote evaluation and identity resolution](https://www.amplitude.com/docs/feature-experiment/remote-evaluation), [data model](https://www.amplitude.com/docs/feature-experiment/data-model), [server SDK](https://www.amplitude.com/docs/sdks/experiment-sdks/experiment-node-js), and [T-test analysis](https://amplitude.com/docs/feature-experiment/experiment-theory/analyze-with-t-test). Metrics, UI details, weights, and numeric values are proposed assumptions.
