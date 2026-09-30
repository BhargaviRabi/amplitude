# Drive Product Growth With Monetization (Learning Path)

**Type:** Learning path (3 courses) | **Time commitment:** ~55 minutes ("Earn a badge" learning path; overview page states ~1 hr)

---

## About This Learning Path

Monetization and revenue generation are key outcomes that most companies focus on as part of their long-term growth strategy. How to think about monetization and your strategy for improving it varies based on your products and your organizational goals.

In this path, we'll discuss the importance of monetization for driving long-term growth and how to think about what monetization looks like for your specific product. We'll discuss how to analyze your current baseline monetization metrics with Amplitude and develop goals and strategies for improvement.

You will learn the following by the end of this learning path:
- Understand the Pillars of Product Growth
- Understand the Importance of Monetization
- Measure Your Current Level of Monetization
- Uncover Opportunities for Improving Monetization

Related paths: *Drive Product Growth With Acquisition and Activation* and *Drive Product Growth With Retention and Engagement* (covered as separate .md files in this catalog extraction).

This path contains 3 courses, covered as three parts below:
1. **Understanding the Pillars of Product Growth** (10 min, 2 lessons) — *identical shared course already fully documented in this catalog extraction; see note below.*
2. **Drive Product Growth With Monetization** (44 min, 14 lessons)
3. **Drive Product Growth With Monetization - Assessment** (graded assessment; see note at the end of this document)

---

# Part 1: Understanding the Pillars of Product Growth

This is the exact same shared course ("Understanding the Pillars of Product Growth," 10 minutes, 2 lessons: "The Pillars of Product Growth" and "Your Product's Critical Event and Usage Interval") that opens the *Drive Product Growth With Acquisition* learning path. Its full content — including the complete text of both lessons, the 6-hotspot "Three pillars of digital product growth" interactive diagram, and both embedded videos ("What Is My Critical Event?", 1:51, and "What Is My Product's Usage Interval?", 2:22) — has already been fully transcribed in **`18_Drive_Product_Growth_With_Acquisition.md`** (Part 1 of that document), since it is the same underlying course record on the platform (course slug `understanding-the-pillars-of-product-growth`) and only needs to be documented once. Please refer to that file for the complete text; it is not duplicated here to avoid redundancy, per the platform's own course de-duplication (the course auto-registered as "Complete" for this path as soon as it was completed once).

---

# Part 2: Drive Product Growth With Monetization

**Time commitment:** 44 minutes | 14 lessons across 3 sections

### About this course
Monetization and revenue generation are key outcomes that most companies focus on as part of their long-term growth strategy. How to think about monetization and your strategy for improving it varies based on your products and your organizational goals.

In this course, we'll discuss the importance of monetization for driving long-term growth and how to think about what monetization looks like for your specific product. We'll discuss how to analyze your current baseline monetization metrics with Amplitude and develop goals and strategies for improvement.

**Part 1 - Understand the Importance of Monetization**
- Articulate the importance of monetization for driving long-term growth.
- Determine the key metrics for measuring monetization for your product.
- Check your data taxonomy to ensure you have the relevant events and user properties instrumented.

**Part 2 - Measure Your Current Level of Monetization**
- Discover and verify your conversion path.
- Measure your conversion rate (CVR).
- Collect other key monetization data points (revenue, recurring revenue metrics).

**Part 3 - Uncover Opportunities for Improving Monetization**
- Segment your users.
- Find users that drop off.
- Understand the context throughout the user journey.
- Develop a hypothesis and goals.
- Determine your strategy for achieving your goals.

## Section: Understand the Importance of Monetization

### Lesson 2.1: Understanding Monetization (3 min)

One could argue that monetization is the most important of the three growth pillars of acquisition, retention, and monetization. However, it is often the least invested.

**[Video: "Monetization Overview", duration 2 min 50 sec — Wistia embed, hosted by Amplitude Academy. No transcript is exposed in the underlying page data; per the surrounding text, it covers why monetization is important and the levers available to impact a monetization strategy.]**

### Lesson 2.2: Metrics that Matter (2 min)

Understanding and improving your monetization strategy relies on identifying metrics that matter to monetization. Depending on your instrumentation of Amplitude Analytics, some metrics may be trackable in Amplitude Analytics, while others may only be found outside of Amplitude. This lesson provides an overview of several key monetization metrics: what they are, how to measure them, and why they matter. A reference table lays out three categories:

| Category | Metrics that Matter |
|---|---|
| **Conversion** | Conversion rate (CVR) |
| **Revenue** | Total revenue; Average revenue per paying user (ARPPU)/Average Order Value (AOV); Average revenue per visitor (ARPV)/Average revenue per user (ARPU) |
| **Recurring Revenue** | Monthly Recurring Revenue (MRR); Net Revenue Retention (NRR) |

