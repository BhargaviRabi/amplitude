# Adobe Migration Implementation Enablement

**Type:** On-demand course | **Time commitment:** 50 minutes (45 min main lesson + 5 min scenario quiz)

*Note: this course required a "checkout"/enrollment step (a free enrollment flow, not a paid purchase) via a "Get started" button before the lesson content became accessible — unlike every other course in this catalog, which was accessible directly. This was completed to access and extract the course content below.*

---

## About This Course

This course will cover how to implement Amplitude for a customer migrating off of Adobe. This course is designed to help Professional Services roles to:
- Explain how the implementation process differs slightly for Adobe migrations
- Explain the key differences between Adobe and Amplitude, including recognizing terminology for similar features or concepts
- Adapt each implementation phase (kickoff, scope, send in data, and rollout) for an Adobe migration
- Implement Amplitude Analytics for a customer migrating off of Adobe

*Note: the course page mentions "Looking for the slide deck? Check your partner resource area (Highspot for resellers; Gdrive folder for Solution Partners.)" — an external, account-gated resource not accessible/reproducible here.*

---

## Lesson: Migration Framework (6 min)

**[Video embedded, 6 min]** — no transcript exposed. Based on the course's overall structure (which proceeds directly into phase-specific "Migration Callouts" for Kickoff & Scope, Send in Data, and Rollout), this video is expected to introduce the overall framework for how a standard Amplitude implementation is adapted specifically for an Adobe migration scenario.

## Lesson: Migration Callouts: Kickoff & Scope (12 min)

**[Video embedded, 12 min]** — no transcript exposed.

**Session/Page View-Based vs. Event-Based.** Born out of the website era, marketing analytics vendors captured unique visitors, visits, and page views by default. While there were always events within those page views and sessions, the architecture was built around pages loading and sessions (typically lasting until 30 minutes of consecutive inactivity). This model first encountered challenges when organizations began deploying single-page applications (SPAs) — marketing analytics vendors had to create workarounds to account for activity within page views. Product analytics tools have traditionally had an event-based model that worked in the app or website paradigm; this model made sense to product teams that like to track many customer actions, many of which take place between page views, and product teams tended to desire a deeper level of granularity than their marketing counterparts. Some intra-page interactions (filters, product image hovers, etc.) might be better suited for event-based tracking vs. page-based tracking.

**What Adobe Customers Are Used To (reference table, reproduced in full):**

| Adobe Concept | Notes |
|---|---|
| Typical Industries | Retail, e-commerce, media |
| Visits ("Sessions") / Session Metrics | Adobe treats sessions as a 1st party element so that all reports, cohorts, and properties can be viewed at the session level (Bounce Rate, Entry Rate, Exit Rate) |
| Page Views / Landing Page Conversion | Particularly relevant in e-commerce and media industries; also used for B2B lead capture — marketing campaigns to "squeeze" pages |
| User Segments | Works similarly to Amplitude's Cohorts |
| Marketing Campaign & Channel Set Up | Adobe has a Channel rule builder feature similar to Amplitude's Channel Classifiers |
| Virtual Report Suites | Works opposite of Amplitude Portfolio Views, where different child views are created from one parent project (virtual report suites can be turned into Amplitude projects if necessary — see quiz feedback below) |

**Key Callouts for KPI Alignment & Scoping for Adobe Migrations:**
- Identify key Adobe metrics currently relied on for business reporting (e.g. Visits, Unique Visitors, Revenue, Entries, Exits, Downloads, etc.).
- Differentiate between migration requirements vs. net new value, to highlight Amplitude capability value-adds (e.g. Journeys, Conversion Drivers, etc.).

**Key Callouts for Engineering Kickoffs for Adobe Migrations:**
- Amplitude makes it easy to instrument for both client- and server-side data sources — Amplitude will work with the partner/customer to ensure a plan exists for all initial data sources.
- Amplitude has different ways of defining Unique Users and User Sessions compared to Adobe — Amplitude will help the customer understand the differences and make the best decision on how to define these, to ensure data confidence and integrity.

## Lesson: Migration Callouts: Send in Data (12 min)

**[Video embedded, 12 min]** — no transcript exposed.

**What Adobe Customers Are Used To (reference table, reproduced in full):**

