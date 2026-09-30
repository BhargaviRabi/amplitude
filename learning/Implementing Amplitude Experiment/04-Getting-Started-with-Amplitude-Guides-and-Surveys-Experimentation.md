# Getting Started with Amplitude Guides and Surveys Experimentation

**Source:** Amplitude Partner Training — [Getting Started with Amplitude Guides and Surveys Experimentation](https://trainingpartners.amplitude.com/getting-started-with-amplitude-guides-and-surveys-experimentation)

This is a standalone course (not a multi-course learning path). Time commitment: **10 minutes**.

## About this course (verbatim)

> Have you been wondering how to experiment on your Amplitude guides and surveys to test and optimize what your users see? This course is designed for users who want to understand how to run experiments in Amplitude Guides and Surveys from setup through rollout.
>
> By the end of this course, you'll be able to:
> - Understand how Amplitude Guides and Surveys Experimentation fits into Amplitude's suite of products
> - Use the Amplitude Guides and Surveys Experimentation workflow to run experiments on your Amplitude guides and surveys
>
> Time commitment: 10 minutes
>
> You should take this course if:
> - You are a current Amplitude Guides and Surveys user and you want to learn how to run experiments on your content.

The course has one lesson group ("Course Overview," 8 minutes) containing a single interactive text lesson with two parts, plus an optional feedback form.

---

## Lesson 1 of 2: Overview (3 min)

### The Amplitude Digital Analytics Platform

> Amplitude Guides and Surveys Experimentation allows you to easily run experiments on guides and surveys, so you can determine whether a visual change will have the impact you were hoping for. Before we dive into the specifics of experimentation, let's take a look at how the product fits into the rest of the Amplitude ecosystem.
>
> Amplitude's Digital Analytics Platform is purpose-built to help teams understand customer behavior and uncover which actions lead to the best business outcomes.
>
> Click through the numbered hotspots below, in order, to learn more about the Amplitude Digital Analytics Platform.

The lesson displays an interactive 3-layer diagram of the Amplitude Digital Analytics Platform, with a numbered hotspot on each layer (captured in full, in click order 1→2→3):

**Layer 1 — Data** (icon: connected nodes) — sub-items shown: Data Warehouse, Governance, Privacy & Security.
> **The Data Layer:** "Amplitude's Data Management capabilities make data accessible and easy for all teams to use, enabling them to make better decisions."

**Layer 2 — Insights** (icon: lightbulb) — sub-items shown: Analytics, Session Replay.
> **The Insights Layer:** "We ingest your data into Amplitude's database to surface insights within Amplitude's Analytics and Session Replay features."

**Layer 3 — Action** (icon: target) — sub-items shown: Activation, Web Experimentation, Feature Experimentation, Guides and Surveys.
> **The Action Layer:** "Amplitude empowers you to take action on your findings, like creating behavior-based audiences, building personalized experiences, running targeted tests, and tailoring in-product communication."

> **Explanation:** This diagram is positioning Guides and Surveys Experimentation as one of four "Action" capabilities (alongside general Activation, Web Experimentation, and Feature Experimentation) that all sit on top of the same Data and Insights foundation. In other words, guides/surveys experimentation isn't a separate product — it's the same underlying Amplitude Experiment engine, applied specifically to in-product guide and survey content rather than to a web page or a feature flag.

---

## Lesson 2 of 2: The Experimentation Workflow (5 min)

Opening text:

> Whether you know you want to start experimenting with guide or survey content before you build it, or you already have some content built that you wish to improve, you can easily create an experiment. Click through the workflow image below for more details.
>
> **NOTE:** When you run an experiment on a guide or survey, you build the variant experiences and manage the setup of *triggers* and *limits* within Amplitude Guides and Surveys. *Triggers* and *limits* remain constant across all variants. *Targeting* is managed within Amplitude Experiment.

The lesson centers on one large interactive workflow diagram with a color-coded legend:
- 🔵 Blue = Action within Amplitude Guides and Surveys
- 🟣 Purple = Action within Amplitude Experiment

The workflow chain (in order) is: **Create a guide or survey** → *(Amplitude Guides and Surveys section)* **Click the Start an experiment icon** → **Select the experiment type** → **Create/edit the variants** → **Click the Manage experiment button** → *(Amplitude Experiment section)* **Define the goals and metrics** → **Add descriptions to the variants** → **Define targeting details** → **Test the experiment** → **Run the experiment** → **Analyze results** → then either **Iterate and continue the experiment** *or* **Roll out the winning variant** → **Ongoing management and maintenance**.

Every node in the diagram has a clickable hotspot with detailed guidance. All hotspots were expanded and are captured below, in workflow order:

**1. Create a guide or survey**
> "Create a guide or survey first. Then make sure you **save** it."

**2. Click the Start an experiment icon**
> "Once you have a saved guide or survey, click the *Start experiment* icon to begin building alternative experiences." (Screenshot shown: the Guides/Surveys builder for a guide named "360 Privacy," with the Start-experiment icon highlighted next to the Save button.)

**3. Select the experiment type**
> Choose between the options shown:
> - *A/B test* - a simple test where you compare the performance of one version of your content against another
> - *Multi-armed bandit* - a test where the number of users exposed to your variants changes automatically based on which version is performing better. Better performing variants receive more traffic, while poorer performing ones lose traffic.

(Screenshot shown: a "New experiment type" dialog with A/B test and Multi-armed bandit radio options and a Continue button.)

**4. Create/edit the variants (a.k.a. "Edit variants")**
> "Click the + to add a new variant. Click a variant name to view and edit it."
>
> "Variants differ from each other in content, but not in setup. You can make a small change in copy, styling, or imagery, or create a completely different experience with a different number of steps or guidance."
>
> "The important thing to remember is to ensure you are supporting a common goal with your variants, since the 'winner' is the variant that outperforms the other relative to your goal."

(Screenshot shown: the "AmpliFlip — Free Trial A/B Test v2" builder with two variants, "various" and "silly," and a sample "Announcement" modal block being edited.)

**5. Click the Manage experiment button**
> "To further configure the experiment, you need to continue in Amplitude Experiment by clicking *Manage experiment*."

(Screenshot shown: a "Promo Code Failure Recovery Guide" example with the Manage experiment button highlighted, and a preview of a "Having trouble with your promo code?" guide message listing troubleshooting tips — check for typos, verify expiry, one code at a time, minimum order value.)

**6. Define the goals and metrics**
> "Select or create a metric that defines the goal of your guide or survey. It should be the main metric you hope to move by running this experiment. Ideally, it should drive both customer and business success."
>
> "Perhaps you simply want to drive survey engagement. For that, your metric could be Uniques of Survey Submitted. If you want to increase the number of free-trial sign-ups, then you can create a metric for Uniques of Trial Sign-ups or whatever event is tied to your goal."
>
> "For more information on creating metrics, expand the Create a metric section below this image."

(Screenshot shown: a Metrics (3) panel with a Primary Metric — "Uniques of Loyalty Program Sign Ups," should Increase by 2% (MDE) — and two Secondary Metrics, "Conversion of Complete Purchase" and "Current Arr," both set to Increase, plus an "Add Metric" control.)

**7. Add descriptions to the variants (a.k.a. "Variants")**
> "In this Amplitude Experiment section, the only thing you can modify about your variants is the *description* of each one."
>
> "You control the content, design, and names of your variants from within Amplitude Guides and Surveys."
>
> **NOTE:** "Variant A is the control, which represents a user's experience without a guide or a survey."

(Screenshot shown: a Variants (3) table — control/Control, on, treatment-vwz — each with an Edit link.)

**8. Define targeting details (a.k.a. "Targeting")**
> **Audience:** Select your audience segment(s) as you normally would in Amplitude Guides and Surveys.
>
> **Distribution:** Amplitude Experiment automatically evenly distributes your audience amongst the variants. If you want to change that at all, customize the distribution.
>
> **NOTE:** "If you want to examine only data on users' interactions with your guide or survey, reduce the distribution for the control to 0% and distribute the rest amongst the remaining variants."
>
> **Rollout:** Determine what percentage of your target audience should be included in the experiment.

**9. Test the experiment**
> "Add testers prior to running the experiment, to ensure your content displays and acts the way you originally intended."
>
> "A tester can only test one variant at a time. If you need a tester to try out multiple variants, you will need to manually move them from one variant assignment to another as they complete their test(s)."

(Screenshot shown: a "Testing Assignments" panel listing each variant — off, control, on, treatment-vwz — with User/Device ID and Cohort assignment controls and "Add Me" shortcuts.)

**10. Run the experiment**
> "After all tests are run and the variants are ready for your audiences, click *Start Experiment*."

(Screenshot shown: the experiment toolbar with a highlighted "Start Experiment" button, and the Targeting tab showing an Assignment/Testers view with Segment 1 at 100% rollout and "All Other Users" at 0%.)

**11. Analyze results**
> "Your experiment is over when it reaches statistical significance. Then, you will see a summary of the performance of your variants."
>
> "Amplitude will suggest which one to roll out based on its performance against the control and any other variants. You can scroll down to look at more specific data on how each variant performed, but what you really need to focus on is the relative performance of each variant."
>
> "The one with the higher percentage is the winner and the one you should roll out to your users."

(Screenshot shown: an Activity/Analysis view with a "Running Progress" summary — days running, event count, "Statistically Significant" badge — and a metrics comparison table showing Baseline vs. Treatment percentages.)

**12. Complete the experiment**
> "When the test is over, click *Complete Experiment*. Then choose which variant to roll out to your users."
>
> "When you roll out a winning guide or survey, it is changed into a published guide/survey for those specified in your targeting section, and the losing variant(s) are deleted. You can continue to manage the content as you would any other guide or survey from within Amplitude Guides and Surveys."
>
> "If you roll out the control, the variants are archived."

(Screenshot shown: a "New View Cart Button [COMPLETED]" experiment with a "Complete Experiment" button highlighted, a Running Progress summary showing "25.9%" vs. "33.0%" variant performance, and an Analyze section with a metrics comparison table.)

### Repeated notes appearing throughout the lesson (captured once here; they recur as fixed side context next to every hotspot above)

> **NOTE:** Your experiment is over when it has reached statistical significance. Statistical significance basically means the test results occurred because of the change you introduced in your product, not because of random chance.
>
> If you make a decision on a winner before significance has been reached, you may not experience the same or similar results in the future as you did during the experiment. Reaching significance means there is a high probability you will see similar results when you roll out the winner.
>
> You can customize statistical settings for Amplitude Guides and Surveys experiments just like for any other experiment, which can impact when statistical significance might be reached. See the Statistical Settings in Amplitude Experiment course for more information.
>
> **NOTE:** See the Analyze Test Results course for more information on how you can analyze your experiment's results.

### Optional expandable section: "Create a metric (video)"

> "When you start configuring your experiment in Amplitude Experiment, your first step is to define a goal or metric. For more information on creating a metric, watch this video:"

**Video: "Create a metric in Amplitude"** — an Amplitude Academy-branded instructional video (title card shown, embedded inline in this optional/expandable section).

> **Explanation:** This whole lesson is essentially a guided tour of a single screen recording/diagram split into 12 clickable stops. The throughline worth holding onto: everything about *what the variants look like* (content, design, names, triggers, limits) is controlled back in Amplitude Guides and Surveys, while everything about *the statistical experiment itself* (goals/metrics, variant descriptions, audience targeting, testing, running, and analyzing) is controlled in Amplitude Experiment via the "Manage experiment" hand-off in step 5. That Guides-and-Surveys/Experiment split mirrors the same Data→Insights→Action layering shown in Lesson 1.

### Feedback (not reproduced)

The course ends with an optional "We'd love your feedback" form; its content is not reproduced here per project scope.

---

*End of file for "Getting Started with Amplitude Guides and Surveys Experimentation."*
