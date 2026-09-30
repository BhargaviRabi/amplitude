# Drive Conversion with Funnel Analysis and Journeys

**Type:** On-demand course | **Time commitment:** 8 minutes

---

## About This Course

Learn how to investigate a conversion problem from first question to actionable recommendation, using Amplitude's Global Agent to start and Funnel Analysis, Pathfinder, and Journey Map to investigate.

**By the end of this course, you'll be able to:**
- Use Global Agent to ask a conversion question and interpret the chart it builds in response.
- Use Funnel Analysis to quantify where users are dropping off in a conversion flow.
- Use Pathfinder to discover what users are actually doing instead of converting, including unexpected friction events.
- Use Journey Map to compare two user groups who hit the same friction event and determine what separates the ones who convert from the ones who abandon.
- Translate a Journey Map finding into a specific, segmented product recommendation.

**You should take this course if you:**
- Are new to Amplitude Analytics
- Have taken the "Getting Started with Amplitude Analytics" course

---

## Lesson 1 — Drive Conversion in Your Product (8 min)

Conversion problems rarely have obvious causes.

**[Video: "Conversion - funnels and journeys", 3 min 08 sec]** — shows how one PM uses Global Agent and three Amplitude charts (Funnels, Pathfinder, and Journey Maps) to find out exactly why users are abandoning checkout, and what to do about it. (No on-page transcript available.)

### When to use each chart

Each chart answers a different question. Use this as a reference when deciding where to start an investigation:

- **Funnel Analysis**
  *When to use it:* You have a specific sequence you want to measure. You know the path, but you want the numbers — or you want to build a cohort based on funnel logic.
  *The core question:* Where are users dropping off, and how many?
  *Potentially hands off to:* Journeys, which bridges the gap between your ideal funnel and the paths users actually take.

- **Pathfinder**
  *When to use it:* You want to explore how users generally navigate your product at a specific point, without defining the path in advance.
  *The core question:* What paths are users taking through my product? What's happening in those paths that I didn't expect?
  *Potentially hands off to:* Funnel Analysis to measure a path you discovered precisely, or Journey Map to compare two groups on a path you found.

- **Journey Map**
  *When to use it:* You want to understand the specific actions users take before, after, or between specific events.
  *The core question:* How do different groups of users move from one point to the next in my product, and where do their paths diverge?
  *Potentially hands off to:* Session Replay to watch the actual user experience at the moment of divergence, a cohort for follow-up targeting, or back to Funnel Analysis to put hard numbers on a pattern Journey Map revealed.

### Questions each chart can answer

**Funnel Analysis:**
- What percentage of users complete checkout from Add to Cart to Complete Purchase?
- At which step are users abandoning my onboarding flow?
- How has my signup-to-activation conversion rate changed over the last 90 days?
- Do mobile users convert at a different rate than desktop users?
- *Ask Global Agent:* "Why did conversion drop?" or "Compare conversion rates between mobile and web"
- Save dropped-off users as a cohort to target with messaging or analyze further

**Pathfinder:**
- What are users doing after they reach Checkout?
- What paths lead users to activate after signing up, and which ones lead to drop-off?
- What are users doing immediately before they cancel their subscription?
- What paths do users take after viewing a feature, and which ones lead to deeper engagement?
- In Pathfinder, you can anchor on a user property value instead of an event — useful when you want to explore paths for a specific audience rather than a specific action.

**Journey Map:**
- Of users who hit an error at Checkout, who recovered and completed the purchase, and what did they do differently?
- How long does it take users to move between two key events, and where are they losing time?
- What paths do converted users take between two events, compared to users who dropped off?
- How does one user segment move through a flow compared to another?
- After Journey Map surfaces a path pattern or drop-off, save those users as a cohort to target with messaging or analyze further.

### Interactive: Explore the controls

An interactive widget lets you click through the configuration controls of two chart types.

**Tab: Funnel Analysis Chart**

- **Control 1 — Events + Event Order** *"What you're measuring, and in what sequence."* Each event in the funnel represents one step a user must complete. The order setting defines how strictly that sequence is enforced.
  - *In this order* — users must complete the steps in sequence, but other events can occur in between.
  - *Exact order* — no other events between steps. The strictest definition.
  - *Any order* — all events must occur, but sequence doesn't matter.
  - *Exclude users who did* (below the funnel events) removes users who triggered a specific event at any time within the funnel — useful for removing error states or experiment variants from the analysis.
  - *When you'd use this:* Use "In this order" for a checkout funnel where users must add to cart before paying; use "Exact order" when you want to measure a strict onboarding sequence; use "Exclude users who did" to remove users who hit an error event between two steps.

