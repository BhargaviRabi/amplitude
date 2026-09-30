# Drive Product Growth With Retention and Engagement (Learning Path)

**Path tagline:** "Earn a badge when you learn how to measure your user retention and engagement in Amplitude, and develop goals and strategies for improving those metrics to drive long-term product growth." **[Time: ~1.5 hrs]**

**Path description:** User retention and user engagement are key outcomes that all organizations should focus on as part of their long-term growth strategy. In this path, we'll discuss the relationship between retention and engagement when it comes to driving long-term growth and consider what retention and engagement look like for your specific product. We'll discuss how to analyze your current baseline retention and engagement metrics with Amplitude and then develop goals and strategies for targeting each.

**You will learn the following by the end of this learning path:**
- Understanding the Pillars of Product Growth
- Understand the Importance of User Retention and Engagement
- Measure Your Current Level of Retention and Engagement
- Uncover Opportunities for Improving Your Retention and Engagement

**You should complete this path if:**
- You are responsible for setting success metrics for a new feature or initiative and identifying new levers to move those metrics
- You have taken Digital Analytics Foundations and Getting Started with Amplitude Analytics courses in Amplitude Academy or a live training session
- You have experience building and interpreting analyses in Amplitude Analytics

**Time commitment:** ~1.5 hours

**Cross-sell note (from path page):** "You may also be interested in learning about other product growth pillars, like acquisition and monetization. If so, check out Drive Product Growth With Acquisition and Activation and Drive Product Growth With Monetization."

This path contains 3 courses: (1) Understanding the Pillars of Product Growth, (2) Drive Product Growth With Retention and Engagement, (3) Drive Product Growth With Retention and Engagement - Assessment.

---

## Part 1: Understanding the Pillars of Product Growth (10 min)

