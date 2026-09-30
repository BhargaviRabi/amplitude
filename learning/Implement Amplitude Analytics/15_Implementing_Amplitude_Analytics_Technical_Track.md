# Implementing Amplitude Analytics: Technical Track (Learning Path)

**Type:** Multi-course learning path | **Estimated time to complete:** 4-6 hours (5 sub-courses)

This learning path trains technical roles on Professional Service teams on how to implement Amplitude, giving them hands-on practice with the Amplitude Analytics SDK.

**Prerequisite:** Implementing Amplitude Analytics (this catalog's Course 14) or the bootcamp equivalent.

This file combines all 5 sub-courses in this path: IMPL-TECH-1 through IMPL-TECH-5.

---

# PART 1: IMPL-TECH-1 Deep Dive: Amplitude's Data Ingestion Methods

**Estimated time:** ~30 minutes

*Note: this course's internal lesson metadata/navigation footer displays a stale/mismatched label ("IMPL-EXP-1 Experimentation Implementation Overview") — likely reused content scaffolding from another course template in the CMS. The actual page title, sidebar heading, and all lesson content confirmed via direct inspection correctly belong to "IMPL-TECH-1 Deep Dive: Amplitude's Data Ingestion Methods."*

## About This Course

While the Implementing Amplitude Analytics learning path provided an overview of Amplitude's data ingestion methods, this course dives deeper in order to upskill the technical roles at delivery partners handling the more technical aspects of implementing Amplitude. This course is the first in the technical track learning path that follows the Implementing Amplitude Analytics learning path.

After taking this course you'll be able to:
- List and explain Amplitude's data ingestion methods (autocapture, DW, cloud storage, HTTP APIs, Attribution APIs, Browser SDK, Snowflake and S3)
- Determine when/whether to use autocapture or precision capture/tracking or a combination
- Use an Amplitude Data ingestion "cheat sheet" to identify the most common Amplitude libraries and integrations for a given use case

---

## Lesson: Choose the right Data Ingestion Method (5 min)

**[Video embedded, 5 min]** — no transcript exposed.

**"Choose the Right Data Ingestion Method" reference table (reproduced in full):**

| Method | Description | Why? |
|---|---|---|
| Client-side | Install Amplitude's SDK onto clients and tag events for tracking (incl. Google Tag Manager) | Simplest initial instrumentation |
| Server-side | Connect in-house data pipeline; map existing data to Amplitude's event schema | Track server-side events; leverage existing user data tracking workflows |
| Hybrid | Combination of client-side and server side | Benefits of simpler implementation & ability to track server-side events |
| Data Layer | Turn on connection to Amplitude within your existing data layer (Segment, mParticle, etc.) | Events get sent automatically; already have a 3rd-party data layer — can be extremely easy if the CDP is already in place |

**Data Sources:**
- *Client-side:* Open Source Amplitude SDKs (docs) — Web: TypeScript/JavaScript, React; Mobile: Android, iOS, Unity Plugin, Flutter, React Native.
- *Server-side:* Node.js (docs), HTTP API (docs), Batch Event Upload API (docs), Java (docs), Python (docs).
- *Third Party (docs):* mParticle, Segment, Google Tag Manager, Tealium, and many more.

**Cheat Sheet:** learners are directed to refer to the "Amplitude Data Ingestion Cheat Sheet" throughout this course.

## Lesson: Browser & Mobile SDKs (6 min)

**[Video embedded, 6 min]** — no transcript exposed.

**Browser SDK.** Client-side SDK for capturing user events and properties in a JavaScript or TypeScript context. Supports out-of-the-box default event, user properties, and web attribution/UTM tracking. (Dev docs, Quick start guide linked.)
- *Default events + properties:* Page views; Sessions; Form interactions; File downloads; Attribution (UTMs + referrer); Device info (platform, OS, carrier, language, device type); Geo-location (lat/lon, IP, city, country).
- *Plugins:* extend the SDK's behavior — e.g. modifying event properties (enrichment plugin) or sending to third-party endpoints (destination plugin). A plugin is an object with optional fields `name` and `type` and methods `setup()`, `execute()`, and `teardown()`.

**Mobile SDKs.** Client-side SDKs for capturing user events and properties. The Android and iOS SDKs support out-of-the-box default event and user properties tracking. (Android, iOS, React Native, Flutter — Quick start guides linked for each.)
- *Default events + properties:* Sessions; App lifecycles; Screen views; Element Interactions; Deep links; Device info (platform, OS, carrier, language, device type); Geo-location (lat/lon, IP, city, country).
- *Plugins:* extend the SDK's behavior similarly (enrichment type / destination type), as an object with methods `setup()` and `execute()`.

## Lesson: Autocapture (6 min)

**[Video embedded, 6 min]** — no transcript exposed.

**Considerations for using Autocapture (numbered list):**
1. **SDK.** Can you install Amplitude's SDK in your website or app? Are you instrumenting with a third-party CDP?
2. **Security and Privacy.** What are the PII implications of your industry? How does this impact your data collection strategy?
3. **Data Management.** What are your expectations around data management — distributed governance or a strict, centralized team?
4. **Site Architecture.** How is your site structured? Is your front end stable enough to handle visual tagging?
5. **Event volume.** What's your expected traffic and available event volume/MTU count? Are there volume concerns around instrumenting?

**Setting up Autocapture:**
- *Web:* Browser SDK 2.10 and above (docs). Enabled by default: Attribution, pageViews, Sessions, formInteractions, fileDownloads, elementInteractions.
- *Mobile:* iOS Swift 1.8.0 and above (docs); Android Kotlin 1.17 and above (docs). Default: Sessions, Screen Views, Application Interactions, Default Amplitude User Properties.

**Hero image:** "Setting up Autocapture in Amplitude" — illustrative screenshot/diagram of the Autocapture setup flow in the Amplitude UI.

**Autocapture Volume.** Autocapture events count towards event volume — choose what to track to control volume. Volume Estimation guidance:
- **Basic:** little impact, scales linearly with DAU.
- **Medium:** use DAU × average number of pages viewed to estimate.
- **High:** follow up with the Amplitude team if volume is a concern.

**Hero image:** "Autocapture volume from basic to high" — illustrative diagram.

**Interactive sorting exercise: "Autocapture is not always the best fit"** — *"Determine whether the situation is likely a 'hard blocker' or 'discussion required' based on the video above."* Extracted programmatically from the interactive block's `piles`/`items` structure:

| Category | Situations |
|---|---|
| **Hard Blocker** | SDK Eligibility; Migrations |
| **Discussion Required** | Existing Tracking Plan; Volume Concerns; Privacy; Site Architecture |

## Lesson: Server-side Sources (2 min)

**[Video embedded, 2 min]** — no transcript exposed.

**Server-Side SDKs.** Server-side SDKs for capturing user events and properties: Java, Node, Go, Python (quick start guides linked for each). Alternatively, server-side data sources can be instrumented using Amplitude APIs.

**Interactive sorting exercise: "HTTP API or Batch API?"** — *"Determine whether the scenario aligns with the HTTP API or the Batch API."* Extracted programmatically:

| API | Scenario |
|---|---|
| **HTTP API** | No more than 30 events per second per user/device; Real-time ingestion into Amplitude |
| **Batch API** | No more than 1000 events per second per user/device; Delayed ingestion into Amplitude (several minutes) |

**Technical Considerations for HTTP API and Batch API:**
- `event_type`, `time`, and either `user_id` or `device_id` is required on every event.
- Always retry if no 200 status code is received (wait 30 seconds if 429 "TooManyRequests").
- Send an `insert_id` key to deduplicate events (should be unique for every event sent for a user/device).
- To populate Amplitude-reserved user properties, set values for those keys outside the `user_properties` dictionary.
- To avoid common errors such as `user_id` = "null" for all users, there is a 5-character minimum for `device_id` and `user_id`.

## Lesson: Tag Manager Sources (4 min)

**[Video embedded, 4 min]** — no transcript exposed.

**Google Tag Manager:**
- *Client-Side Integration:* uses Amplitude Browser SDK; requires initialization of the SDK and tag setup on all pages to be tracked; enriches data with default properties and events captured by the SDK; more granular control over instrumentation via SDK functionality.
- *Server-Side Integration:* uses Amplitude HTTP API; can leverage existing GTM tags and data layer to map/forward to Amplitude fields.

**Tealium:**
- *Tag Manager (client-side):* load the Amplitude Browser SDK snippet via Tealium tags on your site and implement tags to fire analytics tracking to Amplitude.
- *Data Layer (server-side):* leverage the existing Tealium data layer to map and forward analytics tracking to Amplitude server-side, using the Amplitude HTTP API.

## Lesson: Warehouse Sources (2 min)

**[Video embedded, 2 min]** — no transcript exposed.

**Snowflake Import.** A SQL-driven import method for events + properties that supports backfill and ongoing ingestion (dev docs linked). **Note:** time-based imports for ongoing event ingestion require a separate column indicating when the data was loaded into the table Amplitude imports from — often "server upload time," distinct from "event time" (when the actual event occurred).

**BigQuery Import.** A SQL-driven import method for events + properties that supports backfill and ongoing ingestion (dev docs linked). **Note:** this integration requires a GCS bucket in addition to a BigQuery table — Amplitude recommends one dedicated to Amplitude import purposes. The ingestion process must offload data to a GCS bucket before ingesting it into Amplitude, due to BigQuery's limited export options.

## Lesson: Cloud Storage Sources (2 min)

**[Video embedded, 2 min]** — no transcript exposed.

**Amazon S3 Import.** A converter-configuration (mapping-rules-based) import method for events + properties that supports backfill and ongoing ingestion (dev docs, converter configuration reference linked). **Note:** S3 files must contain one event per line and be in JSON, CSV, or Parquet format (may be compressed); file names should be unique and uploaded approximately in the events' chronological order; files should not be updated once uploaded to S3.

**Google Cloud Storage Import.** A converter-configuration (mapping-rules-based) import method for events + properties that supports backfill and ongoing ingestion (dev docs, converter configuration reference linked). **Note:** after the initial ingestion from GCS, data organization must conform to this standard for subsequent imports: `{bucket name}/{GCSPrefix}/{YYYY}/{MM}/{DD}/{HH}/{optional}/{additional}/{folder}/{structure}/{file name}`.

## Lesson: Quiz (Check Your Understanding)

*Extracted programmatically from the quiz lesson's `items` array (top-level `correct` field cross-checked against `corrects` array — no mismatch found for this quiz, unlike the AI-first Methodology course's certification quiz).*