Detail on each metric (presented as interactive tab cards, each with a Definition and a "Why to measure" list):

**Conversion**
- **Conversion rate (CVR)** — *Definition:* A conversion rate records the percentage of users who have completed a desired action (e.g., going from a free trial to paid subscription, or purchasing an item after viewing an ad). **CVR = # of users completing an action / # of users exposed to the opportunity of completing the action.** *Why to measure:* An effective way of comparing and contrasting the performance of multiple advertising channels; can measure the success of campaigns and reveal which channels are most effective; can be used to set ROI expectations when scaling a campaign; can help spot issues with a product and highlight areas for improvement.

**Revenue**
- **Total revenue** — *Definition:* Total revenue, or Gross Revenue, represents the total income your company generates from selling goods or services before any expenses are deducted. It includes all sources of revenue and provides a macro-level view of your business's overall earnings performance. **Total Revenue = sum of all revenue sources over a specific timeframe.** *Why to measure:* Helps you understand the overall financial performance of your product or service; critical for tracking growth, setting targets, and investment decisions. *(Note callout: You must determine if you need gross or net revenue for your calculations — net revenue removes all refunds, returns, and cancellations from the gross revenue total. The course continues to simply refer to "total revenue" throughout, but use whatever is best for your situation.)*
- **Average revenue per paying user (ARPPU) & average order value (AOV)** — *Definition:* ARPPU is the revenue your company generates per paying user or visitor; AOV is the revenue your company generates per order. Which one matters most may depend on your type of business. **ARPPU = total revenue / # of paying users. AOV = total revenue / # of checkouts.** *Why to measure:* Can inform decision-making by helping you understand which channels, networks, campaigns, and creatives attract the most valuable customers; allows you to understand the characteristics of a paying user so you can get similar ones through lookalike remarketing.
- **Average revenue per visitor (ARPV) & average revenue per user (ARPU)** — *Definition:* the revenue your company generates per visitor/user; ARPV and ARPU are synonymous terms (the course uses ARPV going forward). **ARPV = total revenue / # of unique visitors.** *Why to measure:* See how much value the average user brings to your business; provides a benchmark for making certain product decisions.

**Recurring Revenue**
- **Monthly recurring revenue (MRR)** — *Definition:* measures your predictable, regularly recurring revenue each month. **MRR = # of subscribers × Average monthly revenue per user.** *Why to measure:* Helps build accurate budgets; lets you plan better for the future.
- **Net revenue retention (NRR)** — *Definition:* like user retention, net revenue retention is the revenue you retain over a given period, usually measured monthly. **NRR = MRR at end of time period / MRR at beginning of time period.** *Why to measure:* Indicates how well you are holding on to your existing customer base — if your NRR rate is growing, so is your business.

### Lesson 2.3: Check Your Instrumentation (2 min)

Your ability to calculate and track the metrics that matter to you using Amplitude is highly dependent upon your specific instrumentation. If your Amplitude instance is already instrumented using the Amplitude Browser SDK 2.0 or newer, you likely have all the events and properties you need, as Amplitude's Autocapture is enabled by default and ingests click interactions as two events — *Element clicked* and *Element changed* — each with a predefined set of properties. To track specific user actions and events more precisely, use visual labeling alongside Autocapture.

If you find it difficult to calculate the metrics that matter, you may need to instrument new events or properties. In general, to effectively track your monetization metrics, you need to ensure you have your critical event, onboarding events, the initial value exchange event, all revenue-generating events, conversion path events and properties, activation events and user properties, and UTM source properties instrumented.

Linked resources (button stack):
- **Learn Your Data Taxonomy** (Academy Video) — see this Amplitude Academy video to learn how to identify what events and properties you currently have instrumented.
- **Instrument Events/Properties** (Academy Course) — see this Amplitude Academy course to learn how to instrument more events and properties.
- **Instrument Events with Autocapture** (Academy Course) — see this Amplitude Academy course to learn how to instrument events using Autocapture and visual labeling.

**Instrumentation checklist** (this list is not intended to be exhaustive — use it to help focus on your current instrumentation and determine what work, if any, needs to be done):
- Critical event and event properties
- Activated orgs and activated users properties
- Onboarding events and event properties
- Conversion path events and event properties
- Initial value-exchange event and event properties
- UTM sources and properties
- [Amp] Revenue event
- [Amp] Revenue (Verified) event
- [Amp] Revenue (Unverified) event
- All revenue-generating events and properties

Ensure all revenue-generating events have at least the following properties: *$revenue*, *$price*, *$productId*, *$quantity*, *$revenueType*, *$eventProperties*. (See the Amplitude Documentation Center for more on tracking revenue.)

*Note: If your instrumentation has more than one revenue-generating event (as opposed to one event with separate properties), it may help to create a custom event that combines all revenue-generating events into a single event — useful for calculating net revenue when negative-revenue events are separate from revenue-generating events. (See the Amplitude Documentation Center for more on custom events.)*

