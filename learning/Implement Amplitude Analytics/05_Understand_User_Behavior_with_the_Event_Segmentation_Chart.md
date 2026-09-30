# Understand User Behavior with the Event Segmentation Chart

**Type:** On-demand course | **Time commitment:** 7 minutes

---

## About This Course

Event Segmentation is the foundational Amplitude chart for understanding what your users are doing in your product. This course takes a deep dive into Event Segmentation, teaching you to combine events and event properties with user segments so you can track metrics over time, see how new features or updates affect user behavior, and build custom formulas to extend Amplitude's prebuilt metrics. This course builds on "Getting Started with Amplitude Analytics" and demonstrates where and why to use some lesser-known features within Event Segmentation. While designed for users who are newer to Amplitude or event-based analytics, experienced users may also find something they didn't already know.

**After taking this course you'll be able to:**
- Build and interpret a basic Event Segmentation chart
- Interpret how various metrics are calculated and how to change the default options
- Extend the chart's built-in functionality with custom functions

**You should take this course if you:**
- Are new to Amplitude Analytics
- Have taken the "Getting Started with Amplitude Analytics" course

---

## Lesson 1 — Event Segmentation Chart Overview (4 min)

Event Segmentation charts at Amplitude can be both versatile and powerful.

**[Video: "Building an Event Segmentation Chart", 3 min 37 sec]** — walks through options when segmenting events. (No on-page transcript available.)

**Every chart answers one question:** *"How often did [who] do [what], counted [how]?"*

Changing any of four dimensions changes the answer the chart gives you. This lesson uses an interactive, numbered diagram of the Amplitude chart-builder UI (Events / Add Event / Measured As / Segment By) where each of the four numbered hotspots reveals one dimension:

- **Dimension 1 — Event (what)** *"The action you're tracking."* Filters narrow which occurrences count. If you filter Play Song or Video where Genre = Pop, only pop song plays are included. The user count only reflects users who played pop songs; other plays don't count.
  *When you'd use this:* Track a specific feature action, like "Export Report" or "Invite Sent"; filter to one variation of an event, like purchases over $100 or sessions longer than 5 minutes; narrow to a specific platform, like mobile-only plays or web-only logins.

- **Dimension 2 — Group-by (how sliced)** *"How you're breaking results down."* Splits results into buckets. If you group by Country, every user is still in the chart — just sorted into their country bucket. No one is excluded. The totals still add up.
  *When you'd use this:* Compare feature adoption across plan types — free trial vs. paid; see which device type (mobile, desktop, tablet) drives the most engagement; break down an event by region or country for a geographic view.

- **Dimension 3 — Metric (how counted)** *"How you're counting occurrences."* How you count determines what your numbers mean. **Uniques** counts each person once. **Event Totals** counts every occurrence — including multiple actions by the same user. A chart showing 12,000 Event Totals does not mean 12,000 users.
  *When you'd use this:* Uniques — reporting adoption: "How many users tried this feature?"; Event Totals — reporting volume: "How many times did this happen?"; Average — reporting depth: "How many songs does a user play per day on average?"

- **Dimension 4 — Segment (who)** *"Which users you're including."* Narrows which users are included. If you add Country = US in the Segment By module, only US users appear in your chart. The denominator changes — non-US users are excluded entirely.
  *When you'd use this:* Restrict the chart to paid users only, or free trial users only; compare two specific audiences side by side by adding a second segment; scope analysis to users who completed onboarding before measuring engagement.

**Selecting a metric**

If you're confused about what you are seeing, remember to check what the chart is counting and how. This lesson includes an interactive example — a `checkout_completed` event scenario (Last 7 days, All Users) — with three tabs, each showing the same underlying data measured a different way:

- **Unique Users — "How many people completed checkout?"** 4,543 unique users this week (+12% vs. prior week). Each user is counted once per day, no matter how many times they checked out — a power user who completed checkout 4 times on Tuesday still counts as 1 for that day.
  *Watch for this:* Switch to a bar chart in Amplitude and the same user is deduplicated across the *entire date range* — not per day. Your Unique Users number will drop. It's not a bug; line and bar charts count differently.
  *✨ Try it out:* "How many unique users triggered my most popular event each day over the last 7 days?"

- **Event Totals — "How many checkouts actually happened?"** 6,712 total checkouts this week (+18% vs. prior week). Every occurrence of the event is counted — that power user who checked out 4 times on Tuesday counts as 4. This number is always ≥ Unique Users — never lower.
  *Read the gap:* Notice Event Totals is ~1.5× higher than Unique Users here. That gap tells you repeat checkouts are common — some users check out multiple times per day. A small gap means most users do it once and stop.
  *✨ Try it out:* "How many times was my most popular event triggered each day this week — show me total occurrences, not unique users."

- **Average — "How often does a typical user complete checkout?"** 1.47 avg checkouts per user (+4% vs. prior week). Divides total occurrences by unique users. A value of 1.47 means the average user who checked out this week did so 1.47 times. It shows depth of engagement — not just whether users acted, but how much.
  *Compare to Uniques:* If Uniques are flat but Average is rising, you're getting more repeat behavior from the same users — deepening engagement, not growing your audience. A rising Average with rising Uniques means both breadth and depth are growing.
  *✨ Try it out:* "What is the average number of times users trigger my most popular event per day this week?"

## Lesson 2 — Knowledge Check (3 min)

**Result on file:** Passed — 2 of 2 correct (100%).

1. **You're looking to see the variation in the number of times users purchased songs or videos — which metric would you use?**
   Options: Frequency / Uniques / Average / Active %

2. **Someone points out that the chart you made has a problem: when you add the totals from the bars of unique ticket purchasers together (898,569), they equal far more than the total number of unique users who purchased a ticket (285,440). What's going on?**
   Options:
   - There is likely an error in the Amplitude backend and you should contact support.
   - Users made purchases in more than one category and are duplicated in each bar.
   - The issue is that two different things are being compared — one chart is showing unique users and the other is showing event totals.
   - The person is sending you information from the test project, so the numbers are different.

*(The quiz UI marks each question "Correct answer" once passed but does not expose which specific option was selected in the page text, so option text is reproduced above without individually marking the chosen answer.)*

---

## Feedback

This course ends with a "We'd love your feedback" survey lesson — navigational/administrative, not course content.

---

## Summary / Explanation

This course is a focused deep-dive on a single chart type that "Getting Started with Amplitude Analytics" only introduced briefly. It reduces every Event Segmentation chart to one question — "How often did [who] do [what], counted [how]?" — and maps that question onto four configurable dimensions: which **event** (with filters) you're tracking, how results are **grouped** (sliced into buckets without excluding anyone), which **metric** counts occurrences (Uniques vs. Event Totals vs. Average, each answering a different business question), and which **segment** of users is included (which actually excludes people, unlike group-by). The core insight the interactive examples drive home is that Uniques and Event Totals will diverge whenever users repeat an action — Event Totals is always ≥ Uniques — and Average (Event Totals ÷ Uniques) tells you whether growth is coming from more people acting (breadth) or the same people acting more (depth). The Knowledge Check then tests exactly this distinction: recognizing when two numbers "don't add up" because they're actually measuring different things (uniques vs. totals), not because of a data error.