**Q1. A gaming company is launching a new mobile game and wants to track in-game interactions. They need real-time insights for user engagement analysis and visibility in their marketing efforts quickly. Which approach should they use?**
- ☑ **(correct)** Client-side instrumentation
- ☐ Hybrid instrumentation
- ☐ Data layer instrumentation

**Q2. Your social media company is implementing Amplitude's data tracking that serves millions of users daily. You want to capture all user sessions and interactions, but you're concerned about data quality and the sheer volume of events being sent to Amplitude. What combination of tracking methods should you use?**
- ☑ **(correct)** Use autocapture for basic user actions like page views, limit element interactions tracking, and implement precision tracking for high-value events such as form submissions, logins, and purchases.
- ☐ Rely solely on precision tracking for all events, defining every interaction manually to avoid unnecessary event capture.
- ☐ Enable autocapture for every single user interaction and send all events without any filtering.

**Q3. Your customer has a legacy system that stores user event data in Amazon S3. You also want to track real-time events directly from your backend systems to Amplitude for analysis. Which combination of ingestion methods should you use to efficiently manage historical data from S3 and real-time events from your backend?**
- ☑ **(correct)** Use Cloud Storage Ingestion to import historical data from S3 and the HTTP API or Server Side SDKs to send real-time events directly from the backend to Amplitude.
- ☐ Use autocapture for all events and rely solely on the Batch API to handle the backend tracking.
- ☐ Enable precision tracking to track real time data using Server Side SDKs and backfill historical data using Batch API.

**Q4. You are working with a customer who has multiple data sources containing the same data set: Amazon S3, Snowflake, and a backend system that can implement the Node.js SDK. The data is frequently updated in the backend systems, and the customer wants to ensure that updated values are also updated in Amplitude and real time ingestion is not needed. Which combination of Amplitude's data ingestion methods should the customer use to capture updated and mutated data effectively from all three sources?**
- ☑ **(correct)** Use Snowflake data ingestion source for event tracking from the backend.
- ☐ Use the Amplitude HTTP API to send real-time updates from Snowflake and S3, while implementing the Node.js SDK for tracking events from the backend.
- ☐ Use the Amplitude Node.js SDK to send real-time events, while utilizing S3 for batch uploads of historical data.

*(Note: this question's correct answer as extracted — "Use Snowflake data ingestion source for event tracking from the backend" — is a somewhat unusual match for the scenario as worded, which describes updates needing to flow from S3, Snowflake, AND a backend system without real-time requirements; the extracted answer text itself only mentions Snowflake. This is reproduced exactly as authored in the course data; it may reflect that Snowflake's SQL-driven import method is being used as the representative/primary answer among the three warehouse/mutation-friendly sources discussed in this lesson, since warehouse imports — unlike one-time S3 batch uploads — support capturing updated/mutated values on an ongoing basis.)*

**Q5. You are tasked with implementing event tracking for a website using Google Tag Manager (GTM) and Amplitude. The website already uses GTM for handling various tags. Your team needs to start sending data to Amplitude without making direct changes to the website's source code. What is the most efficient way to integrate Amplitude with GTM to track events such as user clicks, page views, and form submissions?**
- ☑ **(correct)** Use Amplitude's client-side GTM template and configure tags to fire on specific triggers to send data.
- ☐ Install the Amplitude SDK directly on the website and manually configure the GTM to load it for event tracking.
- ☐ Use a custom JavaScript in GTM to push events to Amplitude's HTTP API whenever an event occurs on the site.

## Lesson: Course feedback (optional)

Standard optional feedback survey lesson — not course content.

---

### IMPL-TECH-1 Summary / Explanation

This course is the technical-track deep dive into the four ingestion methods (Client-side, Server-side, Hybrid, Data Layer) that were introduced at a conceptual level in IMPL-4 of the main Implementing Amplitude Analytics path — here, each method gets its own concrete SDK/API inventory (Browser SDK, Mobile SDKs, Server-side SDKs in Java/Node/Go/Python, HTTP API, Batch API, Snowflake/BigQuery warehouse imports, S3/GCS cloud storage imports, and GTM/Tealium tag-manager integrations) along with the specific technical constraints of each (rate limits, required fields, file-format requirements, deduplication via `insert_id`, minimum ID lengths). The course's central technical judgment call is Autocapture eligibility, evaluated across five dimensions (SDK installability, security/privacy/PII, data governance model, site architecture stability, and event volume) and reinforced by the "hard blocker vs. discussion required" sorting exercise — a more granular, technical-role version of the "Autocapture is no longer the default recommendation" guidance introduced at a strategic level in the 2026 AI-first Methodology course. A second recurring technical judgment call is HTTP API vs. Batch API selection, governed by a straightforward but easy-to-miss threshold: HTTP API for real-time, lower-throughput needs (≤30 events/sec/user) and Batch API for higher-throughput, delay-tolerant needs (≤1000 events/sec/user) — tested directly by the sorting exercise and echoed in the quiz.

