# Optimize Experiments with Amplitude (Learning Path)

**Type:** Learning path with 5 items (1 intro video + 3 on-demand courses + 1 path assessment)
**Time commitment:** ~1 hour (about 75 minutes per the path's own detailed estimate)
**Source:** Amplitude Training Partners — `path/optimize-experiments-with-amplitude`

---

## About This Path

Upskill your Amplitude Experiment expertise! Learn to design test plans, optimize statistical settings, and analyze results for smarter, data-driven decisions.

**Audience:** This path is designed for Amplitude Experiment users looking to upskill their experimentation abilities.

Learn how to design structured test plans, configure statistical settings, and analyze experiment results with confidence. Dive into concepts like MDE, power levels, confidence intervals, and segmentation to ensure your tests are both valid and actionable. By the end, you'll be equipped to run more effective experiments, interpret results accurately, and make data-driven decisions that drive product growth.

**Pre-requisite:** You must have completed the *Getting Started with Amplitude Experiment* learning path to fully take advantage of the information covered in this path.

**By the end of this path, you'll be able to:**
- Design a robust experiment by creating a detailed test plan
- Focus your experiment with a clear hypothesis
- Locate and identify statistical settings in an experiment
- Identify how statistical settings will impact an experiment, including Bonferroni correction, CUPED, test types, winsorization, MDE, power settings, custom exposure settings, and confidence levels
- Configure statistical preferences for an experiment to reduce the estimated duration
- Analyze the results of an experiment
- Determine next steps at the conclusion of an experiment, even when the test is not statistically significant
- Segment results using Amplitude Analytics and save them for sharing and future reference

**Time commitment:** 75 minutes

**You should take this course if:** You are comfortable running experiments in Amplitude and want to improve your ability to design good tests, configure statistical settings, and analyze results.

> **Editor's note (explanation):** This path is the direct sequel to "Getting Started with Amplitude Experiment." Where that course taught the mechanics of running an experiment, this path teaches how to run a *good* one — a rigorous test plan, correctly configured statistics, and a disciplined way of reading the results afterward, whatever they turn out to be.

This path contains **5 items**, presented in sequence:
1. Optimize Experiments with Amplitude – Introduction (video)
2. Design Robust Experiments with Detailed Test Plans (19–20 min course)
3. Statistical Settings in Amplitude Experiment (20 min course)
4. Analyze Test Results from Amplitude Experiment (17–20 min course)
5. Optimize Experiments with Amplitude Assessment (path-completion quiz)

---

## Item 1: Optimize Experiments with Amplitude — Introduction (Video)

A short intro video for the path, titled "Optimize Experiments with Amplitude." Hosted via Wistia (`fast.wistia.net`), embedded as an iframe on its own page with no sidebar navigation — just a "Next Course" control. No transcript/captions were exposed by the embedded player for extraction.

**Video title card content (visible before playback):** "Optimize Experiments with Amplitude" with an Amplitude icon and a small bar-chart illustration.

> **Explanation:** This video functions as a spoken/visual restatement of the path's written description above — framing the "why" of the path (upskilling experimentation ability, designing structured test plans, configuring statistics, analyzing results) before the learner moves into the first real course.

---

## Item 2: Design Robust Experiments with Detailed Test Plans

**Type:** On-demand course · **Time commitment:** 19–20 minutes

### About This Course

Experimentation requires a commitment of time and resources. Designing an experiment that is a good use of your organization's time and resources is key. To do it right, you should create a detailed test plan. This course walks you through the elements that should be present in your plans and includes guidance on how best to complete those elements.

This course is designed for Amplitude Experiment customers who need to understand how to design a good experiment that measures what you intend to measure, is an appropriate use of company resources, and whose results can be trusted.

**By the end of this course, you'll be able to:**
- Design a robust experiment by creating a detailed test plan
- Focus your experiment with a clear hypothesis

**Time commitment:** 20 min

**You should take this course if:**
- You are new to Amplitude Experiment or are new to experimentation
- You are familiar with the Amplitude Experiment workflow covered in *Getting Started with Amplitude Experiment*
- You want to carefully plan a robust experiment and need to know what your plan should be comprised of

### Curriculum (9 lessons + Knowledge Check + feedback)

#### Lesson 1: Introduction to Test Plans (2 min)

A test plan is precisely what it sounds like: your plan for conducting a test or experiment. Watch the video below to understand why a test plan is essential and what components make up a complete one.

**Video in this lesson:** unnamed/untitled short video on why a test plan is essential and what makes up a complete one.

Look through this sample test plan (opens in a new tab) before we get started, and use it as you move through this course. The sample test plan is built using an Amplitude Notebook. To learn how to use Notebooks, see this video (opens in a new tab) in Amplitude Academy.

#### Lesson 2: Write a Problem Statement (4 min)

Watch the video below to learn what makes a good problem statement.

**Video in this lesson:** *"Problem Statement"* — explains what makes a good problem statement (this lesson is almost entirely video-driven; there is minimal surrounding text).

#### Lesson 3: Form a Hypothesis (2 min)

A hypothesis is a specific, testable prediction of how to solve the problem detailed in your problem statement. It may restate the problem, but it also offers a solution. Your hypothesis should focus your experiment on the results you expect due to the changes you plan to implement to fix your problem, and act as a starting point and north star as you design the test.

**Elements of a solution-oriented hypothesis:** Your hypothesis should be solution-oriented and contain a **cause**, an **effect**, and a **rationale** (presented as interactive flip-cards in the lesson):

- **Cause** — the changes you will introduce. Examples: "If we add a brief description of Advance Care Planning on the dashboard…"; "If we allow users to exit from the rating step…"; "If we remove the Save for later icon from the search results list…"
- **Effect** — what you believe will happen as a result of those changes. Examples: "...users will be more engaged with the planning tool…"; "...users will buy more services…"; "...more users will purchase an item instead of saving it for later…"
- **Rationale** — why you believe the effect will occur. Examples: "...because users will understand the value of Advance Care Planning."; "...because users will not be frustrated with the pay-for-service workflow."; "...because more users will click into an item's main page and see more item details."

There should be enough detail in your hypothesis that one shouldn't need to ask too many questions about your prediction because it explains exactly what you will do to try to fix something.

**Hypothesis examples (Poor vs. Good, tabbed comparison):** Just because a hypothesis may contain a cause, effect, and rationale, does not necessarily make it a good one. An example of a hypothesis that has room for improvement needs to be more specific and communicate exactly what will be done to fix the problem. Your hypothesis doesn't have to be novel or groundbreaking — you may want to try something that has been done elsewhere but hasn't been done in your product before. It is perfectly fine for your rationale to be: "We haven't done this before, and we hope it will work."

#### Lesson 4: Set Goals and Track Metrics (4 min)

Watch the video below to learn what to include in the Goals and Metrics section of a test plan.

**Video in this lesson:** *"Goals and Metrics"*.

Ask around to see if others are testing changes on the same page or in the same conversion funnel. If this is the case, you can either run your experiments at different times or on different subsets of traffic and determine if the experiments need to be mutually exclusive. Otherwise, it is hard to objectively measure whose changes caused the movements in metrics.

**Additional resources referenced (Help Center articles):**
- Multiple hypotheses testing in Amplitude Experiment (Bonferroni correction)
- How Amplitude Experiment uses sequential testing for statistical inference
- The experiment design phase: Define your experiment's goals

#### Lesson 5: Create Variants (1 min)

Every experiment has one control experience and at least one additional variant (or treatment). The control experience is the same experience users already go through in your product today. This provides a baseline against which to measure the effectiveness of your variant(s).

**Expandable sections:**
- **Collaboration** — Product and design teams should work together to decide the variant experiences. Once you have narrowed down your options, work with engineering teams to validate your variant(s) and let you know what is possible given any time constraints, resource allocations, or technological limitations. This will also provide an opportunity to determine engineering dependencies (if any) and whether or not you need to instrument new events.
- **Multiple variants** — You can create multiple variants for your experiment, but that will require more user traffic to gather enough data to ensure results you see are meaningful, which means your experiment may need to run longer than you'd like. Be mindful of the kind of traffic you see in the areas of your product you are testing on before committing to testing out multiple variants. Just like with tracking multiple metrics, the probability of making an error (by basing a critical business decision on a false positive result) increases rapidly with the number of variants you are testing. Amplitude uses the **Bonferroni correction** to account for this.

When you've settled on your changes, describe the current experience (the control) and the changes you want to make (the variant) in your test plan. If you can, include visual designs or mock-ups.

#### Lesson 6: Target and Allocate Users (1 min)

Even if your problem statement and hypothesis indicated the population(s) that should be assigned to either the control or treatment in your experiment, it is best to list out your targeted audiences.

**Expandable sections:**
- **QA testing groups** — Before rolling out an experiment, test it with a small group for QA purposes. List the names of those testing the experiment for quality assurance in this section.
- **Targeted user segments** — Target specific user segments based on: User groups, Defined cohorts, or User properties.
- **Non-targeted user buckets** — Bucket non-targeted users based on: Organization, Geographic location, or Company ID.

**Sticky bucketing:** Amplitude Experiment uses consistent bucketing by default, meaning that users are bucketed into the same variant given that the user and targeting rules remain static. Sometimes, you may want to change your allocation after starting an experiment. This could lead to users being allocated to different variants from the one they've already seen (called *variant jumping*). Enabling sticky bucketing will ensure users continue to receive the same variant once they've been allocated to one, regardless of the current targeting. If you want to roll out the winning variant of an experiment to all users, you will need to disable sticky bucketing so Amplitude can re-allocate all your users to that variant.

Changing targeting rules on an active experiment with sticky bucketing enabled may cause a **sample ratio mismatch (SRM)**, which may skew experiment results. To help avoid this, only change targeting or allocation settings on an active experiment after understanding the potential effects of such a change.

**Allocation:** Next, define the percentage rollout and the allocation ratios for each segment or group. Generally, uniform weights will suffice, splitting participants equally among the experiences.

#### Lesson 7: Define a Timeline (1 min)

It is important to communicate your anticipated timeline for testing, whether this is imposed upon you from elsewhere or one you define on your own.

Generally, two business cycles should be sufficient to run your test. The length of a business cycle depends on the metric you track. For example, if you are testing a new way to update monthly subscription selections, one business cycle would be equivalent to one month. For many experiments where cycles occur more rapidly, two weeks would suffice. However, this is highly dependent on your traffic, the primary metric chosen, the number of variants you have, and whether or not the metrics you are tracking are long-term or short-term.

Don't forget to account for the time required to develop your variants and implement the experiment. Try to get an accurate estimate of the overall required timeline, as it may help prioritize or de-prioritize your experiment.

#### Lesson 8: Analyze Results (1 min)

In the analysis section, detail what breakdown analyses you expect to perform:
- Determine if the treatment affects different segments of users differently. For example, maybe the treatment is good for power users, but the control is good for everyone else.
- List calculations you may want to do, such as determining the annual revenue increase if the winning variant is rolled out to all users.
- List out specific questions you hope to answer with your analysis.

Your results and analyses should be added in this section once the experiment has concluded. That way, the test plan document contains all important, relevant information regarding this experiment.

#### Lesson 9: Plan for Future Work (2 min)

The final section should contain a rough outline of what to do once the experiment is over, based on the potential analysis and outcomes of your experiment. Outcomes for a variant generally fall into one of three categories, each an expandable section:

- **Significant results (variant success)** — Determine how you will roll out this experience. Will you do a gradual rollout? What groups of users will be a part of the rollout? Regardless of how you plan your rollout, it is best practice to end the experiment and commit to implementing the winning variant in your codebase or feature delivery system. Since it takes time to update your app fully, direct traffic toward the winner to keep the experience running and available for all users it is intended for. In Amplitude Experiment, you can then convert your experiment to a flag to reduce confusion in the application. If you are still determining if you are ready to convert the experiment to a flag, keep it running as an experiment.
- **Significant results (variant failure)** — Dig into your results and find out what went well, what was learned, and what could have been done differently. Decide if you should make adjustments and run another test or not. Consider which metrics you might change and which ones should remain.
- **Non-significant results** — If you get non-significant results, will you re-test? Do you have the time and resources to do so? What adjustments are you willing to make? What adjustments are you unwilling to make? If you are not going to re-test, how will you use your learnings from this experiment? Depending on the type of experiment you are running (such as a do-no-harm test), non-significant results may have been your goal — if so, treat these results like the Significant results for a variant success.

You can be as detailed as you wish here. It is good to think about potential outcomes, so you are prepared for whatever results come. And just like in the Analysis section, add your actual future work plans once your experiment and analyses are complete so everyone involved clearly understands the test results and what steps need to happen next.

#### Conclusion: Knowledge Check + Summary and Additional Resources (1 min)

You can learn more about the material presented in this course in the Academy, Help Center, and Community:

- **Amplitude Academy:** Provide context and share important information with Notebooks (video)
- **Help Center:** Multiple hypothesis testing in Amplitude Experiment; FAQ: Experiment duration estimates in Amplitude Experiment; How Amplitude Experiment uses sequential testing for statistical inference; Sample ratio mismatches: Debug issues with experiment allocations
- **Developer Center:** Variant Jumping
- **Community:** View topics in the Experiment forum

Thanks for completing this course! You've reached the end of *Design Robust Experiments with Detailed Test Plans*. Click "Next" to share your feedback on this course by completing a short survey.

(This course also includes a **Knowledge Check** graded quiz and a **We'd love your feedback** survey, both immediately preceding/following the Summary lesson; personal quiz-attempt data is not reproduced here.)

---

## Item 3: Statistical Settings in Amplitude Experiment

**Type:** On-demand course · **Time commitment:** 20 minutes

### About This Course

This course takes you deeper into experimentation using Amplitude by teaching you how to configure statistical settings in your experiments to enhance the accuracy and reliability of your tests.

This course is designed for Amplitude Experiment users who understand the basics of product experimentation and are looking to take their skills to the next level.

**By the end of this course, you'll be able to:**
- Locate and identify statistical settings in an experiment
- Identify how statistical settings will impact an experiment, including Bonferroni correction, CUPED, test types, winsorization, MDE, power settings, custom exposure settings, and confidence levels
- Configure statistical preferences for an experiment to reduce the estimated duration

**Time commitment:** 20 minutes

**You should take this course if:** You are comfortable running experiments in Amplitude and want to further optimize your tests.

### Curriculum (7 lessons)

#### Lesson 1: Overview (2 min)

Amplitude is a powerful platform offering a suite of tools for digital analytics and experimentation, with built-in functionality that simplifies complex statistical calculations. However, to fully leverage Amplitude Experiment and gain deeper insights from your tests, it's crucial to understand the statistical settings available and how modifying them can impact your results.

**Configurable settings covered in this course:**
- **Test type:** Determine the type of experiment to run based on your needs. Choose between an A/B test or a multi-armed bandit.
- **Minimum goal:** Define the minimum effect size required to consider results significant.
- **Winsorization level:** Adjust how extreme values are handled to mitigate the impact of outliers.
- **CUPED (Controlled-experiment using pre-existing data):** Enable or disable to reduce variance using historical data.
- **Bonferroni correction:** Toggle this correction on or off to manage multiple comparisons.
- **Testing method:** For an A/B test, choose between a sequential Test or a T-test.
- **Confidence level:** Set the statistical confidence threshold for detecting meaningful differences.
- **Custom exposure settings:** Define a time window for capturing a valid conversion event.
- **Power level:** Adjust the statistical power to balance sensitivity and confidence in detecting effects.

> **NOTE:** The availability of some settings may depend on your Amplitude plan type. For further assistance, contact your Amplitude CSM or account specialist.

#### Lesson 2: Experiment Types (3 min)

When setting up a new experiment in Amplitude, one of the first decisions you'll need to make is whether to run an **A/B test** or a **multi-armed bandit**. Understanding the differences between these two approaches will help you select the best method for your goals.

> **NOTE:** You can add multiple variants to either an A/B test or a multi-armed bandit. There is no limit to the number of variants you can add.

#### Lesson 3: Goals and Outliers (4 min)

**Minimum goals:** When running experiments in Amplitude, you can select one metric as your primary goal. This metric is the key indicator of success for your experiment. You can also add secondary metrics to provide additional insights into your experiment's performance or help determine whether rolling out the variant is worthwhile. However, only the primary metric allows you to set a minimum goal, also known as the **Minimum Detectable Effect (MDE)** or minimum acceptable change. This threshold helps define whether your experiment is considered successful.

> **NOTE:** Setting an MDE is optional. If you do not specify a minimum goal, Amplitude will apply a default MDE of 2%.

The minimum goal is expressed as the relative percentage change you need to observe in your primary metric compared to the control's performance. For example: if your control's baseline performance is 20%, and you set an MDE of 2%, the expected change is 0.4% (since 2% of 20% = 0.4%). Your variant is considered successful if its performance exceeds 20.4% (for an increase) or falls below 19.6% (for a decrease), depending on the outcome you are measuring.

**Impact of MDE on experiment duration:**
- Lower MDE → Larger sample size → Longer experiment duration (more data is required to detect small changes)
- Higher MDE → Smaller sample size → Shorter experiment duration (larger effects are easier to detect, requiring less data)

**Note:** For multi-armed bandit experiments, MDE is only used to estimate the experiment duration and does not impact the experiment after it starts.

#### Lesson 4: Statistical Analysis Settings (4 min)

Amplitude Experiment applies default statistical preferences to analyze your experiments. Each of the following can be expanded for detail; all five were expanded and their full content captured:

- **CUPED (Controlled-experiment using pre-existing data):** CUPED is a technique designed to reduce variance in your experiment by leveraging historical data. By distributing users with similar characteristics more evenly across variants, CUPED minimizes bias caused by clustering like-minded participants in the same variant. This reduction in variance can help your experiment reach statistical significance faster. **Key Requirements:** You must have at least 14 days of representative pre-experiment data available; CUPED is not suitable for experiments targeting new users or tracking events that were not instrumented during the pre-experiment period.
- **Bonferroni correction:** When testing multiple hypotheses (e.g., testing more than one treatment variant against a control), the likelihood of false positives increases. The Bonferroni Correction is a statistical method that adjusts significance thresholds to reduce this risk, providing more confidence in positive results. However, because it is a conservative approach, it may increase the likelihood of false negatives (failing to detect a true effect). **Key Points:** Enabled by default — for single-hypothesis tests, Bonferroni Correction has no effect; for multiple-hypothesis tests, you can view both corrected and uncorrected significance values by hovering over the info icon next to the significance percentage.
- **Statistical method:** You can select one of the following: **Sequential Test (default)** — lets you check your results at any time without compromising statistical validity; unlike traditional methods that require a predetermined sample size, sequential testing lets you monitor results continuously as data accumulates, stop the experiment early once statistical significance is reached, and accelerate experimentation by reducing the time needed to detect meaningful differences. **T-tests** — ideal when your sample size is small, the difference between the Maximum Detectable Effect and Minimum Detectable Effect is small, or you expect regular variations (e.g., lower usage on weekends); T-tests can be one-sided (tests for a difference in one direction) or two-sided (tests for a difference in either direction); before running a T-test, calculate the required sample size per variant using the Duration Estimator, and do not conclude the experiment until this sample size is reached. **Thompson sampling (multi-armed bandit only)** — the only available statistical method for multi-armed bandit tests, which dynamically reallocates traffic to the best-performing variant throughout the experiment; you can adjust the frequency of traffic reallocation using the dropdown settings.
- **Confidence level:** Indicates how confident Amplitude Experiment is that your results would be replicable if the experiment were repeated multiple times. The default setting is 95%, meaning there is a 5% chance of incorrectly concluding that a variant is effective when it is not (false positive). Lowering the confidence level increases the likelihood of reaching statistical significance faster, but also increases the risk of false positives. **Recommendation:** Do not set the confidence level below 80%, as results may become unreliable at lower thresholds.
- **Exposure settings:** Allow you to define a time window within which a user's interaction with the metric event is considered a valid conversion event. This helps you capture conversions that occur within a relevant timeframe after exposure. Time window options: set the window in seconds, minutes, hours, or days; choose whether to count only the first exposure event or any exposure event within the specified window. **Note:** This setting applies to all defined metrics for your experiment. However, exposure windows do not apply to retention metrics.

You can also see the statistical preferences article in the Amplitude Documentation Center.

#### Lesson 5: The Duration Estimator (4 min)

> **Note:** A duration estimator is also available within the feature experimentation creation workflow, once you select your primary metric.

Before you build your experiment, it is best to have an idea of how long it may take for your experiment to reach statistical significance. To do that, use the duration estimator, accessible on the Experiments dashboard page.

The duration estimator in Amplitude Experiment provides the key insight of an estimated run time to help you plan your experiment effectively. This represents the number of days until your experiment reaches statistical significance.

First, input the event that represents your experiment's audience. Amplitude uses historical traffic data to estimate expected traffic for this event. Then, input your success metric and desired MDE. Amplitude uses historical conversion data with the MDE to generate a targeted conversion rate. If you don't have good historical data for your target events and metrics, you can enter the daily traffic and conversion rate manually. The initial estimate assumes you only have 2 variants: a control and a treatment.

After entering your traffic and success metric data, the duration estimate displays, along with a duration scenarios chart that lets you explore different confidence and lift combinations and their resulting duration estimate.

**Advanced Settings (editable statistical settings that impact estimated duration):**
- **Confidence Level:** How sure you want to be that a win is real and not a random chance.
- **Statistical Power:** The probability of detecting a true effect when it exists (default: 80%).
- **Rollout:** The percentage of targeted users that will be exposed to the experiment.
- **Number of Variants:** The number of variants your experiment will have, including the control variant.
- **CUPED:** Reduces variance in your experiment by leveraging historical data.

**Note:** When using the duration estimator in the feature experimentation workflow, traffic estimates, the control mean, and the standard deviation are automatically calculated based on your historical data. However, if the data for exposure or proxy events is missing or unrepresentative, use your domain knowledge to manually adjust these inputs.

#### Lesson 6: The Experiment Results Chart (2 min)

Many of the statistical settings available for configuring experiments in Amplitude Experiment can also be adjusted within the Experiment Results chart. If you are analyzing experiment results using this chart, you'll find statistical preferences conveniently located at the top of the chart builder. A screenshot in the lesson highlights the available statistical preferences for customization.

> **NOTE:** Max winsorization and power settings are not available in the Experiment Results chart.

Additionally, you can define the minimum goal for each metric in the experiment, as shown in the image to the right.

#### Lesson 7: Knowledge Check

A graded, in-course knowledge-check quiz. Personal quiz-attempt data is not reproduced here.

> **Explanation:** This course is essentially a guided tour of every dial available on an Amplitude experiment's statistics panel — what each one does, its default, and when to change it. The throughline is a trade-off every setting shares: tightening statistical rigor (higher confidence, Bonferroni correction, lower MDE) buys reliability at the cost of a longer-running test, while loosening it (lower confidence, higher MDE, CUPED, sequential testing) buys speed at some cost to certainty.

---

## Item 4: Analyze Test Results from Amplitude Experiment

**Type:** On-demand course · **Time commitment:** 17–20 minutes

### About This Course

This course takes you deeper into experimentation using Amplitude by teaching you how to analyze your experiment's results and decide how to proceed.

This course is designed for Amplitude Experiment users who understand the basics of product experimentation and want to improve their skills.

**By the end of this course, you'll be able to:**
- Analyze the results of an experiment
- Determine next steps at the conclusion of an experiment, even when the test is not statistically significant
- Segment results using Amplitude Analytics and save them for sharing and future reference

**Time commitment:** 20 minutes

**You should take this course if:** You are comfortable running experiments in Amplitude and want to improve your ability to analyze results.

### Curriculum (5 lessons + Knowledge Check + feedback)

#### Lesson 1: Overview (2 min)

When an experiment concludes, there are three possible outcomes:
- Significant results (winner)
- Significant results (non-winner)
- Non-significant results

Significant results indicate that Amplitude Experiment has detected a meaningful difference, suggesting that the observed effects are unlikely to be due to random chance. Amplitude Experiment provides insights into your results and recommends next steps. The Summary card highlights how the best-performing variant compares to the control (if the experiment reached statistical significance) and how it aligns with your primary metric goal.

In general: significant results lead to clearer decisions on the next steps, while non-significant results may require further investigation before drawing conclusions.

**Multi-Armed Bandit Considerations:** Multi-armed bandit (MAB) experiments dynamically adjust traffic to different variants based on performance. As a result, MAB results provide a narrative of how the experiment unfolded, rather than a straightforward comparison of variants.

#### Lesson 2: Significant Results: Winner (2 min)

If your test results in a clear, significant winner, you'll likely want to roll out that variant. Your first step is to complete the experiment and redirect all appropriate traffic to the winning variant. When you choose to roll out, Amplitude can adjust the allocation to all users (or to only the targeted users) for you. If you want to do some other custom rollout, you will need to adjust the targeting settings manually.

**After that, you have a few options, based on timing:**
1. **Commit the winning code to production (best practice).** *Note: Once the winning code is deployed, the experiment flag should be turned off.*
2. **If code deployment takes time, convert the experiment into a feature flag.** *Note: Once the code is deployed, the feature flag should be turned off.* *Note: Converting an experiment to a flag removes metrics, exposure events, start and end dates, sticky bucketing, and testing instrumentation. To preserve the context of the full experiment, save your results in an Experiment Results chart before converting to a flag.*
3. **If you need an immediate solution and cannot commit the winner to code or convert it into a flag, you can keep the experiment running while adjusting traffic toward the winning variant.** *Note: Leaving a web experiment turned on will continue to use your impressions quota.*

#### Lesson 3: Significant Results: Non-winner (2 min)

Even if your test does not yield a successful outcome, it still provides valuable insights. Running an experiment and obtaining significant results—whether positive or negative—gives you new data about your users and your product that you didn't have before. As long as you use these findings to inform future decisions, your time and effort were well spent.

**Steps to move forward:**
1. **Turn off the test.** If a variant is underperforming or negatively impacting users, complete the experiment and roll back the treatment to prevent further disruption.
2. **Analyze your results.** Add filters and segment the data to uncover deeper insights. Consider filtering by platform (web vs. mobile), device type (iOS vs. Android), or location (regional variations). Consider selecting defined segments such as all exposed users except for those who variant jumped, or new users. Look for trends or patterns that inspire future experiments or help refine targeting strategies.
3. **Conduct a retrospective.** Hold a review session to discuss what went well in the experiment process, key learnings from the results, what could be done differently in a future iteration, and insights from segmentation and the new questions they raise.

> **NOTE:** Be cautious when drawing conclusions from segmented results. To confirm whether a specific segment behaves consistently, run a new test with a focused hypothesis targeting that group.

#### Lesson 4: Non-significant Results (4 min)

Not every test will yield significant results, but that doesn't mean the experiment was a failure. Sometimes non-significant results are good, such as when monitoring guardrail metrics in a Do No Harm experiment — in these cases, your path forward is clear. It becomes more difficult to know how to proceed when your success metric does not reach a significant level of performance.

At the conclusion of each test, you'll need to decide whether to: keep it running to collect more data (for sequential tests), roll out the winning variant, or roll back to pre-experiment conditions. (If you roll back, decide whether to run a new experiment based on your findings or move on to the next test in your queue.)

**Guiding questions (each expandable with further detail — all captured):**
- **Are there any data quality issues?** What does the data quality checklist say about any quality issues with your experiment?
- **How close are you to a conclusive result?** Do you have the time to continue running the experiment until the results are statistically significant (for sequential tests)?
- **What is the cost of running the test longer (for sequential tests)?** Does the potential benefit of reaching a conclusive result outweigh the resources required? How will keeping the test running impact future sprints? Will extending the test delay other planned experiments or product updates?
- **Is it worth the risk to roll out an inconclusive winner?** If the confidence interval is close to favoring one side, is the potential downside of implementing the "wrong" variant acceptable? What are the other possible effects of rolling out a variant that performs in the opposite direction than intended? *(Note: the confidence interval represents the range of expected values if the test were re-run. Moving forward with inconclusive results means accepting the risk that the variant may not have the intended effect, as the current performance may be due to pure chance.)*
- **What insights can you extract from the data?** Did certain user segments perform differently? Could retesting with a new hypothesis or target audience yield clearer results? Does the data suggest that a modified version of the experiment might be more successful?
- **Do you have the time and resources to run a follow-up experiment?** Or is there pressure to accept the current results and move on?

Regardless of the path you eventually choose, make sure to review the results as a team and seek input from different perspectives, and document your findings — including your rationale for the decision — to inform future experiments (e.g., saving your experiment's results in a notebook or dashboard).

#### Lesson 5: Use Case: Job Posting Traffic (non-significant results) (7 min)

A worked case-study walkthrough, presented across several "Continue" screens:

**Setup:** A digital consulting firm aimed to increase traffic to its job posting page to attract new talent for upcoming projects. The hypothesis was that moving the "View Job Postings" action button from below the fold to within the hero image on the homepage would increase traffic to the job posting page by at least 2%.

**Results after 30 days:** Relative lift: 11.8%. Significance level: 68.7% (not statistically significant). Confidence interval: (–3.031, 3.586).

**Interpreting the initial results:** At first glance, the treatment performed well in relative terms. However, the confidence interval suggests that the observed lift might be due to chance, as the lower bound extends into the negative range — ideally the lower end of the confidence interval would be closer to 0 rather than –3.031 before rolling out the change. Also, even though the experiment is not significant, a significance of only 68.7% is too low. Given this uncertainty, the instructor's initial instinct is to continue running the experiment, but first to analyze user segments to see if any particular groups drove the observed performance.

**Segmenting the results:** To better understand how different user segments behaved, filter the experiment analysis results and create charts in Analytics. At the top of the analysis page, add filters and segment the data by platform, device type, location, or other properties, or select defined segments (e.g., all exposed users except variant-jumpers, or only new users). You can also click charts on the Activity page to watch Session Replays of users who experienced each variant for qualitative context.

**Build charts in Amplitude Analytics using experiment data:** Click "Open in Chart" in the Analysis section to open all experiment data in an Experiment Results chart, which can be manipulated or saved for broader sharing; it also explicitly shows which events and properties from the experiment should be selected to build other charts in Analytics. (The lesson includes a clickable hotspot graphic showing where to find these events and properties.)

**Segmentation walkthrough:** First select all users who performed the exposure event (usually the Amplitude Exposure event, verifiable in experiment settings) to guarantee the analysis looks only at users who were part of the experiment — add the exposure event in the segmentation module within "+ Performed" and align the timeframe with the experiment test window. Then choose a property to segment by; starting with "Device Family" revealed: Mac OS X and iOS user performance increased, while Windows and Android user performance remained relatively constant — prompting further investigation into a possible new experiment tailored to Windows/Android users. Other segment properties explored (Country, Device Type, Language, Membership Level) showed no meaningful trends, so the analysis concluded, charts were added to a notebook, and everything was shared with the team.

> **NOTE:** Funnel Analysis charts are another great tool to use when analyzing your results.

**Decision:** After reviewing the findings, the team decided to let the experiment run for two more weeks to see if the confidence interval and significance level would improve. After the additional two weeks, the experiment still did not reach statistical significance, but the significance increased to 80.3% and the confidence interval improved to (-0.834, 3.585) — narrower and closer to a positive outcome. Coupled with the improved significance, these updated results reduced the risk of rolling out a non-performing variant, so the team decided to roll out the new button layout, as the risk of negative impact was now minimal.

> **NOTE:** This experiment did not include any secondary or guardrail metrics. If your experiment includes these, be sure to analyze their results before making a final decision.

(This course also includes a **Knowledge Check** graded quiz and a **We'd love your feedback** survey; personal quiz-attempt data is not reproduced here.)

> **Explanation:** This course teaches the decision framework for "what do I do with these results?" — first classifying the outcome (clear winner / clear non-winner / inconclusive), then applying the matching playbook, and finally demonstrating the whole process end-to-end with a real, messy example where the "right answer" only emerged after extending the test and segmenting the data.

---

## Item 5: Optimize Experiments with Amplitude Assessment

Take this assessment to complete the learning path and check your understanding of optimizing your use of Amplitude Experiment. This is the path-completion graded assessment (analogous to the badge quiz in *Getting Started with Amplitude Experiment*); personal quiz-attempt data is not reproduced here.
