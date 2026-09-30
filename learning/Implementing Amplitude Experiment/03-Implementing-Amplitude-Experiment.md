# Implementing Amplitude Experiment (Learning Path)

**Source:** Amplitude Partner Training — [Implementing Amplitude Experimentation](https://trainingpartners.amplitude.com/path/implementing-amplitude-experiment)

**Path description (verbatim):** "This learning path trains Professional Services partners on how to implement Amplitude Experimentation."

**Recommended prerequisite:** Implementing Amplitude Analytics

**Estimated time to complete the path:** 2.5 hours

This is a combined file covering all 5 courses in the "Implementing Amplitude Experiment" learning path:

1. IMPL-EXP-1 — Experimentation Implementation Overview (8 min)
2. IMPL-EXP-2 — Design Phase: Align on a Test Plan (55 min)
3. IMPL-EXP-3 — Integrate and Deploy Phase (Feature Experimentation) (1 hr)
4. IMPL-EXP-4 — Mock Scenario Capstone Project (2 hr 30 min)
5. IMPL-EXP-5 — Decide Phase: Analysis, Action, & Governance (1 hr) — **registration-gated / inaccessible**, see note in that section.

> **Editorial note (added by the summarizer, not part of the original course):** This path is aimed at Professional Services / delivery partners who will actually run an Amplitude Experimentation implementation project for a customer, end‑to‑end: aligning on a test plan, wiring up the SDKs and deployments, launching the test, and finally interpreting results and helping the customer decide what to do next. IMPL‑EXP‑1 through IMPL‑EXP‑3 map onto the first three phases of that project (Design → Integrate & Deploy → the start of Decide), IMPL‑EXP‑4 is the graded capstone exercise that proves you can do it, and IMPL‑EXP‑5 covers the back half of the Decide phase (analysis, action, governance).

---

## Course 1: IMPL-EXP-1 — Experimentation Implementation Overview

**URL:** https://trainingpartners.amplitude.com/impl-exp-1-experimentation-implementation-overview

### About this course (verbatim)

> This foundational course provides an overview for delivery partners of how to implement Amplitude Experimentation. This course is the first in a learning path designed to train delivery partners to successfully implement Amplitude Experimentation for a customer.
>
> After taking this course you'll be able to:
> - Explain the capstone project at the end of this learning path
> - Explain the Amplitude Experimentation implementation process and typical timeline
>
> Estimated completion time: 8 minutes

This course has 2 lessons, both video-based.

### Lesson 1 of 2: Learning Experience Overview (2 min)

**Video: "Exercises Overview"** — a 2:06 video walking through the four phases of the implementation program and the hands-on exercise tied to each:

| Phase | What the exercise covers |
|---|---|
| **Design** | Create a hypothesis and associated metrics. |
| **Integrate & Deploy** | Configure Web Experimentation in your company's private sandbox. Technical roles can go on to take the technical track and integrate Feature Experiment. |
| **Capstone Project** | (Partially obscured by the video's play button in the on-screen text, but the visible portion reads along the lines of) "…\[recommendations\] for a mock scenario" — **(Manually graded as a live meeting or recording)**. |
| **Decide: Analysis, Action, & Governance** | Determine if an experiment was a success or not, and whether you would roll out, roll back, or continue running the experiment. |

### Lesson 2 of 2: Implementation Process Overview (4 min)

Text on the page: "High level overview of the implementation process for Experimentation, which takes about 90 days."

**Video: "Experimentation Implementation Timeline"** — a 5:56 video showing the end-to-end implementation timeline as a 4-stage horizontal flow:

- **Design** — 1 Week
- **Integrate & Deploy** — 2-4 Weeks
- **Decide** — 4 Weeks
- **Ongoing Success & Partnership** — (ongoing)

Example activities shown under each stage:
- **Design:** Implementation Kickoff; Experiment Design Workshop; Instrumentation Walkthrough.
- **Integrate & Deploy:** Consult on Integration & Best Practices; Instrumentation & Data Checks; Configuration Checks; Launch Experiment.
- **Decide:** Results Review; Experiment Platform Training.
- **Ongoing Success & Partnership:** Executive Business Review; Success Planning; Proactive Monitoring of Experiment Adoption; Share Best Practices on Continuous Experimentation.

The video footer notes the overall timeline runs roughly **45–60 days** end to end.

> **Explanation:** This first course is purely orientation — no hands-on work yet. Its whole job is to (a) preview the capstone exercise so you know what you're working toward, and (b) plant the 4-phase mental model (Design → Integrate & Deploy → Decide → Ongoing Success) and the ~90-day/45-60-day timeline that every later course in the path refers back to.

### Assessment / Feedback (not reproduced)

The course includes a "Check your understanding" quiz and a "Course feedback" form after the lessons. Per project scope, quiz questions/answers and feedback-survey content are not reproduced in this file (they are not taught content, and would capture this learner's personal quiz attempt data).

---

## Course 2: IMPL-EXP-2 — Design Phase: Align on a Test Plan

**URL:** https://trainingpartners.amplitude.com/impl-exp-2-design-phase-align-on-a-test-plan

### About this course (verbatim)

> This course dives into the Design Phase of an Experimentation implementation project in which you'll align on a test plan with the customer.
>
> After taking this course you'll be able to:
> - Guide a customer through the Design Phase and align with customer on a Test Plan
> - Select the right instrument method Web Experimentation or Feature Experimentation
> - Validate the problem
> - Form a Solution Oriented Hypothesis
> - Predict a result
>
> Estimated completion time: 55 minutes

This course has 6 lessons, organized under two headings: "Design Phase Overview" and "Form a Hypothesis."

### Lesson 1 of 6: Design Phase Overview (6 min)

Text on the page:

> Experimentation implementation timeline starts with the design phase, which takes about 1 week.
>
> The Experimentation workflow shows the detailed processes from creating a deployment, a test plan, testing and running the experiment, to analyzing the results and taking action. A key part of the design phase is to create a test plan.

**Video: "Workflow overview"** (5:52) — shows the full experimentation workflow as a flowchart:

Create Deployment → Install SDK in codebase → Create an Experiment → Define Goals, Variants, and Allocation → **Create a Test Plan** (highlighted as the focus of this phase) → Test the Instrumentation → Run the Experiment → Analyze Results → (branches to) Roll back the experiment / Ramp up the experiment → Share Results → Iterate on the results / Commit changes to Code.

The video uses a color legend: blue = action within Amplitude Experiment; teal = engineering work required outside of Amplitude; purple = action outside Amplitude.

### Lesson 2 of 6: Sample Test Plan (3 min)

Text on the page lists Resources: "Favorite Video Button Experiment (Sample Test Plan)" and "Guided Tutorial (Sample Test Plan)" (both external links).

**Video** (2:59) — a screen walkthrough of a sample test-plan document ("Favorite Video Button Experiment") in what appears to be a Confluence-style doc tool, showing sections for:
- **Guardrail Metrics** — unique views, likes, shares and social engagement ("Track in Analytics").
- **Variants**
- **Control** — "Current state has 'favorite' button icon…" (with an accompanying mobile-app screenshot of the feature).

### Lesson 3 of 6: Validate the Problem (20 min)

Text on the page:

> Your turn: validate the problem
>
> Make a copy of this worksheet (opens in a new tab) and fill out the "Validate your problem" table.

**Video: "Align problem with your business KPIs"** (14:04) — a long walkthrough using an example customer, **AmpliTunes**, a music-playing software company, with example business goals:
- Increase user engagement by 5% annually
- Drive purchase of songs up by 2%

It illustrates a KPI funnel diagram running from top-level Revenue down through Users → Purchase song or video → Engagement (Play song or video) → Social Shares/Join Community, showing how a feature-level metric ladders up into a business KPI.

The lesson then hands off to a "your turn" exercise where the learner fills out a "Validate your problem" table in a companion worksheet (external link, not reproduced here since it requires the linked doc).

### Lesson 4 of 6: Form a solution oriented hypothesis (11 min)

Text on the page:

> Your turn: form a solution oriented hypothesis:
>
> Continue to the "Create your hypothesis" tables in your worksheet (opens in a new tab) to form a solution oriented hypothesis:
> - Add cause, effect, rationale to your problem statement?
> - What elements will the variant have? What will be different?

**Video: "Form a Solution Oriented Hypothesis"** (9:13) — a title-card-led video (Amplitude branding, "Design Phase: Align on a Test Plan") walking through how to write a hypothesis that specifies a cause, an effect, and a rationale, and how to describe what the experiment's variant will actually change.

### Lesson 5 of 6: Predict a Result (15 min)

Text on the page (captured in full):

> Identify your metrics
>
> **Primary Metric:** The main metric you hope to move by running this experiment.
> Example: Increase in trial sign-up conversions
>
> **Minimum Detectable Effect (MDE):** The relative % change you expect to drive on your primary metric as a result of your changes.
> Example:
> - Baseline Conversion Rate: 20%
> - MDE (10%): 10% of 20% = 2%
> - New Target Conversion Rate: 20% + 2% = 22%
>
> **Secondary Metrics:** Additional metrics you hope to move with this experiment.
> Example: Increase in paid subscription conversion
>
> Your turn: identify your primary metric
>
> Continue to the "Predict a result" table in your worksheet (opens in a new tab).

**Video: "Identify Your Metrics"** (10:05) — walks through the same Primary Metric / MDE / Secondary Metrics framework shown in the text above, using the same worked MDE example (20% baseline → 22% target at a 10% MDE).

> **Explanation:** This is one of the more important conceptual lessons in the whole path — the MDE calculation shown here (`MDE% of baseline = absolute lift`, so `baseline + (MDE × baseline) = target`) is the standard way Amplitude Experiment frames statistical power/sample-size planning, and it recurs in the "Statistical Settings" course elsewhere in this training program.

### Lesson 6 of 6: Resources

Text on the page (captured in full):

> **Sample Test Plans**
> - Favorite Video Button Experiment (Sample Test Plan) (opens in a new tab)
> - Guided Tutorial (Sample Test Plan) (opens in a new tab)
> - \[Make a Copy\] Test Plan Template (opens in a new tab)
>
> **Learn more**
> - Amplitude Academy Course "Design Robust Experiments with Detailed Test Plans" (opens in a new tab)
> - Conversion rate optimization and A/B testing webinar "Designing High Impact Experiments" (opens in a new tab)
> - Tips for Successful Website User Experience Analysis blog — https://amplitude.com/blog/website-user-experience-analysis (opens in a new tab)

### Assessment / Feedback (not reproduced)

As with IMPL-EXP-1, this course ends in a "Check your understanding" quiz and a "Course feedback" form; neither is reproduced here.

---

## Course 3: IMPL-EXP-3 — Integrate and Deploy Phase (Feature Experimentation)

**URL:** https://trainingpartners.amplitude.com/impl-exp-3-integrate-and-deploy-phase-feature-experimentation

### About this course (verbatim)

> This course covers the Integrate and Deploy Phase of an Experimentation implementation project, where we ensure the technical foundation for experimentation is properly set up.
>
> After taking this course you'll be able to:
> - Guide a customer through the Integrate & Deploy Phase, answering any questions they may have
> - Distinguish between what the Experiment Platform provides versus what the SDK provides in terms of functionality
> - Given a scenario, explain to the customer why they should (or do not need to) run an A/A test, addressing some caveats.
> - Sequence the recommended steps for instrumentation
> - Create a deployment in the Experiment UI
> - Distinguish between remote evaluation and local evaluation
> - Review A/B results (treatment shows a significant lift, treatment is significantly underperforming, or non-significant results) with customer and decide whether to roll out or roll back
> - Identify when an experiment is "ready for a decision."
>
> Estimated completion time: 1 hour

This course has 9 lessons under three headings: "Integrate & Deploy Phase Overview," "Installing and Validating Experiment SDK," and "Creating a Deployment."

### Lesson 1 of 9: Integrate and Deploy Overview (5 min)

Text on the page:

> In the Experimentation implementation timeline, the Integrate and Deploy phase is second and spans about 2-4 weeks.

**Instrumentation Scope table** (captured in full):

| Column | Item | Details |
|---|---|---|
| **Client** | iOS (Swift) | Latest version: 1.3.0 — 68kb |
| **Client** | Android | Latest version: 1.3.0 — 27kb |
| **Client** | JavaScript Client | Latest version: 1.2.0 — 28kb |
| **Client** | React Native | Latest version: 0.3.0 |
| **Server** | JavaScript Server SDK | Latest version: 1.0.1 — Compatible with Node 10+; bundle with the JavaScript Client SDK for server-side rendering |
| **Rest API** | REST API | `https://api.lab.amplitude.com/v1/vardata` |

Resources listed: "Amplitude: Experiment Implementation Workbook" and "Amplitude Feature Experiment: Instrumentation Walkthrough - Initial Implementation Scope slide" (both external links).

### Lesson 2 of 9: Installing and Validating Experiment SDK, Part 1 (5 min)

Text on the page:

> The first three phases of the workflow overview happen around the same time: create deployment, install SDK in codebase, and create a test plan.

**Video: "Install an Experiment SDK"** (5:29):

> Installing an SDK only needs to be done **one time for each different environment** you have for your application that you want to run experiments on.

Shown with icons for **Client-side SDK** and **Server-side SDK**, plus: "SDKs send a request to Amplitude Experiment to determine which flag configurations should be served to a particular user." A link to the "Amplitude Developer Center: Feature Experimentation" is given for installation guidance.

### Lesson 3 of 9: Installing and Validating Experiment SDK, Part 2 (7 min)

**Video: "Why run an A/A test?"** (7:38) — gives three reasons to run an A/A test (an experiment where both variants get identical treatment, used purely to validate the pipeline):

1. Check that Experiment is implemented correctly — Assignments/Exposures/Primary Metric events are all received as expected.
2. Check that users are receiving consistent variant assignments as user properties.
3. No unexpected behavior while running the A/A test.

### Lesson 4 of 9: Installing and Validating Experiment SDK, Part 3 (2 min)

**Video: "Recommended Steps for Instrumentation"** (2:06) — lays out a 3-step recommended rollout sequence:

1. **A/A Test on Prod** *(recommended for first-time instrumentation)* — Validate SDK/API implementation with real-life traffic; validate any specific targeting rules; identify unintended behavior such as variant jumping or statistical anomalies.
2. *(middle step, partially obscured by the video player in the recording)* — appears to continue validating targeting rules, positioned between the A/A test and the full A/B test.
3. **A/B Test on Prod** — Launch the experiment for the new feature on Prod.

### Lesson 5 of 9: Creating a Deployment (5 min)

Text on the page (captured in full):

> Create a deployment in the Experiment UI
>
> In Amplitude Experiment, a Deployment is a key part of setting up your experiments. It acts as a set of access keys that allow you to route feature flags and experiments to the right users. Each deployment is assigned a Deployment Key, which is project-specific and is used to target users and log assignments automatically.
>
> A key decision when setting up a deployment is selecting the right type of key:
> - Client-side keys should be used with client-side SDKs.
> - Server-side keys are required for server-side SDKs and the REST API.
>
> Deployments are typically named based on the platform or service they support. For example, you might have separate deployments for iOS, Android, and Web, or for different backend services.
>
> Each deployment belongs to an Amplitude Analytics project. While a project can have multiple deployments—allowing flexibility for different platforms—each deployment is tied to only one project.
>
> Lastly, it's important to note that a deployment only needs to be created once per environment. That means if your organization has different environments like staging, production, or test, you will need to create separate deployments for each one.
>
> A few key things to remember about deployments:
> - A deployment is associated with a single Amplitude Analytics project
> - Experiments and flags are grouped into deployments
> - Determines to which Analytics project Assignment events are sent
> - Multiple deployments can be associated with the same Analytics project
> - Application needs the deployment key to initialize Experiment SDK
> - A given flag/experiment can only be included in deployments that share a common Analytics project
> - A deployment is either client-side or server-side

**Video: "Create a deployment in the Experiment UI"** (4:34) — reiterates the same points visually: a Deployment is a set of access keys routed to flags/experiments; deployments are generally named after the platform (client-side) or service (server-side) which variants are served to; deployments live within Amplitude Analytics projects (a project can have multiple deployments, but each deployment attaches to only one project); creating a deployment only needs to be done once per environment.

### Lesson 6 of 9: Configure Feature Experiment (8 min)

Text on the page — a 6-step configuration checklist (captured in full):

1. **Define experiment type** — Hypothesis Test or Do No Harm.
2. **Define metrics** — Used to measure success of experiment; include the direction and MDE.
3. **Determine exposure event** — SDK implementation will auto-trigger an Exposure event.
4. **Define variants** — By default, treatment and control variants are created; add payload if necessary.
5. **Define allocation** — determine rule-based user segments (Targeted Users), which allows you to target users by user property, or All Users.
6. **Confirm analysis settings** — Unless you have special use cases, leaving the default analysis settings is recommended.

**Video: "Design an experiment in the Experiment UI"** (8:15) — walks through the same 6 numbered steps shown above as a UI walkthrough.

Below the video, the page poses: **"How are you evaluating users?"** with two expandable sections (both fully expanded and captured below):

**Remote Evaluation**
- *How does it work?*
  - Calling `start()` makes an HTTP request to Amplitude, passing user identity information.
  - Amplitude servers determine the appropriate variants for the user and return them.
- *Benefits*
  - Richer targeting options
    - User property values
    - Cohort membership
  - Identity resolution
  - Allows sticky bucketing

**Local Evaluation**
- *How does it work?*
  - Calling `start()` downloads flag/experiment configurations to your application.
  - Assignments are determined according to the downloaded rules without making an HTTP call.
  - Any property values to be used in targeting must be provided to the SDK.
- *Benefits*
  - Faster variant assignment
  - One roundtrip call on startup as opposed to a roundtrip call per user with remote evaluation
  - More scalable for server-side applications

Evaluation docs linked: "Remote evaluation" (https://amplitude.com/docs/feature-experiment/remote-evaluation) and "Local evaluation" (https://amplitude.com/docs/feature-experiment/local-evaluation).

> **Explanation:** This remote-vs-local distinction is one of the most practically important choices in a Feature Experimentation implementation. Remote evaluation is simpler and gives richer targeting (server-side cohort/property lookups, sticky bucketing) at the cost of a network round trip per user/session. Local evaluation front-loads a single config download and then assigns variants entirely client-side/in-process, which is faster and scales better — especially for server-side applications handling many requests — but you must ship any targeting property values to the SDK yourself since there's no live server round trip to look them up.

### Lesson 7 of 9: Deploy the Experiment (4 min)

Text on the page:

> Sample analysis data
>
> View sample analysis data on the partner training demo site (opens in a new tab).

**Video: "Make a Decision"** (4:25) — presents 3 general outcome scenarios and their next steps:

1. **Treatment shows a significant lift** → Roll out the experiment and convert it to a flag.
2. **Treatment is significantly underperforming** *(label partially obscured in the recording, but this is the clear middle case between "lift" and "non-significant")* → Roll back the experiment.
3. **Non-significant results** → Continue running the experiment, OR iterate on the experiment design, OR end the experiment.

### Lesson 8 of 9: Demo: Create the test based on test plan (19 min)

**Video** (19:04) — an extended screen-recorded demo of building an experiment/goal in the Amplitude Experiment UI. Highlights visible on screen:

- A "Goals" configuration panel: "Set clear goals to track your experiment's impact — success goals to improve metrics and guardrails to maintain or prevent drops."
- An "Enable Recommendation" toggle, with the note "Designate a metric as a goal to get recommendations."
- A reminder: "Remember that all metrics are divided by number of exposures in each variant. You do not need to divide your formula metrics by UNIQUES(UID)."
- A worked example goal: **"Total Purchases will increase by 2%"** — Metric: Total Purchases; Type: Success/Guardrail; Direction: Increase/Decrease; plus an "Add a Goal" control and advanced options.
- The surrounding experiment-setup screen also shows panels for Targeting, Goals, Variants, Analysis Settings, and Delivery Settings — i.e., this demo is walking through populating the same experiment-configuration screen described conceptually in Lesson 6, using the test plan created earlier in the path as the source material.

### Lesson 9 of 9: Resources

Text on the page (captured in full):

> **Templates**
> - Amplitude: Experiment Implementation Workbook (opens in a new tab)
> - Amplitude Feature Experiment: Instrumentation Walkthrough - Initial Implementation Scope slide (opens in a new tab)
>
> **Help Docs**
> - Create a Deployment (opens in a new tab)
> - Remote evaluation (opens in a new tab)
> - Local evaluation (opens in a new tab)
>
> **Sample Analysis Data**
> - View sample analysis data on the partner training demo site (opens in a new tab).

### Assessment / Feedback (not reproduced)

This course also ends with a "Check your understanding" quiz and a "Course feedback" form; neither is reproduced here.

---

## Course 4: IMPL-EXP-4 — Mock Scenario Capstone Project

**URL:** https://trainingpartners.amplitude.com/path/implementing-amplitude-experiment/impl-exp-4-mock-scenario-capstone-project

**Estimated time:** 2 hr 30 min

### About this exercise (verbatim)

> Show us you can define and document a test plan for a fictional customer! Review the Experiment Capstone Project Mock Scenario Prompt and submit/upload the 5 parts of your assignment in the following submission pages.
>
> Please allow 4 weeks for a team member to review your work and share feedback with you. When they mark this course complete, you will receive an email inviting you to accept your Certified Amplitude Delivery Partner badge.
>
> Estimated time on this assignment: 3.5 hours:
> - 2.5 hours to define test plans (20-30 minutes per customer scenario)
> - 1 hour to record your video and submit.

### Linked mock-scenario prompt document (structure only)

The exercise links out to an external Google Doc, the "Experiment Capstone Project Mock Scenario Prompt," which contains 4 fictional customer scenarios for the learner to write test plans against:

- **AmpliCook** 🧑‍🍳
- **AmpliPost** 💌
- **AmpliStub** 🎫
- **AmpliCare** 👶

...and a **Scoring Rubric** section used to grade the submission.

> **Note on scope:** Per instruction, this file does not reproduce the full text of each of the four fictional customer scenarios or the detailed scoring rubric — those live in the linked external Google Doc and are graded exercise material (with a 4-week human review turnaround) rather than taught course content. The "About this exercise" text above, which describes what the capstone is and how it's graded, is captured in full.

> **Explanation:** This capstone is the credentialing gate for the whole path — completing it (with a passing review) is what triggers the "Certified Amplitude Delivery Partner" badge invitation. Structurally it mirrors the skills taught in IMPL-EXP-2 and IMPL-EXP-3: for each of the 4 fictional companies, the learner writes a test plan (problem validation → hypothesis → predicted result, per IMPL-EXP-2's worksheet flow) and it's reviewed against a rubric, then a recorded video presumably walks through the plan and/or a mock configuration.

---

## Course 5: IMPL-EXP-5 — Decide Phase: Analysis, Action, & Governance

**URL:** https://trainingpartners.amplitude.com/impl-exp-5-decide-phase-analysis-action-governance

**Access status:** ⚠️ **This course is registration-gated and its lessons could not be accessed.** The course page displays a banner: "In order to register, you must complete the following: IMPL-EXP-1 Experimentation Implementation Overview, IMPL-EXP-2 Design Phase: Align on a Test Plan, IMPL-EXP-3 Integrate and Deploy Phase (Feature Experimentation)." Clicking "Get Started" does not navigate into the course, and the curriculum list item has no accessible link — the LMS requires those three prerequisite courses to be marked "complete" for this account before it will unlock IMPL-EXP-5's lesson content. That prerequisite-completion gate could not be satisfied from this browsing session, so only the public "About this course" overview below was accessible.

### About this course (verbatim)

> This course dives into the Decide Phase of an Experimentation implementation project, where we take a close look at the results of our experiment and analyze what happened.
>
> After taking this course you'll be able to:
> - Guide a customer through the Decide Phase
> - Describe what an experimentation program model consists of
> - Given a description of a company's experimentation program maturity, identify which model is right for it.
> - Help customers build a program management and data governance process specific to experimentation and share best practice
>
> Estimated completion time: 1 hour

### Visible (locked) curriculum

- **IMPL-EXP-5 Decide Phase: Analysis, Action, & Governance** (1 hr 0 min) — Text Lesson *(locked)*
- **Check your understanding** — Quiz *(locked)*
- **Course feedback** — Form *(locked)*

> **Explanation:** Based on the stated learning objectives, this final course picks up right where IMPL-EXP-3's "Make a Decision" lesson (the 3-scenario roll-out/roll-back/iterate framework) leaves off, and extends it from a single experiment's result into a repeatable **program**: it appears to cover experimentation program maturity models (i.e., how a company's experimentation practice should scale/govern itself as it matures) and how to help a customer set up ongoing program management and data governance around experimentation — which lines up with the "Ongoing Success & Partnership" stage shown in the IMPL-EXP-1 implementation-timeline video. Because the lesson content itself is locked behind completing IMPL-EXP-1 through IMPL-EXP-3 in the LMS (a state this browsing session could not change), the actual lesson text, videos, and any accordions/tables inside it could not be captured — only this publicly visible course-overview page.

---

*End of combined file for the "Implementing Amplitude Experiment" learning path.*