---

# PART 2: IMPL-TECH-2 Ingest Data for Amplitude's Marketing Analytics capabilities

**Estimated time:** 30 minutes (25 min main lesson + 5 min scenario quiz)

## About This Course

This course builds on the data ingestion deep dive course for technical roles by focusing on ingesting data for Amplitude's marketing analytics capabilities. This course is part of the technical track learning path that follows the Implementing Amplitude Analytics learning path.

After taking this course you'll be able to:
- Explain Amplitude's marketing data instrumentation flow
- Configure your attribution data
- Define channels in Amplitude Data
- Connect ad network data
- Stream and sync audiences

---

## Lesson: Marketing Data Instrumentation Flow and Features Supported (5 min)

**[Video embedded, 5 min]** — no transcript exposed.

**Marketing Data Instrumentation Flow (numbered list):** Plan → Send Data → Create Reports → Activate Audiences.

**Amplitude Marketing Features Supported:**
- **Define Acquisition Channels.** Configure custom digital marketing channels via derived properties.
- **Measure Campaign Effectiveness.** Segment users via UTM parameters and channels across multiple chart types.
- **Web Analytics View: Out-of-the-Box Amplitude Marketing Reports.** Jumpstart insights into marketing initiatives (e.g. targeted paid sources and ad campaigns).
- **Multi-touch Attribution Models.** Attribute reusable models to events and critical product conversion by users and campaign channels.
- **Session Analysis: Entry/Exit.** Identify user traffic and channel entries with engagement and other in-depth session tracking analysis.
- **Predefined & Custom Metrics.** Create reusable metrics available across Amplitude for faster insights.
- **Ad-Network Integrations.** Import advertising campaign impressions, clicks and costs.
- **Audiences / Cohort Syncs.** Target specific user groups with personalized experiences and compare campaign performance.

## Lesson: Configure Your Attribution Data (3 min)

**[Video embedded, 3 min]** — no transcript exposed.

**Get Started Tracking Attribution — Overview.** Capturing attribution data is key to configuring marketing channels and understanding insights for most marketing use cases; Amplitude considers it the foundation to all things related to marketing analytics.

**Recommended Action:** identify which of the 3 recommended methods to use to track attribution data:
1. **Amplitude SDKs (Auto-Tracking).** Web: automatic UTM tracking using Browser SDK. iOS: automatic Deep Link tracking with "Link URL" and "Link Referrer." Android: automatic Deep Link tracking with "Link URL" and "Link Referrer."
2. **Track Manually.** Campaigns need to be tagged to key URLs and deep links; capture parameters from the URL and set as user properties.
3. **Third Party.** Send attribution data from major attribution providers directly to Amplitude (full list of integrations linked).

## Lesson: Define Channels in Amplitude Data (5 min)

**[Video embedded, 5 min]** — no transcript exposed.

**Overview.** Defined channel classifications take attribution data further, enabling high-level analysis of marketing tactics: they provide insight into how marketing efforts across various channels perform against critical product user flows, and help make informed decisions based on channel effectiveness.

**Example Use Cases / Example Metrics table (reproduced):**

| Example Use Case | Example Metrics |
|---|---|
| Distribution of traffic landing on your website via different channels | Breakdown of core metrics (acquisition, conversion, retention) by channel |
| Top traffic/campaign sources | # of visitors/critical events by channel; most visited pages by source |
| — | # of visitors segmented by device/location by channel; bounce rates by channel breakdown |

**Key Considerations:**
- Prerequisite: attribution data instrumented in Amplitude.
- Channel definitions are applied dynamically and retroactively.
- Calculated at query time, so values are not available in raw data.
- Uses Amplitude's Derived properties functionality behind the hood — the same logic applies while setting any rules.
- **Order matters!** (1) top-to-bottom ordering DOES matter; (2) left-to-right column ordering does NOT matter.
- If users don't match the values defined, they will reflect channels = "(none)".

**Key Considerations — Values (interactive tabs, reproduced):**
- **ANY:** means any non-null value of the source property.
- **(none):** refers to the source property not being present/blank values. In case of blank values or properties not present, both rules attribute an event to Direct.
- **Blank values:** assumes the property is not present with the event and is to be ignored.

**Key Considerations — CDP Sources.** Most CDPs (Segment, mParticle) capture the "referrer" from the Document Object Model (DOM), which updates on each page load — as a result, only the first event of a session is typically attributed to an external referrer, when applicable. This can cause inaccuracies in Channel attribution when building a Channel classifier, particularly for Organic traffic that depends on referrer data.
- **Recommended no-code solution:** use Entry Analysis to attribute sessions based on the first detected Channel for the session. *Limitation:* Entry Analysis does not account for session expiration due to inactivity or mid-session referrer changes.
- **Optimal solution (needs eng work):** custom code to exclude internal referrers — create a custom JS variable (translating to a new user property in the tracking plan) for "referrer," `referrer_exclude_internal`: if the value in `window.document.referrer` matches (regex) an internal domain/page, set this as null; if no match, set this as the value from `window.document.referrer`. Configure the CDP SDK to read the "referrer" value from this JS variable, not `window.document.referrer` (a custom user prop may also be used). Use the newly configured user property for configuring the "Channel" definition in Amplitude.

## Lesson: Connect Ad Network Data (2 min)

**[Video embedded, 2 min]** — no transcript exposed.

**Overview.** Advertising impressions, clicks, and cost data resides with the advertising network — Amplitude allows configuring and automating the import of this network metric data to perform analysis. **Currently supported networks:** Google Ads, Facebook Ads.

**Example Use Cases / Example Metrics:** analyze spend on campaigns and measure ROAS by connecting to conversions; identify conversion data by ad marketing initiatives to measure impact/performance; ranked most-effective campaigns and associated costs driving conversion metrics; ROAS; total daily ad metrics by campaign; total cost associated with ad impressions/interactions/clicks.

**Recommended Action:** in Amplitude Data, set up the Ad Network platform as a data source and use the newly imported "Daily Ad Metric" event to begin analysis.

**Add New Data Source with Ad Network — Steps:**
1. Navigate to the Sources section of Amplitude Data.
2. Under the "Marketing" section, look for the desired Ad-Network: Google Ads or Facebook Ads.
3. Follow the UI instructions through the 3-step OAuth process (Google Ads Customer ID needed to connect Google Ads; Facebook Ads Account ID needed to connect Facebook Ads).
4. If needed, import past data for a given period — up to 2 years back.

**What will be imported?** A "Daily Ad Metric" event, with properties: Ad Impressions, Ad Clicks, Ad Cost, Ad Conversions, Ad Interactions, Ad Group ID, Ad Group Name, Ad Group Type, Ad ID, Ad Name, Ad Platform, Ad Segment Device, Campaign Advertising Channel Type, Campaign End Date, Campaign ID, Campaign Name, Campaign Start Date, Final URL, Tracking URL Template. Sets user properties: UTM Campaign, UTM Content, UTM Channel, UTM Medium, UTM Term. Imported once per day per ad.

