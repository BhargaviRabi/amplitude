# Getting Started with Amplitude Experiment

**Type:** On-demand badge course · **Time commitment:** 40 minutes
**Source:** Amplitude Training Partners — `getting-started-with-amplitude-experiment-1`

---

## About This Course

This course introduces you to Amplitude Experiment, Amplitude's platform for running web and feature experiments to test product changes and ship with confidence. This course is designed for product managers, engineers, marketers, and growth teams who want to learn how to plan, run, and analyze experiments using Amplitude.

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

> **Editor's note (explanation):** This is Amplitude's onboarding course for its A/B-testing and feature-flagging product, "Amplitude Experiment." It sets the stage for everything else in this training track by first explaining the *concept* (why experiment, what's the difference between "Web" and "Feature" experimentation), then walking through the *mechanics* (setup → plan → build → run → analyze → roll out), and finally introducing feature flags as a related but distinct capability. Completing it and its quiz earns a Credly badge.

---

## Curriculum Overview (10 Lessons)

1. Introduction to Amplitude Experiment — What is Amplitude Experiment? (5 min)
2. The Amplitude Experiment Workflow (2 min)
3. Set Up: Web Experimentation (3 min)
4. Set Up: Feature Experimentation (8 min)
5. Plan Your Experiment (4 min)
6. Build and Run: Web Experiment (4 min)
7. Build and Run: Feature Experiment (4 min)
8. Track, Analyze, and Complete an Experiment (5 min)
9. Feature Flags and Rollouts (5 min)
10. Additional Resources / Conclusion

After the 10 lessons, the course path also contains a graded **Assessment** (a scored knowledge-check quiz needed to earn the badge), a **"We'd Love Your Feedback"** survey form, and a final **Conclusion** screen.

---

## Lesson 1: What is Amplitude Experiment? (5 min)

### The Amplitude AI Analytics Platform

Amplitude Experiment sits inside a broader platform built to help teams move from insight to action. Before diving into how Experiment works, it helps to understand where it fits.

**Videos in this lesson:**
- *"1. DAP Overview"* — an embedded video (hosted on Articulate's media player, `embed.articulateusercontent.com`) that visually walks through where Amplitude Experiment fits inside the overall Amplitude Digital Analytics Platform (DAP), reinforcing the surrounding text about Experiment being one part of a larger insight-to-action platform.
- *"1.2 What is Amplitude Experiment?"* — a second embedded video going deeper into what Amplitude Experiment is and does, illustrating the concepts described in the text below (no on-page transcript/captions were exposed by the player; the video visually reinforces the adjacent text content).

### What is Amplitude Experiment?

Amplitude Experiment gives product, engineering, marketing, and growth teams a shared platform for testing ideas and shipping with confidence. It comes in two forms: Web Experimentation for teams optimizing web experiences without engineering support, and Feature Experimentation for teams building and releasing product changes.

### Amplitude Web Experimentation vs Amplitude Feature Experimentation

Amplitude experiments can be delivered as web experiments or feature experiments, depending on your product and what you're trying to test.

Amplitude **Web Experimentation** is a low-code/no-code way to run experiments directly on your website without requiring engineering resources. Marketing teams, growth teams, and web product managers can run split URL tests to see which pages perform best, use a visual editor to test changes to copy, formatting, and media, or apply custom code for changes the visual editor doesn't support.

Amplitude **Feature Experimentation** is for teams building and releasing product changes across any platform. It requires engineering involvement to install an SDK and build feature variants, but works on web, mobile, server, and beyond. Feature experiments deliver testing experiences as feature flags for your target audiences.

| Amplitude Web Experimentation | Amplitude Feature Experimentation |
|---|---|
| Requires implementation using the Amplitude Web Experiment script or the Amplitude unified script | Generally implemented using an SDK or an API |
| Enables no-code experimentation | Requires engineering work to implement features and flags |
| Supported on web apps | Supported on any platform or system |
| Best for marketing, growth, or web product managers | Best for product and engineering teams |

### Interactive Activity: "Which type of experimentation is right for you?"

With multiple choices, it can be difficult to determine which experimentation type is best for you. The lesson includes a drag-and-card-sort activity: sort each use case into the correct category ("Amplitude Web Experimentation" or "Amplitude Feature Experimentation") to find out which aligns best. (Recorded state on the page: "6/6 Cards Correct", with a "REPLAY" option.)

> **Explanation:** The takeaway from Lesson 1 is a decision rule: if you need a fast, no-code way to test website content/design and don't need engineering help, use **Web Experimentation**. If you're testing a feature deep in a product (mobile app, backend logic, cross-platform), you need **Feature Experimentation**, which requires an SDK/API and engineering effort.

---

## Lesson 2: The Amplitude Experiment Workflow (2 min)

### The Amplitude Experiment workflow

Regardless of whether you are running a web or feature experiment, the high-level workflow is the same. The steps below apply to both paths. You will notice two points where your specific approach diverges depending on the type of experiment you are running.

### Navigate Amplitude Experiment

Now, let's take a brief tour of the Amplitude Experiment user interface. We will review each of the options in the left-hand navigation and provide a quick explanation of what you can do in that area of the product.

**Interactive activity:** "Click each hotspot on the Amplitude homepage below to learn more." (An image of the Amplitude Experiment UI with clickable hotspots over each navigation item, each revealing a short explanation of that section of the product. The underlying hotspot copy was not extractable as static text — it only appears after each hotspot is clicked within the interactive graphic.)

> **Explanation:** This lesson previews the shared, platform-agnostic workflow (create → set up → plan → build/run → analyze → complete) that lessons 3–8 will each expand on in detail, and orients you to where in the Amplitude Experiment UI each stage happens.

---

## Lesson 3: Set Up: Web Experimentation (3 min)

### Before you begin

You must install Amplitude Analytics on your website prior to installing the experimentation script to enable experiment event tracking to Amplitude for analysis.

Once Amplitude Analytics is installed and running, inject the web experiment script into your page's header to connect your web-based product to Amplitude Experiment.

> **NOTE:** If you use Amplitude in your web product with the Amplitude unified script instead of an SDK, you do not need to install the web experimentation script separately. Amplitude Web Experimentation works automatically when the Amplitude unified script is installed. You can skip ahead to the next lesson.

### Find the script

There are a few ways to find the correct script to paste in the header code. The lesson has a 2-card flip/click-through ("1 of 2" / "2 of 2") presenting two options:

**Option 1 — Create an experiment in your project**
The easiest way is to create a new experiment in your web project. Then, after you give the experiment a name and URL, look for the "Site Setup" section and simply copy the script shown. You can archive this experiment later if you don't want to use it or see it in your list of experiments.

**Option 2 — Use your Analytics API key**
Another way to get the correct script is to copy the code template from the Amplitude Documentation site. Go to amplitude.com/docs (opens in a new tab), search for "web experimentation," and copy the generic script shown.

You will also need to have your Amplitude Analytics project's API key to paste into the script so it can connect to your Amplitude project. To find the API key, go to your Amplitude app and:
1. Click the gear icon at the top right
2. Go to Organization Settings
3. Click on Projects
4. Search for your desired web-based project and click on it
5. Then click to manage your API Key(s)
6. Copy the appropriate key and paste it into the script from the documentation site

### Inject the script

Paste the script into the `<head>` element of your site, as high up as possible. This placement prevents flickering, which occurs when a page loads its original content before the experiment variant has a chance to render.

In this example, my web host does not allow me access to edit the full HTML header. However, I can paste this script in the top-most part of the header element as shown.

And that's it! Once you paste in the script, you are ready to run web experiments.

> **NOTE:** Turn off restrictive ad blockers in your browser settings for the visual editor to work properly.

### Amplitude Plugins

Amplitude plugins for content management systems like WordPress and Shopify enable access to Amplitude Analytics, Amplitude Web Experimentation, and Amplitude Session Replay via each platform's marketplace or app store. The plugin provides the same experiment functionality as the unified script.

> **NOTE:** The Shopify plugin causes flickering due to how Shopify loads scripts. To avoid this, add the asynchronous web script with the anti-flicker snippet to your `[theme.liquid]` file. See the Amplitude Documentation site for more details.

> **NOTE:** Amplitude also has plugins for headless CMS platforms such as Contentful. These require greater technical setup, including SDK installation, so they are not covered under Web Experimentation in this course. See the Amplitude Documentation site and Amplitude Academy for more details on these plugins.

> **Explanation:** This lesson is a practical, step-by-step setup guide: get Analytics running first, then get the Web Experiment script into your `<head>` tag (either by copying it from a new experiment's Site Setup screen, or by hand-assembling it from the docs + your project API key), placed as high as possible to avoid flicker. CMS users (WordPress/Shopify/Contentful) have plugin shortcuts, each with its own caveat.

---

## Lesson 4: Set Up: Feature Experimentation (8 min)

### Create a deployment

In Amplitude Experiment, a **deployment** is how you serve a group of flags or experiments for code execution. Deployments live under Amplitude projects. A project can have multiple deployments, but each deployment can only be attached to one project.

**To create a deployment:**
1. Go to Deployments in Amplitude Experiment
2. Click Create Deployment
3. Choose the Amplitude project you want to associate with the deployment
4. Add a name and select Client-side or Server-side, depending on where the SDK will be installed

> **NOTE:** Client-side deployments run on a client device such as a web browser or mobile app. Server-side deployments run on a server you control, such as a web server or batch processing system. Server-side deployment keys should be kept secret.

### Install the SDK

The next step is installing the SDK. All SDKs send a request to Amplitude Experiment to determine what flag configurations should be served to a particular user.

Amplitude provides SDKs for the most popular programming languages and libraries. If no SDK is available for your codebase, you can use the REST API.

### Implementation options

If you are unsure of what method to use to install the SDK, use the decision chart to help you. You can also download a PDF of the Implementation Options (opens in a new tab). *(The decision chart itself is a graphic embedded in the lesson; its branching logic was not exposed as extractable static text — only the surrounding explanatory text above/below it.)*

### Amplitude Developer Documentation

"Click the button at the right to learn more about available Amplitude Experiment SDKs and APIs." — links out to Amplitude's developer documentation site.

### Assignment and exposure events

One key element that affects your Amplitude Experiment implementation is how you plan to handle assignment and exposure events, which allow you to accurately track (and then analyze) a user's progress through an experiment.

**Video in this lesson:** *"Assignment and Exposure"* — explains **assignment events** (fired when a user is assigned to a variant) and **exposure events** (fired when the user actually sees/experiences that variant) and how they impact your implementation. For more technical detail, the lesson points to the Amplitude Developer Center.

### Remote and local evaluation

Determining which variant a user is bucketed into for a given experiment or flag configuration is called **evaluation**. You can choose between remote evaluation and local evaluation.

**Video in this lesson:** *"Remote and Local Eval"* — compares the two evaluation methods.

| Remote Evaluation | Local Evaluation |
|---|---|
| Evaluation is performed on Amplitude's servers | Evaluation is performed locally on the client or server |
| Supports Amplitude ID resolution and advanced targeting (geolocation, user properties, cohort membership) | Does not support Amplitude ID resolution or advanced targeting |
| Uses historical user data from Amplitude Analytics | Does not use historical user data from Amplitude Analytics |
| Supports sticky bucketing | Does not support sticky bucketing |
| Slightly higher latency due to server request | Best suited for server-side implementations requiring fast response times |
| Best for most use cases | Best when latency is a hard requirement |

> **Explanation:** Feature Experimentation setup is more technical than Web Experimentation: you create a deployment (client-side or server-side), install an SDK/REST API, and make two architectural decisions — (1) how you'll track assignment vs. exposure events, and (2) whether evaluation happens remotely (richer targeting, more latency) or locally (faster, less targeting power).

---

## Lesson 5: Plan Your Experiment (4 min)

### Why planning matters

Regardless of whether you are running a web or feature experiment, and regardless of how simple the test may seem, a written test plan makes your experiment more rigorous, easier to share, and more useful as a record over time. Explicitly writing out the experiment design and rationale makes it clear to others why you are testing and what you are hoping to learn.

You can leverage the **Amplitude Global Agent** to help you form your plan.

### Elements of a test plan

Your test plan should cover the following elements (each is an expandable accordion section in the lesson):
- Problem statement and supporting data
- Hypothesis, goals, metrics
- Variants
- Targeting and timeline

> **NOTE:** Before you set your experiment timeline, use the **Duration Estimator** to calculate how long your experiment needs to run based on your target sample size and expected effect size. To understand how to use the Duration Estimator and learn how to customize other statistical settings in your experiments, see the *Statistical Settings* course on Amplitude Academy.

### Plan with AI

The Amplitude Global Agent can assist with planning your experiment. Chat with the assistant and describe your problem. You can share supporting data with the agent or ask it to create charts that help communicate the problem you identified. Then have the Agent generate a hypothesis which you can use to base an experiment on.

You can offer suggestions for the hypothesis and the Agent can refine it. Once you settle on a firm hypothesis, prompt the Agent to generate a full test plan you can use in Amplitude Experiment. The Agent will give you all the key information as described in the previous section. **Verify the output:**
- The problem statement AI generates should reflect the specific issue, not a generic one. Edit if it is too broad.
- The hypothesis should align with your observations, domain knowledge, and expertise.
- The primary metric should be directly tied to the change you are making and based on the action you expect users to take. If the suggested metric does not exist in your Amplitude project or is not the right one, change it before proceeding.

Take your time creating your test plan. A good test plan helps you make sure you are testing the right thing, measuring it correctly, and making the most of your time.

**"Test Plans"** — a link/button in the lesson ("VIEW COURSE") pointing to a related Amplitude Academy course on designing robust experiments with detailed test plans.

> **Explanation:** Before building anything, write down the problem, hypothesis, metrics, variants, targeting, and timeline. Amplitude's Global Agent (an AI assistant) can draft this for you from a described problem, but you're responsible for checking that the AI-generated problem statement, hypothesis, and primary metric are specific and correct before proceeding.

---

## Lesson 6: Build and Run: Web Experiment (4 min)

Watch the video below to understand how to build and run a web experiment in Amplitude.

**Video in this lesson:** *"3. Build and Run Web Exp"* — a walkthrough demonstrating the end-to-end process of building a web experiment (e.g., in the visual editor) and launching/running it.

> **NOTE:** When using the visual editor, look for AI-assisted editing options when selecting elements. Amplitude's AI can suggest copy variations or layout adjustments based on your goals.

> **NOTE:** When running a multi-armed bandit experiment, optimization is done on the primary metric only. Secondary metrics are for reporting. If you want to optimize two metrics simultaneously, use a weighted average or run an A/B test instead.

> **Explanation:** This short, mostly video-driven lesson demonstrates the actual "build" step for web experiments using the visual editor, plus two important caveats: AI-assisted editing exists for suggesting copy/layout changes, and multi-armed bandit experiments only optimize a single primary metric (use a weighted average or a plain A/B test if you truly need to optimize two metrics at once).

---

## Lesson 7: Build and Run: Feature Experiment (4 min)

At this point in the Amplitude Feature Experiment workflow, your deployment is created, the SDK is installed, and you have a detailed test plan. Watch the video below to understand how to build the experiment in Amplitude.

**Video in this lesson:** *"Create a Feature Exp"* — demonstrates building/creating the feature experiment in the Amplitude Experiment UI.

### Knowledge Check (in-lesson, ungraded practice)

**Question 1:** Put the steps of the Amplitude Experiment workflow in order. Options presented (shuffled): Create the experiment, Create a test plan, Activate the experiment, Install the SDK, Create a deployment, Test the variants — to be placed into Step 1 through Step 6. (Page state recorded: "Correct" — i.e., the correct order was: 1. Create a test plan, 2. Create a deployment, 3. Install the SDK, 4. Create the experiment, 5. Test the variants, 6. Activate the experiment, based on the workflow order taught across Lessons 4–7.)

**Question 2:** Sort the steps of the Amplitude Experiment workflow into the categories "Action needed within Amplitude Experiment" and "Action needed outside of Amplitude Experiment." (Page state recorded: "6/6 Cards Correct.")

> **Explanation:** This lesson is the Feature-Experimentation counterpart to Lesson 6 — it's where you actually build the experiment in the UI now that setup (Lesson 4) and planning (Lesson 5) are done — followed by two practice activities that reinforce the overall workflow sequence and which steps happen inside vs. outside the Amplitude Experiment product.

---

## Lesson 8: Track, Analyze, and Complete an Experiment (5 min)

Now that we have started the experiment, the video below will go over what we can do while the experiment is running, and how to analyze it once it is over.

**Video in this lesson:** *"4. Track and Analyze Web Exp"* — covers monitoring a running experiment and analyzing results once it concludes.

### Complete the experiment

When the results of an experiment are in, one of three scenarios will present itself. You either have:
- Statistically significant (or conclusive) results where your variant won out over the control
- Significant results where your variant did not win out over the control
- Results that are not conclusive, where it is not clear which variant won

When reviewing the results of an experiment, it's important to have a perspective on what your next steps should be depending on the outcome.

> **NOTE:** When determining a winner, consider how well the variant performed with respect to the desired goal, not just how it performed against the control.

The lesson presents three tabbed outcomes — **CONCLUSIVE WINNER**, **CONCLUSIVE NON-WINNER**, **INCONCLUSIVE** — with guidance under the "winner" tab:

Prepare to roll out.
- **Best practice:** Implement the changes permanently in your product.
- **Next best:** If you can't make those changes immediately, adjust traffic allocation toward the winner and keep it running as an experiment.

> **NOTE:** Running multiple tests concurrently can negatively impact webpage performance. For optimal performance, run as few concurrent tests as necessary.

### Options when an experiment ends
- Keep the experiment running
- Roll out the winning variant
- Roll back the treatment

Regardless of the outcomes of your experiments, sharing the results is crucial if you want to create and maintain a culture of experimentation within your organization. Be sure to celebrate your wins and learn from losses.

> **Explanation:** This lesson closes the loop on the experiment lifecycle: monitor it while running (video), then classify the outcome into one of three buckets (clear winner / clear non-winner / inconclusive) and choose a corresponding action — roll out the winner, keep testing, or roll back — and finally, share results org-wide regardless of outcome.

---

## Lesson 9: Feature Flags and Rollouts (5 min)

### What is a feature flag?

A **feature flag** enables or disables a function or feature in your product without deploying new code each time. Feature flags determine which portions of code are executed in the moment, as the code runs. This allows new features to be deployed without making them visible to users, or visible only to a specific subset of users.

A feature flag can range from a simple IF statement to more complex decision trees that act on different variables.

Since feature flags are implemented in code, they require a development or engineering partner to configure them within your application and can have a wide range of use cases.

### Use cases
- Gradual Rollouts
- Try Out New Features in Production
- Release Anytime
- Roll Back Features
- Audience Targeting

### The feature flag workflow

The image below provides a high-level overview of the feature flag creation process in Amplitude Experiment. Watch the video to see the full workflow in action.

**Video in this lesson:** *"The Amplitude Feature Flag Workflow"* — demonstrates the full feature-flag creation workflow in the product.

> **Explanation:** Feature flags are presented as a close cousin of feature experiments — same underlying mechanism (code-level on/off or branching logic) but used for controlled rollout/release management (gradual rollouts, canary releases, audience targeting, kill-switches) rather than strictly for A/B testing.

---

## Lesson 10: Additional Resources / Conclusion

You can learn more about the material presented in this course in the Amplitude Help Center, Community, and website. Additional resources listed:

- **Amplitude Documentation:** Amplitude Web Experiment (all related articles); Amplitude Feature Experiment (all related articles)
- **Community:** View topics in the Amplitude Experiment forum

**Thanks for taking this course!** You've reached the end of *Getting Started with Amplitude Experiment*. Click Next Lesson to take a short knowledge check to complete the course and earn a badge.

---

## Assessment

A graded, scored knowledge-check quiz that must be passed to complete the course and earn its Credly badge. (Quiz questions are drawn from a question bank tied to the learner's own account/progress; this document does not reproduce personal quiz-attempt data.)

## We'd Love Your Feedback

A short survey/feedback form soliciting the learner's feedback on the course.

## Conclusion (final screen)

> If you did not successfully complete the assessment, feel free to retake it as many times as you need. You may find it helpful to review the content of the lessons in this path before attempting the assessment again, but that is not required.
>
> If you did successfully complete the assessment, congratulations! Look for an email from "Amplitude via Credly" for instructions on how to accept your badge.
>
> Click "Next" to submit your feedback, or choose from one of the options below.
- Earn your next badge
- Find your next course
