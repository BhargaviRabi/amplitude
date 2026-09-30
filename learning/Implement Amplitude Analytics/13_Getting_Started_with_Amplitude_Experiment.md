# Getting Started with Amplitude Experiment

**Type:** On-demand course | **Time commitment:** 40 minutes

---

## About This Course

✨ *Note: the course landing page displays a banner: "We've launched our AI Platform! Learn more."*

This course introduces you to Amplitude Experiment, Amplitude's platform for running web and feature experiments to test product changes and ship with confidence.

This course is designed for product managers, engineers, marketers, and growth teams who want to learn how to plan, run, and analyze experiments using Amplitude.

**By the end of this course, you will be able to:**
- Explain how Amplitude Experiment fits into the Amplitude AI Analytics Platform
- Distinguish between Web Experimentation and Feature Experimentation, and identify which is right for your use case
- Describe the end-to-end experiment workflow
- Set up your environment for Web or Feature Experimentation
- Use AI-assisted tools to plan and build your experiment
- Build and run a web experiment using the visual editor or URL redirects
- Build and run a feature experiment using the Amplitude Experiment UI
- Analyze results and make an informed decision on how to complete your experiment
- Create and manage feature flags for gradual rollouts and targeted releases

**Recommended prerequisite:** None.

**You should take this course if:** You have implemented Amplitude Analytics and want to understand how to run experiments or use feature flags.

---

## Section: Introduction to Amplitude Experiment

### Lesson 1 — What is Amplitude Experiment? (5 min)

**The Amplitude AI Analytics Platform.** Amplitude Experiment sits inside a broader platform built to help teams move from insight to action. Before diving into how Experiment works, it helps to understand where it fits.

**[Video: "DAP Overview", 1 min 40 sec, Amplitude Academy / Wistia]** — overview of where Experiment fits within the Amplitude AI Analytics Platform. (No on-page transcript available.)

**What is Amplitude Experiment?** Amplitude Experiment gives product, engineering, marketing, and growth teams a shared platform for testing ideas and shipping with confidence. It comes in two forms: Web Experimentation for teams optimizing web experiences without engineering support, and Feature Experimentation for teams building and releasing product changes.

**[Video: "1.2 What is Amplitude Experiment?", 1 min 44 sec]** — (No on-page transcript available.)

**Amplitude Web Experimentation vs Amplitude Feature Experimentation.** Amplitude experiments can be delivered as web experiments or feature experiments, depending on your product and what you're trying to test.

Amplitude Web Experimentation is a low-code/no-code way to run experiments directly on your website without requiring engineering resources. Marketing teams, growth teams, and web product managers can run split URL tests to see which pages perform best, use a visual editor to test changes to copy, formatting, and media, or apply custom code for changes the visual editor doesn't support.

Amplitude Feature Experimentation is for teams building and releasing product changes across any platform. It requires engineering involvement to install an SDK and build feature variants, but works on web, mobile, server, and beyond. Feature experiments deliver testing experiences as feature flags for your target audiences.

| Amplitude Web Experimentation | Amplitude Feature Experimentation |
|---|---|
| Requires implementation using the Amplitude Web Experiment script or the Amplitude unified script | Generally implemented using an SDK or an API |
| Enables no-code experimentation | Requires engineering work to implement features and flags |
| Supported on web apps | Supported on any platform or system |
| Best for marketing, growth, or web product managers | Best for product and engineering teams |