**Key Considerations:**
- The "Daily Ad Metric" event is not tied to any real user in Amplitude — it contains aggregated data on a campaign level.
- **Data Freshness:** Google may occasionally update ad metrics one or more days after a click occurs, which may cause slight discrepancies between Google Ads and Amplitude numbers.
- Importing data from Google Ads requires that the Google Ads Manager account has administrator privileges.
- For networks not yet part of Amplitude's integrations list, customers can push ad-metric events server-side using Amplitude APIs or a data warehouse.

## Lesson: Stream and Sync Audiences (4 min)

**[Video embedded, 4 min]** — no transcript exposed.

**Overview.** Amplitude helps engage specific audiences with personalized messaging and drive customer lifetime value by syncing customer data in Amplitude (including behavioral data) with the rest of the growth stack, such as Braze or Facebook — creating automated or on-demand syncs based on Growth Marketing needs.

**Example Use Cases:** use customer data to target segments for product upgrades and offers, driving deeper product adoption and revenue growth (e.g. New User Conversion, Cross-Sell/Up-Sell Existing Users, Re-target Dormant Users); use behavioral data from Amplitude to create cohorts for an in-product experience, personalizing content, recommendations, and communications.

**What is available to export?**
- **Cohorts.** Amplitude supports two types: *Behavioral* (clusters of users grouped by past actions) and *Predictive* (clusters of users grouped by actions Amplitude anticipates they will take in the future).
- **Computations.** Transform events or event properties into computed user properties — usable as a configurable filter in Amplitude charts, or synced to an external destination for personalization.

**Key Considerations:**
- If a downstream destination isn't in Amplitude's list of integrations, one of two available APIs can be used to export data: Cohort API or Profile API.
- Users on certain plans may be limited in their ability to use Audience syncing in certain ways.
- Amplitude Audiences is not currently available to customers based in the European Union.

## Lesson: Course Resources

- Help Docs: `https://amplitude.com/docs/data/autocapture`
- Amplitude Data Ingestion Cheat Sheet
- Cross-referenced chart-type courses/articles: "Unlock Engagement Insights with Session Analysis" (session charts); "Drive Product Adoption with Retention Analysis" (retention chart); Revenue LTV chart help article (track monetization of new users); "Discover User Paths with Journeys"; "Analyze Multiple Metrics at Once with Data Tables" (data tables).

## Lesson: Scenario Questions (Check Your Understanding) — separately-rendered quiz (5 min)

*This quiz is reached via its own lesson URL (not embedded inline in the Rise course JSON). Extracted via the "Show Answers" review screen, visually confirmed via screenshot for checkbox/strikethrough state (this learner account had already completed it with a 5 of 5 / 100% score).*

**Q1. A subscription-based software company wants to retarget dormant users with personalized offers based on their previous product usage. Which Amplitude capability should you recommend to implement this strategy?**
- ☐ Entry/Exit Analysis to identify how users enter the product and where they exit
- ☑ **(correct)** Audiences/Cohort Syncs to target specific user groups based on their behavior and sync to marketing tools
- ☐ Ad-Network Integrations to import advertising campaign data from platforms like Google Ads and Facebook

*Feedback: Audiences/Cohort Syncs enables creating behavioral cohorts of dormant users and syncing these segments to marketing tools, delivering personalized offers based on past product usage.*

**Q2. A mobile gaming company is implementing Amplitude and wants to track which ad campaigns drive both initial installs and subsequent in-app purchases. They have an existing relationship with AppsFlyer for attribution. What would you recommend for their implementation?**
- ☐ Implement manual tracking by capturing deep link parameters and setting them as user properties in the implementation
- ☑ **(correct)** Send attribution data from AppsFlyer directly to Amplitude to track campaign performance and connect it to in-app behavior
- ☐ Switch from AppsFlyer to using Amplitude's Browser SDK with auto-tracking features

*Feedback: leveraging the existing AppsFlyer-Amplitude integration is most efficient, combining AppsFlyer's specialized mobile attribution with Amplitude's analytics without requiring significant infrastructure changes.*

**Q3. A media company is setting up channel definitions in Amplitude and has several overlapping rules that could apply to the same traffic. How should they structure their rule definitions for optimal accuracy?**
- ☑ **(correct)** Order rules from most specific to most general, as rules are evaluated in sequence from top to bottom
- ☐ Place rules with the highest traffic volume first to optimize processing efficiency
- ☐ Order doesn't matter as long as all relevant properties are included in each channel definition

*Feedback: ordering from most specific to most general ensures highly targeted channel definitions capture their intended traffic before broader rules apply, since rules are evaluated top to bottom.*

**Q4. A B2B software company wants to identify which marketing channels bring in users who are most likely to convert to paying customers. What implementation method and analysis approach should you recommend?**
- ☐ Create behavioral cohorts based on signup events and sync them back to marketing platforms
- ☐ Set up manual tracking by tagging campaigns with UTM parameters and capturing these as user properties in the implementation. Connect ad network data from Google Ads and Facebook to measure direct ROAS from advertising campaigns
- ☑ **(correct)** Use Amplitude SDK to send data, leveraging Autocapture. Define custom marketing channels using derived properties, then use Multi-touch Attribution to analyze which channels drive conversions

*Feedback: implementing the Browser SDK with auto-tracking establishes a foundation for accurate attribution data collection; combined with custom channel definitions and Multi-touch Attribution analysis, this identifies which marketing efforts bring in the highest-quality leads.*

**Q5. A financial services company is sending data using Segment CDP and analyzing traffic and conversions by Channels and notices that many conversions classified as "Direct" traffic are coming from "Organic" sources. The Channel Classifier is confirmed configured correctly. What is the most likely cause of this misattribution?**
- ☑ **(correct)** Internal referrers are overwriting the original email referrer information.
- ☐ Channel Classifier will consider Organic and Direct as the same channel.
- ☐ Organic clicks aren't properly tagged with UTM parameters, causing them to appear as Direct traffic

*Feedback: many CDPs lack the ability to exclude internal referrers, which can result in all events after the first session event being classified as "Direct" due to internal domain referrals. Prevent this with Entry/Exit analysis (no-code) or code changes to exclude internal referrers.*

## Lesson: Course feedback (optional)

Standard optional feedback survey lesson — not course content.

---

### IMPL-TECH-2 Summary / Explanation

This course extends the ingestion methods from IMPL-TECH-1 into Amplitude's marketing-analytics-specific capabilities, following a four-step flow: Plan → Send Data → Create Reports → Activate Audiences. Its most technically dense content is the channel-definition rules engine, where two easy-to-miss constraints are tested directly in the quiz: rule evaluation order (top-to-bottom, most-specific-first) determines accuracy since rules apply in sequence, and a common real-world pitfall — CDPs like Segment only capturing referrer data via the DOM on the first page load of a session — causes legitimate Organic traffic to misattribute as "Direct" after the first event, correctable via Entry/Exit Analysis (no-code) or custom referrer-exclusion code (engineering-required). The course also distinguishes two related-but-distinct marketing capabilities that the quiz separately tests: Ad-Network Integrations (importing aggregated, campaign-level "Daily Ad Metric" events from Google/Facebook Ads, not tied to individual users) versus Audiences/Cohort Syncs (exporting individual-level behavioral or predictive cohorts to downstream marketing tools for targeting) — the former measures ad spend/performance, the latter activates segments for personalized engagement.

