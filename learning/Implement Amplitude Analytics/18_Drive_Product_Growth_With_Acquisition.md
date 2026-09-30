# Drive Product Growth With Acquisition (Learning Path)

**Type:** Learning path (3 courses) | **Time commitment:** 50 minutes

---

## About This Learning Path

For any successful business, growth is a balancing act between three competing but closely interrelated priorities: acquisition, retention, and monetization. Regardless of where you choose to focus first, for a business to grow sustainably, acquisition, retention, and monetization must be thought of as part of a bigger picture. Moving a lever in one, will have an impact on another.

In this path, we'll discuss the importance of user acquisition for driving long-term growth, and how to think about what acquiring new users looks like for the digital arm of your business. We'll discuss how to analyze your current baseline acquisition and activation metrics with Amplitude and develop goals and strategies for improvement.

You will learn the following by the end of this learning path:
- Understanding the Pillars of Product Growth
- Understand the Importance of Acquisition and Activation
- Measure Your Current Level of Acquisition and Activation
- Uncover Opportunities for Improving Your Acquisition and Activation

You should complete this path if:
- You are responsible for setting success metrics for a new feature or initiative and identifying new levers to move those metrics
- You have taken the Digital Analytics Foundations and Getting Started with Amplitude Analytics courses in Amplitude Academy, or a live training session
- You have experience building and interpreting analyses in Amplitude Analytics

Related paths: *Drive Product Growth With Retention and Engagement* and *Drive Product Growth With Monetization* (covered as separate .md files in this catalog extraction).

This path contains 3 courses, covered as three parts below:
1. **Understanding the Pillars of Product Growth** (10 min, 2 lessons)
2. **Drive Product Growth with Acquisition and Activation** (37 min, 12 lessons)
3. **Drive Product Growth With Acquisition and Activation - Assessment** (graded assessment; see note at the end of this document)

---

# Part 1: Understanding the Pillars of Product Growth

**Time commitment:** 10 minutes | 2 lessons

### About this course
For any successful business, growth is a balancing act between three competing but closely interrelated priorities: acquisition, retention, and monetization. Regardless of where you choose to focus first, for a business to grow sustainably, acquisition, retention, and monetization must be thought of as part of a bigger picture. Moving a lever in one, will have an impact on another.

By the end of the course, you'll be able to:
- Define acquisition, retention, and monetization.
- Explain how acquisition, retention, and monetization can impact each other and product growth as a whole.
- Determine your critical event and understand why it's important for measuring meaningful acquisition and retention, and driving monetization.
- Determine your product usage interval and understand how it impacts the way you analyze your product growth.

You should take this course if: You are planning to analyze acquisition, retention, and monetization use cases in Amplitude.

## Lesson 1.1: The Pillars of Product Growth (5 min)

For any successful business, growth is a balancing act between three competing but closely interrelated priorities:
- **Acquiring new customers** and immediately showing them value
- **Retaining customers** by having them continuously engage with your product
- **Monetizing** customers as they realize deeper, prolonged value

Depending on your role in the business and the maturity of your product, your focus may currently be on just one of these three pillars of growth. **User acquisition** may be a focus for new products just reaching product-market fit, while optimizing **monetization** strategies may come later. **Retention** is a keystone that matters at all stages of growth because it is a measure of how well you provide continued value to your users; however, your retention tactics may change as your business priorities change.

Regardless of where you choose to focus first, for a business to grow sustainably, acquisition, retention, and monetization must be thought of as part of a bigger picture. Moving a lever in one, will have an impact on another.

### Interactive: Three pillars of digital product growth
*How do acquisition, retention, and monetization all interplay with one another? This is an interactive "labeled graphic" (hotspot) exercise built around a triangle diagram with "Digital Product Growth" at the center and three pillar circles at the vertices: Retention & Engagement (top), Acquisition & Activation (bottom left), Monetization (bottom right), connected by arrows in both directions along each edge. All 6 hotspots were visited; each reveals the following:*

1. **Newly acquired users must be retained.** For your business to grow, you have to bring in new users. But what good is it if they simply sign-up and then never return? If you don't have a solid strategy to show your users value and retain them, your product becomes a leaky bucket.
2. **Retained users drive acquisition.** Happy, engaged users can be your number one marketing asset. They can bring in new users through virality and user-generated content, as well as by sharing and inviting people in their network. As these new users see value and stay engaged, you can set off a self-perpetuating flywheel of growth.
3. **Acquired users must be monetized.** Even if you have the best strategy in the world for acquiring new users, if you can't convert a key proportion of them into paying customers, or generate ad revenue, your business won't be able to grow sustainably.
4. **Monetization strategies lead to new paying customers.** For some businesses, a monetization strategy can be a competitive differentiator. Thoughtful pricing plans, trial periods, and exposure to paid features through product-led growth (PLG) strategies can both lead to new paying customers and ultimately boost net revenue.
5. **Monetization fuels meaningful retention.** An effective monetization strategy will keep your current customers coming back for more. The best way to maintain and increase your bottom line is to keep your current customers paying for what you are offering.
6. **Retention relates to monetization.** As you retain more users for longer period of time, a thoughtful monetization strategy will convert a proportion of those users into paying customers, ultimately resulting in increased customer lifetime value and net revenue.