- **Control 2 — Measured as** *"What the funnel is calculating."* Changes what question the chart answers.
  - *Conversion* — what percentage of users completed each step? The default view. Choose to count by Unique Users or Event Totals.
  - *Over Time* — how has the conversion rate at each step changed over your date range? Use this to see if a change improved or hurt conversion. Select the specific steps to target.
  - *Time to Convert* — how long does it take users to move from one step to the next? Shows the median time at each step. Select the specific steps to target.
  - *Completed within* sets the timeframe in which a user must complete all steps to count as converted. A 1-day window means users must complete the full funnel within 24 hours. Extending this window captures users who take longer.
  - *When you'd use this:* Use Conversion to diagnose a drop-off problem right now; use Over Time to see if a product change improved conversion; use Time to Convert to find where users are getting stuck or delaying.

- **Control 3 — Segment by** *"Which users are included in the analysis."* Filters the entire funnel to a specific user population. Unlike Group by (which splits users into buckets), Segment by narrows who is included at all — users who don't match the segment are excluded entirely. Import a saved segment or build one inline using user properties and cohorts. Only one segment can be applied at a time.
  - *When you'd use this:* Scope the funnel to paid users only to understand their specific conversion behavior; limit to users who completed onboarding before measuring activation; compare two specific audiences by running the funnel twice with different segments.

- **Control 4 — Group by** *"How each segment breaks down."* Splits the segment into buckets by a user property. If you group by Country, every user still counts — they're simply sorted into their country bucket. Totals add up across buckets; conversion is calculated independently for each. Good for spotting where the funnel performs differently.
  - *When you'd use this:* Compare conversion across plan types (free vs. trial vs. paid); see which platform converts best (iOS vs. Android vs. Web); surface geographic patterns by country, region, or acquisition channel.

**Tab: Journey Chart: Pathfinder + Journey Map**

- **Control 1 — Paths** *"The anchor event(s) for the analysis."* Defines where path analysis starts, ends, or is bounded.
  - *Starting with* — shows all paths users took after a specific event.
  - *Ending with* — shows all paths that led to a specific event, looking backward.
  - *Between* — shows all paths between two events, including paths that never reached the second event.
  - *Pathfinder vs. Journey Map:* In Pathfinder, you can anchor on an event or a user property value. In Journey Map, you can anchor on events only. The Converted/Dropped Off toggle also only becomes active when using Between mode with two events defined.

- **Control 2 — Measured as** *"How users are counted and the analysis window."* Uniques counts each user once per path. Event Totals counts every time the path was taken, including multiple times by the same user. Completed within sets the session or time window in which paths are counted — the default is 1 session; extending this window captures paths that span multiple sessions.
  - *When you'd use this:* Use Uniques when you want to understand how many people took a path; use Event Totals when frequency of the path matters, not just who took it; extend the completion window when your users' journeys span multiple days.

- **Control 3 — Only show paths that include** *"Filter the chart to paths containing a specific event."* Filters the chart to show only paths where a specific event occurred — use this when Pathfinder has surfaced an unexpected event and you want to isolate paths where it appears, to understand who hits it and what they do next. Without this filter, all paths from the anchor event are shown; with it, only paths containing your specified event are included.
  - *When you'd use this:* After Pathfinder reveals a friction event, filter to paths including that event to study it; isolate paths that include a specific error event to see what users do after hitting it; focus on paths where a key feature was used to understand what comes before and after.

- **Control 4 — Segment by** *"Which users are included in the path analysis."* Narrows the analysis to a specific user population. Only one segment can be applied at a time; users who don't match the segment are excluded from all paths shown. Import a saved segment or build one inline with user properties and cohorts.
  - *When you'd use this:* Limit paths to mobile users only to see how their behavior differs from desktop; scope to new users to understand early-lifecycle path patterns; filter to a specific cohort to see how a particular audience moves through the product.

### Interactive: Interact with the charts

A second interactive widget demonstrates deeper, non-control interactions available on each chart type, using an example scenario (Add to Cart → Checkout → Confirm Payment Info → Complete Purchase).

**Tab: Funnel**

- *Funnel (Default) — "Reading a funnel chart" ("How conversion is shown step by step")* — A funnel measures how many users complete each step of a defined sequence. Each bar represents one step. The solid portion is users who continued; the hatched portion above it is users who dropped off at that step. The first bar is always 100%, showing everyone who entered the funnel. Every subsequent bar is a percentage of that original group, not the previous step. The step-to-step drop-off between bars is usually more useful than the cumulative percentage — it tells you exactly where the biggest loss is happening. In the example, the biggest percentage drop from one step to the next is between Checkout and Confirm Payment Info: most users who abandon (not by the number of users, but by the percentage of users from the previous step) do so before they ever enter their payment details.

- *Funnel: Microscope — "Drilling into a data point" ("What happens when you click a bar")* — Clicking on any data point in a funnel chart opens up the Microscope popup for the users represented by that data point:
  - **Show Journeys** — Launches a Journey Map pre-configured for the step you clicked, showing paths taken by converted and dropped-off users at that exact point. The most direct handoff from Funnel Analysis to Journey Map.
  - **Watch Session Replays** — Opens Session Replay filtered to users at this funnel step. Watch actual recordings of real sessions at the moment users converted or abandoned — view what they saw, where they hesitated, what they clicked. Answers questions charts can't: was something confusing? Was something broken?
  - **Run Deep Insight** — Runs an AI analysis on users at this step, surfacing patterns and hypotheses about what's driving conversion or drop-off. Best used as a starting point for a hypothesis — it tells you what to investigate further, not the final answer.
  - **Create Cohort** — Saves the converted or dropped-off users at this step as a named cohort for use in other charts or sharing with other teams. Common uses: track whether drop-offs return later, compare their behavior in Pathfinder, or hand the cohort to a marketing team for targeting.