---

# PART 3: IMPL-TECH-3 Implement the Amplitude SDK

**Estimated time:** 2 hr 25 min (25 min video walkthrough + 2 hr hands-on graded exercise)

## About This Course

In this course, you'll finally get hands-on with implementing Amplitude using a guided tutorial. This course is part of the technical track learning path that follows the Implementing Amplitude Analytics learning path.

After taking this course you'll be able to: Implement the Amplitude SDK on a basic website using provided instructions and code.

---

## Video Walkthrough Lessons ("WATCH ISHAN Implement the SDK")

*Every lesson in this section consists solely of a single embedded instructional video with no additional on-page text, code snippets, or transcript exposed in the page data — this is a live screen-recorded coding walkthrough series presented by an instructor named Ishan, using a demo web application called "Battleboat" (a Battleship-style game) as the hands-on instrumentation target. Each video's title and duration are reproduced below exactly as captured; no transcript is available for any of them.*

- **[Video: "Setup", 2 min]** — no transcript exposed.
- **[Video: "Run the Battleboat web app", 3 min]** — no transcript exposed.
- **[Video: "Install Amplitude with Autocapture", 2 min]** — no transcript exposed.
- **[Video: "Track an Event", 2 min]** — no transcript exposed.
- **[Video: "Instrument Ship Placement events", 7 min]** — no transcript exposed.
- **[Video: "Instrument gameplay events", 7 min]** — no transcript exposed.
- **[Video: "Add User Property", 5 min]** — no transcript exposed.

## Lesson (Graded assignment): Submit your SDK Implementation Exercise (2 hr)

**"Show us you're ready to do the technical side of an Amplitude implementation!"**

Instructions (reproduced in full):
1. Follow the SDK Implementation Exercise instructions to implement Amplitude.
2. Take screenshots while going through the exercise and paste them into a provided slide deck template.
3. Upload the deck with 10 screenshots at the submission link provided on the page.

Learners are asked to allow 4 weeks for a team member to review their work and share feedback; an email notification is sent when the course is marked complete. Questions can be directed to partner-enablement@amplitude.com.

## Lesson: Course feedback (optional)

Standard optional feedback survey lesson — not course content.

---

### IMPL-TECH-3 Summary / Explanation

This course is the technical track's hands-on centerpiece: rather than teaching new conceptual material, it walks a technical learner through actually instrumenting a real (if small, demo-scale) web application — "Battleboat," a Battleship-style game — end to end, following the sequence: set up the environment, run the Battleboat app locally, install the Amplitude SDK with Autocapture enabled, track a first custom event, then instrument two feature-specific event groups (ship placement events and gameplay events), and finally add a user property. This progression mirrors, at the level of literal code, the conceptual ingestion-method and event/property distinctions taught earlier in IMPL-TECH-1 (client-side SDK installation, Autocapture enablement, precision/custom event tracking) and in the "Amplitude Schema" and "User identification" lessons of IMPL-4 in the main Implementing Amplitude Analytics path (event vs. user properties). Because all seven walkthrough lessons are video-only with no on-page transcript or code listing, this document cannot reproduce the actual code changes Ishan makes on screen — learners must watch the videos directly for the specific SDK calls and syntax. The course concludes with a graded, portfolio-style deliverable (a 10-screenshot slide deck documenting the learner's own completed implementation), reviewed by an Amplitude team member within 4 weeks, functioning as this technical track's equivalent of a milestone checkpoint comparable to the main path's capstone project.

---

# PART 4: IMPL-TECH-4 Resolve the most common data discrepancy issues

**Estimated time:** 22 minutes

## About This Course

No implementation is perfect; you'll inevitably encounter data discrepancy issues. Prepare to identify and resolve the most common issues before you encounter them on the job. This course is part of the technical track learning path that follows the Implementing Amplitude Analytics learning path.

After taking this course you'll be able to:
- Identify the most common data discrepancy issues
- Explain the right approach to the most common data discrepancy issues
- Explain charts' calculations under the hood when needed to debug

---

## Lesson: How to approach data discrepancies (10 min)

**[Video embedded, 10 min]** — no transcript exposed.

**Interactive accordion, reproduced in full (5 discrepancy scenarios):**

**1. Attribution data mismatched.** *Symptom:* customer reports discrepancy between Attribution Events and Users in the attribution platform vs. Amplitude.
- *Common Causes:* Amplitude ingests this event data using the Attribution API, identified by IDFA, IDFV, or ADID. Post-ingestion, Amplitude tries to map these events to an existing user. If Amplitude can't match attribution events to an existing user, they're held for up to 72 hours. If an event isn't matched within 72 hours, Amplitude drops the attribution data.
- *Resolution:* this functionality exists to ensure fake installs do not inflate the User count — expect to see a lesser number of Attribution Events and Users in Amplitude vs. the source platform.

**2. Discrepancy between Data Warehouse and Amplitude.** *Symptom:* customer reports discrepancy between Events and Users in internal Data Warehouse vs. Amplitude.
- *Common Causes:* ad-blockers blocking Amplitude libraries (resulting in low user count/event volume in Amplitude); bot traffic (resulting in higher counts in Amplitude); differences in user identity logic between Data Warehouse and Amplitude; differences in triggers for events between the two systems; instrumentation issues resulting in missing data in Amplitude.
- *Resolution:* implement a domain proxy to relay events to Amplitude (preventing ad-blockers from loading Amplitude libraries); block bot traffic by applying bot filters in Amplitude; understand how Amplitude tracks unique users and compare against Data Warehouse identity logic; ensure event triggers are aligned between systems; review instrumentation for missing data.

**3. Discrepancy between Incumbents and Amplitude.** *Symptom:* customer reports discrepancy between Events, Users, Session counts, or Attribution between an incumbent platform vs. Amplitude.
- *Common Causes:* data collection and processing differences; differences in event-tracking triggers and session definitions; differences in user identity logic; differences in channel classification logic and attribution methodologies applied; instrumentation issues resulting in missing data in Amplitude.
- *Resolution:* differences between analytics platforms are expected, with no universal fix. Understand differences in data collection methods (attribution, session definition, identity resolution) between the incumbent platform and Amplitude; for missing users, compare user presence in both platforms; for missing events, analyze the event stream of the same user in both systems.

**4. New user count discrepancy.** *Symptom:* customer has recently implemented Amplitude and is reporting an unusually high New User count.
- *Common Causes:* a user is counted "new" in Amplitude when the first event for that user is seen — with a new implementation, even existing users can be counted as new. Due to incorrect instrumentation, Device ID may be regenerating or splitting in the case of multiple SDK instances.
- *Resolution:* backfill existing users with a dummy event whose event timestamp is the date when the users were originally new; check instrumentation for multiple initializations of Amplitude SDKs; check SDK setup to ensure Device ID is not regenerating.

**5. Discrepancy between ad platforms and Amplitude.** *Symptom:* the Daily Ad Metric event reports different numbers for clicks, impressions, and conversion metrics for an ad campaign compared to the ad platform itself.
- *Common Causes:* ad networks may occasionally update metrics one or more days after a click occurs — this may happen when a conversion occurs days after the initial click, or when invalid traffic is detected and removed.
- *Resolution:* ad metric events cannot be updated after original ingestion in Amplitude. To correct data, delete the incorrect records from the affected date and backfill manually — or use Snowflake to send ad-metrics data to Amplitude instead, since Snowflake ingestion supports data mutability, allowing updates to older records.