| Category | Notes |
|---|---|
| Tag Management System | Adobe Tag Manager; Adobe Launch — the Extension is fine for exploring initial data, but not recommended as a primary instrumentation source; Tealium — not updated to the latest SDK version |
| Solution Design Reference Document | Spreadsheet/blueprint for data collection & tracking requirements — may be outdated or not heavily used across the organization |
| Data Augmentation Tools | (SAINT) Classifications → maps to Amplitude's Derived Properties, Lookup Tables |

**Key Adobe Migration Callouts:**
- **For Taxonomy Planning:** there is the option to translate elements of the customer's Adobe Solution Design Reference into an initial Amplitude taxonomy, to take advantage of existing work and knowledge.
- **For Data QA:** the customer may want to see that key metrics have minimal discrepancies between platforms (e.g. Visits, Unique Visitors, specific Hits totals) — Amplitude will work with them within reason to get as close to parity as possible.

## Lesson: Migration Callouts: Rollout (10 min)

**[Video embedded, 10 min]** — no transcript exposed.

**What Adobe Admins Are Used to Doing (reference table, reproduced in full):**

| Category | Notes |
|---|---|
| Siloed Reporting and Hard to Teach Casual Users | A specialized team who knows Adobe well, but it's hard to teach, self-service, and out-of-the-box for casual users; difficult to collaborate and share reports, with limited content hierarchy |
| Analysis Workspace | Analysis Workspace serves as a single, robust interface for every analysis; typical workflow is to start with Analysis Workspace with the option of adding more visualizations |
| Limited Data Governance | Typically partner with an outside vendor/consultant to alleviate data issues; difficulty in managing the same analytics objects (Calculated Metrics and segments) |

## Lesson: Summary / Adobe Migration Success Stories (3 min)

**[Video embedded, 3 min]** — no transcript exposed. Based on the lesson title, this closing video is expected to summarize the course and present real customer success stories from prior Adobe-to-Amplitude migrations.

## Lesson: Scenario Questions (Check your understanding) — separately-rendered quiz (5 min, 7 questions, 100% required to pass)

*This quiz required taking it live (not pre-completed) and required a 100% score to pass, with a "Show Answers" review only available after passing. It was completed across three attempts (57% → 85% → 100%) to determine the correct answer for every question; all seven are reproduced below with their exact feedback text.*

**Q1. An organization is migrating from Adobe Analytics to Amplitude. During the implementation kickoff, they request to start by replicating their existing Adobe data model and metrics. Based on best practices for Adobe migrations, what is the most appropriate response?**
- ☐ Agree to replicate the Adobe model exactly in Amplitude to ensure continuity.
- ☑ **(correct)** Explain that starting fresh with a focus on business use cases and KPIs will optimize their Amplitude implementation.
- ☐ Recommend using Amplitude's Launch integration exclusively for all data collection tasks.

*Feedback: this is especially true if part of the reason the customer is switching to Amplitude is because their Adobe implementation is messy. At a minimum, even if they want to do a more direct replication, they're likely to be able to cut half of what they track in Adobe that they never use. Note, however, if the client insists on replicating the Adobe model, you should accommodate that.*

**Q2. An Adobe migration client wants to import their historical Adobe Analytics data into Amplitude. How should you address this request?**
- ☐ Suggest a direct bulk upload of all historical Adobe data into Amplitude without translation.
- ☑ **(correct)** Propose translating key Adobe metrics into Amplitude's taxonomy and importing only relevant historical data.
- ☐ Recommend against importing any historical data to encourage a fresh start.

*Feedback: translating key Adobe metrics ensures that imported data aligns with Amplitude's event-based model, making it both relevant and actionable.*

**Q3. An Adobe user asks about how "virtual report suites" map to Amplitude. What is the best explanation you can provide?**
- ☐ Virtual report suites are directly equivalent to Amplitude's projects.
- ☑ **(correct)** Virtual report suites resemble Amplitude's saved segments or dashboards, which can filter data dynamically.
- ☐ Virtual report suites are similar to Amplitude's cohorts, which filter users.

*Feedback: Amplitude's saved segments and dashboards offer similar functionality to Adobe's virtual report suites, allowing for dynamic data filtering and tailored insights. Note that virtual report suites can be turned into Amplitude projects if necessary — first find out how the customer is using virtual report suites before making a firm recommendation.*