### Lesson 2.4: Knowledge Check #1 (1 min, scored)

**Question (Multiple Choice):** Why is it important to check your instrumentation before trying to measure your current monetization strategy performance?
- A better and more complete instrumentation will result in higher monetization and revenue metrics. *(incorrect)*
- **The ability to build charts that track monetization metrics depends on the types of events and properties that are properly instrumented. ← Correct answer**
- Users cannot complete revenue-generating actions in your product until the associated events and properties are instrumented. *(incorrect)*

**Feedback:** The ability to build charts that track most monetization metrics depends on the types of events and properties that are properly instrumented.

## Section: Measure Your Current Level of Monetization

### Lesson 2.5: Discover Your Conversion Path (5 min)

The first step in measuring your current level of monetization is to ensure you have a definitive picture of what the path to making a purchase looks like for your business. Depending on your product, this path may only have two steps, or it may have many steps — it depends on how many steps are required of every customer to make a purchase. Even if you think you know what the path to purchase is, it is best to double-check using Amplitude Analytics' Journeys chart, as there may be elements of the path-to-purchase you are not aware of.

**Case study introduced: *StrutSmart*** — a fictional ecommerce company that sells clothing, shoes, and accessories online and through their mobile app. *StrutSmart* data is used throughout the rest of this course.

After looking at instrumentation, the only revenue-generating event is **Complete Purchase**, representing the moment a customer has paid for their order. The conversion path is comprised of the events every customer making a purchase must trigger. Using the journey map in the Journeys chart, look for paths that end with **Complete Purchase**.

### Optional review accordion
- "Optional: Review how to build and use the Journeys chart" — links to Amplitude Academy (no video/transcript here, text-only guidance link).

Walkthrough (hotspots) to set up the journey map to find *StrutSmart's* conversion path:
1. **Path type.** Since the conversion path ends with a known revenue-generating event, the path type is set to end with the selected event.
2. **Add an event.** Add the revenue-generating event (Complete Purchase) the conversion path is known to end with; filters can be added by event properties if needed.
3. **Edit visible events.** If the journey map is too difficult to read, filter events by hiding/showing specific events, and group events together.
4. **Look for patterns.** Note events that show up repeatedly across multiple paths — some or all may be part of the conversion path. In this view: **Add to Cart, View Cart,** and **Checkout** appear in most paths.
5. **Expand paths further.** Add more paths to the main view, or expand paths further back to see more of an individual path's journey.

It soon becomes apparent that many customers who completed a purchase had to trigger: **Add to Cart, View Cart, Checkout,** and **Complete Purchase**. But did all of them need to? Once you think you've identified your conversion path, think critically: are there other ways users can trigger the revenue-generating event(s)? Did all users who triggered the revenue-generating event have to trigger ALL events in the path? If there are multiple revenue-generating events, did you explore and compare the paths leading to each?

To test this, the instructor adds the starting event (**Add to Cart**) and ending event (**Complete Purchase**) and looks for paths *between* those two events that do NOT include **View Cart** and **Checkout**. Result: it turns out there must be a way to complete a purchase without triggering View Cart and/or Checkout. **This means the real conversion path regarding monetization is Add to Cart and Complete Purchase.** Some customers may trigger events before or between these two, but they represent the generic path that must be taken to buy something from StrutSmart.

### Your turn! (reflection prompt, not graded)
What is your conversion path? Before moving forward, identify a potential conversion path for your product (to be used throughout the rest of the course). Questions to ask:
- What is the revenue-generating event(s)?
- Are there multiple ways users can trigger the revenue-generating event(s)?
- Do all users who ultimately trigger the revenue-generating event(s) have to trigger ALL events in the path found?
- If there are multiple revenue-generating events, did you explore the paths leading to each and compare them?

*(Links to a shared Amplitude demo chart for personal reflection — not part of the extractable course content.)*

### Lesson 2.6: Measure Your Conversion Rate (3 min)

Once you know your conversion path, you can measure your conversion rate (CVR) using Funnel Analysis.

### Optional review video
- **"Build a Funnel Analysis Chart"** — 4 min 41 sec video (Wistia). Description: "Optional: Review how to build a funnel analysis chart." No transcript exposed.

*Note: If you have multiple revenue-generating events (e.g., "Buy Now" and "Checkout"), you can create a custom event that combines all revenue-generating events into one, then use it to measure overall conversion. Similarly, you can look at conversion for all revenue-generating events in the funnel by combining events inline. (See Amplitude Docs on Custom Events and Combining Events Inline.)*