**"Expect discrepancies" — general guidance:**
- **Document the differences** — know how each system defines and collects metrics.
- **Set expectations** — help stakeholders understand why differences exist.
- **Implement fixes where possible** — use the resolutions discussed for addressable issues.
- **Create consistent reporting processes** — build reports that account for known discrepancies.

**Linked resource:** Help Docs — `https://amplitude.com/docs/faq/data-discrepancies-with-other-platforms`.

## Lesson: Under the hood: how chart calculations impact data (7 min)

**"Beyond the basics: Funnel, Retention, Propcount formula, and OOTB Session metrics in Data tables."** Learn more about how chart calculations impact data by browsing the linked help docs:
- Funnel charts: "Interpret your funnel analysis," Funnel Analysis FAQ
- Retention charts: "Interpret your funnel analysis" (as labeled in-course), Retention Analysis FAQ
- Propcount Formula help
- OOTB Marketing Metrics in Data Tables; Marketing metrics recipes ("Use sessions, channels, and attribution to drive marketing analytics")

*(This lesson consists solely of linked reference documentation with no embedded video.)*

## Lesson: Quiz (Check Your Understanding)

*Extracted programmatically from the quiz lesson's `items` array.*

**Q1. A marketing team notices that Amplitude is reporting fewer attributed installs from a Facebook ad campaign compared to their attribution platform (e.g., Adjust or AppsFlyer). The marketing team is concerned about this discrepancy. What's the most likely reason for this difference?**
- ☑ **(correct)** Amplitude uses Attribution API to match Install events.
- ☐ Amplitude overreports installs from Facebook ads, causing higher conversion numbers.
- ☐ Amplitude doesn't track user IDs, so the discrepancy is related to missing user data.

**Q2. A customer team is investigating discrepancies in user count data between Amplitude and the internal data warehouse. You've found that Amplitude is reporting fewer users than the warehouse. What could be the cause of this discrepancy?**
- ☑ **(correct)** Amplitude is likely excluding bot traffic, while the internal warehouse isn't.
- ☐ The internal data warehouse uses a different user ID resolution method, leading to overcounting users in Amplitude.
- ☐ Amplitude doesn't track new users, only returning users, causing discrepancies in reporting.

**Q3. You are troubleshooting a new user count discrepancy where a sudden spike in new users is reported after implementing Amplitude for the first time. The customer has backfilled existing users already. What is the most likely reason for this issue?**
- ☑ **(correct)** Device ID regeneration or multiple instances of the Amplitude SDK are creating duplicate new user profiles.
- ☐ Amplitude's session definition is different from the internal system's session, causing users to be misclassified as new.
- ☐ The internal system is not tracking new users, while Amplitude is overreporting them due to faulty event triggers.

**Q4. A customer has enabled Google Ad integration to send ad data to Amplitude. You've noticed discrepancies between the conversion data reported by Google Ads and Amplitude, where Amplitude is reporting fewer conversions. What's the most likely reason for this discrepancy?**
- ☑ **(correct)** Google Ads retroactively updates conversion data after fraud detection, while Amplitude does not adjust past data.
- ☐ Amplitude includes data from bot traffic, whereas Google Ads excludes such traffic.
- ☐ Amplitude uses a different event-tracking methodology, which leads to higher event counts in the platform.

## Lesson: Course feedback (optional)

Standard optional feedback survey lesson — not course content.

---

### IMPL-TECH-4 Summary / Explanation

This course is a troubleshooting reference organized around five recurring discrepancy patterns a technical implementer will encounter, each following the same Symptom → Common Causes → Resolution structure. A unifying thread across nearly all five scenarios (and directly tested three separate ways in the quiz) is that "Amplitude reports a lower number than another source" is very often the *expected, correct* behavior rather than a bug: the 72-hour attribution matching window intentionally drops unmatchable attribution events to prevent fake installs from inflating user counts, bot-traffic filtering intentionally excludes non-human traffic that a less-filtered warehouse might still count, and ad-network platforms like Google Ads can retroactively revise conversion numbers after fraud detection in ways Amplitude's immutable ad-metric events don't automatically follow. The other major theme is diagnosing Device ID/user-identity issues — a "New user count discrepancy" is very often not a data problem at all but an artifact of how "new" is defined (first event seen for that user ID), compounded by real instrumentation bugs like Device ID regenerating due to duplicate SDK initializations. Practically, this course also cross-references the earlier IMPL-TECH-2 lesson's "Daily Ad Metric" event and Snowflake's data-mutability advantage over one-time S3 batch imports (first introduced in IMPL-TECH-1) as the specific fix for ad-platform discrepancies that need retroactive correction.

---

# PART 5: IMPL-TECH-5 Audit data and provide recommendations

**Estimated time:** 30 minutes

## About This Course

In this course, you'll learn how to use an established guide to approach taxonomy and data audits, and why doing so is critical to a customer's long-term success using Amplitude. This course is part of the technical track learning path that follows the Implementing Amplitude Analytics learning path.

After taking this course you'll be able to:
- Explain the value and process of a formal Data Audit
- Recognize the impact certain data issues (ID resolution, incorrect event timing, etc.) can have long term
- Follow the Amplitude guide for approaching Taxonomy and Data Audits
- Using a spreadsheet provided, perform a check: identify issues and associated risks, and correct any issues

---

## Lesson: Value and Process of a Formal Data Audit (2 min)

**[Video embedded, 2 min]** — no transcript exposed.

## Lesson: What to Check in a Data Audit (2 min)

**[Video embedded, 2 min]** — no transcript exposed.

**"What to Check" checklist:** Identity Resolution; Syntax Consistency; PII; Duplicate events and properties; Deprecated and unused data; Unexpected warnings; Event consolidation opportunities; Missing Object IDs; Missing Session ID / Insert ID. *(The remaining lessons in this course each cover one item from this checklist in detail.)*

## Lesson: Identity Resolution (2 min)

**[Video embedded, 2 min]** — no transcript exposed.

**Why does it matter?** When user identity is not resolved correctly, it leads to inaccurate counting of unique users, significantly impacting the accuracy of analysis.

**How to Check it:**
- For any event, segment users by User ID (None vs. Not None) to see how many users lack a User ID.
- For any event with a User ID, group by Device ID and analyze Unique Users — too many users on one device may signal identity resolution issues.
- Build a User Composition Chart by Device ID for the last 365 days — outlying "Users per Device ID" may indicate reuse of Device IDs.
- Build a chart for any event, group by Device ID, and analyze Event Totals — outlying "events per Device ID" may indicate reuse of Device IDs among anonymous users, which becomes an issue when linked to a User ID.

**How to fix it?**
1. Investigate the User ID/Device ID logic — is the User ID unique per user? Are multiple anonymous users being assigned a single Device ID?
2. Fix instrumentation: send events with Device ID only until the user performs a verification event (e.g. login); when the user logs out, reset their User ID and Device ID so future anonymous users aren't tracked under the same IDs.

## Lesson: Checking for PII (2 min)

**[Video embedded, 2 min]** — no transcript exposed.

**Why does it matter?** Regulations like GDPR and CCPA impose strict limits on PII collection and use, especially by third parties. Non-compliance can result in severe consequences. Generally, PII is not needed for analytics using Amplitude.

**How to Check it:**
1. Look for properties in the tracking plan that look like PII (name, phone number, address, first name, last name).
2. Check in any Amplitude chart, or user look-up, for the values of these properties.