### Your turn! (reflection prompt, not graded)
- Between acquisition, retention, and monetization, which of these is **your team's** number one priority?
- What is your role in your business or team's acquisition, retention, or monetization strategy?

*(Links to a shared Google Doc worksheet for personal reflection — not part of the extractable course content.)*

## Lesson 1.2: Your Product's Critical Event and Usage Interval (5 min)

We've mentioned how **acquisition, retention, and monetization** are three key building blocks of product growth. Now let's get down to the specifics of *your* product and business.

With every analysis you build in Amplitude, you should keep in mind the usage patterns that are unique to your product, and use that knowledge to guide how you visualize and dig deeper into your behavioral data.

Before moving on, make sure you understand these two concepts related to your product's usage: your **critical event** and your **usage interval**.

### Your critical event
Your critical event is the key event or events most closely tied to the actions that users take when they are realizing value in your product.

**[Video: "What Is My Critical Event?", duration 1:51 — Wistia embed, hosted by Amplitude Academy.]** *No transcript is exposed in the underlying page data for this video; per the course framing, it explains the concept of a product's "critical event" (the key action(s) tied to a user realizing core value in a product) and why identifying it matters for acquisition, retention, and monetization analysis.*

### Your usage interval
Your product's usage interval is the cadence with which you expect users to trigger your critical event.

**[Video: "What Is My Product's Usage Interval?", duration 2:22 — Wistia embed, hosted by Amplitude Academy.]** *No transcript is exposed in the underlying page data for this video; per the course framing, it explains how to determine the expected cadence (daily, weekly, etc.) at which users should trigger the critical event, and why this cadence should shape how retention and conversion analyses are built.*

### Your turn! (reflection prompt, not graded)
- **What is your critical event?** You'll use it to analyze your product metrics throughout this learning path.
- **What is your product's usage interval?** Keep this interval in mind especially when building retention and conversion analyses.

---

# Part 2: Drive Product Growth with Acquisition and Activation

**Time commitment:** 37 minutes | 12 lessons

### About this course
User acquisition and activation — the process of growing your user base and showing them initial value — is the first stage of any company's long-term growth strategy. This involves investing in the right acquisition channels to acquire new users, guiding them through their first onboarding, and activating them with an initial show of value. Making a good "first impression" on your new users sets them up for long-term engagement and retention. How to think about your acquisition and activation strategy depends on your product, business goals, and stage of growth.

In this course, we'll discuss the importance of user acquisition for driving long-term growth, and how to think about what acquiring new users looks like for the digital arm of your business. We'll discuss how to analyze your current baseline acquisition and activation metrics with Amplitude and develop goals and strategies for improvement.

**Part 1 - Understand the Importance of Acquisition and Activation**
- Articulate the importance of acquisition and activation for driving long-term growth
- Determine the key metrics for measuring acquisition and activation for your product
- Check your data taxonomy to ensure that the relevant events and user properties are instrumented in order to carry out your analyses

**Part 2 - Measure Your Current Level of Acquisition and Activation**
- Analyze your active users and new users in Amplitude
- Analyze your sign-ups and sign-up conversion in Amplitude
- Analyze your critical activation funnels in Amplitude
- Analyzer acquisition channels in Amplitude

**Part 3 - Uncover Opportunities for Improving Your Acquisition and Activation**
- Deepen your data investigation by leveraging different analytical questions and tools
- Uncover optimal paths for conversion and drop-off
- Generate an insight-backed hypothesis based off your investigative analyses
- Implement product and marketing strategies for increasing acquisition and activation

You should take this course if: You have taken Digital Analytics Foundations and Getting Started with Amplitude Analytics courses in Amplitude Academy or a live training session.

## Lesson 2.1: Understanding Acquisition and Activation

Welcome to Amplitude's course on analyzing your acquisition and activation strategy.

**[Video: "Understanding Acquisition and Activation", duration 2:28 — Wistia embed, hosted by Amplitude Academy. Video description in page data: "Define the stages of acquisition and activation and the metrics that matter." No transcript is exposed in the underlying page data.]**

### Acquisition-related use cases
Acquisition is one of three major pillars of growth. Every business must continue to acquire and activate new users, as well as engage and retain them in order to grow in a sustainable manner. However, the flavor of your acquisition challenge may be different depending on your organization's current stage of growth and your team's immediate challenges.