Walkthrough (hotspots) to calculate CVR in Amplitude Analytics:
1. **Add events.** Add all events of the conversion path; specify if the path should be *this order*, *any order*, or *exact order*.
2. **Add logic clauses to events.** For more nuanced paths, combine events inline, mark an event as optional, or compare events within the funnel.
3. **Specify a conversion window.** Select an appropriate conversion window — changing the window impacts the total conversion rate, so capture conversions in the timeframe that matters most.
4. **View total CVR.** For funnels with more than 2 steps, this can be changed to a takeaway showing the largest drop-off step or the slowest conversion step.
5. **Save the chart.** Save and add to a dashboard to keep track of CVR.

Result: **StrutSmart's CVR for completing the path Add to Cart → Complete Purchase within 12 hours over the last 30 days is 22.7%.** To continue monitoring and improving monetization strategy, this chart (and others built in this course) should be saved and added to a dashboard.

### Your turn! (reflection prompt, not graded)
What is your CVR? Use the conversion path found in the last lesson and build your own Funnel Analysis chart to measure CVR over the last 30 days; save the chart and add it to a dashboard.

### Lesson 2.7: Collect Other Data Points (6 min)

After finding your conversion path and calculating CVR, collect data points for the other monetization metrics that matter: total revenue, AOV, ARPPU, ARPV/ARPU, MRR, or NRR. Exactly how to calculate each metric in Amplitude is unique to your organization and dependent on your instrumented events/properties.

*Note: For each chart below, since daily values over the last 30 days are being viewed, selecting **Average Value** from the takeaway dropdown displays the average daily value. Since the goal is average monthly values, **Overall Value** is used instead — it provides the average value for the entire 30-day range, including repeat business from individual customers throughout that time.*

**Revenue** (process cards, each numbered steps + resulting StrutSmart figure):
- **Total revenue:** (1) Add revenue-generating event(s), group by *$revenue*. (2) Measure as Sum of Property Value. (3) Change takeaway metric from Current Value to Overall Value. (4) Relabel y-axis "Total Revenue." (5) Save chart to dashboard. **Result: total revenue over the last 30 days is $13.9M.**
- **Average order value (AOV):** (1) Add revenue-generating event(s) twice — group instance A by $revenue, leave instance B alone. (2) Add a formula: PROPSUM(A) / TOTALS(B). (3) Change takeaway to Overall Value. (4) Relabel y-axis "Average Order Value." (5) Save to dashboard. **Result: AOV for the last 30 days is $81.70.**
- **Average revenue per paying user (ARPPU):** (1) Add revenue-generating event(s) twice — group instance A by $revenue, leave instance B alone. (2) Add formula: PROPSUM(A) / UNIQUES(B). (3) Change takeaway to Overall Value. (4) Relabel y-axis "Average Revenue Per Paying User." (5) Save to dashboard. **Result: ARPPU for the last 30 days is $176.**
- **Average revenue per visitor (ARPV):** (1) Add revenue-generating event (A), group by $revenue. (2) Add "Any active event" (B) to represent active visitors. (3) Add formula: PROPSUM(A) / UNIQUES(B). (4) Change takeaway to Overall Value. (5) Relabel y-axis "Average Revenue Per Visitor." (6) Save to dashboard. **Result: ARPV for the last 30 days is $39.70.**

*Note: total revenue can be used in conjunction with other metrics for further insights — e.g., a flat ARPU with rising total revenue may signal a growing user base, while rising ARPU with flat total revenue may signal user churn or market saturation.*

*Note: custom metrics can be saved for each of these to make re-creating or building new charts easier — see Amplitude Academy's "Track Business Goals with Metrics" course.*

**Recurring revenue:**
- **Monthly recurring revenue (MRR):** (1) Select revenue-generating event, narrowed to recurring revenue events only (e.g., filtered by *revenueType* = *subscription income*). (2) Measure as Sum of Property Value ($revenue). (3) Set date picker to last 30 days. (4) Change takeaway to Overall Value. (5) Relabel y-axis "Recurring Revenue." (6) Save to dashboard. **Result: MRR for the last 30 days is $13.4M.**
- **Net revenue retention (NRR):** Starting from the MRR chart: (1) Click Compare dropdown, select previous month. (2) Select percent option to see MRR change as a percentage from the previous month. (3) Relabel y-axis "Percent Change in Net Retention Revenue." (4) Save as a new chart (to not lose the MRR chart) and add to dashboard. **Result: percent change of MRR over the last 30 days is 2.77%, so NRR = 2.77% + 100% = 102.77%.**

### Your turn! (reflection prompt, not graded)
Which metrics matter to you? A linked sample notebook provides example charts built for a fictional media streaming company capturing each metric from this and the previous lesson. Which will you track? What other metrics do you need? An org admin can copy the notebook to your org, or you can recreate each chart from scratch with your own data.

### Lesson 2.8: Knowledge Check #2 (2 min, scored — two questions)