**Which type of experimentation is right for you?** With multiple choices, it can be difficult to determine which experimentation type is best for you. This lesson uses a sorting/matching interactive activity — sort each use case into the correct category. The statements and their correct category assignments (per the activity's data) are:

*Amplitude Web Experimentation:*
- You want to optimize a public-facing website without involving engineering
- You need to test changes to a web page like copy, images, or layout
- Your team doesn't have engineering resources available for flag-based experiment

*Amplitude Feature Experimentation:*
- You want to experiment on web, mobile, or server-side experiences
- You work on a product team with engineering support
- You want to deliver changes through feature flags in your codebase

*(Note: the six statements and the two category labels were both present in the underlying lesson data; the above groupings reflect the most natural pairing of each statement to its category based on the course's stated distinctions between Web and Feature Experimentation.)*

## Section: The Amplitude Experiment Workflow

### Lesson 2 — The Amplitude Experiment Workflow (2 min)

Regardless of whether you are running a web or feature experiment, the high-level workflow is the same. The steps below apply to both paths. You will notice two points where your specific approach diverges depending on the type of experiment you are running. This lesson uses a numbered labeled-graphic diagram of the workflow — each step is reproduced below:

1. **One-time Setup** — Install the web experimentation script (Web) or create a deployment and install the SDK (Feature). Done once per project.
2. **Plan** — Create a thorough test plan before building. Define the problem statement, hypothesis, target audience, metrics, and variants.
3. **Build the experiment** — Create the experiment in Amplitude. Configure goals, variants, targeting, and allocation. Feature experiments require code to be injected into your codebase.
4. **Deploy the experiment** — Test and run the experiment. Then watch the experiment while it runs. Check data quality, exposure counts, and variant distribution.
5. **Analyze the results** — Once the experiment reaches statistical significance or the run time ends, review the results and determine a winner.
6. **Complete the experiment** — Roll out the winning variant, roll back the experiment entirely, or continue running the experiment with a new iteration.
7. **Share results** — No matter what action you take once you analyze the results, you should share those results with your team and keep everyone in the loop on how the experiment went and what was learned from it.
8. **Implement changes** — For changes you want to make more permanent, the very last thing in the workflow is to implement those changes in your product.

**Navigate Amplitude Experiment.** Now, let's take a brief tour of the Amplitude Experiment user interface. We will review each of the options in the left-hand navigation and provide a quick explanation of what you can do in that area of the product. This lesson uses a hotspot diagram of the Amplitude Experiment homepage — each hotspot is reproduced below:

- **Create** — To create a new experiment, click Create > Experiment and choose from Feature or Web. You are then guided through the creation process.
- **Access Amplitude Experiment** — Access the various sections of Amplitude Experiment here.
- **Overview** — Overview provides a brief snapshot of recent activity, announcements, and potential helpful resources.
- **Experiments** — Experiments houses all created experiments in your org, and provides some high-level information about those experiments.
- **Feature Flags** — Feature Flags houses all created feature flags in your org and provides some high-level information about them.

### Lesson 3 — Set Up: Web Experimentation (3 min)

**Before you begin.** You must install Amplitude Analytics on your website prior to installing the experimentation script to enable experiment event tracking to Amplitude for analysis. Once Amplitude Analytics is installed and running, inject the web experiment script into your page's header to connect your web-based product to Amplitude Experiment.

**NOTE:** If you use Amplitude in your web product with the Amplitude unified script instead of an SDK, you do not need to install the web experimentation script separately. Amplitude Web Experimentation works automatically when the Amplitude unified script is installed. You can skip ahead to the next lesson.

**Find the script.** There are a few ways to find the correct script to paste in the header code. This lesson uses a 2-card process component:

*Note: this step-by-step walkthrough contains an authoring placeholder ("Introduction"/"Summary" tab labels with Lorem-ipsum filler text — "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In purus velit, tincidunt ac nibh quis, sollicitudin varius libero. Nullam at mi felis. Donec a scelerisque augue, sit amet porttitor nibh. Suspendisse at lorem ut elit placerat blandit." — reproduced here verbatim as found in the source, per instructions to omit nothing.)*

1. **Create an experiment in your project** — The easiest way is to create a new experiment in your web project. Then, after you give the experiment a name and URL, look for the "Site Setup" section and simply copy the script shown. You can archive this experiment later if you don't want to use it or see it in your list of experiments.
2. **Use your Analytics API key** — Another way to get the correct script is to copy the code template from the Amplitude Documentation site. Go to amplitude.com/docs, search for "web experimentation," and copy the generic script shown. You will also need to have your Amplitude Analytics project's API key to paste into the script so it can connect to your Amplitude project. To find the API key, go to your Amplitude app and: (1) Click the gear icon at the top right, (2) Go to Organization Settings, (3) Click on Projects, (4) Search for your desired web-based project and click on it, (5) Then click to manage your API Key(s). Copy the appropriate key and paste it into the script from the documentation site.

**Inject the script.** Paste the script into the `<head>` element of your site, as high up as possible. This placement prevents flickering, which occurs when a page loads its original content before the experiment variant has a chance to render. *(Illustrated with a screenshot showing an example where the author's web host does not allow full access to edit the HTML header, so the script is pasted in the top-most part of the header element that is accessible.)*

And that's it! Once you paste in the script, you are ready to run web experiments.

**NOTE:** Turn off restrictive ad blockers in your browser settings for the visual editor to work properly.

**Amplitude Plugins.** Amplitude plugins for content management systems like WordPress and Shopify enable access to Amplitude Analytics, Amplitude Web Experimentation, and Amplitude Session Replay via each platform's marketplace or app store. The plugin provides the same experiment functionality as the unified script.

**NOTE:** The Shopify plugin causes flickering due to how Shopify loads scripts. To avoid this, add the asynchronous web script with the anti-flicker snippet to your `[theme.liquid]` file. See the Amplitude Documentation site for more details.

**NOTE:** Amplitude also has plugins for headless CMS platforms such as Contentful. These require greater technical setup, including SDK installation, so they are not covered under Web Experimentation in this course. See the Amplitude Documentation site and Amplitude Academy (course: *The Contentful Plugin for Feature Experimentation*) for more details on these plugins.

### Lesson 4 — Set Up: Feature Experimentation (8 min)

**Create a deployment.** In Amplitude Experiment, a deployment is how you serve a group of flags or experiments for code execution. Deployments live under Amplitude projects. A project can have multiple deployments, but each deployment can only be attached to one project.

To create a deployment: (1) Go to Deployments in Amplitude Experiment. (2) Click Create Deployment. (3) Choose the Amplitude project you want to associate with the deployment. (4) Add a name and select Client-side or Server-side, depending on where the SDK will be installed.

**NOTE:** Client-side deployments run on a client device such as a web browser or mobile app. Server-side deployments run on a server you control, such as a web server or batch processing system. Server-side deployment keys should be kept secret.

**Install the SDK.** The next step is installing the SDK. All SDKs send a request to Amplitude Experiment to determine what flag configurations should be served to a particular user. Amplitude provides SDKs for the most popular programming languages and libraries. If no SDK is available for your codebase, you can use the REST API. *(Illustrated with an "Implementation Options" decision-chart image, with a downloadable PDF referenced for offline use.)* A "Documentation" button links to the Amplitude Developer Documentation for available Amplitude Experiment SDKs and APIs.

**Assignment and exposure events.** One key element that affects your Amplitude Experiment implementation is how you plan to handle *assignment* and *exposure* events, which allow you to accurately track (and then analyze) a user's progress through an experiment. This lesson uses a 2-item accordion:

**[Video: "Assignment and Exposure", 6 min 23 sec]** — explains these two event types and how they can impact your implementation. (No on-page transcript available.)

- **Assignment events** — represent the moment a user is assigned to a particular variant. When `.fetch()` is called, the request to the Amplitude Experiment evaluation service triggers an assignment event sent to Amplitude. Assignment events can be automatically tracked and should be used for monitoring and debugging an experiment, not for analysis.
- **Exposure events** — represent the moment a user is actually exposed to the variant and can be considered part of your experiment. If using Amplitude's automatic exposure tracking, exposure events are triggered when `.variant()` is called. Amplitude's standard `[Experiment] Exposure` events don't count toward event volume. Exposure-based user properties are required for experiment analysis.

For more technical details on assignment and exposure tracking, see the Amplitude Developer Center.

**Remote and local evaluation.** Determining which variant a user is bucketed into for a given experiment or flag configuration is called *evaluation*. You can choose between *remote* evaluation and *local* evaluation.

**[Video: "Remote and Local Eval", 3 min 45 sec]** — compares the two evaluation methods. (No on-page transcript available.)

| Remote Evaluation | Local Evaluation |
|---|---|
| Evaluation is performed on Amplitude's servers | Evaluation is performed locally on the client or server |
| Supports Amplitude ID resolution and advanced targeting (geolocation, user properties, cohort membership) | Does not support Amplitude ID resolution or advanced targeting |
| Uses historical user data from Amplitude Analytics | Does not use historical user data from Amplitude Analytics |
| Supports sticky bucketing | Does not support sticky bucketing |
| Slightly higher latency due to server request | Best suited for server-side implementations requiring fast response times |
| Best for most use cases | Best when latency is a hard requirement |

### Lesson 5 — Plan Your Experiment (4 min)

**Why planning matters.** Regardless of whether you are running a web or feature experiment, and regardless of how simple the test may seem, a written test plan makes your experiment more rigorous, easier to share, and more useful as a record over time. Explicitly writing out the experiment design and rationale makes it clear to others why you are testing and what you are hoping to learn. You can leverage the Amplitude Global Agent to help you form your plan. *(Illustrated with screenshots of a Global Agent chat interface.)*

**Elements of a test plan.** Your test plan should cover the following elements. This lesson uses an expandable accordion:

- **Problem statement and supporting data** — A strong problem statement will clearly define the specific problem you're trying to solve. Include supporting data that fuels your design process, such as data from Amplitude Analytics charts and dashboards and/or other analytics sources, heat maps, support channels, user research, etc.
- **Hypothesis, goals, metrics** — Your hypothesis should explain how you plan to solve the problem. It states a cause, an expected effect, and the rationale connecting them. Write this before you build anything. It's what your experiment is designed to prove or disprove. Your goals define what you want to achieve as a result of the experiment. Use your business objectives, product KPIs, and the features related to your problem statement to help narrow them down. Your primary metric should be directly tied to the change you're introducing and based on the action you expect users to take after encountering it. This is the number that determines whether your hypothesis was supported.
- **Variants** — Add descriptions and/or examples of the experiences your audiences will see to help define and communicate the differences between your variants.
- **Targeting and timeline** — Include target audiences and sample sizes of those audiences to help speed up creating the experiment. And also be sure to include a testing timeline, so you and your team understand the time constraints around your experiment. **NOTE:** Before you set your experiment timeline, use the Duration Estimator to calculate how long your experiment needs to run based on your target sample size and expected effect size. To understand how to use the Duration Estimator and learn how to customize other statistical settings in your experiments, see the *Statistical Settings* course on Amplitude Academy (cross-referenced as "Statistical Settings in Amplitude Experiment").

**Plan with AI.** The Amplitude Global Agent can assist with planning your experiment. Chat with the assistant and describe your problem. You can share supporting data with the agent or ask it to create charts that help communicate the problem you identified. Then have the Agent generate a hypothesis which you can use to base an experiment on.

You can offer suggestions for the hypothesis and the Agent can refine it. Once you've settled on a firm hypothesis, prompt the Agent to generate a full test plan you can use in Amplitude Experiment. The Agent will give you all the key information as described in the previous section. Verify the output:
- The problem statement AI generates should reflect the specific issue, not a generic one. Edit if it is too broad.
- The hypothesis should align with your observations, domain knowledge, and expertise.
- The primary metric should be directly tied to the change you are making and based on the action you expect users to take. If the suggested metric does not exist in your Amplitude project or is not the right one, change it before proceeding.

Take your time creating your test plan. A good test plan helps you make sure you are testing the right thing, measuring it correctly, and making the most of your time. A "View Course" button links to additional content on designing robust experiments with detailed test plans.

### Lesson 6 — Build and Run: Web Experiment (4 min)

Watch the video below to understand how to build and run a web experiment in Amplitude.

**[Video: "3. Build and Run Web Exp", 5 min 02 sec]** — (No on-page transcript available.)

**NOTE:** When using the visual editor, look for AI-assisted editing options when selecting elements. Amplitude's AI can suggest copy variations or layout adjustments based on your goals.

**NOTE:** When running a multi-armed bandit experiment, optimization is done on the *primary* metric only. Secondary metrics are for reporting. If you want to optimize two metrics simultaneously, use a weighted average or run an A/B test instead.

### Lesson 7 — Build and Run: Feature Experiment (4 min)

At this point in the Amplitude Feature Experiment workflow, your deployment is created, the SDK is installed, and you have a detailed test plan. Watch the video below to understand how to build the experiment in Amplitude.

**[Video: "Create a Feature Exp", 8 min 31 sec]** — (No on-page transcript available.)

**Knowledge Check** (embedded, ungraded practice questions within this lesson):

**Question 1: Put the steps of the Experiment workflow in order.** *(Matching-type interactive activity; the item-to-step pairing embedded in the lesson data is reproduced below as the intended correct order for the Feature Experimentation setup/build sequence — distinct from, and more granular than, the 8-stage high-level workflow diagram in Lesson 2):*
- Step 1: Create a deployment
- Step 2: Install the SDK
- Step 3: Create a test plan
- Step 4: Create the experiment
- Step 5: Test the variants
- Step 6: Activate the experiment

**Question 2: Sort the steps of the Amplitude Experiment workflow below into the categories "Action needed within Amplitude Experiment" and "Action needed outside of Amplitude Experiment."** *(Sorting-type interactive activity; the three statements to sort are listed below. The lesson data did not expose a pre-defined correct category for each item, so the following categorization is offered as a reasonable inference based on the course's own description of each action — e.g., Lesson 4 states that injecting code into your codebase is engineering work, while creating an experiment and configuring allocation happen inside the Amplitude Experiment product UI:)*
- *Action needed WITHIN Amplitude Experiment (inferred):* Create an experiment; Configure allocation
- *Action needed OUTSIDE of Amplitude Experiment (inferred):* Inject experiment code into codebase

### Lesson 8 — Track, Analyze, and Complete an Experiment (5 min)

Now that we have started the experiment, the video below will go over what we can do while the experiment is running, and how to analyze it once it is over.

**[Video: "4. Track and Analyze Web Exp", 2 min 44 sec]** — (No on-page transcript available.)

**Complete the experiment.** When the results of an experiment are in, one of three scenarios will present itself. You either have: statistically significant (or conclusive) results where your variant won out over the control; significant results where your variant did not win out over the control; or results that are not conclusive, where it is not clear which variant won. When reviewing the results of an experiment, it's important to have a perspective on what your next steps should be depending on the outcome.

**NOTE:** When determining a winner, consider how well the variant performed with respect to the desired goal, not just how it performed against the control.

This lesson uses a 3-tab component covering each outcome:

- **Conclusive Winner** — Prepare to roll out. *Best practice:* Implement the changes permanently in your product. *Next best:* If you can't make those changes immediately, adjust traffic allocation toward the winner and keep it running as an experiment. **NOTE:** Running multiple tests concurrently can negatively impact webpage performance. For optimal performance, run as few concurrent tests as necessary.
- **Conclusive Non-winner** — You still learned something because you tested. Turn off the test — do not leave a negative experience live. Segment your results — you may find a valuable insight that will help you make your next decision. Hold a retro — what went well? What did we learn? What would we do differently if we ran it again?
- **Inconclusive** — Knowing when to stop an experiment is difficult. Consider your options: *Opportunity cost* (what is the cost of running the test longer? Does it outweigh the potential benefit of getting a conclusive result?); *Time remaining* (how close are you to a conclusive result? Check the confidence interval); *Seek input* (don't make the decision alone — review as a team); *Segment your results* (you may find a valuable insight that will help you make your next decision); *Retest* (if the potential impact of your test idea is important enough, you may want to try again with a slightly different experience); *Move on to the next test* (sometimes it's necessary to move on to the next priority — you can always revisit the test at another time).

**Options when an experiment ends:**
- **Keep the experiment running** — Change the end date and continue if you need more time to reach a conclusive result.
- **Roll out the winning variant** — Select the winning variant and define who it rolls out to. A custom rollout requires manual changes in the targeting section.
- **Roll back the treatment** — Ends the experiment. Variants are deactivated, and users see the experience as it was prior to the experiment.

Regardless of the outcomes of your experiments, sharing the results is crucial if you want to create and maintain a culture of experimentation within your organization. Be sure to celebrate your wins and learn from losses.

## Section: Feature Flags

### Lesson 9 — Feature Flags and Rollouts (5 min)

**What is a feature flag?** A feature flag enables or disables a function or feature in your product without deploying new code each time. Feature flags determine which portions of code are executed in the moment, as the code runs. This allows new features to be deployed without making them visible to users, or visible only to a specific subset of users. A feature flag can range from a simple `IF` statement to more complex decision trees that act on different variables. Since feature flags are implemented in code, they require a development or engineering partner to configure them within your application and can have a wide range of use cases.

**Use cases:**
- **Gradual Rollouts** — When a feature is ready to release, control which subset of users can access it. Roll out gradually to catch issues early and reduce risk. Increase the rollout percentage as confidence grows.
- **Try Out New Features in Production** — Test versions of a feature on different groups of real users. Manually track key metrics to see which version performs best before committing. Amplitude Experiment uses feature flags to deliver variant experiences for formal tests and tracks key metrics automatically.
- **Release Anytime** — With feature flags, you can deploy at any time by separating code deployment from release. Keep specific parts of your feature activated while toggling off unfinished changes.
- **Roll Back Features** — Instantly disable a feature that is causing issues without needing a new code deployment. Flags allow you to turn off functionality in real time.
- **Audience Targeting** — Deliver different experiences to specific groups, such as beta users, power users, or users in a particular region, without deploying separate code paths.

**The feature flag workflow.** The image below provides a high-level overview of the feature flag creation process in Amplitude Experiment ("Flags Workflow v2.png"). Watch the video to see the full workflow in action.

**[Video: "The Amplitude Feature Flag Workflow", 4 min 37 sec]** — (No on-page transcript available.)

## Section: Conclusion

### Lesson 10 — Additional Resources

**Additional Resources.** You can learn more about the material presented in this course in the Amplitude Help Center, Community, and website. Here are some additional resources:
- **Amplitude Documentation:** Amplitude Web Experiment (all related articles); Amplitude Feature Experiment (all related articles)
- **Community:** View topics in the Amplitude Experiment forum

*"Thanks for taking this course! You've reached the end of Getting Started with Amplitude Experiment. Click Next Lesson to take a short knowledge check to complete the course and earn a badge."*

---

## Assessment

**Result on file:** Passed — 11 of 12 correct (91%). Elapsed time: 6 minutes.

This quiz's "Show Answers" view visually marks each option with a checkbox. For a correctly-answered question, the selected/correct option(s) appear checked, bolded, and green. For the one *incorrectly*-answered question (Question 5), the option the quiz-taker actually selected but which was wrong appears checked with grey strikethrough text, while the true correct option appears in green bold, unchecked. This distinction is reproduced below via `*(selected)*` and `*(correct)*` annotations.

1. **Which of the following scenarios are examples of an experiment? Select all that apply.**
   - ☐ Changing the homepage welcome image depending on the user's time of day.
   - ☑ **Determining which pricing structure brings in more new subscribers.** *(correct)*
   - ☑ **Determining which UI design gets more users to add items to their shopping cart.** *(correct)*
   - ☐ Displaying an option to "listen offline" for all premium customers.

2. **Which steps of the Amplitude Feature Experimentation workflow require engineering work outside of the Amplitude Experiment product? Select all that apply.**
   - ☐ Define goals, variants, and allocation
   - ☑ **Inject the flag key and variant values into your codebase** *(correct)*
   - ☐ 5 - Analyze results
   - ☐ Create the experiment
   - ☑ **Install the SDK** *(correct)*

3. **After running an experiment, you see a results panel (Variants: Control 26.9%, Treatment 32.7% / +21.7%; Data Quality: Passing; a metric detail card for "Uniques of Paid Subscription Conversion" showing Relative Perf. +21.7%, Absolute Perf. +5.823 Percentage Points, Confidence Interval (-2.184, 13.831), Significance 68.8%, Absolute Value 32.7% / 199 Conversions / 609 Exposures). Your supervisor asks: "What is your degree of certainty that the results you see are due to the changes you tested and not due to chance?" What will you tell them?**
   - ☐ 32.7%
   - ☐ 21.7%
   - ☐ 5.832 pts
   - ☑ **68.8%** *(correct — this is the Significance value, which represents statistical confidence)*

4. **What statements about exposure events are true? Select all that apply.**
   - ☑ **Exposure events do not count toward Amplitude event volume when using automatic tracking.** *(correct)*
   - ☐ Exposure events must happen before assignment.
   - ☑ **A custom exposure event can be used in place of the automatic Amplitude Exposure event, but it will count toward your event volume.** *(correct)*

5. **Donna is setting up her experiment to test a new way of surfacing suggested content after searching for an item. Her implementation of Amplitude Feature Experimentation does not allow her to use automatic exposure tracking, so she must specify the exposure event. The image below shows a potential event stream a user may take in her app, with the most recent event at the top: View Item Picture, View Item Details, Search for Items, View Item Details, Search for Items, View Recommended Item, Search for Items, Main Landing, Log In, Start Session. Which event would be the best one to designate as the exposure event?** — *(quiz-taker's answer was marked incorrect)*
   - ☐ Main Landing
   - ☑ View Item Details *(selected — marked incorrect)*
   - ☐ **Search for Items** *(correct)*
   - *Feedback: That is incorrect. The exposure event should represent the moment a user is actually exposed to a variant. Since Donna wants users to see suggested content after searching for an item, users will be exposed to the experiment after they search.*

6. **Sarah is a web product manager who wants to test whether changing the hero image on her company's pricing page increases trial signups. She has no engineering resources available and does not want to write custom code. Which Amplitude Experiment approach should she use, and why?**
   - ☐ Feature Experimentation, because it gives her more control over variant delivery
   - ☐ Feature Flags, because she only needs to show the new image to a subset of users
   - ☑ **Web Experimentation, because it supports no-code testing on web pages without engineering involvement** *(correct)*

7. **Marcus used the Amplitude Global Agent to generate a test plan for his experiment. The Agent suggested using "Page Views" as the primary metric for an experiment testing a new checkout flow. Why should Marcus reconsider this metric before proceeding?**
   - ☐ Page Views cannot be used as a primary metric in an A/B test
   - ☐ Page Views is not available as a metric in Amplitude Experiment
   - ☑ **Page Views is not directly tied to the change being introduced or the action users are expected to take as a result** *(correct)*

8. **Shawn wants to implement Amplitude Experiment for his organization's application. They are planning on implementing Amplitude Feature Experimentation server-side, but he's not sure whether local or remote evaluation is best. The idea of low-latency is very attractive to him due to the nature of the application, but so is the ability to access user enrichment information, and being able to use sticky bucketing when needed. He reaches out to the rest of the team, and they collectively determine that the ability to use sticky bucketing outweighs everything else. Which evaluation method should Shawn implement?**
   - ☑ **Remote evaluation** *(correct — remote evaluation is the one that supports sticky bucketing)*
   - ☐ Local evaluation

9. **Maria is in charge of implementing Amplitude Feature Experimentation for her organization. They already have Amplitude Analytics implemented using a client-side SDK, but she wants to fetch for flags and experiments server-side. What method should she use for her implementation?**
   - ☐ Use a client-side SDK with an Amplitude Analytics integration.
   - ☐ Implement a custom Exposure tracking provider and identity management with a 3rd-party Analytics SDK.
   - ☑ **Use a server-side SDK and set the assignment event as the exposure event in her experiment design.** *(correct)*

10. **Which of the following scenarios are examples of a feature flag? Select all that apply.**
    - ☑ **Display a "download" option only for subscribers.** *(correct)*
    - ☐ Determine which filter design is easier to use and results in users filtering more often.
    - ☑ **Change the homepage hero image depending on the user's location.** *(correct)*
    - ☐ Change how "add item to cart" buttons are laid out to see if users add more items to their shopping cart.

11. **Jordan is planning a feature experiment and wants to minimize the risk of users seeing different variants across multiple sessions. Which evaluation method and feature should Jordan prioritize?**
    - ☐ Local evaluation with a custom exposure tracking provider
    - ☐ Local evaluation, because it is faster and does not require a network request
    - ☑ **Remote evaluation with sticky bucketing, because it ensures users remain in the same variant throughout the experiment** *(correct)*

12. **An experiment has been running for three weeks. The results show the treatment outperforming the control by 4.2 percentage points, with a significance score of 61%. Your team lead asks whether you should roll out the treatment. What is the most appropriate response?**
    - ☑ **Not yet. A 61% significance score means there is still a meaningful probability that the results are due to chance rather than the change itself** *(correct)*
    - ☐ Yes, the treatment is clearly outperforming the control and should be rolled out immediately
    - ☐ No, the experiment should be ended because the treatment did not reach the minimum goal

## Conclusion

If you did not successfully complete the assessment, feel free to retake it as many times as you need. You may find it helpful to review the content of the lessons in this path before attempting the assessment again, but that is not required.

If you did successfully complete the assessment, congratulations! Look for an email from "Amplitude via Credly" for instructions on how to accept your badge.

*"Click 'Next' to submit your feedback, or choose from one of the options below."* (Options shown: "Earn your next badge", "Find your next course".)

## Feedback

This course ends with a "We'd Love Your Feedback" survey lesson — navigational/administrative, not course content.

---

## Summary / Explanation

This course is a comprehensive introduction to Amplitude's experimentation and feature-flagging platform, structured around the fundamental Web-vs-Feature Experimentation split: Web Experimentation is a no-code option (a script tag) aimed at marketing/growth/web-PM audiences testing page-level changes, while Feature Experimentation is an SDK-based, engineering-dependent option that works across any platform and is delivered through feature flags in code. The course walks through the full experiment lifecycle — one-time setup, planning (with an emphasis on AI-assisted planning via the Amplitude Global Agent, and the importance of choosing a primary metric that is directly tied to the tested change, reinforced by Assessment Q7), building and deploying, and finally analyzing and completing the experiment. Two recurring technical distinctions get significant attention because they're tested directly in the Assessment: assignment vs. exposure events (assignment = bucketed into a variant, for debugging only; exposure = actually saw the variant, used for analysis — tested in Q4 and Q5), and remote vs. local evaluation (remote = server-side, supports advanced targeting and sticky bucketing but higher latency; local = faster but no sticky bucketing or historical data — tested in Q8 and Q11, both hinging on sticky bucketing as the deciding factor). The "Complete the experiment" framework (conclusive winner / conclusive non-winner / inconclusive) and the emphasis on statistical significance (Assessment Q3 and Q12 both test reading a significance score correctly, with the course stressing that even a positive-looking result like +4.2 points at 61% significance is not yet safe to roll out) show the course's practical, decision-oriented focus: not just how to build an experiment in the Amplitude UI, but how to interpret results and act on them responsibly. Feature flags are presented as a related-but-distinct concept from experiments — a general mechanism for controlling code execution (gradual rollouts, instant rollback, audience targeting) that Feature Experimentation happens to use internally to deliver its variants.