Common examples of acquisition-related use cases:
1. **How can I get more users adopt the digital arm of my product?** You may be a traditional brick-and-mortar business with a loyal client base — perhaps a bank, a healthcare provider, or a retail business — looking to drive more of your offline client base to the services on your website or app.
2. **How can I get more users to use my new digital product or feature?** You may have an established digital business and are looking for ways to drive users to a newly launched product or feature, which is a new revenue stream for your organization.
3. **How can I reach a new brand new audience?** You may be an established digital business who sees rich engagement among your ideal customers, but are looking to appeal to new persona or a new demographic.

### Your turn! (reflection prompt, not graded)
Take a moment to consider what your organization's overall acquisition goals are. Where do you and your team fit into those goals?

## Lesson 2.2: Metrics That Matter for Acquisition and Activation

When assessing your current acquisition and activation and developing a strategy for growth, it's important to consider metrics that represent different phases of the customer journey and the key product actions associated with each. *(A reference diagram, "not exhaustive," is shown offering suggested ways of measuring acquisition and activation — image only, not reproducible as text.)*

### Types of acquisition and activation metrics
You'll notice from the diagram above that there are metrics that are focused on counts, metrics that are based on rates, metrics related to channel, and metrics related to cost. This is presented as an interactive tabs component with three tabs:

- **Counts:** Your **raw count** of unique active users, new users, sign-ups and more. These numbers are the basis of all of the rest of your analyses.
- **Rates:** Your **proportion** of users who perform a key conversion event during a specified time window. Sign-up rates, onboarding rates, activation rates, and other critical conversion rates tells you whether your users are getting to the right parts of your product, at the right time, and finding their aha moments.
- **Cost & Channel:** Customer acquisition cost (CAC) and return on ad spend (ROAS) are two common metrics tied to acquisition costs.
  - **CAC** = (total amount invested in acquisition channels) / (number of customers acquired).
  - **ROAS** = (total amount of revenue brought from ad campaigns) / (total spent on advertising).
  - *Note: Because multitouch marketing attribution can make these calculations tricky, the calculation details are covered in a different course.*

## Lesson 2.3: Check Your Instrumentation

In the next several lessons, we will go into how to analyze metrics related to acquisition and activation. If you'd like to leverage similar metrics and analyses for your own business use case, be sure to have the following instrumented (checklist):
- **Your critical event and critical paths.** These are the key actions leading up to and including events that are tied to your product's core value proposition.
- **Sign-up started and completed events.** These events will help you analyze your sign-up funnel.
- **Onboarding events.** These events will make up your onboarding and activation funnels.
- **Marketing attribution.** This includes **UTM parameters** such as source, medium, and campaign, as well as **referrer parameters**, which link the last web page the user was on to the destination page. These properties can help you measure your new user acquisition by channel.
- **User properties related to important user personas.** For example, does your product offer different plan types? You may want to instrument properties that will let you easily segment your users.

### Check for Autocapture events
The events and properties related to your product's critical paths and users might already be instrumented through precision tracking, Autocapture with visual labeling, or a combination of the two. If you're leveraging Autocapture with the **Browser SDK 2** or the **Amplitude WordPress plug-in**, you will automatically capture the following event types:
- Page viewed
- Form started
- Form submitted
- File downloaded
- Start session
- End session
- Attribution
- Element clicked
- Element changed

You can check if your team is using Autocapture by navigating to your Events in Amplitude Data and searching for one of the Autocapture event types (screenshot of Events table shown).

### Check for labeled events
Amplitude's Autocapture ingests click interactions as the event "Element clicked" or "Element changed." If your team leverages Autocapture, you'll also want to check if these click events have been further defined through visual labeling. You can find all of your labeled events in the Events Table in Amplitude Data (screenshot shown).

Talk to someone on your team to make sure you can identify which labeled events correspond to events in your critical click paths. If you're a developer, you can learn more about configuring Autocapture in the Browser SDK 2 documentation.

## Lesson 2.4: Scenario: Acquisition and Activation for Financial Services

The metrics and analyses we will walk through for these lessons will be centered around a fictional product and its acquisition use case. The data we will analyze is a synthetic data set. While the context of these analyses might be different from your product or service, the types of charts and analytical techniques used are universal.

### The AmpliStocks Demo Product

**The situation:** AmpliStocks is a financial services company offering banking, brokerage, and wealth management services that are similar, let's say, to a traditional finserv institution like Charles Schwab. **AmpliStocks wants to grow the number of clients trading stocks using their newly launched web app**, and we're on the team responsible for driving that number up. Our product is instrumented, we have data coming into Amplitude, and we're ready to formulate a data-driven strategy.

**What we know** (flashcard exercise — 6 cards, front/back pairs):
1. **Critical event → Stock Purchased.** AmpliStocks has several critical moments of value for the user, but our team is concerned with the stock purchasing action.
2. **Usage interval → Daily.** The usage intervals of AmpliStocks's different product areas vary. We're interested in capturing **active traders** who will open the app at least once a day to check stock prices.
3. **Acquisition Path →** Clients are being targeted via various channels to **sign-up** for the new app.
4. **Activation Path →** New app users **(1) verify their financial details** and **(2) make their first stock purchase** in order to be considered activated.