**Question 1 (Multiple Response — select all that apply):** Why should you use the Journeys chart to identify your path-to-purchase?
- **You may discover elements of a path you were not aware of by building a journey map. ← Correct**
- **The Journeys chart allows you to choose how to look at paths (using a starting event, ending event, or by looking at paths between events), letting you identify paths ALL users must take to make a purchase. ← Correct**
- The journey map and pathfinder explicitly tell you what your conversion path is for all users. *(incorrect)*

**Feedback:** The Journeys chart allows you to: discover elements of a path you were not aware of by building a journey map; choose how to look at paths (using a starting or ending event, or looking at paths between events), letting you identify paths ALL users must take to make a purchase.

**Question 2 (Matching):** Match the metric with its generic calculation.
| Metric | Correct calculation match |
|---|---|
| CVR (Conversion Rate) | # of users doing an action / # of users exposed to the opportunity of doing the action |
| AOV (Average Order Value) | total revenue / # of checkouts |
| ARPPU (Average Revenue per Paying User) | total revenue / # of paying users |
| ARPV (Average Revenue per Visitor) | total revenue / # of unique visitors |
| MRR (Monthly Recurring Revenue) | # of subscribers × Average monthly revenue per user |
| NRR (Net Revenue Retention) | MRR at end of time period / MRR at beginning of time period |

**Feedback:** CVR = # of users doing an action / # of users exposed to the opportunity of doing the action. AOV = total revenue / # of checkouts. ARPPU = total revenue / # of paying users. ARPV = total revenue / # of unique visitors. MRR = # of subscribers × Average monthly revenue per user. NRR = MRR at end of time period / MRR at beginning of time period.