This is the exact same shared course documented in full in **`18_Drive_Product_Growth_With_Acquisition.md`** (confirmed via the platform: on this path's page, this course card was already marked "Complete" the moment the path was opened — carried over from having completed it earlier in this same catalog-wide review — and it is the identical course record shared across the Acquisition, Monetization, and Retention and Engagement learning paths). It is not re-transcribed here to avoid duplication; see file 18 for the full content, including:
- The 6-hotspot interactive "pillars of product growth" triangle diagram (Acquisition, Activation, Retention, Referral, Revenue — and how the three growth pillars of Acquisition, Retention, and Monetization interrelate)
- The embedded video "What Is My Critical Event?" (1:51)
- The embedded video "What Is My Product's Usage Interval?" (2:22)
- Full text on defining a product's critical event and usage interval as foundational concepts used throughout all three product-growth paths

---

## Part 2: Drive Product Growth With Retention and Engagement (57 min, 16 lessons)

**Course description (from course page):** Learn how to measure your user retention and engagement in Amplitude, and develop goals and strategies for improving those metrics to drive long-term product growth. [On-demand Course]

This course uses a running fictional case study: **AmpliFile**, a fictional B2B company that helps organizations and individual employees easily upload, edit, and share documents, with seamless integrations that keep files connected to the tools users rely on every day. AmpliFile's defining product parameters, introduced early in the course:
- **Critical event:** Uploading a file — this action reflects core value delivery and is the primary signal of meaningful product use.
- **Usage interval:** A few days per week — most users return 1–2 days per week to manage and share work documents.
- **Other key events:** Sending files and adding integrations — these support AmpliFile's document management and workflow integration offering and reflect deeper user engagement.

The course curriculum is organized into 4 sections:

### Section 1: Understand the Importance of User Retention and Engagement

#### Lesson 1: Understanding Retention and Engagement (6 min)

**Why user retention matters for your product.** Retention measures how many users return to your product over time. Acquisition is key for growth because you need users to have a successful product; however, even the best products lose most new users in just a few days. If you focus on retention as a primary growth metric, you can change the trajectory of your company from one that stalls or gradually loses users to one that sustains growth.

**Retention is a powerful growth lever because it:**
- Builds a loyal, engaged user base that drives growth.
- Impacts critical business metrics, including active user count, engagement, customer lifetime value, and payback period.
- Is more cost-effective than acquisition since retaining and monetizing users is far cheaper than acquiring new ones.
- Unlocks monetization strategies once users are consistently returning and seeing value.

**The role of engagement.** While this learning path focuses on driving growth by increasing user retention, engagement is an essential part of that process because user engagement is directly tied to user retention: **users who aren't engaged in your product won't be meaningfully retained long-term.**

**Connecting retention and engagement.** [Embedded video: "Connecting Retention and Engagement," 3 min 51 sec — *no transcript is exposed in the underlying page data; based on the surrounding text, the video explains how user retention and engagement work together to drive growth*.]

**Your turn! (hands-on prompt):** "This path is meant to be hands-on. You'll encounter sections like this throughout the path where you'll answer questions about your product or perform an analysis in your organization. To get started, open your Amplitude instance in another tab or browser so you're ready to explore your product's retention and engagement metrics."

#### Lesson 2: Metrics That Matter (2 min)

Before you can measure your retention and engagement, you need to know which metrics to focus on. This section introduces the key metrics used to analyze a product's current user retention and engagement.

**Retention metrics** (tab 1):
- **Retention Rate:** This is the primary metric when measuring your retention; it's the percentage of users who continue using your product over a given period.
- **Churn Rate:** Churn rate is the inverse of retention rate; it's how many customers are no longer returning to your product.

**Engagement metrics** (tab 2): To establish a baseline for user engagement, you should review a range of metrics, even those you don't plan to include in your engagement goals. This context helps you recognize when a metric falls outside the expected range, so you can investigate and understand what's driving the change. **Example:** A mobile banking app wouldn't focus its engagement efforts on increasing the length of time users spend in the product. However, if they notice session lengths suddenly rise, they can do further session analysis and explore user paths in the product to determine the cause.

To get a comprehensive picture of current engagement, analyze metrics across three key areas:
- **Critical Event:** Critical event metrics help you determine if users are engaging with your product in a way that drives them to get value from the product. (# of times [critical event] is performed per day/week; % of users who perform [critical event] per day/week)
- **Session:** Session metrics help you understand how much time users spend in the product and determine whether that aligns with your expectations. (# of sessions per day/week; average user session length; average daily time spent in product)
- **Feature Engagement:** Feature engagement metrics give you insight into what features users engage with. (Most used features; least used features)

#### Lesson 3: Check Your Instrumentation (2 min)

Your ability to calculate and track the metrics that matter to your retention and engagement in Amplitude depends on your specific instrumentation. This section reviews what's required for effective analysis and confirms a product's instrumentation is set up correctly.

**Ensure your instrumentation captures key events** — confirm you have instrumented the following (checklist):
- **Critical event:** Define and consistently track your critical event. This event should represent the core value your product provides.
- **Events related to your critical path:** What events do you expect users to trigger before and after your critical event?
- **Other key value events for your product:** When you think about a highly engaged user, what do they do in your product?
- **Session ID:** See Amplitude Documentation's "Track sessions" article for more information on this.

**Use visual labeling to define key clicks.** As you review your instrumentation, you may notice gaps, particularly in tracking specific user actions like clicks on key elements. Amplitude's Autocapture and visual labeling features can help address those gaps. If you instrumented Amplitude with the Browser SDK 2.0, Autocapture is enabled by default and ingests click interactions as two events: *Element clicked* and *Element changed*, each with a predefined set of properties. To track specific user actions and events more precisely, use visual labeling alongside Autocapture. [Embedded/optional video, in an accordion: "Use Autocapture and Visual Labeling to Track Website Clicks," 6 min 34 sec — *no transcript exposed; the video is described as showing how Amplitude's Autocapture and visual labeling let you define and track the clicks that matter*.] **Note (impact box):** "Visual labeling is not required for this course. We cover it here because optimizing your event instrumentation can enhance your retention analyses in Amplitude."

**Better understand your taxonomy** — two linked resources are offered (as buttons, not fully described in-page):
- **Academy Video — "Learn Your Data Taxonomy":** Watch this Amplitude Academy video to learn how to identify what events and properties you currently have instrumented.
- **Academy Course — "Instrument Events/Properties":** Take this Amplitude Academy course to learn how to instrument more events and properties.

### Section 2: Measure Your Current Level of Retention

#### Lesson 4: What Does Retention Look Like for Your Product? (2 min)

Now that you've identified which metrics to track and verified your instrumentation is set up with the necessary events and properties, you're ready to begin driving growth through retention and engagement. The first step is to establish a baseline for your current retention and engagement.

**Introduction to AmpliFile.** To demonstrate how Amplitude can help establish this baseline and guide learners through each workflow in this course, the course uses a fictional demo product called AmpliFile — a fictional B2B company that helps organizations and individual employees easily upload, edit, and share documents, offering seamless integrations that keep files connected to the tools users rely on every day.

Product usage information about AmpliFile used throughout the course:
- **Critical event:** Uploading a file — this action reflects core value delivery and is the primary signal of meaningful product use.
- **Usage interval:** A few days per week — most users return 1–2 days per week to manage and share work documents.
- **Other key events:** Sending files and adding integrations — these events support AmpliFile's offering of document management and workflow integration and reflect deeper user engagement that aligns with the product's value proposition.

#### Lesson 5: Perform a Lifecycle Analysis (3 min)

Before diving into specific metrics like retention and churn rates or analyzing how users engage with key features, it's helpful to start with a high-level view of your user base. This section covers how to use Amplitude's Lifecycle chart to segment users and identify high-level retention patterns.

**Measure retention with lifecycle analysis.** The Lifecycle chart segments users into new, active, resurrected, and dormant categories to give a broad overview of retention trends over time. [Optional embedded video, in an accordion: "Lifecycle chart video," 5 min 29 sec — *no transcript exposed; described as reviewing how to build a Lifecycle chart*.]

**Interactive hotspot diagram — "Lifecycle chart for AmpliFile"** (3 hotspots, click each to learn more):
- **Usage interval:** In this context, the usage interval defines how user activity is segmented in the chart. You set the usage interval to days, weeks, or months. A 7-day interval groups users based on their behavior within each 7-day period. For products with frequent usage patterns like AmpliFile, this interval provides a useful snapshot of how usage changes over time.
- **Timeframe:** Since we are grouping users by 7-day intervals, we'll use a 28-day date range to display four complete weekly buckets.
- **Dormant users:** Over the past four weeks, significantly more users have become dormant than have returned. Once users go dormant, many remain inactive. This is an area AmpliFile may want to investigate further.

**Pause and reflect (accordion, with example responses):**
- *What do you notice about AmpliFile's Lifecycle Chart?* — The number of dormant users consistently exceeds the number of resurrected users each week. This indicates that once users go dormant, they aren't returning.
- *What might AmpliFile want to analyze further?* — AmpliFile may want to analyze whether there's friction in the onboarding or post-upload experience that leads to early user drop-off.
- *What might AmpliFile want to focus on improving?* — AmpliFile may want to set a goal and strategy to re-engage dormant users.

**Your turn!:** "Use the Lifecycle chart in Amplitude to perform a lifecycle analysis for your current user base. What do you notice about your user base? Is there anything you'd like to analyze further? Make sure to save the chart in Amplitude so you can reference it when you're developing your retention goals."

#### Lesson 6: Retention and Churn Rates (8 min)

Now that we've reviewed a lifecycle analysis to get a broad view of user activity, it's time to take a closer look at how well AmpliFile retains its users, using the Retention Analysis chart to explore key retention metrics: **retention rate** and **churn rate**.

**Measure your retention rate.** Before using the Retention Analysis chart to explore AmpliFile's retention rate, it's important to understand how your critical event and usage interval shape your retention strategy. [Embedded video: "Measuring retention in the way that matters," 1 min 15 sec — *no transcript exposed; explains why critical event and usage interval are key for measuring meaningful retention*.]

Amplitude includes a prebuilt Retention Analysis chart in the Out-of-the-box Product Analytics (in addition to being able to build one from scratch via the *Create* button). **Interactive hotspot diagram — "Product Analytics: Retention"** (7 hotspots):
- **Overall Retention:** Provides a snapshot of user retention by day, week, or month based on your configured critical event.
- **Day 7 Retention Over Time:** Displays a trend line showing how Day 7 retention changes over time. For AmpliFile, configured to measure Day 7 retention (customizable to any interval).
- **Usage Interval:** Displays your retention measured as your usage interval.
- **Customize:** Configure your retention metrics, including the critical event, return criteria, and retention interval.
- **Chart editor:** Opens the Retention Analysis chart builder for further customization.
- **Create:** Use the *Create* button to build a Retention Analysis chart from scratch.

**Interactive hotspot diagram — custom Retention Analysis chart walkthrough for AmpliFile** (6 hotspots):
- **Starting event:** For overall user retention, select *Any Active Event*. For new user retention, the choice depends on how you define a "new user" (first time Amplitude sees them vs. sign-up). For AmpliFile, new user retention is measured using the event *New User*, instrumented to trigger when someone signs up for the first time.
- **Return event:** *Any active event* shows the overall rate at which customers return regardless of activity; *critical event* shows the rate at which users return and perform the key value event (a more meaningful measure, since customers getting value are more likely to be retained long-term). For AmpliFile: critical event *Upload File*.
- **Measured as...:** There's no single best way to measure retention — *Return On or After* answers "how many users return on X day or after" (shows a higher rate, since it includes multiple days); *Return On* answers "how many users return on exactly X day" (only that one day). AmpliFile uses *Return On or After*.
- **Time interval:** Usage interval is key for selecting the time interval. For a frequent-use product like AmpliFile, it's most common to focus on Day 7 and/or Day 30 retention, so looking at the past 30–45 days gives the needed metric. If usage interval is weekly or monthly, adjust the time interval accordingly.
- **Day 7 retention:** AmpliFile's Day 7 retention rate is 39.8% (also viewable in the breakdown table below the chart).
- **Day 30 retention:** AmpliFile's Day 30 retention rate is 23.9% (also viewable in the breakdown table).

**Note:** "AmpliFile is a fictional demo dataset for training purposes. To compare your retention against industry benchmarks, explore Amplitude's Product Benchmarks."

**Pause and reflect:** *What does AmpliFile's Day 7 and Day 30 retention tell us?* — Although nearly 40% of new users return by Day 7, retention drops to just under 24% by Day 30. This decline is typical for many products, especially during onboarding, but it highlights the importance of engaging users early and helping them realize value quickly to prevent long-term drop-off.

**Measure your churn rate.** Churn rate is the inverse of retention rate: it measures users who **aren't** returning to your product. To view churn rate, change your Retention Analysis chart visualization to a bar chart, which displays both retention and churn rates.

**Interactive hotspot diagram — churn rate walkthrough** (3 hotspots):
- **Bar chart visualization:** To view the churn rate along with the retention rate, change the chart visualization to *Bar chart*.
- **Day 7 churn rate:** 60.2%.
- **Day 30 churn rate:** 76.1%.

**Pause and reflect:**
- *What stands out about AmpliFile's retention and churn rates?* — A Day 7 new user churn rate of 60.2% and a Day 30 churn rate of 76.1% suggest that most new users aren't sticking around for the long term. While this level of drop-off is common for many products, it highlights clear opportunities to improve onboarding and early engagement. **Consider this:** Amplitude's analysis of over 500 million mobile devices found that, on average, 80% of new users stop using an app within just three days of downloading it.
- *What might they want to analyze further?* — Analyze active user retention to understand if ongoing users are more stable than new users; explore whether certain user behaviors or cohorts lead to better retention outcomes; investigate potential friction points in the onboarding experience that may contribute to early churn.
- *What might they want to focus on improving?* — AmpliFile may want to focus on improving its Day 7 retention by optimizing early engagement and onboarding flows.

**Your turn!:** "Use the Retention Analysis chart to calculate your current retention and churn rates. Take time to look at the difference in retention rate based on the starting/return events you select (including your critical event), and keep your usage interval in mind when interpreting the analysis. How do your Day 7 and Day 30 retention rates compare? What stands out about your retention and churn rates? What would you like to analyze further? **Reminder:** Save your charts in Amplitude so you can reference them when developing your retention goals."

#### Lesson 7: Knowledge Check (2 min) — SCORED

**Question 1 (multiple choice):** "The following Retention Analysis chart shows a usage interval analysis for an e-commerce product called AmpliShop. Their critical event is *Complete Purchase*. Based on the chart below, what is their current usage interval?"
- 4 days — incorrect
- **2 days — CORRECT**
- 10 days — incorrect
- **Feedback:** "Their usage interval is 2 days."

**Question 2 (multiple choice):** "The Retention Analysis chart below shows a retention analysis for a fictional team chat product. What is the Day 7 retention rate for users who returned to the product and performed the *Send Message*? (Hint: Use the Breakdown Table.)"
- 15.1% — incorrect
- 10.4% — incorrect
- **10.7% — CORRECT**
- **Feedback:** "The Day 7 retention rate was 10.7%."

### Section 3: Measure Your Current Level of Engagement

#### Lesson 8: Critical Event Metrics (6 min)

While retention tells you *if* users come back, engagement helps you understand *why* they come back and *how* they're getting value. This section covers how to measure different types of engagement and ask the right questions of the data, covering: critical event metrics, session metrics, and feature engagement metrics — starting with critical event metrics.

**Measure critical event metrics with the Event Segmentation chart.** Event Segmentation is a great starting point for measuring user engagement, helping analyze: how many users are triggering key events; how frequently users trigger key events; how event usage trends over time.

**What's my question? / How can I use Amplitude to answer my question? table:** "What percentage of users are performing a specific event?" → "Build and analyze an Event Segmentation chart." [Optional embedded video, in accordion: "Event Seg 2 - Build," 9 min 34 sec — *no transcript exposed; reviews how to build an Event Segmentation chart*.]

**AmpliFile's Event Segmentation analysis** — analyzing how many users triggered AmpliFile's critical event, *Upload File*, over the last 30 days. Presented as a step-by-step interactive process (4 steps):
1. **Select your critical event and measure its Active %.** *Active %* is calculated by dividing the number of users who triggered the event by the total number of active users. The takeaway metric at the top shows the previous day's active % (87.5%).
2. **Click Current % Active to open the dropdown menu.** Changing the takeaway metric to *Overall % Active* shows that 73.4% of active users triggered the *Upload File* event in the last 30 days.
3. **Select Frequency in the Measured As... module.** Shows the distribution of how many times a user triggered *Upload File* each day — a wide distribution; frequency consistently decreases on weekends and increases on weekdays.
4. **Select Average in the Measured As... module.** Once *Average* is selected, change the takeaway metric to *Average Values*: over the last 30 days, an individual user triggered *Upload File* an average of **3.19 times each day**.

**Summary:** "The Event Segmentation chart offers flexibility for analyzing key engagement metrics over time."

**AmpliFile's stickiness analysis.** Stickiness measures how many days in a given timeframe a user triggers an event — the more frequently users trigger an event, the stickier the product. The Stickiness chart shows how many days per week or month users perform a specific event. **What's my question? table:** "How many days out of a given week or month are users performing a specific event?" → "Build and analyze a Stickiness chart." [Optional embedded video, in accordion: "How sticky is my product?," 3 min 21 sec — *no transcript exposed; reviews how to build a Stickiness chart*.]

**Interactive hotspot diagram — AmpliFile's weekly stickiness for the *Upload File* event** (5 hotspots):
- **Event:** Looking at stickiness for AmpliFile's critical event, *Upload File* (or select *Any Active Event* for a broader view).
- **Weekly:** Looking at how many days in a given week users return to complete the selected event on average (monthly stickiness is also possible depending on usage interval).
- **2 days:** On average, 26.7% of users upload a file 2 out of 7 days of the week.
- **3 days:** 24% of users upload a file 3 out of 7 days a week.
- **6 days:** 2.03% of users upload a file 6 out of 7 days a week, which aligns with the earlier event-segmentation insight about lower weekend usage.

**Pause and reflect:**
- *What are the main insights from these analyses?* — In the Event Segmentation analysis, usage drops on weekends; the Stickiness analysis confirmed this, finding the highest percentage of users upload files 2–3 days of the week. This suggests many users use AmpliFile primarily during the workweek.
- *What metrics might they want to explore further?* — Compare engagement patterns for users who frequently upload files to those who don't; analyze the user journey for users who don't upload files during their session.
- *What metrics should they focus on improving?* — Increase engagement among users who use the product less frequently and identify/remove friction points in the user journey.

**Your turn!:** "Use the Event Segmentation and Stickiness charts to establish a baseline for your critical event metrics. You can repeat this analysis for other key value events in your product. Do these metrics surprise you? Why or why not? What else stood out to you as you analyzed your critical event (or other key events)? What would you like to analyze further? **Reminder:** Save your charts in Amplitude so you can reference them when you're developing your retention goals."

#### Lesson 9: Session Metrics (5 min)

Another important group of engagement metrics is session engagement metrics — how often and for how long users engage with your product. The User Sessions chart helps analyze session data, and the Session Engagement Dashboard offers a prebuilt view of key session metrics. [Two optional embedded videos, in an accordion: "Build a User Sessions Chart," 5 min 32 sec, and "Starter Templates," 1 min 58 sec — *no transcripts exposed; the first reviews building a User Sessions chart, the second reviews leveraging Amplitude's dashboard templates*.]

**AmpliFile user session analysis.** Since AmpliFile helps users manage and organize their work documents, time spent in the product can indicate engagement — longer sessions may suggest users are actively uploading, organizing, or integrating documents into workflows. **What's my question? table:** "On average, how many sessions does each user have per day?" → "Build and analyze a User Sessions chart."

*Note: this lesson's underlying course data contained one placeholder/filler text block under the heading "Introduction" — "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In purus velit, tincidunt ac nibh quis, sollicitudin varius libero. Nullam at mi felis. Donec a scelerisque augue, sit amet porttitor nibh. Suspendisse at lorem ut elit placerat blandit." — This appears to be unfinished/leftover authoring-tool placeholder text in the live course and is reproduced here verbatim per the "no content omitted" instruction, though it is not meaningful course content.*

**Summary (as stated in the course data):** "Session metrics give you valuable insight into how often and how long users engage with your product. By exploring metrics like sessions per user, average session length, and total time spent in-product you can establish engagement baselines and identify patterns that impact retention." **Best Practices:** Monitor trends (watch for peaks and valleys in session data; sudden changes can signal product issues or feature adoption); tailor metrics to your product (for AmpliFile, session frequency and length reflect document workflow; other products may prioritize different session behaviors); review regularly (session metrics work best when tracked alongside retention and feature engagement for a full engagement picture).

**Step-by-step interactive process (5 steps):**
1. **Navigate to the Session Engagement Dashboard template.** Open the prebuilt Session Engagement Dashboard from the available dashboard templates, accessible from the *Create* button.
2. **Explore the Session Engagement Dashboard.** This template already includes a chart answering the question. **Note:** by default, charts on this dashboard analyze sessions that include *Any Event* (can be changed to focus on specific events). The takeaway metric shows users have an average of **3.24 sessions per day**, reflecting that on days users engage with AmpliFile, they tend to have multiple sessions.
3. **Click into the chart to view it in more detail.** Clicking the chart titled "How many sessions per user are there each day?" opens the chart builder, revealing it's powered by the User Sessions chart. Two options to continue: return to the starter template for prebuilt analyses, or stay and adjust the *Measured as...* module — this example stays and customizes.
4. **Click Avg Length.** *Avg Length* measures the average session length for all users — for the last 30 days, AmpliFile sessions average **13 minutes per session**. Looking next at whether session length differs for sessions where users complete the critical event at least once.
5. **Change the event to your critical event.** For AmpliFile sessions where users complete the critical event *Upload File*, session length increases to **20 minutes on average** — users who complete the critical event spend longer in the product. Final step: **Click Time Per User and change critical event to Any Active Event** — shows average daily time per user: AmpliFile users spend about **50 minutes per weekday** in the product.

**Pause and reflect:**
- *What are the key takeaways from AmpliFile's user session analysis?* — The average number of sessions per day is high, at 3.24 sessions per day. Since we hope to see at least one session per day, this indicates healthy engagement for AmpliFile.
- *What metrics might they want to analyze further?* — The average session length is 7 minutes longer for users who upload a file versus those who don't. AmpliFile may want to explore what non-uploading users are doing during their sessions.
- *What metrics should they focus on improving?* — Encouraging users to upload a file at the start of a session could increase engagement. However, deeper analysis is needed to confirm this as a priority.

**Your turn!:** "Use the Session Engagement Dashboard to establish a baseline for your session metrics. Do your session engagement metrics surprise you? Why or why not? What else stood out to you as you analyzed your session engagement? What would you like to analyze further? **Reminder:** Save your charts in Amplitude so you can reference them later when developing your retention goals. You can save the full template as your own session engagement dashboard or save individual charts."

#### Lesson 10: Feature Engagement Metrics (4 min)

In the previous sections, we looked at how many users are performing the critical event and how often. A follow-up question for AmpliFile: for users who are using the product but aren't uploading a file, what are they doing? One way to analyze this is by building an Engagement Matrix chart to see the product's most and least utilized features.

**Evaluate feature engagement with the Engagement Matrix.** The Engagement Matrix helps identify which features users engage with most and least often by comparing adoption and frequency of use. **What's my question? table:** "What are the most and least utilized features of my product?" → "Build and analyze an Engagement Matrix chart." [Optional embedded video, in accordion: "Build an Engagement Matrix Analysis," 7 min 21 sec — *no transcript exposed; reviews how to build an Engagement Matrix chart*.]

**Interactive hotspot diagram — Out-of-the-box Engagement Matrix** (6 hotspots):
- **Feature Engagement:** Compare defined features using the Engagement Matrix, which plots features by adoption (percentage of active users) and frequency (average number of times users engage with that feature).
- **Settings:** Click *Customize* to access Product Analytics settings and define specific features to display, or *Create Feature* to define and add a new feature. Features can be defined with tracked events (including custom events) or Feature Flags from experiments.
- **Feature Engagement Comparison (four-quadrant explanation):** Top right = high adoption, high frequency (likely core features — for AmpliFile, *File Upload* and *Edit* appear here). Top left = low adoption, high frequency (possible power features for a small user subset; consider improving accessibility). Bottom right = high adoption, low frequency (one-time events or rarely needed features, e.g. account creation or onboarding tutorial completion). Bottom left = low adoption, low frequency (often candidates for improvement or deprecation).
- **High adoption, high frequency:** *File Upload* and *Edit* are strong performers with active engagement. Users who aren't uploading files may still be editing.
- **Add Integration:** AmpliFile is tracking the *Add Integration* event because the product team is investing in integrations, and customer research confirms integrating AmpliFile into other workflows is central to its value. **Low usage here is concerning and may signal a missed opportunity to drive engagement.** AmpliFile should explore why this feature is underused.
- **Additional views:** Buttons linking to Event Segmentation charts providing further breakdowns of feature engagement.

You can customize the Out-of-the-box Engagement Matrix using the edit button or create a new one from scratch using the Engagement Matrix chart builder. If building from scratch, consider starting with Amplitude's default event **Top and Bottom Global Events** to see your product's most and least popular events. (This example is configured to measure feature usage by monthly active users (MAU) — can be changed to daily or weekly. Values are plotted on the chart and also appear in the breakdown table.)

**Pause and reflect:**
- *What are the key takeaways from AmpliFile's Engagement Matrix analysis?* — Uploading a file and editing a file are well-utilized features. Sending files and adding an integration are underutilized, indicating potential areas for improvement.
- *What might AmpliFile want to analyze further?* — Given that *Add Integration* has low adoption and frequency, AmpliFile may want to investigate what's preventing users from taking this action. Since integrations are a current product investment and core to AmpliFile's value, improving usage could help boost engagement and retention.
- *What metrics should they focus on improving?* — AmpliFile will want to increase adoption of key features like *Add Integration* to strengthen retention and long-term engagement.

**Your turn!:** "Use the Engagement Matrix chart to analyze your top and bottom events. Do any of these events surprise you? Why or why not? What else stood out to you? What would you like to analyze further? **Reminder:** Save your charts in Amplitude so you can reference them when developing your retention goals."

#### Lesson 11: Knowledge Check (3 min) — SCORED

Both questions in this knowledge check use a second fictional example product, **AmpliTunes** — "a fictional music and video streaming platform that allows users to stream songs, watch videos, and create playlists."

**Question 1 (multiple choice):** "AmpliTunes wants to understand how often users are streaming content. They create the following Event Segmentation chart to analyze the average number of times users trigger the *Play Song or Video* event each week. What does this chart tell us?"
- **Users played an average of 17.7 songs or videos per week. — CORRECT**
- 17.7% of users played at least one song or video each week. — incorrect
- Users played a daily average of 17.7 songs or videos. — incorrect
- **Feedback:** "The chart is measuring the weekly average number of Play Song or Video events per user. This means users triggered the event an average of 17.7 times each week, not daily or as a percentage of users."

**Question 2 (multiple choice):** "Look at the following Engagement Matrix for AmpliTunes. On average, what percentage of daily active users (DAUs) triggered the *Select Song or Video* event during the selected timeframe?"
- 100% — incorrect
- **90.37% — CORRECT**
- 85.89% — incorrect
- **Feedback:** "In the given timeframe, 90.37% of DAUs triggered the *Select Song or Video* event. You can find this value in the breakdown table below the chart."

### Section 4: Uncover Opportunities for Improving Your Retention and Engagement

#### Lesson 12: Uncover Opportunities for Further Analysis (2 min)

Now that baseline retention and engagement metrics have been established, it's time to dig deeper and uncover opportunities to improve them. After analyzing your data, start asking questions like: Where are users dropping off or disengaging? What behaviors correlate with higher retention or engagement? What friction points might be preventing key actions? Questions like these help guide you toward identifying actionable opportunities.

**AmpliFile's deeper insights** — applying these questions to AmpliFile's data surfaced three insights (presented as tabs):
- **Lifecycle Chart — Insight:** More users are going dormant than returning. **Questions to explore:** Are new users finding value quickly enough? How can we re-engage dormant users? (Exploring these could lead to strategies like improving onboarding flows or targeting dormant users with re-engagement campaigns.)
- **Stickiness chart — Insight:** Most users return 2–3 days per week; however, a smaller but significant group returns 5+ days per week. **Questions to explore:** Do users who engage 5+ days per week have higher retention rates? What behaviors differentiate high-frequency users from others? (Investigating these could reveal opportunities to encourage more consistent engagement.)
- **Engagement matrix — Insight:** *Add Integration* shows lower engagement than expected. **Questions to explore:** Why aren't users adding integrations more often? Are there usability barriers or discoverability issues? (Answering these could inform product improvements like UI updates or onboarding guides.)

**Why the course focuses on Add Integration:** "The Lifecycle and Stickiness charts highlight trends worth exploring, but they don't indicate a specific problem that needs attention. In contrast, *Add Integration* shows unexpectedly low usage. This is a core part of AmpliFile's value proposition and an area where the product team is actively investing. Improving adoption here could have a meaningful impact on engagement and retention." **For the rest of this course, the focus is one specific opportunity: increasing engagement with the *Add Integration* event.**

**Your turn!:** "Think about your product's retention and engagement data. What questions do you want to investigate further? Jot down a few now, and we'll revisit them through the remainder of the course."

#### Lesson 13: Continue Your Analysis (4 min)

Once opportunities to investigate are identified, it's time to dig deeper into specific opportunities for growth. Amplitude offers many tools and features to help investigate why certain behaviors happen and uncover what's holding users back. This section explores how AmpliFile investigates one priority opportunity: encouraging more users to add integrations.

**Analyze specific user segments with cohorts.** One of the most effective ways to uncover deeper insights is by creating cohorts — groups of users defined by specific behaviors or attributes. Cohorts help answer targeted questions such as: Who is more likely to return? Which features or actions correlate with retention? Where are users dropping off? To investigate the low engagement with *Add Integration*, AmpliFile created two cohorts: (1) users who added at least 1 integration in the last 90 days, and (2) users who have not added an integration in the last 90 days. [Optional linked resource, in accordion: "Optional: Review Behavioral Cohorts" — points to an Amplitude Academy course, "Create and Analyze User Groups with Amplitude's Behavioral Cohorts"; cohort-creation mechanics are explicitly out of scope for this course.]

With these cohorts saved, they can be applied to the "segment by" modal of any chart — for example, a Retention Analysis chart. **Result:** Comparing these cohorts in a Retention Analysis chart reveals a clear difference: **users who add integrations are retained at a higher rate.** This confirms that increasing integration adoption could meaningfully impact retention and engagement.

**Deeper analysis.** Now that *Add Integration* is validated as a key event linked to higher retention, the course investigates why it's underutilized. *(Same "Lorem ipsum dolor sit amet..." placeholder paragraph noted in Lesson 9 also appears again in this lesson's underlying course data under the heading "Introduction" — reproduced here for completeness per the "no content omitted" instruction, though it is clearly unfinished authoring-tool placeholder text rather than substantive course content.)*

**Summary (as stated in the course data):** "Through this analysis, we: Identified a low-adoption feature tied to retention. Used Cohorts to measure its impact. Explored Journeys to spot friction points. Watched Session Replays and analyzed Heatmaps to uncover root causes. By fixing issues like the broken search bar, we can help more users integrate AmpliFile into their workflow, which we hypothesize will improve both engagement and retention."

**Step-by-step interactive process (3 steps — this previews the Summary's conclusion before the analysis is walked through):**
1. **Use Journeys to explore paths and patterns.** Amplitude's User Journeys chart shows the paths users take before or after a key event, helping uncover patterns and friction points. Viewing a journey map with the path endpoint to *Add Integration* reveals a consistent pattern: **many users contact sales right before adding an integration** — suggesting friction, such as confusion about setup or technical barriers, leading users to seek help before completing the task.
2. **Use Session Replay to uncover friction.** Session Replay lets you watch real user sessions to observe behavior and identify usability issues, adding qualitative context to quantitative chart data. Filtering for users who viewed the Integrations page but didn't add an integration revealed: **the search bar on the Integrations page wasn't working properly — users frequently got an "Oops, No Results Found" error message**, and **users repeatedly tried to search, couldn't find what they needed, and abandoned the process.** Even without reviewing every session, the Replay Summary provides a summary of sessions and suggested potential fixes.
3. **Use Heatmaps to validate behavior patterns.** Heatmaps visualize where users click, scroll, and focus attention on a page, helping validate patterns spotted in charts or session replays. The Heatmap for AmpliFile's integration page showed: **heavy click activity on the search bar**, and **fewer clicks on specific integration options than expected** — confirming that users were trying to find integrations, but search friction was stopping them from moving forward.

**Your turn!:** "Continue your analysis in other Amplitude features. You don't need to limit yourself to Cohorts, Journeys, Session Replay, or Heatmaps, but they are generally useful exploratory features that can trigger some interesting questions and analyses. Do any of these metrics surprise you? Why or why not? What else stood out to you? What would you like to analyze further? Remember to save your charts in Amplitude so you can return to them later when you're developing your retention goals."

#### Lesson 14: Develop Your Hypotheses and Goals (4 min)

After analyzing retention and engagement data, you've likely uncovered opportunities for improvement. This section covers how to translate those insights into clear, actionable goals.

**Focus your goals on meaningful retention and engagement.** Effective goals reflect what meaningful retention and engagement look like for your product — they should be data-driven and tailored to how your customers get value. [Embedded video: "Develop goals that drive lasting growth," 1 min 38 sec — *no transcript exposed; covers developing meaningful goals*.]

**From insights to hypotheses to goals.** Of the opportunities identified, AmpliFile prioritized the *Add Integration* event for deeper investigation due to its connection to higher retention. The hypothesis structure used: "If [we do X], then [users will do Y], because [of Z insight]." Once the hypothesis is written, a strong goal is defined — specific, measurable, and tied to a key retention or engagement metric.

**Insight → Hypothesis → Goal table (AmpliFile example):**

| Field | AmpliFile's content |
|---|---|
| **Insight** | Adding integrations is underutilized and linked to higher retention. Session Replay confirmed a broken search feature was creating a blocker, and Journeys showed users often needed to contact sales before completing the step. |
| **Hypothesis** | If we fix the flow for adding integrations and provide in-product guidance, then more users will add integrations, because usage is linked to higher retention but current adoption is blocked by UI issues. |
| **Goal** | **Reduce drop-off on the integrations page from 70% to 30% within one month.** |

**Note:** "This is just one example. AmpliFile can return to the other insights identified in the baseline retention and engagement metrics and develop additional hypotheses and goals."

**Your turn!:** "What are your goals for improving your customer engagement and customer retention? Before you move forward in the course, take some time to develop your initial engagement and retention goals. This is a good time to brainstorm and write down potential goals; your goals may change as you work with your stakeholders to solidify your focus. Ensure that the goals you come up with are: Aligned with the value you offer to customers; Data-driven."

#### Lesson 15: Determine Your Strategy (3 min)

Once retention and engagement goals are set, the next step is planning how to achieve them. This section covers how to turn insights into action by developing strategies aligned with your goals.

**Determine your strategy.** Amplitude provides tools to help move from insight to action, each supporting a different kind of strategy (presented as 4 tabs):
- **Web Experiment:** Amplitude Web Experimentation lets you run A/B, multivariate, and multi-armed bandit experiments on webpages using a visual editor, with no new code. **Try Web Experimentation if:** your data insights suggest changes in copy, images, colors, and other HTML elements on webpages might increase a user's engagement.
- **Feature Experiment:** Amplitude Feature Experimentation lets you run A/B, multivariate, and multi-armed bandit experiments using feature flags. **Try Feature Experimentation if:** your data insights suggest you need to make improvements to critical paths in your mobile or desktop application (not a webpage or corporate website); or you need a controlled rollout of a new feature or product experience.
- **Guides and Surveys:** Amplitude Guides and Surveys allow you to deliver timely and targeted in-product messages to drive adoption, engagement, and retention. **Try Guides and Surveys if:** your data insights suggest users might benefit from an in-product nudge or just-in-time information; or you want to collect timely feedback directly from your users.
- **Cohort Syncing:** With cohort syncing, you can send behavioral cohorts you create in Amplitude to downstream destinations at a one-time or recurring cadence, delivering the right message to the right user group at the right time. **Try cohort syncing if:** your data insights suggest distinct groups of users behave differently in your product; or you have downstream marketing/customer engagement platforms connected to Amplitude.

**Resource (button):** "Amplitude Academy Download" — a summary PDF with links to relevant Amplitude Academy courses to help deepen knowledge of each action-based strategy.

**AmpliFile's strategy for executing its goal. Goal:** Decrease drop-off on the Integrations page from 70% to 30% within one month. Analysis revealed a broken search function on the integrations page — fixing that is the first step. From there, AmpliFile considers several strategies:
- **Launch a guide to promote integrations:** Create an in-product guide that highlights the integrations feature, explains its value, and shows the improved search experience.
- **Run an A/B test with Amplitude Experiment:** Compare two versions of the integrations page — one with only the fixed layout, another with contextual nudges or walkthroughs to encourage engagement.
- **Sync a cohort to a targeted campaign:** Identify users who haven't added an integration and send them a personalized email campaign.

"When you identify multiple ways to act on an insight, it's tempting to try them all at once. But testing one strategy at a time helps you measure impact more accurately and isolate what's working. That's why AmpliFile is starting with a single approach: launching an in-product guide." This is a strong choice because it: reaches users directly in-product; strategically targets both new users and those who haven't added integrations; promotes a feature tied to long-term retention; helps new users realize value sooner. "After measuring the impact of the guide, AmpliFile can revisit other strategies or adjust its goal based on what it learns. Starting with one clear action enables more informed and strategic iteration."

**Your turn!:** "What strategy will you take to achieve your goals? Take some time to consider what strategy you might take to achieve your goals. This is a good time to brainstorm; your strategy may change as you work with your stakeholders to solidify your approach."

#### Lesson 16: What's Next? (1 min)

*Note: this final lesson's underlying course data contains what appears to be leftover/unedited boilerplate text copied from the Monetization course's equivalent "What's Next?" lesson (it explicitly references "monetization levels" and "acquisition and retention programs," which do not match this course's retention/engagement subject matter). Both this apparent leftover text and the course's own final on-page paragraphs are reproduced below verbatim, per the "no content omitted" instruction.*

**Leftover/boilerplate text found in the course data (not fully edited for this course):** "Once you have determined your strategy for moving forward, it is time to implement that strategy and monitor your progress. Ensure you have a dashboard or notebook set up to easily track your metrics that matter (like we have seen throughout this learning path). Make sure you include other important charts and notes that help tell the story you saw in the data, and to be sure the changes you are making are having the intended effect on your monetization levels. Also, be aware of what impacts your monetization initiatives might have on your acquisition and retention programs and vice versa. Then you can start the cycle of continuously improving your monetization strategy."

**Next Steps (final on-page text):** "Now that you've completed your initial retention and engagement analysis and determined your next steps for improving those metrics and driving growth, you'll continue to monitor your progress toward your goals using Amplitude. You've saved all of your charts and can use those to monitor your progress. We recommended putting those into a dashboard or notebook so you can easily track your metrics. You should include other important charts and notes that help tell the story you saw in the data. Keep in mind that this is a continuous process. In a few months, you'll want to take the time to do another thorough analysis of your current retention and engagement and determine whether you need to adjust your goals."

---

## Part 3: Drive Product Growth With Retention and Engagement - Assessment

**Course description (from course page):** "Take this assessment to complete the Drive Product Growth With Retention and Engagement learning path." Listed as Course 3 of 3 in the path, with a curriculum of: the graded assessment itself, a "Conclusion" lesson, and a "We'd love your feedback!" survey lesson.

**Access note:** This assessment course could not be directly accessed for content extraction. Despite the learning path itself being registered (via the path page's "Get started" button, after which the path showed "1 of 3 completed" reflecting the already-complete shared Part 1 course), navigating directly to this course's URL displayed: **"Register for the learning path to register for this course."** This is the same platform behavior encountered for the equivalent graded Assessment courses in both the Acquisition and Monetization learning paths (documented in files 18 and 19): the platform requires the preceding course (here, the 16-lesson "Drive Product Growth With Retention and Engagement" course, ~57 minutes) to be completed sequentially and in real time in the live player — including watching all embedded videos in full — before this assessment course's own lesson URLs unlock, rather than allowing direct navigation once the path is registered. Given that this assessment is a graded re-test of material that has already been fully and exhaustively extracted above (Part 2), and that unlocking it would require an estimated 45–60+ minutes of real-time sequential video playback and interaction clicking with no new substantive content expected (the same pattern held true for the Acquisition and Monetization paths' assessments), a decision was made not to force full live completion purely to extract a graded quiz shell. This is noted transparently here rather than silently omitted.

---

## Combined Path Summary

The "Drive Product Growth With Retention and Engagement" learning path teaches partners how to establish a baseline for, and then systematically improve, a product's user retention and engagement using Amplitude — completing the trio of foundational product-growth paths alongside Acquisition and Monetization (see files 18 and 19). All three paths share the same introductory course, "Understanding the Pillars of Product Growth," which frames acquisition, retention, and monetization as interrelated drivers of growth and introduces the foundational concepts of a product's **critical event** and **usage interval** — concepts this Retention and Engagement path relies on heavily throughout.

Structurally, this path mirrors the shape of the Acquisition and Monetization paths closely: a single fictional case-study product (here, **AmpliFile**, a B2B document-sharing tool, alongside two additional one-off fictional products used only in the two scored knowledge checks — **AmpliShop**, an e-commerce product, and **AmpliTunes**, a music/video streaming product) is used to walk through Amplitude's analytics workflows step by step, moving through four stages: (1) understanding why retention and engagement matter and confirming the underlying event instrumentation is correctly set up; (2) measuring current retention (via Lifecycle charts and Retention Analysis/churn-rate charts) and current engagement (via Event Segmentation, Stickiness, User Sessions, and Engagement Matrix charts); (3) uncovering specific opportunities for improvement by cross-referencing these baseline charts, then drilling deeper with Cohorts, Journeys, Session Replay, and Heatmaps to diagnose root causes (in AmpliFile's case, a broken search bar blocking users from adding third-party integrations); and (4) turning that diagnosis into a formal Insight → Hypothesis → Goal statement and selecting a single, measurable go-to-market strategy (an in-product guide) from among Amplitude's available activation tools (Web Experiment, Feature Experiment, Guides and Surveys, Cohort Syncing).

Two scored knowledge checks (4 questions total) test comprehension of usage-interval identification, Day-7-retention breakdown-table reading, Event-Segmentation-chart interpretation, and Engagement-Matrix percentage reading — all fully captured above with their correct answers and feedback text. As with the Acquisition and Monetization paths, this path's final graded "Assessment" course (Part 3) could not be directly unlocked without a full live sequential completion of the preceding course and is documented via an explicit access note rather than fabricated or silently omitted. Two minor authoring artifacts were also identified and preserved verbatim for completeness: a "Lorem ipsum" placeholder paragraph appearing twice in the course data (Lessons 9 and 13), and a "What's Next?" closing lesson (Lesson 16) whose underlying data contains leftover boilerplate text referencing "monetization" rather than retention/engagement — both are flagged in-line above as apparent unedited template artifacts rather than intended course content.