With this in mind, the course proceeds to measuring current acquisition and activation metrics for AmpliStocks.

## Lesson 2.5: Count Active and New Users (7 min)

Let's start with the basics. When acquisition is going well, your **active users** are growing in number. Your count of active users is the first metric you should start with when measuring acquisition or engagement. In Amplitude, the best way to count your active users is using the **Event Segmentation chart**.

### Optional review videos (accordion)
- **"Event Segmentation - Build"** — 6 min 36 sec video (Wistia). Description: "Optional: Review how to build an Event Segmentation chart." No transcript exposed.
- **"Starter Templates"** — 1 min 58 sec video (Wistia). Description: "Optional: Review how to leverage Amplitude's dashboard template." No transcript exposed.

### What is my count of active users?
In Amplitude, you can take a number of different approaches to eventually arrive at the correct active user analysis. You can:
- Create a new Event Segmentation chart from the *Create* menu
- Start with a dashboard template or a chart template
- If available in your organization, leverage Ask Amplitude to generate this chart with AI

*(Note callout: Ask Amplitude and Amplitude's other AI features are evolving rapidly — see Amplitude's documentation to learn more.)*

Click through the steps below (walkthrough with annotated screenshots) to find out how to use pre-built templates to build a basic Event Segmentation chart that shows daily/weekly/monthly active users over a specified date range:
1. **Start from a chart template.** Amplitude chart templates are a fast, easy way to get to your product's first data insight — accessible through the *Create* menu, including DAU, WAU, and MAU charts.
2. **OR: Start from a dashboard template.** Alternatively, start from a dashboard starter template such as the **Getting Started KPIs (Web)** dashboard template, which contains a number of common charts, including a DAU chart.
3. **Select the DAU chart.** By default, this chart shows the daily count of unique users who triggered any active event over the last 30 days.
4. **Change the date range.** For AmpliStocks, the instructor changes the date range to March 1–June 30 (a little over one quarter) to see how things changed as a result of March acquisition campaigns.
5. **View your average DAUs over the date range.** An interesting spike appears in DAUs on April 10, where the DAU count goes from 200–500 active users to 4x that number (worth investigating further). To see the average DAU value across March 1–June 30, the takeaway metric is changed to show *Average Values*, revealing **an average of 1.29k DAUs** from March 1 to June 30.
6. **View your average WAUs over the date range.** Changing the chart's time interval from daily to weekly shows **an average of 8.01k WAUs** from February 27 to July 2 (date range adjusts to accommodate full calendar weeks).
7. **View your average MAUs over the date range.** Changing to monthly shows **an average of 34k MAUs** from March 1 to June 30.

It's good to see active user counts generally trending upward — these numbers are often used as proxies for user growth. To get a more accurate count of *new* users (not just *active* users), analyze the default Amplitude **New User** event.

### What is my count of new users?
Note that the **New User** event is surfaced by default by Amplitude when a user logs their first event (including inactive events) to Amplitude. Going back to the daily active user chart, filtering to only new users during March 1–June 30 (hotspot walkthrough):
1. **Choose New User in the Events Module.** Instead of **Any Active User**, select **New User** to filter events to the New User event only.
2. **Choose to view Average Values.** This surfaces the average number of users who were new each day between March 1 and June 30.

Result: an average of **1.11K new users per day** between March 1 and June 30. This curve follows a similar trajectory as the daily active user curve for this time period, and the average number of daily new users is also very similar to the average number of daily active users.

### Check your knowledge (inline knowledge check, multiple choice)
**Question:** In the chart above, which of the following Event Segmentation options will show us what percent of our daily active users are new users?
- Event Totals
- **Active % ← Correct answer**
- Frequency

**Feedback (correct):** For the above chart, **Active %** will plot the percentage of all active users who triggered the **New User** event.

### What is my month-over-month new user growth?
While raw user numbers can be helpful, showing how a trend changes from period to period can tell an even more powerful growth story. Comparing new users in April to new users in March (hotspot walkthrough):
1. **Adjust the date range.** Date range adjusted to April 1–April 30 to compare to the previous month.
2. **Change to a bar chart visualization.** Bar charts are useful to view the aggregate count of unique new users during the specified date range.
3. **Compare to the previous month.** Using the compare-to-previous-period feature.
4. **Toggle between absolute count and percent change.** By absolute numbers: **36,590 unique new users** in April vs. **9,255 unique new users** in March. As a percent change: a **295% increase** in new users from March to April.