**How to fix it?**
1. Immediately delete all attributes containing PII (this step still does not delete historic data).
2. Use the User Privacy API if the customer needs to scrub an end user's entire data; if the customer wants to retain an end user's data but just delete the PII, a Data Sanitization request needs to be raised.

*Note: if the customer needs to send PII for any reason, it's best that they consult their legal teams first.*

## Lesson: Events and Property Syntax Consistency (2 min)

**[Video embedded, 2 min]** — no transcript exposed.

**Why does it matter?** Clear and consistent nomenclature is essential for effective event taxonomy and data utility. Clear event names should be descriptive and indicate what is occurring; consistency ensures all events follow the same syntax. Inconsistent naming can lead to event/property duplication, causing team confusion, which may lead to a long-term lack of data trust.

**How to Check it:**
1. Review event and property data to check for multiple naming conventions (in the Events or Properties tab in Amplitude Data).
2. Click on Events and check "similar events" for potential duplicates. *(Note: may not be efficient for a customer with a high volume of event types, since each event must be checked individually.)*

**How to fix it?**
1. Create a naming convention and share it with the team — define it under Settings → General in Amplitude Data.
2. If no duplicates exist, change the display name of events and properties to match the convention; if duplicates exist, remove them by updating instrumentation or using transformations.

## Lesson: Duplicate Events and Properties (2 min)

**[Video embedded, 2 min]** — no transcript exposed.

**Why does it matter?**
- **Data Inaccuracy:** duplicates inflate metrics, leading to misleading insights and incorrect conclusions.
- **Skewed Metrics:** duplicates distort event counts, user counts, and engagement rates.
- **Increased Costs:** duplicates consume extra storage, raising costs.
- **Adoption Challenges:** duplicate names from multiple developers cause confusion, hindering Amplitude adoption.

**How to Check it.** Duplicate events are basically instrumentation errors, of two kinds: **true duplicates** (same events/properties triggering twice) and **duplicate names** (the same events/properties come with different naming conventions from different CTAs/platforms).
1. Review Data Assistant recommendations for duplicate events.
2. Click on Events and check "similar events" for potential duplicates.
3. Read through event and property data to check for multiple naming conventions (Events or Properties tab).

**How to fix it?**
- *True Duplicates:* review instrumentation to identify duplicate event/property triggers; modify instrumentation to remove duplicate triggers, keeping the event/property that follows the naming convention.
- *Duplicate Names:* go to the Events/Properties tab and select duplicates; use transformations to merge events or properties; modify instrumentation to remove duplicates.

## Lesson: Deprecated and Unused Data (2 min)

**[Video embedded, 2 min]** — no transcript exposed.

**Why does it matter?**
- **Deprecated Data:** events/properties no longer relevant to analytics (often due to UI or business changes) clutter taxonomy and may confuse Amplitude users, leading to adoption issues.
- **Unused Data:** events/properties not used in analysis for a long time still count against the event volume limit, causing unnecessary costs.

**How to Check it:**
- *For Events:* Amplitude Data → Events → Advanced tab → select a lookback window (30/90/180 days). [Deprecated] filter by "30/90/180 days volume" < 10. [Unused] filter by "30/90/180 days queries" < 10. Sort by "last seen" (ascending) and review the list.
- *For Properties:* Amplitude Data → Properties → Event or User Properties tab. Sort by "last seen" (ascending) to identify deprecated properties; sort by "30 days query" (ascending) to identify unused ones.

**How to fix it?**
1. Review the list of such events/properties.
2. Consult with the team to check if they're still required.
3. Block the events/properties in Amplitude — whether or not past data still needs analysis.
4. Update instrumentation to remove deprecated/unused events from the codebase.

## Lesson: Resolve Unexpected Warnings (1 min)

**[Video embedded, 1 min]** — no transcript exposed.

**Why does it matter?** These events/properties were not planned as part of the taxonomy and could be instrumentation errors — they clutter the taxonomy and may cause confusion among Amplitude users, creating adoption challenges.

**How to Check it:**
- Amplitude Data → Home — "Unexpected events" appear under the Data Health section.
- Amplitude Data → Properties — under Event Properties/User Properties, properties marked with "unexpected" status are visible.

**How to Fix it:**
1. Go to Data → Events/Properties tab.
2. Change the Status filter to "Unexpected."
3. Click on the "Unexpected" status against the event/property and choose a desired action.

## Lesson: Event Consolidation Opportunities (2 min)

**[Video embedded, 2 min]** — no transcript exposed.

**Why does it matter?**
- **Scaling Taxonomy:** creating a new event for each CTA complicates taxonomy management and lacks scalability as the product evolves.
- **Increased Complexity:** analyzing actions like "sign-ups" becomes cumbersome, requiring aggregation of multiple events each time.

**Example:** instead of separate events "completed signup with Facebook" and "completed signup with Google," the preferred approach is a single event "completed signup" with an event property `type` = "Facebook" or "Google".

**How to Check it:**
1. Review Data Assistant recommendations for duplicate events.
2. Click on Events and check "similar events" for potential duplicates.
3. Read through event and property data for consolidation opportunities.

**How to Fix it:**
- *Without Transformation:* create a custom event consolidating events with duplicate names (e.g. "page viewed" and "viewed a page" → "page viewed"); hide the visibility of the original events; modify instrumentation to make event names consistent.
- *With Transformations:* go to the Events tab in Amplitude Data; select such events and merge them into property values.

## Lesson: Missing "Session ID/Insert ID" properties (2 min)

**[Video embedded, 2 min]** — no transcript exposed.

**Why does it matter?**
- **Session IDs** indicate a user's session on the website/app. Missing Session IDs impact session-level analysis and may cause unavailability of charts (e.g., User Sessions, Pathfinder).
- **Insert ID** is required to de-duplicate events when duplicates are ingested — automatically generated by SDKs, but must be sent explicitly for server-side events. If absent, this may lead to event duplication.

**How to Check it:**
- *Session ID:* events without session IDs will have a default session ID of -1, and the event will appear with a green font.
- *Insert ID:* must be checked at the raw event level — navigate to an event in a user's profile, then click on the Raw view.

**How to Fix it:**
- *Session IDs:* SDKs automatically set session IDs — enable `config.defaultTracking.sessions` for Start/End Session events. Server-side: set `session_id` in the request payload. Integrations: check documentation to see if session IDs are sent (e.g., Segment automatically sends them). A custom session property can use an existing property for session tracking; a custom session definition limits Amplitude capabilities and doesn't create a session ID.
- *Insert IDs:* send a unique `insert_id` for all events (retroactive application is not possible); Insert IDs must be random, long, and unique.

## Lesson: Missing "Object IDs" (1 min)

**[Video embedded, 1 min]** — no transcript exposed.