*(Note: in the raw course data, only the first three answer rows carry an explicit `correct: true` flag while the latter three carry `correct: false` — this is almost certainly a data-entry quirk of this particular matching-exercise format rather than a meaningful signal, since a matching exercise's "answer key" is the pairing itself, and the feedback text confirms all six pairings shown above as correct.)*

## Section: Uncover Opportunities for Improving Monetization

### Lesson 2.9: Segment Your Users (4 min)

Now that you have a baseline for measuring your monetization program, you can strategize on how to improve it — by digging into your data to understand how, when, and why customers are buying, so you can get them coming back for more. One strategy: go through the metrics already calculated and group segments of users in various ways — compare segments already tracked, or group users by various user properties to see how different populations compare and what impact they have on the overall metric.

**Suggested properties to group users by** (accordion): Geographic locations, Platform types, Operating system, Device types, Plan or account type, UTM source, Any other user properties you have instrumented.

**StrutSmart example:** Grouping the AOV chart by UTM source shows customers from **Instagram and Facebook have the highest AOVs**. Orders from users who navigate directly to the site average about half the value of those from Instagram — an opportunity to improve recommendations for direct-navigation users. Changing the segmentation chart to count only unique instances of Complete Purchase, grouped by UTM source, shows the channel with the highest *volume* of orders is direct navigation, but the channel with the highest *value* (orders × AOV) is Instagram — prompting further investigation into what makes Instagram customers spend more (targeting? user behavior?) and whether that can be replicated in other channels.

### Lesson 2.10: Find Users That Drop Off (4 min)

One way to understand customers is by identifying who doesn't complete the conversion funnel, then hypothesizing why based on observations. The easiest way: create a cohort from the CVR chart of all customers who dropped off the conversion path.

Walkthrough (process cards):
1. **Go to CVR chart.**
2. **Create cohort of drop-offs.** Click the top section of the 2nd funnel step (users who dropped off) to open Microscope, then click Create Cohort and save. This cohort holds all users who completed step 1 but dropped off before completing step 2 within the conversion window.
3. **Create cohort of conversions.** Also create a cohort of users who completed the conversion path, for potential future use.

*Note: most cohorts created via Microscope are static; cohorts created from a basic funnel analysis are behavioral. (See Amplitude Docs on creating cohorts via Microscope.)*

**StrutSmart example continued:** Grouping the CVR chart's segment by UTM source shows customers who don't complete the conversion path in 12 hours most frequently come from **Bing, Twitter, and directly from the site**, while Instagram and Facebook users convert more frequently — aligning with the AOV-by-UTM-source finding from the previous lesson.

*Note: another way to look at conversion is CVR for returning customers — add an "Event Historical Count ≠ 1" filter to each funnel event.*

**User Composition chart** (hotspot walkthrough) — investigating segments and cohorts:
1. **Select property for composition.** UTM source selected, continuing the UTM source investigation.
2. **Add cohorts and segments.** Added the cohort who completed the conversion path and the cohort who did not complete it within 12 hours, to highlight differences.
3. **Change the chart view.** Switch to bar chart view to see percentage shifts of each user property type between cohorts.

Result: while the Funnel showed Bing and Twitter had the lowest conversion rates, the User Composition chart shows **Google has the largest shift in the percentage of customers who drop off versus those who convert** — a greater proportion of non-converting customers come from Google than converting customers. This suggests something about Google as a UTM source worth investigating, ideally to even out the distribution so drop-off and conversion proportions match per source.

### Optional review video
- **"Build a User Composition chart"** — 3 min 46 sec video (Wistia). Description: "Optional: Review how to use the User Composition chart." No transcript exposed.

### Your turn! (reflection prompt, not graded)
Improving monetization means improving your CVR. Questions to consider: Who drops off? Who converts? How do customers who completed purchases compare to those who did not? Make cohorts and explore differences with a User Composition or Segmentation chart.

### Lesson 2.11: Understand the Context Throughout the User Journey (4 min)

Looking at CVR of various segments/cohorts can only tell you so much — to understand *why* customers take the actions they do, explore the larger customer journey via the **Journeys chart** (pathfinder and journey map views). The course already used a journey map to discover the conversion path; now it builds one to analyze what users did while on the path to conversion.

*Note: journey maps are also accessible via Microscope in the Funnel Analysis chart, but the Journeys chart offers more functionality for deeper exploration.*

**Building the journey map** (process steps):
1. Add starting and ending events to find paths between the two.
2. Filter for events, exclude events, expand by event properties as needed.
3. Adjust the conversion window as needed.
4. Add a user segment to dig into a specific population — the cohort of users who dropped off in the first 12 hours, to see what their paths looked like.
5. Toggle between **Converted** and **Dropped Off** to understand the differences.

As journeys are explored, the instructor looks for a place where users get stuck (payment failures? page errors?). **Viewing more paths** reveals: some experienced a "promo code failure," quite a few kept adding recommended items to their carts but did not check out, and others ended their session at various points. This raises the question of how many non-converters (within the original window) eventually completed a purchase — prompting a conversion-window edit.

Expanding the window (to 1 day, then 5, then 10 days) and toggling to the "converted" journey map: many more people converted outside the original window (converting users went from 0 to nearly 14,000). The large portion of users who kept adding items to their cart eventually converted **after 4 days 19 hours**. This suggests the original conversion window for CVR should be reconsidered (to be discussed with the team) — and raises the question of whether something can be done to get customers converting *sooner*.

**Time to Convert graph** (process): to compare earliest vs. latest converters: (1) switch Funnel chart from measuring Conversion to Time to Convert; (2) increase window to 30 days; (3) set uniform 0.5-day buckets from 0–30 days; (4) open Microscope, create a cohort of customers who converted after 30 days. Result: the median conversion window over 30 days is nearly **4 days 22 hours** — closely matching the 4 days 19 hours average seen in the journey map. The goal is to bring these numbers down so customers complete purchases earlier.

With the "converted after 30 days" cohort and the "converted after 12 hours" cohort, the instructor could compare their Journeys paths to understand why some customers delay so long (do they keep shopping but not check out? not revisit their cart for days/weeks? wait for new promo codes?) — but first wants to know what drives customers from different UTM sources to convert quickly vs. after 30 days, covered in the next lesson.

### Your turn! (reflection prompt, not graded)
Build journey maps for your segments/cohorts to see what they did before converting or dropping off; adjust conversion windows to compare fast vs. slow converters. Questions: Do drop-off customers get stuck at a payment page or sign-in step? Where do people get stuck? What do they do before they drop / before they convert? How do the fastest conversion paths compare to the slowest? What journey types lead to first-time (or repeat) purchases?

### Lesson 2.12: Develop Your Hypothesis and Goals (4 min)

Time to develop a hypothesis around what is impacting the observed data and set goals. When it's unclear why a customer does or doesn't trigger a certain event, Amplitude's **conversion drivers** tool (accessible only via the Funnel Analysis chart) can help — it automatically sorts, aggregates, and analyzes all events occurring for each user between two funnel steps, identifying which actions most strongly correlate with the outcome (completing the funnel or not).

*Note: correlation does not equal causation — a strong correlation between an event and completing a purchase does not mean that event caused the purchase. Targeted experiments are needed to fully understand causation, but correlation data can still help draw logical conclusions and give ideas for next steps.*

**Setup:** Build a funnel viewing only (a) customers who converted in the first 12 hours plus those who did not convert at all, and (b) customers who converted after 30 days plus those who did not convert at all (after saving a cohort of non-converters-after-30-days).

*Note: the "converted after 30 days" cohort is very small (less than 1% of all users who entered the funnel) — be wary of strong conclusions from this group alone; it's used for ideas to help the entire customer base.*

Walkthrough (hotspots):
1. **Add events** — the conversion path events.
2. **Check the conversion window** — should match the largest conversion window across any cohorts added to a segment.
3. **Add segments and cohorts** — segment 1: converted-within-12-hours + all-non-converters; segment 2: converted-after-30-days + all-non-converters.
4. **Explore conversion drivers** — click a section of the funnel's final step; starts with those who converted within the 12-hour window.

*Note: session replays of converters and non-converters can also provide anecdotal contextual data.*

**Conversion drivers analysis** (process cards):
1. **Driving conversion in 12 hours:** Top 3 correlating events: **View Checkout Recommended Item (+0.33), Add Shipping Info (+0.21), Promo Code Applied (+0.16)**. Add Shipping Info is disregarded as something most purchasers would do regardless (correlation ≠ causation); the other two warrant further analysis.
2. **Expand by property:** Expanding "View Checkout Recommended Item" by UTM source — Instagram has the strongest correlation (+0.18, technically a "weak positive"), with other sources slightly lower. UTM source wasn't a huge factor once accounting for viewing recommendations, but some sources performed better. Improving recommendations during checkout (or in ads) might increase completed checkouts if recommendations are good enough.
3. **Expand by property (continued):** Same pattern for "Promo Code Applied" by UTM source — Instagram highest, others declining. A well-timed promo code might push a hesitant user to complete a purchase.
4. **Driving conversion after 30 days:** Users converting after 30 days appear to do more research (reading reviews, ratings, item pictures, viewing recommendations) regardless of UTM source, and are slightly influenced by push notifications. Possible actions: improve display of reviews/ratings/recommendations; check cart-reminder push notification timing/optimization.

**Goals set for StrutSmart:**
- Increase the 12-hour CVR by 2% over the next 30 days, with a focus on users from Google and those who come directly to the site.
- Decrease the median overall time-to-convert in a 30-day window from 4 days 22 hours to less than 4 days 12 hours.
- Increase AOV for users who navigate directly to StrutSmart by 8%.

### Your turn! (reflection prompt, not graded)
Use conversion drivers to identify levers to improve monetization strategy — remembering correlation ≠ causation. Questions: What impacted their buying decision? How does merchandising affect conversion (what are people searching for but not finding, or wanting but out of stock)? How do previous analyses relate to one another for certain user segments?

### Lesson 2.13: Determine Your Strategy for Achieving Your Goals (3 min)

The prior lessons generated a lot of information and ideas for optimizing StrutSmart's monetization strategy; next steps depend on available resources, tools, and time.

### Amplitude tools (interactive tabs — identical content to the equivalent section in the Acquisition course, reproduced here in full)
- **Amplitude Web Experimentation:** Run A/B, multivariate, and multi-armed bandit experiments on webpages using a visual editor, with no new code. **Try if:** your data insights suggest changes in copy, images, colors, and other HTML elements on webpages might increase a user's engagement.
- **Amplitude Feature Experimentation:** Run A/B, multivariate, and multi-armed bandit experiments using feature flags. **Try if:** your data insights suggest you need to improve critical paths in your mobile or desktop application (not a webpage or corporate website), or you need a controlled rollout of a new feature/experience.
- **Amplitude Guides and Surveys:** Deliver timely, targeted in-product messages to drive adoption, engagement, and retention. **Try if:** your data insights suggest users would benefit from an in-product nudge or just-in-time information, or you want to collect timely direct feedback.
- **Cohort Syncing:** Send behavioral cohorts created in Amplitude to downstream destinations at a one-time or recurring cadence. **Try if:** your data insights suggest distinct groups of users behave differently, and you have downstream marketing/engagement platforms connected to Amplitude.

*(A downloadable "Amplitude Academy Download" summary PDF button links to https://academy.amplitude.com/take-action-on-your-data-insights — external resource, not part of the extractable course content.)*

### Determine your strategy — StrutSmart's goals-to-strategy table

| Goals | Strategies | Rationale |
|---|---|---|
| Increase the 12-hour CVR by 2% over the next 30 days, focused on Google and direct-navigation users. Decrease median overall time-to-convert in a 30-day window from 4 days 22 hours to less than 4 days 12 hours. | Send promo codes valid only for a few hours/days to customers who keep items in their cart longer than 10 hours. Include ratings and high-level reviews in targeted ads across UTM sources to encourage quicker buying decisions. Optimize the timing of push notifications and cart reminders to encourage earlier conversion without overwhelming or annoying customers. | If successful, median overall time-to-convert will decrease, hopefully causing the 12-hour CVR to increase. |
| Increase AOV for users who navigate directly to StrutSmart by 8%. | Optimize recommendation engines for direct-navigation users to target them more individually with more meaningful suggestions. Include optimized recommendations in cart-reminder push notifications. | More meaningful suggestions should cause customers to add items to their cart they might otherwise have omitted, increasing AOV. |

If you've generated goals for product improvement, marketing strategies, or personalized experiences, you have choices for how to act:
- Ideally, **methodically build and run experiments** to test new experiences and pinpoint exactly which changes drive the best results — Amplitude Experiment (or, for web products, Amplitude Web Experimentation) is a good tool for this.
- If explicit experimentation isn't available, **create feature flags for specific customer segments and track performance** with Amplitude Analytics.
- Build **target audiences** based on user properties and **sync those audiences to downstream destinations** like messaging campaigns or targeted marketing channels.
- Use **Amplitude Guides and Surveys** with target audiences to nudge them or gather feedback.

Most strategies boil down to creating a more personalized customer experience — tailoring experiences/communications so customers find what they need when they need it. Ways to do this:
- Rewards and exclusive offers tailored to a user's specific interests using past purchase data
- Product recommendations relevant to the individual consumer based on demographics and history
- Subscriptions tailored to the needs and interests of a unique customer
- Personalized push notifications on mobile apps, delivered at the most relevant time for each user
- Biometric recognition in physical stores that identifies customers on arrival, educating staff on their unique preferences

It is up to you to do the research, analysis, and testing to determine what your customers actually need to become (and continue to be) paying customers.

### Your turn! (reflection prompt, not graded)
Take the goals set in the previous lesson and determine strategies to try to meet them.

### Lesson 2.14: What's Next? (1 min)

Once you have determined your strategy, it is time to implement it and monitor progress. Ensure you have a dashboard or notebook set up to track the metrics that matter, including other important charts and notes that tell the story seen in the data, and confirm the changes you're making are having the intended effect on monetization levels.

Also be aware of what impacts your monetization initiatives might have on your acquisition and retention programs, and vice versa — then start the cycle of continuously improving your monetization strategy.

### Thanks for taking this course!
You've reached the end of *Drive Product Growth With Monetization*. Click "Return to Learning Path" to complete this course and continue along the learning path.

---

# Part 3: Drive Product Growth With Monetization - Assessment

**Course 3 of 3** in the Drive Product Growth With Monetization learning path.

"Take this assessment to complete the Drive Product Growth With Monetization learning path."

**Access note:** As with the corresponding assessment in the Drive Product Growth With Acquisition path, this course is individually registration-gated behind full, in-platform sequential completion of Part 2 above (all 14 lessons, including watching each embedded video — "Monetization Overview" 2:50, "Build a Funnel Analysis Chart" 4:41, "Build a User Composition chart" 3:46 — to completion and satisfying each "Complete the content above before moving on" gate in the live player, plus correctly answering both embedded, scored Knowledge Checks along the way). All of Part 2's substantive content — including both inline scored knowledge checks (with correct answers and full feedback text reproduced above, extracted directly from the underlying course-data JSON) — was fully captured via the underlying course-data API, independent of the platform's own lesson-completion/progress tracking. Because unlocking this assessment course requires real-time sequential playthrough of Part 2 purely to satisfy the platform's own progress gating (not to access any new content, all of which has already been captured), the assessment course's own item bank was not reachable within this extraction session. Given its description ("Take this assessment to complete the...learning path"), it most likely re-tests comprehension of the material already fully documented in Parts 1–2 of this document, consistent with the pattern observed for the equivalent Acquisition-path assessment.

---

## Combined Path Summary

This learning path ("Drive Product Growth With Monetization," ~55 minutes total) is the second of the three parallel "Drive Product Growth" paths in this catalog, sharing Part 1's foundational acquisition/retention/monetization framework with the Acquisition and Retention & Engagement paths. Part 2 is the practical core: it treats monetization as the natural third leg of the growth stool after acquisition and retention, opening with a taxonomy of monetization metrics (conversion, revenue, and recurring-revenue categories — CVR, total revenue, AOV, ARPPU, ARPV, MRR, NRR — each with its own formula and rationale) before walking through the full analytics workflow using a single running fictional case study, the ecommerce company **StrutSmart**: first verifying the true conversion path with a Journeys map (discovering that "Add to Cart → Complete Purchase" is the real, minimal path, not the longer apparent one), then measuring CVR with Funnel Analysis (22.7% within 12 hours), then collecting the remaining revenue metrics with Segmentation charts. The path's most distinctive contribution relative to the Acquisition course is its "Uncover Opportunities" section, which layers segmentation (AOV and CVR by UTM source), cohort-building from funnel drop-off/conversion, User Composition analysis, and — most notably — the **conversion drivers** tool (with its explicit correlation-≠-causation caveat) and extended-conversion-window journey analysis (discovering that a large cohort of "lost" customers actually convert after ~4 days 19 hours–22 hours, prompting a conversion-window policy question) to build a genuinely data-driven hypothesis. It closes, like the Acquisition path, by mapping StrutSmart's resulting goals to concrete tactics and Amplitude's action-layer tooling (Experimentation, feature flags, Cohort Syncing, Guides and Surveys) in an explicit goals/strategies/rationale table — the same insight-to-action template partners can reuse for their own customers' monetization funnels. Part 3, a graded assessment gating official path completion, could not be extracted directly due to the platform's sequential-unlock requirements as detailed above, but its content is expected to test the same material fully documented in Parts 1–2.