*(Note callout: While a 295% month-over-month growth rate is remarkable, it does not reflect the reality of most digital products. Benchmark your new user growth rate against real products in your industry via Amplitude's Product & Web Benchmark Metrics.)*

## Lesson 2.6: Analyze Sign-ups (5 min)

Using Amplitude's default **New User** event is a quick and convenient way to track the growth of your new users. However, a consideration of this event is that a user will be counted as "new" even if they log an event that isn't active. A more conservative way to measure your acquisition is by analyzing an event directly tied to new user sign-ups.

### What is my count of new sign-ups?
Picking up from the daily active users Event Segmentation chart, changing a few settings (hotspot walkthrough):
1. **Choose the sign-up event.** Select the event that triggers when a user has completed the sign-up process.
2. **Measure by uniques.** Shows the unique number of users who triggered **Sign Up Completed** in the March 1–June 30 date range.
3. **View average values.** Shows the average count of daily unique sign-ups over the date range.

Result: an **average of 30.6 unique users** triggered the **Sign Up Completed** event from March 1–June 30, 2023. The chart shows a spike around April 10, similar in trend to the spikes seen in active users and new users for this date range. To diagnose sign-up issues or opportunities, next investigate the app's sign-up process (sign-up rate).

### Optional review video
- **"Build a Funnel Analysis Chart"** — 4 min 41 sec video (Wistia). Description: "Optional: Review how to build a Funnel Analysis chart." No transcript exposed.

### What is my sign-up rate?
To find the sign-up rate, build a funnel chart including events that trigger during the app's sign-up process, for March 1–June 30. Approaches:
- Create a new Funnel chart from the *Create* menu
- Start with a chart template and customize the funnel steps
- If available, leverage Ask Amplitude to generate the chart with AI

Walkthrough (hotspots):
1. **Choose the events in the sign-up flow.** Select **Sign Up Started** as the first event, **Sign Up Completed** as the second event, analyzed "in this order" — meaning conversion paths that begin with Sign Up Started and end with Sign Up Completed, with any number of other events in between.
2. **Measure as conversion, counting by unique users.** Uncovers the proportion of unique users who trigger the **Sign Up Completed** event.
3. **Adjust the conversion window.** Set to one day (target: users finish sign-up within one day).
4. **View the conversion rate.** Result: **sign-up rate is 4.82%** — out of users who triggered Sign Up Started, 4.82% went on to trigger Sign Up Completed.

Less than 5% of users who begin the sign-up process complete it — worth investigating why (covered later in the course).

### Check your knowledge (inline knowledge check, multiple choice, True/False)
**Question:** When I set up a *this order* funnel with two steps in my sign-up flow, users who trigger any other event between these two steps will NOT be considered converted.
- True
- **False ← Correct answer**

**Feedback (correct):** *This order* funnels require users to trigger the events you selected in the order you specified to be converted. **However, users who trigger other events in between the ones specified will also be counted as converted.**

## Lesson 2.7: Analyze Onboarding and Activation Funnels

Once a new user has signed up for an account, there is usually a series of guiding steps that leads them to finding initial value in your product. The user's first aha moment, and the beginnings of habit formation, are what define the activation stage. Onboarding and activation are often used synonymously. With some products — like AmpliStocks and other financial service products — new user onboarding might specifically entail additional steps a user needs to take after sign-up and *before* they realize value.

### What is my onboarding rate?
As part of onboarding for AmpliStocks, a new user needs to add and verify their bank account. Date range stays March 1–June 30, conversion window 1 day, measuring conversion rate by unique users (hotspot walkthrough):
1. **Select your onboarding funnel events:** (1) Add Bank Account, (2) Verify Bank Account, (3) Successfully Verified Bank Account.
2. **View total conversion rate.** The total conversion rate — through the last step of the funnel — is **19.1%**. For funnels with more than 2 steps, it's also valuable to see which step had the largest drop-off or was slowest to convert (via the takeaway dropdown).

**19.1%** of users in the four-month date range successfully verify their bank account within one day of adding it. While informative about the verification flow's usability, it isn't an accurate measurement of activation — that requires a funnel measuring users reaching an aha moment: users who **completed sign-up** and eventually went on to **purchase stock**.

### What is my activation rate?
Building a two-step funnel with the aha moment as the last step, coming after sign-up completion (hotspot walkthrough):
1. **Select activation events:** **Sign Up Completed** (first step), **Stock Purchased** (second step, the aha moment).
2. **Adjust the conversion window.** Set to **7 days** (allowing time for users to familiarize themselves with the product before reaching the aha moment).
3. **View the conversion rate.** Result: **58%** — for users who completed sign-up, 58% went on to purchase stock within seven days (March 1–June 30 date range).

An activation rate of 58% in a seven-day window is promising — over half of users who sign up go on to trigger Stock Purchased. Natural next question: how *long* does it take most users to make their first stock purchase?

### What is my time to activate?
The time it takes for a new user to activate is sometimes referred to as **time to value**. The faster users realize first-time value, the quicker they're set down the path of habit creation. Adjusting the previous Funnel Analysis chart (hotspot walkthrough):
1. **Filter by historical count.** Filtering the **Stock Purchased** event by the Amplitude property **Historical Count**, set to **1st** — capturing each user's first-ever trigger of the Stock Purchased event.
2. **Measure as 'Time to Convert.'** Shows a distribution of time to complete the funnel steps within the 7-day conversion window. Over 40% of conversions completed within 7 days happened in the first hour after entering the funnel.
3. **View median time to convert.** The median time to convert during the 7-day window is **a little over 11 hours**, with over 40% of conversions happening within the first hour.

AmpliStocks's median time to first stock purchase is around eleven hours, but almost half of conversions happen within one hour — suggesting some users make their first purchase in the same session as sign-up, while others return the next day. Investigating session metrics or other engagement metrics alongside this funnel may be valuable.

### Your turn! (reflection prompt, not graded)
- What do your important onboarding or activation funnels look like?
- What could your new user's aha moment be?
- Do you have an idea what your conversion window should be?

## Lesson 2.8: Analyze New User Acquisition Channels

One last important type of analysis for getting your acquisition baseline: **channel analysis**. Most new user acquisition efforts involve marketing campaigns, growing organic traffic, and other paid and non-paid channels. Amplitude's channel classifiers and out-of-the-box marketing analyses make it simple to see where new users are coming from.

### Optional review videos (accordion)
- **"Campaign Reporting"** — 6 min 05 sec video (Wistia). Description: "Optional: Review channels in Amplitude." No transcript exposed.
- **"2. Build Data table"** — 2 min 44 sec video (Wistia). Description: "Optional: Review how to build a Data Table." No transcript exposed.

### Where do my new users come from?
Building a data table breaking down acquisition by paid and organic channels, first checking the team's channel definitions in Amplitude Data (screenshot shown: events with utm_source = Google classified as Paid Search; Instagram, Facebook, and Youtube classified as Paid Social).

Building the data table (hotspot walkthrough):
1. **Analyze the New User event by uniques.**
2. **Group by your channels** using the correct channel classifier dropdown.
3. **Break down your channels by utm_source** for more detail.
4. **Adjust the date range** to stay consistent with other analyses.
5. **View table and chart** (chart view alongside the default table view).
6. **Visualize the data as a bar chart** (instead of the default line chart).

Result: **AmpliStocks' paid channels are doing the best**, with paid search (Google) bringing in the most new users. Of the paid social channels, Instagram performs best.

### How does my activation rate compare by channel?
Using Data Tables' multidimensional analysis capability with a saved custom **Activation Rate** metric (the conversion rate from Sign Up Completed to Stock Purchased within a 7-day window), removing the utm_source group-by and viewing this metric alongside new user count (hotspot walkthrough):
1. **Add a metric** — the Activation Rate metric, next to the new user count.
2. **Toggle the chart visualization** — viewing the activation funnel grouped by channel.

Result: **while activation rates across channels are fairly similar, new users from organic search have a slightly higher activation rate at 60.24%.**

## Lesson 2.9: Deepen Your Data Investigation (1 min)

Now that we have analyzed metrics to get a baseline understanding of our acquisition and activation, it's time to dig deeper into our data to uncover interesting insights that may lead us to growth opportunities.

### Tools for slicing and dicing your data
When faced with a chart on a dashboard, it can sometimes be daunting to know what analytical question to ask next. Cultivating that curiosity requires practice and deep familiarity with your product and data. Questions to ask to continue data exploration:
- How does my analysis change if I **segment my users by persona**?
- What does my analysis look like if I **group by certain properties**?
- **What paths** do users who drop out of my conversion funnel take?
- How does one **user cohort** behave compared to another?
- What are users doing **before and after a key conversion event**? What does their user journey look like?
- Can a **different data visualization** offer a different sort of insight?
- Is there data in the form of **session replays or surveys** that might offer more perspective?

As an extended example, the course uses one of the open questions from the AmpliStocks analysis and applies these questions to dig deeper (continued in the next lesson).

## Lesson 2.10: Uncover Paths to Conversion and Drop-off

In the initial AmpliStocks analyses, only 4.82% of users completed the sign-up funnel in the 1-day conversion window. Because signing up is the first step to activation, the goal is to boost the sign-up completion rate.

### Optional review video
- **"2. Build a Journeys Chart"** — 2 min 38 sec video (Wistia). Description: "Optional: Review how to build a Journeys chart." No transcript exposed.

### Explore sign-up paths
Using Journeys to see the top paths users take between **Sign Up Started** and **Sign Up Completed**. Journeys can look at data in a 45-day range. Between May 15 and June 30, Journeys shows that **67.4% of users** followed the first-listed path between Sign Up Started and Sign Up Completed: **Personal Details Added → Selfie Made → ID Uploaded → ID Verified**. With this, a new sign-up funnel with these additional steps can be built and explored.

### Investigate the lowest converting steps
With the new funnel built with the additional steps discovered in Journeys, the biggest drop happens between the **ID Uploaded** and **ID Verified** steps. Clicking into the drop-off area of the bar reveals **62%** of users who completed the ID Uploaded step do not complete the sign-up funnel. Possible causes: a system error or undue friction in the sign-up path. Next step: use Journeys to analyze the drop-offs further.

### Explore drop-off paths and drivers of churn
Using the **Microscope** feature to delve deeper into funnel data (walkthrough):
1. **Click the appropriate bar to open Microscope** — clicking the top part of the bar on the ID Verified step to investigate users who churned at this step.
2. **Show user journeys.** Reveals paths users take after churning at the ID Verified step — 10.7% of these users triggered the **Discover More** event, raising a question of correlation with churn.
3. **Show drivers of drop-off.** Using Microscope's *Conversion Drivers* view: the **Discover More** event has a **positive correlation score**, meaning a correlation exists between triggering this event and dropping off the funnel (not necessarily causation, but worth exploring further).

The **Discover More** event is triggered when a user clicks a button at the top of the sign-up flow — possibly distracting users at this step.

### Watch how users navigate your product
If friction is suspected, Amplitude's **Session Replay** can show exactly how and where users get stuck. Navigating to Session Replay through the funnel shows event streams and replays of users who triggered **ID Uploaded** but got stuck after. *(Note: this Session Replay example is from a different demo environment — "AmpliMoney" — for illustrative purposes only, unrelated to the AmpliStocks analyses above.)* Walkthrough (hotspots):
1. **View your relevant Session Replays** — viewing replays that include the **Start Sign Up** event.
2. **Choose a replay** — selecting replays that include the event of interest.
3. **Watch the replay** — watching the user navigate the website.
4. **Review the replay summary and highlights** — instead of watching replays start to finish, Amplitude AI summarizes each replay; clicking through summaries of several replays gives a general sense of user sentiment and friction points.

### Wrap-up
Going back to the AmpliStocks product, the plan is to build a hypothesis around the **Discover More** event: will removing the button or making it less noticeable improve the sign-up rate? *Note: improving AmpliStocks' sign-up conversion is one potential angle for improving new user activation rate. Since this funnel is upstream of the stock trading feature, further investigation into users who have already completed sign-up and bank verification may also be valuable in the future.*

## Lesson 2.11: Develop a Hypothesis and Set Your Strategy

Based on the investigative analyses, it's time to formulate a hypothesis and a strategy to improve the metrics — turning insights into action.

### Tools to act on your data insights
Amplitude provides tools to move from insight to action, each supporting a different kind of strategy. Interactive tabs component with four tabs:

- **Web Experiment:** Amplitude Web Experimentation lets you run A/B, multivariate, and multi-armed bandit experiments on webpages using a visual editor, with no new code. **Try Web Experimentation if:** your data insights suggest changes in copy, images, colors, and other HTML elements on webpages might increase a user's engagement.
- **Feature Experiment:** Amplitude Feature Experimentation lets you run A/B, multivariate, and multi-armed bandit experiments using feature flags. **Try Feature Experimentation if:** your data insights suggest you need to make improvements to critical paths in your mobile or desktop application (not a webpage or corporate website), or you need a controlled rollout of a new feature or product experience.
- **Guides and Surveys:** Amplitude Guides and Surveys allow you to deliver timely and targeted in-product messages to drive adoption, engagement, and retention. **Try Guides and Surveys if:** your data insights suggest users might benefit from an in-product nudge or just-in-time information, or you want to collect timely feedback directly from users.
- **Cohort Syncing:** With cohort syncing, you can send behavioral cohorts created in Amplitude to downstream destinations at a one-time or recurring cadence, delivering the right message to the right user group at the right time. **Try cohort syncing if:** your data insights suggest distinct groups of users behave differently in your product, and you have downstream marketing or customer engagement platforms connected to Amplitude.

*(A downloadable "summary PDF" button links to https://academy.amplitude.com/take-action-on-your-data-insights — external resource, not part of the extractable course content itself.)*

### State a data-driven goal and hypothesis
Reflecting on the AmpliStocks analyses, the metric presenting the most opportunity for immediate improvement was the sign-up rate.
- **Goal:** Increase sign-up rate by 2 percentage points in the next quarter.
- **What we know:**
  - Only 4.82% of users completed sign-up within a day of starting the flow.
  - The biggest drop-off in the sign-up funnel happened between the ID Uploaded and ID Verified steps.
  - About 11% of users who drop off at this step click on the Discover More button.
- **Hypothesis:** The Discover More button could be distracting new users from completing AmpliStocks' sign-up flow.

### Implement a strategy
Candidate strategies considered for AmpliStocks:
1. **Run an experiment removing or modifying the Discover More button.** Use Amplitude's Web Experimentation to test whether removing or modifying the button's appearance results in a statistically significant increase in conversion between ID Uploaded and ID Verified — and whether that ultimately affects the sign-up rate metric.
2. **Nudge all users along the sign-up flow with a walkthrough.** Use Amplitude's Guides and Surveys to provide a more guided experience instead of having users navigate the flow themselves.
3. **Send an email with resources to users who drop off after the ID Uploaded step.** Save a cohort of users who drop off after ID Uploaded, sync it to a customer engagement platform, and send a personalized email with troubleshooting documentation links.

While all are valid strategies, it's best to try them one at a time to understand what's truly working. Which strategy to try first depends on available resources, time, and stakeholder input. After implementing a strategy, you can revisit other strategies or adjust goals based on what you learn — starting with one clear action enables more informed, strategic iteration.

### Your turn! (reflection prompt, not graded)
What strategy will you take to achieve your goals? This is a good time to reflect on your data insights and brainstorm opportunities for improving your acquisition and activation metrics. Your strategy may change as you work with stakeholders to solidify your approach.

## Lesson 2.12: What's Next?

The process of growing a business — balancing the demands of acquisition, retention, and monetization and driving the metrics that matter to you upward — is one that is cyclical and iterative.

After you have executed a plan for moving your metrics, it will soon be time to come back into Amplitude to measure the impact of that product change or personalized communication on your bottom line. As your business (or team) needs begin to evolve, you may find yourself moving more into the territory of retention and engagement and monetization. Regardless of whether your focus shifts or not, it is worth remembering that tugging on one growth lever is almost certain to move the others.

### Thanks for completing this course!
You've reached the end of **Drive Product Growth with New User Acquisition and Activation**. Click "Next" to begin a short assessment to test your understanding of this material. You will then be asked to share your feedback by completing a short survey.

---

# Part 3: Drive Product Growth With Acquisition and Activation - Assessment

**Course 3 of 3** in the Drive Product Growth With Acquisition learning path.

"Take this assessment to complete the Drive Product Growth With Acquisition and Activation learning path."

**Access note:** This course is individually registration-gated behind full, in-platform sequential completion of Part 2 above (each of its 12 lessons must be marked complete by watching each embedded video to completion and satisfying each "Complete the content above before moving on" gate in the live player). All of Part 2's substantive content — including its two inline scored knowledge checks (with correct answers reproduced above) — was fully extracted via the underlying course-data API, which is independent of the platform's own lesson-completion/progress tracking. Because progressing this course also requires a matching amount of real-time video playback (the videos in Part 2 alone total roughly 35+ minutes across "optional review" and required clips) purely to satisfy the platform's sequential-unlock gating rather than to access any new content, the assessment course's own item bank was not reachable within this extraction session. Its curriculum, per the platform, consists of three items: "Drive Product Growth With Acquisition and Activation - Assessment" (the graded quiz itself), "Conclusion," and "We'd love your feedback!" (a survey) — no further text is exposed for these items until the course is unlocked. Given the course description ("Take this assessment to complete the...learning path"), the assessment most likely re-tests comprehension of the material already fully captured in Parts 1 and 2 of this document.

---

## Combined Path Summary

This learning path ("Drive Product Growth With Acquisition," 50 minutes total) is the first of three parallel "Drive Product Growth" paths in this catalog (the other two cover Monetization, and Retention and Engagement), all built around the same foundational framework: acquisition, retention, and monetization are three interrelated pillars of product growth, where moving one lever inevitably affects the others. Part 1 establishes this shared vocabulary — the three pillars, plus the cross-cutting concepts of a product's **critical event** (the key value-realizing action) and its **usage interval** (the expected cadence of that action) — concepts that recur throughout every "Implementing Amplitude Analytics" and "Drive Product Growth" course in this catalog. Part 2 is the practical core of the path: using a single running fictional case study (the "AmpliStocks" financial-services demo product), it walks step-by-step through the full acquisition-and-activation analytics workflow in Amplitude — counting active and new users (Event Segmentation), measuring sign-up and onboarding/activation rates and time-to-activate (Funnel Analysis), attributing new users to acquisition channels (Data Tables), and then digging into *why* a funnel underperforms using Journeys, Microscope (conversion drivers), and Session Replay. The path closes its analytical arc by modeling the full insight-to-action loop for AmpliStocks: a concrete, numbers-backed goal (raise sign-up rate 2 points), a testable hypothesis (a distracting "Discover More" button), and three concrete tactics mapped to Amplitude's own action-layer tools (Web/Feature Experimentation, Guides and Surveys, Cohort Syncing) — a template partners can reuse directly with their own customers' acquisition funnels. Part 3, a graded assessment gating official path completion, could not be extracted directly due to platform sequential-unlock requirements as detailed above, but its content is expected to test the same material fully documented in Parts 1–2.