**Why does it matter?** Object IDs are properties shared across events in a flow or funnel, representing a singular instance of that flow/funnel. When applied correctly, Object IDs can link events together, display breakdowns of events by the property, and more. **Example Object IDs for an e-commerce platform:** Product ID (tracks a user's journey from Product Page to Checkout); Cart ID (tracks the journey of a specific cart from creation to checkout); Order ID (tracks orders, deliveries, returns, and replacements).

**How to Check it.** Properties can be reviewed in Amplitude Data — click on a property to view more information about it.

**How to Fix it.** Update instrumentation to add relevant properties to events that will enable filtering and grouping.

## Lesson: Use Case Completeness (2 min)

**[Video embedded, 2 min]** — no transcript exposed.

**Why does it matter?** The objective of the implementation is to deliver a complete, high-quality dataset to support the initial high-priority, business-critical use cases and KPIs. Failure to achieve this compromises the value customers derive from Amplitude.

**How to Check it:**
1. Review the defined Use Cases and KPIs in the Analytics Use Cases tab in the Implementation Workbook.
2. Create charts for each of the KPIs.
3. Document gaps in data, like missing events/properties and incorrect events/properties.

**How to Fix it:**
1. Communicate the gaps to the customer.
2. Align on a plan to instrument the missing event or property.
3. Align on a plan to rectify erroneous events or properties.

## Lesson: How will you do it? (2 min)

**[Video embedded, 2 min]** — no transcript exposed.

**How to audit data:**
- Leverage information in the "Taxonomy Best Practice" tab in the Implementation Workbook and Amplitude Help Center Documentation.
- Use the "Taxonomy and Data QA" tab in the Implementation Workbook to audit taxonomy.
- Document findings as "Pass"/"No Pass" results and share feedback with customers.

## Lesson: Course Resources

**Data Auditing Resources:** "How to QA Your Taxonomy" (Professional Services internal resource); Help Docs: `https://amplitude.com/docs/get-started/tracking-your-progress#qa-your-instrumentation`.

## Lesson: Quiz

*Extracted programmatically from the quiz lesson's `items` array — no mismatch found between the per-answer flag and the authoritative `correct` field for this quiz.*

**Q1. You're conducting an initial data audit for a client who recently implemented Amplitude. You notice a high proportion of events without User IDs when segmenting users for a key conversion event. What should be your first recommended action?**
- ☑ **(correct)** Investigate the User ID and Device ID logic to determine if each user is being assigned a truly unique identifier.
- ☐ Immediately implement transformations to consolidate all events with missing User IDs.
- ☐ Suggest the client upgrade to a higher tier Amplitude plan with better identity resolution capabilities.

**Q2. You're reviewing a client's Amplitude implementation and notice they have separate events for "Signup Started on Home Page," "Signup Started from the top menu," and "Signup Started from the checkout flow." What should you recommend?**
- ☑ **(correct)** Use transformations to consolidate these into a single "Signup Started" event with a "location" property that captures the specific signup CTA location and modify instrumentation to capture a single event.
- ☐ Keep the separate events but create a new custom event that combines all three events for analysis.
- ☐ Maintain the current structure since having separate events provides more granular data for analysis.

**Q3. During an audit, you discover that a client's Amplitude implementation does not allow them to answer one of their primary business questions about user retention by acquisition channel, which was documented in their Implementation Workbook. What should be your first action?**
- ☑ **(correct)** Communicate the gap to stakeholders and develop a plan for instrumenting the missing parameters to define the acquisition channel property needed for the key use case.
- ☐ Suggest the client modify their business question to align with the data that's currently available in their implementation.
- ☐ Create a workaround using existing data that approximates the answer to their business question.

**Q4. You're reviewing a client's Amplitude implementation and notice inconsistent syntax in their event naming — some events use camelCase (e.g., "buttonClicked"), others use snake_case (e.g., "button_clicked"), and some use spaces (e.g., "Button Clicked"). What should you recommend?**
- ☑ **(correct)** Create a formal naming convention, document it in Amplitude Settings, update display names to match the convention, and use transformations to standardize the data structure.
- ☐ Leave the current naming structure as is since changing it could break existing dashboards and analyses.
- ☐ Create separate event taxonomies for each naming convention to maintain organization without disrupting current implementations.

**Q5. While reviewing a client's server-side Amplitude implementation, you notice duplicate events appearing in their data. After investigation, you discover they aren't using Insert IDs in their event payloads. What should you recommend?**
- ☑ **(correct)** Ensure they send a unique Insert ID for all events by implementing a random, sufficiently long identifier that's uniquely generated for each event.
- ☐ Implement a transformation rule in Amplitude to automatically deduplicate events based on timestamp and event properties.
- ☐ Switch from server-side to client-side tracking since client-side SDKs automatically handle deduplication.

## Lesson: Course feedback (optional)

Standard optional feedback survey lesson — not course content.

---

### IMPL-TECH-5 Summary / Explanation

This is the technical track's capstone knowledge course: a systematic, nine-point data audit checklist (Identity Resolution, PII, Syntax Consistency, Duplicate Events/Properties, Deprecated/Unused Data, Unexpected Warnings, Event Consolidation Opportunities, Missing Session ID/Insert ID, Missing Object IDs, plus Use Case Completeness as a tenth cross-cutting check) that an implementation partner applies as a final quality gate. Several items directly extend concepts from earlier courses in this path: Insert ID deduplication for server-side events was introduced technically in IMPL-TECH-1's HTTP/Batch API considerations and reappears here as the direct fix for a duplicate-events audit finding; PII handling echoes IMPL-3's taxonomy-building guidance (from the main Implementing Amplitude Analytics path) and again recommends legal consultation and the User Privacy API/Data Sanitization request as remediation paths, with the caveat that fixing PII issues going forward does not retroactively delete historic data. The course's most consistently tested principle across all five quiz questions is a specific order of operations: diagnose/investigate root cause first (identity logic, naming inconsistency, Insert ID absence), THEN apply a durable structural fix (formal naming conventions plus transformations, unique Insert IDs, gap communication to stakeholders) — explicitly rejecting shortcuts like immediately merging data without investigation, silently working around a use-case gap, or switching tracking methods instead of fixing the root instrumentation issue. This audit-and-recommend skill set closes out the Technical Track by giving partners a formal, repeatable process (documented as "Pass"/"No Pass" results against the Implementation Workbook's "Taxonomy and Data QA" tab) for validating the quality of any Amplitude implementation, their own or otherwise.

---

## Combined Path Summary: Implementing Amplitude Analytics — Technical Track

Taken together, this 5-part technical track deepens the four ingestion-method categories and general implementation lifecycle taught in the main "Implementing Amplitude Analytics" path into concrete, hands-on technical skill: IMPL-TECH-1 supplies the full SDK/API inventory and the Autocapture/HTTP-vs-Batch API decision frameworks; IMPL-TECH-2 specializes that ingestion knowledge into marketing analytics (attribution configuration, channel-definition rule ordering, ad-network integration, audience syncing); IMPL-TECH-3 has learners actually write the instrumentation code against a demo "Battleboat" application and submit a screenshot-documented deliverable for review; IMPL-TECH-4 prepares learners for the inevitable data-discrepancy conversations that follow any real implementation, built around the recurring insight that Amplitude "under-reporting" relative to another source is very often correct, intentional behavior rather than a bug; and IMPL-TECH-5 closes the track with a formal, checklist-driven data-audit methodology that a partner applies as a final quality gate on any implementation. Across all five courses, a few technical themes recur and compound: Insert ID/deduplication logic (IMPL-TECH-1 → IMPL-TECH-5), PII handling and legal-compliance caution (IMPL-TECH-2's channel/CDP discussion → IMPL-TECH-5's dedicated PII audit lesson), and the Snowflake/warehouse-import data-mutability advantage over static S3/Batch imports (IMPL-TECH-1 → IMPL-TECH-4's ad-platform discrepancy fix). Completing this track, on top of the main Implementing Amplitude Analytics path, is what the path's own prerequisite framing positions as full readiness for the technical side of a real Amplitude delivery-partner engagement.