**Q4. During training, a user mentions bounce rates, a common metric in Adobe. How would you explain its calculation in Amplitude?**
- ☐ Bounce rate in Amplitude is identical to Adobe's bounce rate and requires no adjustments.
- ☑ **(correct)** Amplitude calculates bounce rates as the count of sessions with a single page view event / total sessions.
- ☐ Amplitude does not track bounce rates as it focuses solely on events.

*Feedback: Amplitude defines bounce rate as the percentage of sessions with only one event, aligning with its event-based structure and offering actionable insights.*

**Q5. During the kickoff phase of an Adobe migration, the client wants to start by identifying every metric and report they currently use in Adobe Analytics. What should you recommend to ensure a smooth scope and kickoff process?**
- ☑ **(correct)** Focus on understanding the client's top business questions and priorities, then align their metrics to these needs.
- ☐ Agree to replicate all existing Adobe metrics and reports to maintain continuity for the client.
- ☐ Advise the client to discard their current metrics and start completely fresh in Amplitude.

*Feedback: focusing on the client's top business questions ensures that the migration is aligned with their priorities, allowing for a meaningful and efficient implementation.*

**Q6. During the "send in data" phase, the client wants to rely entirely on their Adobe Launch integration to send data into Amplitude. What should you recommend?**
- ☐ Discourage using Launch altogether and require rebuilding all data collection from scratch.
- ☑ **(correct)** Use Launch only for initial exploration, then transition to Amplitude's SDKs and APIs for data collection.
- ☐ Rely exclusively on Launch, as it ensures a smoother migration from Adobe.

*Feedback: using Launch for initial exploration is a practical approach, but transitioning to Amplitude's SDKs maximizes scalability and long-term efficiency.*

**Q7. In the rollout phase, a client accustomed to Adobe asks why there are no virtual report suites in Amplitude. How do you respond?**
- ☑ **(correct)** Explain that Amplitude uses projects and saved segments to provide comparable functionality.
- ☐ Recommend creating new virtual report suites within Amplitude to match Adobe.
- ☐ Advise the client to avoid segmenting data in Amplitude entirely.

*Feedback: projects and saved segments in Amplitude offer a flexible alternative to Adobe's virtual report suites, aligning with Amplitude's event-based model.*

## Lesson: Course feedback (optional)

Standard optional feedback survey lesson — not course content.

---

## Summary / Explanation

This course is a specialized addendum to the main Implementing Amplitude Analytics methodology, aimed specifically at partners handling customers who are migrating away from Adobe Analytics (or Adobe Experience Cloud more broadly) rather than implementing Amplitude fresh. Its throughline, reinforced across every quiz question, is a deliberate rejection of "lift and shift": rather than replicating Adobe's data model, metrics, and reports one-to-one, the recommended approach is to use the migration as an opportunity to refocus on business use cases and KPIs (echoing the KPI-first philosophy taught in IMPL-2 of the main path), while still respecting client requests to replicate Adobe's model when they insist. The course maps several Adobe-specific concepts onto their nearest Amplitude equivalents: Adobe's session/page-view-based architecture (born from the website era) contrasts with Amplitude's event-based model, which better suits granular product-team tracking; Adobe's Virtual Report Suites map loosely onto Amplitude's saved segments/dashboards for dynamic filtering (and can be converted into full Amplitude projects when appropriate, though the recommended first step is always to understand how the customer actually uses their virtual report suites before prescribing a specific Amplitude equivalent); Adobe's (SAINT) Classifications map onto Amplitude's Derived Properties and Lookup Tables; and bounce rate, ported directly, is redefined as the percentage of sessions containing only a single event. On the technical side, the course gives a clear staged recommendation for Adobe Launch: useful for initial data exploration, but partners should guide customers toward Amplitude's own SDKs and APIs as the primary, scalable instrumentation source rather than relying on Launch indefinitely. Across the kickoff/scope, send-in-data, and rollout phases, the course consistently frames Adobe-experienced stakeholders' assumptions (their existing Solution Design Reference document, their trained-up specialist Adobe admin team, their familiarity with Analysis Workspace) as a starting point for translation and education, rather than as a target for literal replication in Amplitude.

