# Implementing Amplitude Experiment - capstone submission guide

Prepared from the supplied course summary and 2025 capstone PDF. This package contains four complete mock test plans and a recording script. Four notebooks have also been created in Bhargavi Devi's Space in partner-training and checked after reloading. Reviewer access, your recording, and Academy submission remain outstanding. No experiments were launched and no results were measured.

## Your completed notebooks

These are the actual notebook URLs, verified in the signed-in browser. They are not proof of reviewer access. The current sharing UI shows **Copy Link**, and the inspected sharing panel lists only the owner; confirm the reviewer or required sharing scope before submission.

| Scenario | Saved notebook |
|---|---|
| A - AmpliCook | [Open Scenario A](https://app.amplitude.com/analytics/partner-training/notebook/s92ecypn) |
| B - AmpliPost | [Open Scenario B](https://app.amplitude.com/analytics/partner-training/notebook/a5r7idjc) |
| C - AmpliStub | [Open Scenario C](https://app.amplitude.com/analytics/partner-training/notebook/0p70on2d) |
| D - AmpliCare | [Open Scenario D](https://app.amplitude.com/analytics/partner-training/notebook/m22c35p0) |

The notebook copies contain the plan content mapped to the original template headings. The local Markdown files contain expanded implementation and calculation detail. Start by reviewing the existing copies; you do not need to create duplicates. Steps 2–3 below explain the creation/sharing workflow for reference and future edits.

## What you must submit

The PDF specifies **five items**: one 8–10 minute recording of you explaining the four plans, plus one Amplitude notebook invite link for each of Scenarios A, B, C, and D. The plans should be copies of the official Test Plan Template saved in your own Space in the partner-training organization.

You do not need to build four applications, launch production experiments, collect real results, or submit an SDK repository for this Course 4 assignment. The technical sections demonstrate how you would implement and validate each proposed experiment. The separate technical exercise in the learning folder is a different assignment.

## Files to use

| File | Purpose |
|---|---|
| `Scenario-A-AmpliCook.md` | Mobile ad-density test with retention protection |
| `Scenario-B-AmpliPost.md` | Full-price subscription test focused on net revenue |
| `Scenario-C-AmpliStub.md` | Recommended-seat test using server local evaluation |
| `Scenario-D-AmpliCare.md` | SmartProfile navigation test using server remote evaluation |
| `Recording-Script.md` | Approximately nine-minute explanation to rehearse and record |
| `Rubric-and-QA-Checklist.md` | Requirement mapping and final submission checks |

All scenario numbers, traffic rates, proposed event names, prices, payloads, and UI details are labeled mock assumptions. The supplied brief provides qualitative supporting evidence, not measured baselines. Keep that distinction in the notebooks and your narration. A hypothetical plan does not require inventing analytics findings.

## Step 1 - Review the plans and personalize them

1. Read the problem, hypothesis, metric table, variants, allocation, timeline, and decisions in each plan.
2. Add your name as the plan owner and your submission date in the notebook. Proposed Product/Engineering/Analytics approvers are roles in the mock engagement; do not invent named approvals.
3. Keep the assumption labels. If you have real customer data, replace assumptions only with verified numbers and identify the source, timeframe, denominator, and persona.
4. Explain the distinction between percentage points and relative percentage changes. For example, conversion from 12% to 13.2% is a 1.2-point absolute increase and a 10% relative increase.
5. Be comfortable explaining why the four technical approaches differ, as shown below.

| Scenario | Experiment focus | Integration | Why |
|---|---|---|---|
| A | Do No Harm on retention, with revenue improvement required | iOS/Android client SDKs, remote evaluation | Existing native client application and Analytics instrumentation |
| B | Hypothesis Test on revenue per exposed user | Web/mobile client SDKs, remote evaluation; backend-authoritative billing | Coordinated experience across web and mobile; price integrity at checkout |
| C | Hypothesis Test on purchase conversion | Server SDK, local evaluation | Removes remote flag-evaluation round trip from the request path |
| D | Hypothesis Test on profile completion | Server SDK, remote evaluation | Amplitude identity resolution is required |

## Step 2 - Create the four Amplitude notebooks

The original PDF links to the [official Test Plan Template](https://app.amplitude.com/analytics/partner-training/notebook/46ej1doc). This URL was extracted from the PDF's actual hyperlink, not guessed.

1. Open the template while signed into the Amplitude account used for partner training.
2. Confirm that the organization is **partner-training**. If you cannot access the template, request access from your training contact. Do not create a paid organization or substitute an unrelated production project.
3. Use the notebook's copy action. The PDF shows a **Copy Notebook** dialog with a name and location selector; current menu wording may differ.
4. Choose your own Space as the destination. Use a title such as **Scenario A - AmpliCook - [Your name]**. Save the copy.
5. Replace the template guidance with the corresponding plan content. Match problem, hypothesis, goals/metrics, variants, allocation, timeline, analysis, and next steps to the template's existing headings. Add integration/QA, assumptions, and sources as additional text sections if necessary.
6. Paste Markdown as readable text and format headings/tables in the notebook editor if it does not preserve them. Check that long metric definitions have not been lost or truncated.
7. Repeat from the original template for B, C, and D. Create four separate notebooks, not four sections in one shared notebook.
8. Reopen each saved notebook and verify its scenario title, complete metric table, timeline, and decision section.

Completed in this session: the official template was accessible and all four copies were created in the personal Space labeled Bhargavi Devi's Space. The original template was not edited.

## Step 3 - Create reviewer-accessible invite links

1. In Scenario A's notebook, open **Share**.
2. Use the reviewer's access level and the **Copy Invite Link** workflow specified by the PDF. Viewing access is sufficient for assessment unless the course says otherwise.
3. Copy the resulting link into the submission worksheet below. Do not paste the original template's link or a local file path.
4. Repeat for B, C, and D. Confirm that the four URLs open four different notebooks with matching scenario titles.
5. Verify that the intended training reviewer can access the notebooks. Opening a link in your own signed-in browser verifies the destination but does not prove reviewer permissions. Use the sharing dialog's access information; if needed ask the training contact to verify access. Organization-scoped links may legitimately require sign-in, so failure in an anonymous window alone is not proof of broken sharing.

Do not guess a reviewer email address. The example person in the PDF screenshot is not an instruction to send that person an invitation.

## Step 4 - Record your explanation

1. Open the four completed notebooks in scenario order.
2. Read `Recording-Script.md` aloud once. Aim for 8–10 minutes total, approximately two minutes per scenario. Rehearse with a timer; speaking pace and pauses determine actual duration.
3. Use your usual screen recorder. Record your own explanation with clear audio; the brief does not require a slide deck. Face camera is optional unless the current submission page says otherwise.
4. Show the problem/hypothesis, metric table, and decision section as you discuss each scenario. Do not read every line.
5. State at the beginning that this is a mock design and numeric baselines are assumptions to validate before launch.
6. Explain the rationale: A protects retention; B prioritizes net revenue; C needs local evaluation for latency; D needs remote identity resolution and persona-specific checks.
7. Export an accepted format such as MP4. Suggested filename: `Implementing-Amplitude-Experiment-Capstone-[YourName].mp4`.
8. Watch the complete recording once. Confirm readable text, audible speech, 8–10 minute length, all four scenarios, and no accidental sensitive material on screen. The live Academy page checked on 21 September 2026 shows a 500 MB maximum upload size. Use an accepted video format such as MP4 and recheck any format restriction shown by the uploader.

The script is preparation for your recording. No video file has been created, and no synthetic recording is being presented as you.

## Step 5 - Submit in Partner Academy

1. Open [Course 4: Mock Scenario Capstone Project](https://trainingpartners.amplitude.com/path/implementing-amplitude-experiment/impl-exp-4-mock-scenario-capstone-project) in your signed-in training account.
2. The live page shows “Capstone Project (Experimentation) Question 1 of 5.” Question 1 is “Upload your video recording here,” with a 500 MB maximum. Upload the recording, then use Next Question and follow the live labels for Scenarios A–D. No answers have been submitted in this session.
3. Upload your finished recording in the video submission field.
4. Paste Scenario A's notebook invite link into Scenario A's field, and repeat for B, C, and D.
5. Review all five entries before submitting. Ensure each link is the saved copy in your Space.
6. Complete the submission actions shown by the course and verify a saved/submitted confirmation for each part. Save a confirmation screenshot or note for your records.
7. Keep the four notebooks accessible during review. The course summary asks you to allow up to four weeks for feedback. Respond to any request for changes; the PDF says a resubmission may require recording yourself again.

### Submission worksheet

| Item | Status/value to fill after doing the step |
|---|---|
| Plan owner / preparation date | Bhargavi Devi / 19 September 2026; actual submission date still pending |
| Target Amplitude Space | Bhargavi Devi's Space; [personal Space](https://app.amplitude.com/analytics/partner-training/space/personal/all) (resolves for the signed-in user) |
| Scenario A notebook URL | [Saved notebook](https://app.amplitude.com/analytics/partner-training/notebook/s92ecypn); reviewer access pending |
| Scenario B notebook URL | [Saved notebook](https://app.amplitude.com/analytics/partner-training/notebook/a5r7idjc); reviewer access pending |
| Scenario C notebook URL | [Saved notebook](https://app.amplitude.com/analytics/partner-training/notebook/0p70on2d); reviewer access pending |
| Scenario D notebook URL | [Saved notebook](https://app.amplitude.com/analytics/partner-training/notebook/m22c35p0); reviewer access pending |
| Video file and measured duration | Not recorded |
| Reviewer access checked | Not verified |
| Academy submission confirmation | Not submitted |

## How to explain the statistics clearly

**Baseline** is the current metric level. **MDE** is the effect size used to plan sensitivity. **Power** is the chance of detecting that assumed effect under the planning model. **Confidence interval** describes estimation uncertainty under that model. A **harm margin** is the maximum loss considered acceptable; it is a business choice agreed before launch, not a result discovered afterward.

The plans use alpha 0.05, 80% planning power, and fixed-horizon 95% intervals. Amplitude commonly defaults to sequential testing; fixed horizon is an explicit choice for these mock designs because the sample calculations and final analysis can be specified consistently. Do not use sequential defaults with fixed-horizon stopping rules accidentally. If the customer prefers sequential analysis, use its matching duration estimator and rules before launch and revise the plans.

For non-inferiority, “not statistically worse than zero” is insufficient. For A, the lower bound of the retention difference must be above -2 percentage points. If the interval is [-3, +1] points, safety is unresolved even though zero lies inside it. If it is [-1, +1], it excludes the unacceptable loss. Guardrail success also needs enough precision, not merely a nonsignificant harm test.

All required rollout gates must pass. Secondary metrics explain mechanism and inform future work; they are not additional opportunities to declare the experiment a winner. The plans do not claim independent confirmatory significance for every secondary metric or segment. Daily incident checks can stop harmful treatment without authorizing an early efficacy claim.

### Sample-size calculation notes

These are approximate planning calculations, not measurements or final production power analyses. All values are per arm. Let `z_alpha = 1.959964` and `z_power = 0.841621`.

- Continuous user-level metric: `n = ceil(2 * (z_alpha + z_power)^2 * SD^2 / absolute_MDE^2)`.
- Binary safety margin near zero true difference: `n = ceil(2 * (z_alpha + z_power)^2 * p * (1-p) / margin^2)`. Using the 95% two-sided lower bound is conservative relative to a one-sided alpha 0.05 test.
- Two-proportion superiority: with `p_bar = (p0+p1)/2`, `n = ceil((z_alpha*sqrt(2*p_bar*(1-p_bar)) + z_power*sqrt(p0*(1-p0)+p1*(1-p1)))^2 / (p1-p0)^2)`.

| Scenario | Main calculation | Approximate requirement | Rounded planned enrollment |
|---|---|---|---|
| A | Retention 40%, 2-point margin; revenue SD 1.40, delta 0.07 | 9,419 and 6,280/arm | 10,000/arm |
| B | Revenue SD 6.40, delta 0.16 | 25,117/arm | 26,000/arm |
| C | Conversion 12% → 13.2% | 12,004/arm | 13,000/arm |
| D | Client safety 10%, 1.5-point margin; client conversion 10% → 11.5% | 6,280 and 6,693/arm/client role | 7,000/arm/role; 28,000 total |

Use the largest validated requirement across the primary and required safety metrics. Revenue tails, role imbalance, repeated devices, sequential methods, and inventory clustering may change these numbers. Actual launch requires updated variance, rates, eligible unique traffic, and statistical review. Minimum runtime covers weekly cycles; follow-up allows late outcomes to mature. Fast recruitment alone does not shorten a 30-day revenue window.

The additional rule requiring the observed uplift to meet the business target is stricter than significance versus zero. The nominal 80% planning power does not imply 80% probability of passing all rollout gates at exactly the assumed MDE.

## Source precedence and completion claims

The PDF is the controlling source for this assignment's required deliverables. It explicitly says successful completion of this learning path **does not result in a badge**, whereas the local course summary quotes a badge invitation. Do not promise a badge; follow the current Academy's outcome or ask the training team to reconcile this discrepancy.

The rubric totals 21 points with a passing score of 19. The package covers all seven criteria, but only Amplitude's reviewer can assign a grade. The original PDF and course-summary file have been preserved unchanged.

Sources: supplied `Capstone Project - Mock Test Plan - Implementing Amplitude Experiment (2025).pdf`, supplied `03-Implementing-Amplitude-Experiment.md`, and official Amplitude documentation linked in each plan. Documentation checked on 2026-09-19. The live template was read and the More → Copy flow was verified. The current Share dialog uses Copy Link rather than the PDF's older Copy Invite Link label. Reviewer access remains unverified.

## Final verification - 21 September 2026

All four notebook copies were checked for persisted content after reload/open. Scenario D was re-opened on 21 September and its metrics, timeline, analysis, future work, and remote-evaluation appendix were verified. The Academy video-upload field and 500 MB limit were read; no file or answers were submitted. Reviewer access remains unverified.
