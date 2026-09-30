# Getting Started with Amplitude Analytics

**Type:** On-demand course | **Time commitment:** 40 minutes | **Prerequisite:** None

---

## About This Course

Getting Started with Amplitude Analytics is designed to teach you the skills necessary to start using Analytics once your account has been activated. It establishes a framework for understanding how Amplitude Analytics works — where it belongs in Amplitude's optimization system, why its use of events is important, and how to use it to better understand your users and improve your products. It also covers how to use Amplitude's AI capabilities, including Global Chat, to get fast answers from your data.

**By the end of this course, you will be able to:**
- Explain how Amplitude's system can help drive product-led growth
- Navigate Analytics so that you know where to create charts and reports and where you'll administer Amplitude
- Explain how events and properties define your analysis
- Identify which chart types could meet your needs
- Analyze your users' product usage
- Build a cohort
- Share insights
- Use Global Chat to ask questions and get instant answers from your data
- Identify next steps for action on analysis

**You should take this course if:** You're a new Amplitude user who needs an overview of the product so that you know where and how to start building your analysis. It does not assume knowledge of analytics generally.

---

## Course Curriculum

The course is organized into three sections — **Overview**, **Analyzing Data**, and **Sharing Insights and Taking Action** — spread across 6 lessons.

## SECTION: Overview

### Lesson 1 — The Amplitude Platform (4 min)

**Amplitude's Analytics Platform**

Amplitude Analytics is an important piece of what Amplitude offers. However, it's just one piece of the platform.

**[Video: "Digital Analytics 1 - Amplitude's Digital Analytics Platform", 1 min 36 sec]** — introduces how digital analytics fits into Amplitude's overall platform. (No on-page transcript is available for this video; the surrounding text below covers its subject matter.)

**How does digital analytics drive business outcomes?**

Aligning your digital analytics strategy to your business strategy is critical to getting the most out of a digital analytics platform. The lesson outlines four common goals that digital analytics can help you achieve, each shown as a quadrant of an interactive graphic:

- **Data Access & Insight** — Digital product-led companies must serve the data-on-demand expectations and needs of their cross-functional teams. Amplitude Data availability, reliability, and self-service enablement are foundational to standardizing data interpretation and building data trust.
  *Outcomes served:* Increase data literacy, Increase data confidence, Increase data availability, Improve data-driven culture.

- **Drive Business Efficiency** — Scaled data availability and literacy increase productivity and efficiency, which leads to innovation, validated product direction, improved engineering prioritization, and more accurate marketing targeting.
  *Outcomes served:* Improve business alignment, Decrease time to customer value, Decrease time to innovate, Increase employee productivity, Decrease customer acquisition cost, Decrease data management cost.

- **Build Loyalty** — Brand and product loyalty is key. To drive engagement and serve the end user, you must innovate in the direction of the user's expectations, continuously meeting or increasing customer satisfaction standards and even anticipating future customer expectations.
  *Outcomes served:* Decrease churn, Decrease product friction, Increase customer satisfaction, Increase monthly active users.

- **Grow Market Share** — Growing market share is an all-encompassing journey that largely depends on the digital product functioning as the business's revenue center. With growth comes more users, higher revenue, and competitive displacement.
  *Outcomes served:* Increase customer lifetime value, Increase customer acquisition, Decrease competitive risk, Increase revenue.

## SECTION: Analyzing Data

### Lesson 2 — Your Data (5 min)

Understanding the data that you have inside Amplitude is critical to leveraging the whole platform. This lesson is a broad overview of the type of data that Amplitude collects — qualitative and quantitative — that is used throughout the platform.

**Quantitative data in Amplitude**

**[Video: "Amplitude Event Data", 5 min 16 sec]** — covers the basic building blocks of your data: events, properties, sessions, and more. (No on-page transcript available; see the vocabulary below for the concepts it covers.)

*✨ Try it out: "What events are available in my project?"*

**Event and User Vocabulary** — key terms for understanding how events work on the Amplitude platform:

- **Event** — An event is an action a user takes in your product (pushing a button, completing a level, making a payment, etc.). Depending on your product, you should aim to track between 15 and 200 events to get a full understanding of how users are engaging with your app. An *event stream* is a sequence of events (e.g., a user first clicks on an advertisement, then adds the product to their cart, then checks out). An *inactive event* is an event that a user does not perform themselves — something happens on the server, such as "Notification sent" or "Account suspended."
  *✨ Try it out — Prompt: "What events are being tracked in my project?" Next: Ask about any events that you're unfamiliar with.*

- **Event Property** — An event property reflects more detailed information about an event at the time it was tracked. These properties depend on the type of app you have and the specific information you think is necessary for understanding a particular event.
  *✨ Try it out — Prompt: "What properties are available on the [event name] event?" Next: Ask about any event properties that you're unfamiliar with.*

- **User Property** — A user property reflects traits about the individual person using your app. The most important thing to remember is that these user properties reflect the state of the user and apply across all their events.
  *✨ Try it out — Prompt: "What user properties are available?" Next: Ask about any user properties that you're unfamiliar with.*

- **Metric** — A metric is a saved, reusable analysis definition that standardizes how your team measures a specific behavior, outcome, or KPI — think of it as a "single source of truth" for a key measurement. Examples: *New Users* (count of users triggering their first session or sign-up event), *Churn Rate* (% of previously active users who didn't return in a given window), *Trial-to-Paid Conversion* (funnel metric from trial start to first payment).
  *✨ Try it out — Prompt: "What Metrics are available in my project?" Next: Ask about any user properties that you're unfamiliar with.*
  🎓 *Learn more: Track Business Goals with Metrics*

**How does Amplitude resolve identities?**

Amplitude identifies and tracks unique users through a combination of user IDs and device IDs:
- **User ID** — A persistent identifier your app assigns to a logged-in user (e.g., email or database ID). This is the most reliable way to track users across devices and sessions.
- **Device ID** — Automatically generated by the Amplitude SDK for anonymous or logged-out users. It's tied to a specific device/browser.

🎓 *Learn more: Identity resolution in Amplitude*

**Qualitative data in Amplitude**

Quantitative data tells you that 40% of users drop off at checkout, but qualitative data shows you the frustrated rage-clicks, the confusing UI moment, or the survey response saying "I couldn't find the promo code field." Together, they give product teams a complete picture, reducing guesswork and enabling faster, more confident decisions. Amplitude has a few ways to analyze qualitative data:

- **Session replay** — Amplitude's Session Replay lets you watch recorded playbacks of real user sessions, showing exactly how users interact with your product including clicks, scrolls, mouse movements, and form interactions. It's tightly integrated with Amplitude's analytics, so you can jump from a funnel drop-off or anomaly directly into a replay to understand the "why" behind the data. You can filter replays by user properties, events, or segments, making it easy to focus on specific cohorts like churned users or high-value customers. Available on web and mobile platforms.
- **Heatmaps** — Uses Session Replay to provide a visual representation of user engagement on your website or application over time. Analyze patterns of events to identify trends, anomalies, and areas of your product that drive the most engagement.
- **Feedback AI** — Allows you to ingest and analyze qualitative user feedback at scale from sources like surveys, support tickets, and app store reviews. It automatically categorizes feedback into themes such as feature requests, complaints, bugs, and loved features, surfacing the most common pain points and trends without manual tagging. This helps product teams connect quantitative behavioral data with the voice of the customer, enabling faster, more informed product decisions.
- **Surveys** — Allows you to collect in-product feedback directly from users at the right moment in their journey, triggered by specific events, user segments, or page visits. Rather than sending generic email surveys after the fact, you can ask targeted questions precisely when a user completes an action, experiences friction, or reaches a key milestone. Survey responses are automatically connected to the user's behavioral data in Amplitude, so you can correlate what users say with what they actually do. Common use cases include NPS measurement, feature satisfaction scoring, churn reason collection, and onboarding feedback.

### Lesson 3 — Building an Analysis (6 min)

Amplitude makes it easy to explore your data visually through a variety of charts.

**[Video: "Building an analysis", 3 min 57 sec]** — walks through how to analyze new users using Amplitude's Global Agent. (No on-page transcript available.)

**Customizing your analysis** — there are many ways to refine your analysis by adding and filtering events and properties as well as changing what the chart is measuring:

- **Segment by different users** — The Segmentation section lets you filter your analysis to a specific subset of users by defining conditions based on user properties, event properties, or cohorts. You can group-by or add multiple conditions to narrow your audience, and any segments you define apply across all events in the chart.
- **Switch project** — Projects can have different events. If you switch projects, Amplitude will do its best to match the current project to the events in the one you changed to.
- **Choose an event or metric** — You can select one or more events to appear in the chart, filter by properties or other metadata to drill into the data you want to show, and group by event properties.
- **Select how you want to measure** — Options vary by chart type. Common ones:
  - *Uniques* — Counts the number of distinct users who triggered the event at least once in the period.
  - *Event Totals* — Counts every occurrence of the event, regardless of how many times the same user triggered it.
  - *Active %* — Shows what percentage of your active users (DAU/WAU/MAU) performed the event in the period.
  - *Average* — Calculates the average number of times each user triggered the event (Event Totals ÷ Uniques).
  - *Frequency* — Displays a distribution of how often users triggered the event (e.g., how many users did it 1x, 2x, 3x, etc.).
  - *Properties* — Aggregates a numeric event property you choose (e.g., file size, revenue) using sum or average across all occurrences.
  - You can even create your own formulas for measurement.

**Common Amplitude charts**

**[Video: "Amplitude Core Charts Overview"]** — Amplitude has many charts that help visualize data in the way most useful to what you're asking. You don't need to know what chart to use in order to ask a question, but knowing more about how the chart works can help you ask better questions.

- **Event Segmentation** — the foundational Amplitude chart for most users. Built by combining events and event properties with user segments; can be as simple as counting users who fired a specific event, or intricate formulas of events.
  *✨ Try it out:* "Make a chart showing daily average usage for the last 30 days in terms of total events, segmenting by all users and for new users (users who were new in the prior 7 days, rolling)."
  🎓 *Learn more: Understand User Behavior with the Event Segmentation Chart*
- **Data Table** — Add multiple events and metrics relevant to your product KPIs and quickly drill into segments that matter to you, like country, product type, or plan type.
  *✨ Try it out:* "Create a table comparing conversion rates, session counts, and revenue by user plan type for this month."
  🎓 *Learn more: Analyze Multiple Metrics at Once with Data Tables*
- **Funnel** — Helps you diagnose problems by seeing how users navigate a defined event path in your product.
  *✨ Try it out:* "Show me a funnel from first page view to account creation over the last 30 days, broken down by platform."
  🎓 *Learn more: Drive Conversion in Your Product with Funnel Analysis*
- **Retention** — Shows the length of time between when users do two events; great for A/B tests between cohorts.
  *✨ Try it out — Prompt:* "Retention chart for our power-user segment with weekly cohorts. Show D1, D7, D30." *Next:* Ask how power users compare to average user.
  🎓 *Learn more: Drive Product Adoption with Retention Analysis*
- **Sessions** — Shows how long and how often users spend time in your product; great for comparing engagement depth across cohorts.
  *✨ Try it out:* "Do paid users have longer sessions than free users?"
  🎓 *Learn more: Unlock Engagement Insights with Session Analysis*

### Lesson 4 — Behavioral Cohorts (4 min)

**Overview of cohorts**

Amplitude's cohorts help you create and analyze custom user groups based on shared behaviors or properties. Cohorts are useful when you want to compare one group of users to another, focus your analysis on a specific group, or take targeted action based on user behavior.

**[Video: "Creating a behavioral cohort", 2 min 17 sec]** — (No on-page transcript available.)

*✨ Try it out: Create a cohort of users who were new in the last 30 days.*

**Cohort use cases** — cohorts can be used to describe a segment of users throughout the Amplitude platform:
- **In charts** — Apply cohorts to charts to perform targeted analyses on specific user groups.
- **Experiments** — Use cohorts in A/B testing and feature flags with Amplitude Experiment.
- **Guides and surveys** — Target specific cohorts with Guides and Surveys for timely, relevant in-product messaging and support.
- **External tools** — Sync cohorts to downstream destinations to further activate user groups.

*Note: This course focuses on behavioral cohorts, user groups based on past actions. Learn more about cohorts relating to future behavior in the course "Create and Analyze Predictive Cohorts."*

## SECTION: Sharing Insights and Taking Action

### Lesson 5 — Sharing Insights (4 min)

**Content Channels in Amplitude**

Amplitude views analytics as a team sport — insights are only meaningful if the right people can take advantage of the information. In the Amplitude platform, you can collaborate and share your analyses in a variety of ways:

- **Dashboards** — Add related charts and cohorts to a single location for a comprehensive "big picture view." Dashboards can be continuously monitored by a Dashboard Agent (covered later in this course). They're shareable both internally and externally, and can be added to a shared Space to make them easily accessible for teammates who use them regularly.
  - *Scaling with official dashboards and templates:* Dashboards (and Charts) can be designated as "official" to make it clear which ones your organization views as an important single source of truth. Dashboards can also be turned into Templates, making it easy to recreate them for repeatable processes such as A/B tests and marketing campaigns (see the Dashboards Templates course).
  - *Public sharing:* Like charts, dashboards can be shared publicly by creating a public link.
  - *✨ Try it out — Prompt:* "Build a dashboard to monitor the health of my core product metrics." *Next steps:* Ask where improvements could be made.
- **Notebooks** — Create documents in Amplitude that explain insights and provide detailed information to teammates through text blocks, pictures, videos, Amplitude Charts, and more. Like Dashboards, Notebooks are shareable internally and externally and can be added to Spaces.
  *✨ Try it out:* "Create a notebook focusing on which channels are performing best, with a focus on channels that are performing well. Include notes with additional context."
- **Spaces** — Everything created in Amplitude is stored in a Space. Every user has a personal space, viewable only by that user, but you can also create team spaces to store key charts, dashboards, notebooks, and cohorts in a centralized, collaborative location so others on your team can access them.
  *✨ Try it out:* "Create a retention KPI dashboard and add it to my team space."

### Lesson 6 — Taking Action (6 min)

After sharing your insights and deciding what to do, it's time to take action. This lesson covers actions you can take with Amplitude and how you might connect with other tools.

- **Improve your product — Experiment** — A workflow-driven behavioral experimentation platform that lets you modify large sections of your customer's experience, testing different aspects of the user journey. Two categories:
  - *Feature Experiments* — Use feature flags to display or hide functionality or A/B options from your customers.
  - *Web Experiments* — Use a Web editor to make direct changes to your website.
  🎓 *Learn more: Getting started with Amplitude Experiment*

- **Provide user assistance in the product — Guides, Resource Center & Assistant**
  - *Guides* are versatile, in-product messages that gently nudge users toward completing specific tasks, exploring new features, or learning more about your product. Unlike traditional popups, guides focus on being helpful and timely, using behavioral triggers, strike detection, and rate-limiting mechanisms to avoid annoying users.
    *✨ Try it:* Create an in-app guide for users who haven't completed onboarding.
    🎓 *Engage Your Users with Guides and Surveys*
  - The *Resource Center* is a widget that surfaces insightful, useful information to users from anywhere on your site. Within it, *Assistant* is an in-product AI helper that answers questions, recommends content, and can launch in-app guides to walk users through common tasks — it isn't a general-purpose support bot, it helps users succeed in your product.
    🎓 *Deliver Targeted Guidance and Support with a Resource Center*
    🎓 *Assistant Course (coming soon)*

- **Understand user sentiment — Surveys** — A source of user feedback; like guides, they're a targeted way to collect thoughts from users and increase the percentage of those thoughts captured. Surveys support advanced conditional logic based on both survey responses and user properties, enabling branching survey paths and personalized follow-up questions. AI Feedback also lets you create guides and surveys based on insights to better connect with your customers' needs.
  *Read the documentation: AI Feedback*
  🎓 *Learn more: Engage Your Users with Guides and Surveys*

- **Use analytics in third-party tools — Amplitude Activation** — Personalization works when you have the right data; most platforms give you one piece (demographics, behavior, or algorithmic predictions) — Amplitude Activation combines all three. Amplitude is self-serve, so any team can build and launch personalized experiences without waiting on engineers or data scientists, covering the full workflow from segmentation to delivery.
  🎓 *Learn more:* Create and Analyze Predictive Cohorts; Target and Engage Your Audiences with Amplitude Activation

- **Use Amplitude with your other AI tools** — You can access your Amplitude data using natural language, whether working within Amplitude or through third-party tools, via the same industry-standard Multi-Channel Protocol (MCP) server that powers Global Agent. Some integrations are available out of the box; others may require additional technical setup. You can bring your own model, and combine multiple data sources (e.g., Salesforce, HubSpot, Amplitude) to answer questions that require drawing on all of them — useful if you have a negotiated contract with a specific model provider (e.g., OpenAI, Anthropic) and want more control over high-level system prompts, for example to limit what data can be queried by users.
  📄 *Read the documentation: Amplitude MCP Server*

- **Specialized agents** — While the Global Agent is available on-demand, Amplitude's always-on specialized agents focus on high-leverage workflows: monitoring dashboards, analyzing session replays, and optimizing website conversion through experimentation. You start by defining a goal for your Agent (e.g., improving conversion or boosting feature adoption); the Agent uses your Amplitude data to identify patterns and make recommendations you can approve for it to act on.
  - **Dashboard Monitoring Agent** — Continuously analyzes your selected dashboards, looks for meaningful changes in key metrics, and runs root-cause analysis to explain what's driving those shifts (e.g., segments, channels, or mix changes). Pushes clear summaries and recommended next steps into Amplitude, Slack, or email when it finds something.
    *Example use cases:* Monitor core product KPIs without manual reporting; catch conversion drops and anomalies early; automate stakeholder updates in Slack or email.
  - **Session Replay Agent** — Automatically watches hundreds of sessions across your funnels or critical events, identifies friction patterns, curates representative replays, and recommends targeted fixes.
    *Example use cases:* Diagnose funnel drop-off with qualitative evidence; improve mobile UX and accessibility; reduce support tickets by fixing "hot paths."
  - **Website Conversion Agent** — Analyzes user behavior on your website, develops hypotheses, designs and configures experiments, generates page variants (including HTML/CSS/JavaScript for web experiments), launches tests with your approval, and measures results to recommend roll-outs or next iterations.
    *Example use cases:* Continuously optimize key landing pages; fix checkout and sign-up friction; test messaging and layout without engineers.

**Common AI questions**

- *Are models trained using customer data?* No. Amplitude does not train AI Models on any customer's data for Amplitude AI Agents. Agents learn from general best practices from the latest foundation models (interaction patterns, accessibility standards, design practices) plus Amplitude's own expertise layered in via system prompts developed from working with thousands of teams.
- *How do Agents learn and know what to do?* Agents synthesize data from different parts of your Amplitude account — analytics, session replay, experimentation, guides and surveys. The more you already use Amplitude to analyze user behavior, the more context your Agents have to work with. Each Agent builds up its own memory about your specific product; this knowledge stays completely separate and secure for each customer.
- *What models power Agents?* Amplitude uses a combination of models from OpenAI and AWS Bedrock, plus many specialized tools and sub-Agents for different tasks (analysis, running experiments, creating guides). Most orchestration, memory, and session management is supported by Amplitude's backend, so Agents behave like product analytics specialists rather than AI generalists.

---

## Assessment

**Result on file:** Passed — 12 of 12 correct (100%), elapsed time 4 minutes.

1. **What are the steps in Amplitude's AI analytics loop?**
   Options: Collect → Visualize → Report / **Sense → Decide → Act (correct)** / Measure → Analyze → Improve
   *Feedback:* The "Sense-Decide-Act" loop (often OODA: Observe-Orient-Decide-Act) is a continuous, iterative cycle for autonomous agents, AI, and human decision-making. It involves gathering environmental data, analyzing it to form a perception, choosing a course of action, and executing it, then repeating the process based on new outcomes.

2. **Identify the event in: "How many unique users in Germany have purchased a song in the pop genre in the past 7 days?"**
   Options: Pop / Germany / **Purchased a song (correct)**
   *Feedback:* "Purchased a song" is the event because that is what users are doing in the product.

3. **Identify the user property in the same question.**
   Options: Purchased a song / **Germany (correct)** / Pop
   *Feedback:* "Germany" is a user property because it is a property that filters on the users, not the event.

4. **A travel app wants to re-engage users who searched for flights but didn't book within 24 hours. Which Amplitude feature should they use to target this group?**
   Options: Funnel chart / Sessions chart / **Behavioral cohort (correct)**
   *Feedback:* You can use behavioral cohorts to save segments of specific users and target them with features like Guides and Surveys.

5. **An e-commerce team wants to find out where users are dropping off between adding an item to their cart and completing a purchase. Which Amplitude feature should they use?**
   Options: Behavioral cohort / **Funnel chart (correct)** / Retention chart
   *Feedback:* A funnel chart is used to visualize how data moves through a process.

6. **Which of the following is an example of an inactive event?**
   Options: Like Post / **Message Received (correct)** / Skip Ad
   *Feedback:* "Message Received" is an example of an inactive event because the user is not performing an action — an action is being triggered for them.

7. **Which of the following goals can digital analytics help you achieve? (Select all that apply)**
   Options: **Grow Market Share (correct)**, **Build Product Loyalty (correct)**, **Scale Data Access (correct)**
   *Feedback:* A digital analytics product like Amplitude can help you achieve all of these goals.

8. **Which of the following can be shared with external users? (Select all that apply)**
   Options: **Dashboards (correct)**, **Notebooks (correct)**, Spaces
   *Feedback:* You can share both Dashboards and Notebooks with external users by creating a public link. You cannot share Spaces with people outside of Amplitude.

9. **True or False? You can add multiple events in a single Event Segmentation chart.**
   Options: **True (correct)** / False
   *Feedback:* You can add multiple events in an Event Segmentation to compare them to one another.

10. **You want to see the number of times an event was triggered on a given day. Which metric should you select in the "Measured As…" section of the Event Segmentation chart builder?**
    Options: Uniques / **Event Totals (correct)** / Frequency
    *Feedback:* Event Totals shows the total number of times an event was triggered per day. Frequency segments users by how often they triggered the event per day. Uniques shows how many unique users triggered the event per day.

11. **When sharing a dashboard with external users, you must do what?**
    Options: **Create a public link (correct)** / You can't share dashboards with external users / Export the dashboard
    *Feedback:* To share a dashboard with external users, you must create a public link. The dashboard will be shared in view-only mode.

12. **Ferdinand wants to know which fruits are most purchased by users in Jakarta over the last 6 months from his online store, AmpliFruit. Which chart would be best?**
    Options: Funnel / **Event Segmentation (correct)** / Retention
    *Feedback:* The Event Segmentation chart would be best suited to this analysis.

---

## Conclusion

If you did not successfully complete the assessment, feel free to retake it as many times as you need. You may find it helpful to review the content of the lessons in this path before attempting the assessment again, but that is not required.

If you did successfully complete the assessment, congratulations! Look for an email from "Amplitude via Credly" for instructions on how to accept your badge.

(The lesson also offers a closing feedback form — "We'd Love Your Feedback" — and links to "Earn your next badge" / "Find your next course," which are navigational, not course content.)

---

## Summary / Explanation

This course is the foundation of the whole Amplitude Analytics certification path. It frames Amplitude as a system that turns raw product usage into decisions: **events** (what a user does), **event properties** (details about that action), and **user properties** (who the user is) are the atomic building blocks; **metrics** package these into reusable, standardized measurements. From there, the course walks through the main analysis surfaces — **Event Segmentation**, **Data Tables**, **Funnels**, **Retention**, and **Sessions** — and how to refine any of them by segmenting users, switching projects, choosing events/metrics, and picking a measurement type (Uniques, Event Totals, Active %, Average, Frequency, or a custom formula). **Behavioral cohorts** let you save and reuse specific user groups across charts, experiments, guides/surveys, and external tools. Once you have an insight, **Dashboards, Notebooks, and Spaces** are the collaboration layer for sharing it, and **Experiment, Guides/Surveys, and Activation** are the "so what" layer for acting on it — improving the product directly, nudging users in-product, collecting sentiment, or personalizing experiences in other tools. The course closes by introducing Amplitude's AI layer: the on-demand **Global Agent** plus three always-on **specialized agents** (Dashboard Monitoring, Session Replay, and Website Conversion), all built on customer data that is never used to train Amplitude's underlying models, and all reachable via natural language both inside Amplitude and through an MCP server for third-party tools.