**Tab: Pathfinder**

- *Pathfinder: Sankey (default) — "All paths users took, left to right" ("Flow-based view of every sequence")* — The Sankey shows every path users took between your anchor events, ranked by frequency. Read it left to right: the leftmost column is your starting event, each column to the right is the next step. Wider streams mean more users took that path. Use Pathfinder when you know *where* something is happening but not *what* — you're not measuring a predefined sequence, you're seeing everything users actually did, including events and friction points you didn't know to look for.

- *Pathfinder: Sunburst — "Same paths, radial layout" ("Breadth-first view of all paths at once")* — The same path data as the Sankey in a radial layout. The center is your starting event; each ring outward is the next step. Arc size represents the proportion of users who took that path. Use Sunburst when you want to see the full breadth of all paths at once; use Sankey when you want to trace a specific sequence step by step. Same data, different shape, different question.

**Tab: Journey Map**

- *Journey Map: Converted (default) — "Paths that worked" ("Ranked list of routes taken by users who converted")* — Journey Map shows the specific step-by-step paths users took between your two anchor events, as a ranked list. Each row is a distinct path; the percentage shows how many users took it; the time shown is the average time to move from start to end on that path. You are looking at users who completed the ending event — these are the paths that worked. Journey Map is a comparison tool, not a discovery tool — its power comes from toggling between Converted and Dropped Off and looking at what's different between the two groups.

- *Journey Map: Dropped Off — "Paths that didn't work" ("Routes taken by users who never reached the ending event")* — This view shows the users who did not complete the ending event and the paths they took instead. Compare this view to Converted — look for events that appear in one view but not the other, and for paths that end abruptly (a single event followed by nothing), which often signals a dead end. Check the time data: users who spend a long time before dropping off are trying to push through and failing, which is different from users who leave immediately. The Converted/Dropped Off toggle is only active in "between" mode, with both a starting and ending event defined — without an ending event, there is no converted group to compare against.

## Lesson 2 — Knowledge Check

**Result on file:** Passed — 2 of 2 correct (100%).

1. **A PM at a music streaming app notices that the overall trial-to-paid conversion rate dropped 8% last month. They want to find out where in the conversion flow users are stopping. What should they do first?**
   Options: Open Journey Map to compare users who converted to paid against users who didn't / Open Pathfinder starting with the trial start event to see what users do after signing up / Ask Global Agent to build a funnel showing conversion through the trial activation flow

2. **Pathfinder reveals that a large number of users are hitting a "Paywall Viewed" event between Complete Profile and First Listen — an event that wasn't part of the original onboarding design. A PM opens Journey Map and finds that users who converted to First Listen spent an average of 4 minutes between Complete Profile and First Listen; users who dropped off spent an average of 18 minutes. What does this suggest?**
   Options: The paywall is not causing the drop-off; time on step is not a meaningful signal / The conversion window should be extended to capture users who take longer to complete the flow / Users who drop off are spending significantly longer at the paywall, suggesting it's creating friction that motivated users will push through, while others won't

*(The quiz UI marks each question "Correct answer" once passed but does not expose which specific option was selected in the page text, so option text is reproduced above without individually marking the chosen answer.)*

---

## Feedback

This course ends with a "We'd love your feedback" survey lesson — navigational/administrative, not course content.

---

## Summary / Explanation

This course teaches a three-chart investigative workflow for conversion problems, mirroring how an analyst actually works a real drop-off: start broad with **Funnel Analysis** to quantify exactly where in a known sequence users are dropping off (and by how much, step to step, not just cumulatively); when the funnel reveals a big drop but not why, switch to **Pathfinder** to see everything users actually did at that point, undirected — this is how you find friction events nobody designed for; once Pathfinder surfaces a suspect event, use **Journey Map** in Converted-vs-Dropped-Off comparison mode to see what concretely separates the users who pushed through from the users who gave up (often revealed by time-on-step, or by paths that dead-end). Each chart hands off to the next — Funnel to Pathfinder to Journey Map, and from any of them into Session Replay (to watch what happened) or a saved Cohort (to act on it). The "Microscope" popup is the connective tissue that makes this workflow fast: clicking any funnel bar can jump straight into Journey Map, Session Replay, an AI-generated hypothesis (Deep Insight), or a saved cohort, without leaving the chart. The Knowledge Check questions test exactly this diagnostic sequence: knowing to start with a funnel to quantify a known problem, and correctly interpreting a Journey Map time comparison (longer dwell time before drop-off signals friction people are fighting through, not a data or window problem).
