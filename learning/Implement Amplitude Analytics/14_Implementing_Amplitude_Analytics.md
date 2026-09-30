# Implementing Amplitude Analytics (Learning Path)

**Type:** Multi-course learning path | **Combined estimated time:** ~9-11 hours across all sub-courses

This file combines all sub-courses/items in the "Implementing Amplitude Analytics" learning path into a single document, per the requested format for courses with subcourses. The path consists of 7 items: IMPL-1 through IMPL-5, an "AI-first Implementation Methodology 2026 Updates" course, and an "Implementation Capstone Project" graded assignment.

---

# PART 1: IMPL-1 Implementation Overview [2024]

**Estimated time:** 20 minutes (plus a 1-minute supplementary lesson)

## About This Course

This course kicks off the Implementing Amplitude Analytics learning path. It introduces the overall implementation process, explains the capstone project learners will complete at the end of the path, walks through the implementation phases (Kickoff, Scope, Send in Data, Rollout), and introduces the "value map" concept used to tie the implementation back to customer value drivers.

---

## Lesson: Get credit for your learning even if you work together (1 min)

*This is a plain HTML page (not a Rise/SCORM lesson frame) — full text captured verbatim below.*

This course includes a hands-on capstone project. Depending on your role, you may be asked to pair up with another learner to complete it:

- **Business/Strategy-track learners** may be paired with a **Technical-track learner** to complete the capstone project together, since the project spans both non-technical (scoping, KPIs, stakeholder alignment) and technical (implementation, data governance) work.
- **Technical-track learners** may similarly be paired with a Business/Strategy-track learner.

Even when you work together with a partner on the capstone project, **you still each individually get credit for your own learning and completion** of this course path — pairing up to complete the capstone project does not mean only one partner receives certification credit. Each learner should still complete their own individual lessons, quizzes, and knowledge checks in the path; the capstone project itself is the piece that may be completed collaboratively with a partner.

---

## Lesson: IMPL-1 Implementation Overview (20 min)

*Extracted via `__fetchCourse()` — 9 sub-lessons/sections, including video lessons, hotspot/diagram descriptions, and an inline 5-question Quiz.*

### Section: Learning Experience Overview

**[Video: "Learning Experience Overview", 2 min 42 sec]** — introduces how this learning path is structured: a mix of short videos, hands-on exercises, and a final capstone project. The path is built around 4 core exercises that map to the real implementation lifecycle:
1. Kickoff
2. Scope
3. Send in Data
4. Rollout

The lesson also points learners to available resources and support channels (partner community, documentation, and instructor support) if they get stuck at any point in the path.

### Section: Implementation Process Overview

**[Video: "Implementation Process Overview", 3 min 36 sec]** — walks through Amplitude's standard implementation process end-to-end. The lesson includes a slide/diagram illustrating the "Autocapture Hybrid" process — a hybrid approach that combines Amplitude's Autocapture (automatic, code-free event capture of UI interactions) with custom/manual instrumentation for events that need more precise business meaning. The lesson cross-references a separate "Autocapture Refresher" course in the catalog for learners who want a deeper technical refresher on Autocapture specifically.

### Section: Kickoff

**[Video: "Kickoff", 6 min 21 sec]** — covers how to run an effective implementation Kickoff meeting with a customer. Key preparation steps highlighted:
- Review the **value map** provided by the sales team (documenting the customer's value drivers and areas for optimization) before the meeting.
- Use the Kickoff meeting to align on stakeholders, draft Amplitude KPIs, and set expectations for the rest of the implementation.

A **"Value Map Example"** resource link is provided so learners can see a sample value map document.

### Section: Scope

**[Video: "Scope", 4 min 15 sec]** — covers the Scope phase, where the team finalizes the taxonomy and KPIs that will be tracked in Amplitude, directly mapped to the value drivers identified during Kickoff. Aligning on KPIs is emphasized as the single most critical part of this phase (this point is directly tested in the quiz below).

### Section: Send in Data and Rollout

**[Video: "Send in Data and Rollout", 3 min 09 sec]** — covers the final two phases: getting instrumented data flowing into Amplitude ("Send in Data") and rolling the finished implementation out to the broader customer team/organization ("Rollout").

### Section: Check Your Understanding — Quiz

*This is an inline `type: "quiz"` lesson embedded directly in the course JSON (not a separately-scored quiz page). Extracted programmatically from the lesson's `items` array, where each answer choice carries an explicit `correct: true` flag — this allowed exact determination of correct answers without relying on a visual "Show Answers" review.*

**Q1 (Select all that apply — 4 correct answers). What should you do before the implementation Kickoff meeting? Check the 4 correct answers.**
- ☑ **(correct)** Review the value map from sales
- ☑ **(correct)** Document the suggested value drivers in the Implementation Workbook
- ☑ **(correct)** Draft some Amplitude KPIs in the Implementation Workbook
- ☑ **(correct)** Share training resources
- ☐ Finalize KPIs
- ☐ Draft a taxonomy for the team to discuss

**Q2 (Multiple choice). Sarah has prepared for the Kickoff meeting by sending training links, reviewing a sales-PS handoff doc, and watching a demo of the customer's product so that she can start to draft some Amplitude KPIs to go over in the implementation workbook. What critical step did she miss?**
- ☑ **(correct)** She hasn't reviewed the value map to start with the customer's value drivers and areas for optimization.
- ☐ She hasn't drafted a list of stakeholders, timelines, and risks.
- ☐ She hasn't scheduled a taxonomy review.

**Q3 (Multiple choice). What is the most critical part of the Scope phase? Select the best answer.**
- ☑ **(correct)** Aligning on KPIs
- ☐ Getting consensus on the taxonomy
- ☐ Ensuring customers have completed the self-paced foundational training

**Q4 (Multiple choice). What document can you think of as the roadmap to success for implementation?**
- ☑ **(correct)** Implementation Workbook
- ☐ Kickoff Deck
- ☐ Value Map

**Q5 (Multiple choice). During the Scope phase, the most significant risk to the project's timeline and budget is often scope creep. Which activity in this phase is the best way to proactively mitigate this risk?**
- ☑ **(correct)** Finalizing the taxonomy and Key Performance Indicators (KPIs) that directly map to the agreed-upon value drivers.
- ☐ Establishing a formal Change Request (CR) process that requires a project manager to approve any new events or properties requested after the Scope document is signed.
- ☐ Delivering foundational training to the customer's engineering team on the SDK installation and Autocapture to get data flowing quickly and address technical questions early.

---

## Lesson: Course Feedback

Standard navigational/administrative "We'd love your feedback" survey lesson — not course content (confirmed via direct page text: it renders only a "Previous / Course Feedback / Next Course" navigation shell with no substantive text).

---

### IMPL-1 Summary / Explanation

IMPL-1 sets up the mental model for the entire implementation path: a four-phase lifecycle (Kickoff → Scope → Send in Data → Rollout) anchored by two key artifacts introduced early — the **Value Map** (created by sales, capturing the customer's value drivers) and the **Implementation Workbook** (the living "roadmap to success" document that carries KPIs, taxonomy, and scope decisions forward through the rest of the implementation). The quiz reinforces two specific, testable takeaways: (1) before Kickoff, an implementer should already have reviewed the value map and drafted preliminary KPIs/value drivers in the workbook, and (2) once in the Scope phase, finalizing KPIs/taxonomy tied to the value drivers is both the most critical activity and the best safeguard against scope creep — a more effective mitigation, per the quiz's correct answer, than a formal change-request approval process or additional technical training. This front-loads a theme that recurs throughout the rest of the path: successful implementations are driven by business alignment (value drivers, KPIs) established early, with technical execution (data instrumentation, Autocapture) following from that alignment rather than preceding it.

---

# PART 2: IMPL-2 Scope Phase: Finalize KPIs in Scope [2024]

**Estimated time:** 50 minutes

## About This Course

*Note: this course page displays a banner — "This course has been temporarily re-opened as of June 2026. Please bear with us as we await further changes to the implementation process from our Customer Delivery team. We hope to update our curriculum to reflect the new process and deliverables by August. The AI-first Methodology course, now added to the end of this learning path, explains some of the process changes."*

This foundational course provides an overview for delivery partners of how to finalize the KPIs in scope of an implementation project. This course is the first in a learning path designed to train delivery partners to successfully implement Amplitude for a customer.

After taking this course you'll be able to:
- Develop value drivers, areas for optimization, and KPIs using the Implementation Workbook
- Distinguish between business KPIs and Amplitude KPIs
- Follow best practices when developing KPIs
- Answer common customer questions about this phase

---

## Lesson: KPI Alignment & Scoping (4 min)

**[Video embedded — title/topic: "KPI Alignment & Scoping", 4 min]** — this lesson consists of an embedded instructional video with no additional on-page text content beyond the video itself. (No transcript is exposed in the page data; duration and topic are as captured from the lesson title.)

## Lesson: What makes a good KPI? (6 min)

**[Video embedded — title/topic: "What makes a good KPI?", 6 min]** — video content (no transcript exposed).

**A Good Amplitude KPI is...** (numbered list):
1. Linked to a major product change made recently
2. Attached to a product team's decision/hypothesis
3. Immediately actionable
4. Linked to a Value Driver

**Worked examples table** (reproduced in full):

| KPI Best practice | Value driver/Area for optimization | Possible Amplitude KPIs |
|---|---|---|
| Linked to a major product change made recently | Example 1: We recently added 3 more features to help customers discover relevant content. We don't know if that has increased the amount of time user spends in the app. | # unique users; Amount of time user spends in the app if they have engaged in 0-3 features. |
| Attached to a product team's decision | Example 2: We are unsure if we should continue investing in our 'Favorites' feature and would like to understand if that feature is impacting our \<enter business metric\>. | # subscribed users using 'Favorites' feature; # unsubscribed users using 'Favorites' feature |
| Immediately actionable | Example 3: We would like to understand the key flows within in our product so we could build funnels on those to track which steps have the highest dropoff. Knowing this would help us build features to minimize the dropoffs and increase our conversion. | # dropoffs and location of dropoffs in key user flow |

## Lesson: Implementation Workbook: Example KPIs for FinTech (3 min)

**Sample Scope Tracker.** Take a closer look at the sample scope tracker (implementation workbook) for a FinTech customer.

**[Video embedded, 3 min]** — walkthrough of the sample FinTech scope tracker (no transcript exposed).

## Lesson: Trainer feedback on learners' KPIs (5 min)

Listen in on a past virtual bootcamp as training manager Amish Patel gives feedback to Group B on their first draft of KPIs using the Implementation Workbook. Take a look at their value drivers and KPIs in the link below. What do you think they got right? What would you do differently? Watch the videos to hear the trainer's feedback.

**GROUP B KPIs** — "Past Bootcamp Group B's KPIs" — button link to open Group B's Implementation Workbook and review their value drivers and aligned KPIs: `https://docs.google.com/spreadsheets/d/12xALsuPi03x4kHptSv5ZuhhtSlqtHANF_XT3TPbmMrs/view` (external Google Sheets document, not reproduced here — linked resource only).

**[Video: "Positive feedback on Group B's KPIs"]** — embedded video, no transcript exposed.

**[Video: "Constructive feedback on Group B's KPIs"]** — embedded video, no transcript exposed.

## Lesson: Quiz (Check Your Understanding)

*Extracted programmatically from the inline quiz lesson's `items` array (same technique validated in IMPL-1) — each answer's `correct` boolean captured directly.*

**Q1. True or False: You can usually copy and paste the KPIs from the value map into the Implementation Workbook as is.**
- ☑ **(correct)** True
- ☐ False

**Q2. In a KPI alignment meeting, your customer presents 40 KPIs they want to put in Amplitude. What's your next best response or action?**
- ☑ **(correct)** "I understand you're excited to start measuring so many things, but in this first phase, it's better to focus on a smaller set of questions to help standardize, iterate faster, and see quicker time to value. Your SOW also sets a limit of [X] KPIs. Let's discuss which will make the biggest impact on your value drivers."
- ☐ "Great, thanks for being so thorough! You're going to see so many incredible insights in Amplitude that you can start acting on right away. Our next step is to review these and ensure they're linked to a value driver."
- ☐ "I appreciate how thorough you've been, but unfortunately your Statement of Work (SOW) says this project is limited to [X] KPIs, so we won't be able to set all those up. Which are your top priority?"

**Q3. Example 1: We would like to understand the 3 drivers of retention. Identify whether this example follows a best practice or not, and if so, which one.**
- ☑ **(correct)** Does not follow a best practice
- ☐ Linked to a major product change made recently
- ☐ Attached to a product team's decision/hypothesis
- ☐ Immediately actionable

**Q4. Example 2: We recently added a new feature to help customers schedule fitness sessions. We don't know if that has increased their use of the app.**
- ☑ **(correct)** Linked to a major product change made recently
- ☐ Attached to a product team's decision/hypothesis
- ☐ Immediately actionable
- ☐ Does not follow a best practice

**Q5. Example 3: We are unsure if we should continue investing in our 'Recommended' feature and would like to understand if that feature is impacting a key business metric.**
- ☑ **(correct)** Linked to a major product change made recently
- ☐ Attached to a product team's decision/hypothesis
- ☐ Immediately actionable
- ☐ Does not follow a best practice

**Q6. Example 4: We would like to figure out how to improve conversion.**
- ☑ **(correct)** Does not follow a best practice
- ☐ Linked to a major product change made recently
- ☐ Attached to a product team's decision/hypothesis
- ☐ Immediately actionable

**Q7. Example 5: We would like to understand the key flows in our product so we can build funnels on those to track which steps have the highest dropoff. Knowing this would help us build features to minimize the dropoffs and increase our conversion.**
- ☑ **(correct)** Immediately actionable
- ☐ Linked to a major product change made recently
- ☐ Attached to a product team's decision/hypothesis
- ☐ Does not follow a best practice

## Lesson (Practice, ungraded): Your turn: Develop KPIs

You are implementing Amplitude for a media streaming customer called AmpliTunes. The sales team has shared a Value Map with you. Use the value map to fill out the following columns in the Implementation Scope Tracker in a blank Implementation Workbook: Value drivers, Areas for Optimization, and KPIs (develop 8-10). After submitting a link to your KPIs, learners unlock the next lesson, which shows exemplary KPIs created by past learners in the bootcamps, to self-check their work. This exercise is not manually graded, but is a practice opportunity that helps prepare learners for the capstone project (which is graded). The course notes it may review learner submissions to improve the course's own coaching material, and may request sheet access if not shared as "visible to anyone with the link." Learners are told to keep their copy of the workbook for use in the next course (IMPL-3).

## Lesson (Practice): Example KPI Exercises

Review of exercises submitted by past Partner Implementation Bootcamp participants, to compare against one's own first-draft KPIs — three linked example workbooks referenced (external Google Sheets, not reproduced): "Example KPIs for AmpliTunes (SEP 2024 Group B)", "Example KPIs for AmpliTunes (MAR 2024 GROUP 2 Edited Partner Impl Bootcamp)", "Example KPIs for AmpliTunes (MAR 2024 GROUP 1 Edited Partner Impl Bootcamp)". Note in the lesson: these examples use an older version of the implementation workbook.

## Lesson: Course Feedback (optional)

Standard optional feedback survey lesson — not course content.

---

### IMPL-2 Summary / Explanation

IMPL-2 goes one level deeper into the Scope phase introduced in IMPL-1, focusing specifically on how to turn a sales-provided value map into a finalized, actionable set of Amplitude KPIs. The core teaching model is a 4-part "Good KPI" checklist (linked to a recent product change, attached to a product team's decision/hypothesis, immediately actionable, linked to a value driver), which the quiz then drills repeatedly by presenting five example "value driver" statements and asking learners to classify which single best-practice criterion each one satisfies (or whether it satisfies none, as in the vague "understand the 3 drivers of retention" and "figure out how to improve conversion" examples — both scored as **not** following a best practice, since neither is concrete or actionable enough to map to a specific Amplitude query or event). The quiz's customer-conversation question (Q2) is also notable for modeling client-facing communication: the correct response neither simply accepts an oversized 40-KPI request nor flatly refuses it by citing contract limits, but reframes the conversation around focus, iteration speed, and value-driver alignment while still referencing the SOW's KPI limit. The lesson on "Trainer feedback on learners' KPIs" reinforces the same material experientially, by having learners review a real past bootcamp group's draft KPIs against the same criteria. Overall, IMPL-2 operationalizes the single most-emphasized takeaway from IMPL-1's quiz (that finalizing KPIs is the most critical part of the Scope phase) into a concrete, repeatable evaluation method.

---

# PART 3: IMPL-3 Scope Phase: Build a Taxonomy [2024]

**Estimated time:** 70 minutes

## About This Course

*Note: this course page displays the same "temporarily re-opened as of June 2026" banner referencing the AI-first Methodology course, as seen on IMPL-2.*

This foundational course provides an overview for delivery partners of how to build a taxonomy in Scope of an implementation project. This course is the first in a learning path designed to train delivery partners to successfully implement Amplitude for a customer.

After taking this course you'll be able to:
- Translate customer use cases into event taxonomies/schemas using the Implementation Workbook
- Follow best practices when developing taxonomies/schemas
- Explain the goals and required participants of Taxonomy sessions

---

## Lesson: Overview of Building Taxonomy (4 min)

**[Video embedded, 4 min]** — no transcript exposed.

**High-level overview image**: a hero image illustrating the Amplitude implementation process at a high level.

**"A great taxonomy should..." (3-item accordion, reproduced in full):**
- **Align with goals** — Align with your goals and KPIs; consider the user journey and critical paths in your product; don't try to track everything immediately.
- **Include the right events** — Include clear event types that define user actions in your product; include event properties and user properties to add more value to event and user information.
- **Be well organized** — Clear and consistent naming convention; separate into different projects if the data being tracked is significantly different; organize events and related properties in a document.

**Cross-reference:** links to the "Essentials of Data Management" learning path in the Partner Academy for more detail (`https://trainingpartners.amplitude.com/path/essentials-of-data-management-learning-path` — see this catalog's own combined file for that path's full content).

## Lesson: Planning your Schema (6 min)

**[Video embedded, 6 min]** — no transcript exposed.

**"Starting points for a healthy schema" (numbered list):**
1. Create example events and properties within taxonomy template in Data Management platform or implementation workbook.
2. Standardize your taxonomy events and syntax.
3. Validate that the taxonomy will answer the implementation scope (KPIs).
4. Data QA to ensure that production data meets defined standard.

**Linked resource:** "Data planning playbook" — *"Naming convention is important! This data playbook will help you understand the basics of users, events, and properties, and learn techniques for planning your taxonomy."* (`https://amplitude.com/docs/data/data-planning-playbook`)

## Lesson: Example taxonomy (11 min)

**[Video embedded, 11 min]** — Amish walks through the Events tab of a sample Implementation Workbook. Linked resource: "Sample Events tab" (external Google Sheet, not reproduced): `https://docs.google.com/spreadsheets/d/16-AjJUGBON7AzSvfY9M_vHoLZQagHz6lyRy9VeFJevo/edit`.

## Lesson: Common Pitfalls (3 min)

**[Video embedded, 3 min]** — no transcript exposed.

**Event naming pitfalls.** Include inconsistent naming and overly/under-descriptive naming. For example, "user completed signup using Gmail account" is overly descriptive. Instead, name the event "signup completed" and add an event property for "account type."

**Bloated Taxonomy.** Over time, customers will have more and more events in their Amplitude instance. If they don't regularly review and prune their taxonomy, this can lead to unused events, making it difficult for business users to find the relevant data points for their analysis. Tracking unique events for every user action can also result in bloated taxonomies — consider using event properties to consolidate events where applicable.

**Capturing PII.** In attempting to track every data point possible, customers may unintentionally start tracking PII (e.g. names, addresses, phone numbers, etc.). Amplitude can accept PII, but customers should always seek approval from their legal and privacy teams before doing so. Plan your taxonomy with this in mind. The most common PII sent to Amplitude is users' email addresses (often as User ID). Amplitude typically recommends customers use UUID/GUID type identifiers. Most customers have some form of internal identifier which is ideal for this purpose. If they don't have anything other than emails, they can consider hashing the email addresses before sending them to Amplitude.

## Lesson: Model Taxonomy Examples (2 min)

**[Video embedded, 2 min]** — "Practice building cohorts by following along with the video below, using the GTM Demo Environment."

**Example Taxonomies by Vertical:** Media, E-Commerce, B2B.

**Example Customers' Taxonomies:** Online Job Marketplace (+ properties), Email Service Provider Web App, Rideshare Marketing Website.

Cross-reference: "Industry Best Practice Guides" — include sample KPIs (also called use cases/business questions), a recommended taxonomy, and complementary dashboards, tailored to e-commerce, fintech, publications, streaming media, B2B, and healthcare sectors. Noted as revisited later in the "Rolling and Dashboarding" module.

## Lesson: Quiz (Check Your Understanding)

*Extracted programmatically from the inline quiz lesson's `items` array.*

**Q1 (Select all that apply). Which of the following events follow naming best practices?**
- ☑ **(correct)** Favorited song
- ☐ Ticket purchased
- ☐ Playlist added
- ☐ Added playlist
- ☐ Signup
- ☐ Playlist
- ☐ Favorited
- ☐ Clicked CTA from iOS device

*(Note: although phrased "select all that apply," the extracted data marks only "Favorited song" with an explicit correct flag — consistent with the best-practice naming convention of "[Object] [Past-tense Verb]" taught earlier in this lesson, e.g. "signup completed" rather than "user completed signup." The other options either invert this order, omit an object, or are too vague/under-descriptive.)*

**Q2 (Select all that apply). Minah is planning a meeting to go over the schema with the customer. Who should she invite?**
- ☑ **(correct)** Project lead
- ☐ Technical lead
- ☐ Business lead

**Q3 (Multiple choice). You are reviewing your customer's taxonomy and you realize that the User IDs they collect are user email addresses. What's a good next step?**
- ☑ **(correct)** Recommend that the customer use UUID/GUID type identifiers. If they do not have some form of internal identifier, then they may consider hashing the email before sending it to Amplitude.
- ☐ Tell the customer that Amplitude will not accept this data without their legacy and privacy teams signing off on this beforehand.
- ☐ Explain to the customer that this data must be ingested in a specific way to comply with GDPR, and also recommend that they hash the emails before sending.

## Lesson (Practice, ungraded): Your turn: Build a Taxonomy

Define a taxonomy for the KPIs created in the IMPL-2 KPI exercise with AmpliTunes. Learners fill out the Events tab in their copy of the implementation workbook, following best practices and including Event & User Properties. Submitting a link unlocks the next lesson with exemplary taxonomies from past bootcamp learners for self-comparison. Not manually graded, but a practice opportunity whose submissions help improve the course.

## Lesson (Practice): Example Taxonomy Exercises

Review exercises from past Partner Implementation Bootcamp participants: "Example Taxonomy for AmpliTunes (MAR 2024 GROUP 2 Edited Partner Impl Bootcamp)" and "Example Taxonomy for AmpliTunes (MAR 2024 GROUP 1 Edited Partner Impl Bootcamp)" (external Google Sheets, not reproduced).

## Lesson: Course Feedback (optional)

Standard optional feedback survey lesson — not course content.

---

### IMPL-3 Summary / Explanation

IMPL-3 completes the Scope phase trilogy started conceptually in IMPL-1 and continued in IMPL-2: having aligned on value-driven KPIs, the implementer now translates those KPIs into a concrete event taxonomy (the actual events, event properties, and user properties that will be instrumented in the product). The course teaches a three-pillar definition of a good taxonomy — aligned with goals, including the right events, and well organized — and reinforces consistent, un-bloated naming conventions with a specific pattern (object + past-tense verb, e.g. "Favorited song," "signup completed") that the quiz tests directly. A recurring cross-cutting concern introduced here for the first time in this path is **PII handling**: the course explicitly flags that customer taxonomies often unintentionally capture PII (most commonly email addresses used as a User ID) and recommends UUID/GUID-style identifiers or hashed emails instead, always with legal/privacy sign-off — a theme that echoes the data-governance material covered in this catalog's "Essentials of Data Management" course (explicitly cross-referenced in this lesson). The quiz's meeting-invite question (Minah's schema review) reinforces a process/soft-skill point rather than a technical one: only the "Project lead" is marked as the necessary invitee in the extracted data, suggesting the lesson's stakeholder-management guidance treats the project lead as the essential participant for this particular meeting type, distinct from technical or business leads who may be relevant at other points in the process.

---

# PART 4: IMPL-4 Send in Data [2024]

**Estimated time:** ~1.5 hours

## About This Course

*Note: same "temporarily re-opened as of June 2026" banner as IMPL-2/IMPL-3.*

This foundational course provides an overview for delivery partners of the Send in Data phase of an implementation project.

After taking this course you'll be able to:
- Explain the goals and required participants of an Engineering/Instrumentation Kickoff
- Choose the right method of sending data
- Apply user properties and user IDs correctly
- Conduct a Data QA (Data Validation) in Amplitude

---

## Lesson: Data Ingestion Methods (10 min)

**[Video embedded, 10 min]** — no transcript exposed. Accompanied by a hero image.

**Interactive sorting exercise: "Instrumentation support sessions"** — *"Sort the activities below into one of the 3 pillars you should cover at instrumentation support sessions."* Extracted programmatically from the interactive block's `piles`/`items` structure (pile assignments below are the activity's correct/intended pillar):

| Pillar | Activities |
|---|---|
| **Confirm Ingestion Method** | Re-align on handoff/kickoff ingestion methods; Identify sources of data and customer specific issues; Call out/identify blockers and resolution paths |
| **Review Amplitude Schema** | Understand what an "event" represents; User and Event property distinctions; User identification; Session tracking |
| **Best Practice Review** | SDK options; Developer best practices; Backend/supplemental events |

**Knowledge check (matching): "Choose the Right Data Ingestion Model"** — match the data ingestion model to its benefit/reason for use:
- **Client-side** → Simplest initial instrumentation.
- **Server-side** → Track server-side events; leverage existing user data tracking workflows.
- **Hybrid** → Benefits of simpler implementation and ability to track server-side events.
- **Data Layer** → Already have a 3rd-party data layer; can be extremely easy if the CDP is already in place.

**Full ingestion-method reference table (reproduced in full):**

| Method | Description | Why? |
|---|---|---|
| Client-side | Install Amplitude's SDK onto clients and tag events for tracking (incl. Google Tag Manager) | Simplest initial instrumentation |
| Server-side | Connect in-house data pipeline; map existing data to Amplitude's event schema | Track server-side events; leverage existing user data tracking workflows |
| Hybrid | Combination of client-side and server side | Benefits of simpler implementation & ability to track server-side events |
| Data Layer | Turn on connection to Amplitude within your existing data layer (Segment, mParticle, etc.) — events get sent automatically | Already have a 3rd-party data layer; can be extremely easy if the CDP is already in place |

**Sources listed:**
- *Client-side:* Open Source Amplitude SDKs (docs) — Web: TypeScript/JavaScript, React; Mobile: Android, iOS, Unity Plugin, Flutter, React Native.
- *Server-side:* Node.js (docs), HTTP API (docs), Batch Event Upload API (docs), Java (docs), Python (docs).
- *Third Party (docs):* mParticle, Segment, Google Tag Manager, Tealium, and many more.

## Lesson: Amplitude Schema (7 min)

**[Video embedded, 7 min]** — no transcript exposed. Linked resource: "User properties" documentation article on user properties and event properties and how they're applied (`https://amplitude.com/docs/data/user-properties-and-events`).

## Lesson: User identification (3 min)

**[Video embedded, 3 min]** — no transcript exposed. **"Three identifiers used to handle unique users"** — linked article helps readers grasp how Amplitude identifies and tracks unique users with an Amplitude ID, and merge unique users who have more than one Amplitude ID (`https://amplitude.com/docs/data/sources/instrument-track-unique-users`).

## Lesson: Tracking users across products and devices (5 min)

**[Video embedded, 5 min]** — accompanied by a hero image. No further on-page text content beyond the video.

## Lesson: QA/Validation in Amplitude (3 min)

**[Video embedded, 3 min]** — no transcript exposed.

**Event explorer.** If instrumenting Amplitude on web with the Browser SDK, install Amplitude's Chrome extension to see events being triggered in real time while interacting with the website. Alternatively (or if not using SDKs), use the in-tool event explorer to key in on a specific device or user ID and validate events/properties in real time as they're triggered.

**Event Segmentation + User Lookup.** When validating Amplitude event and user counts against other tools or internal systems, use the Event Segmentation chart to look at aggregated metrics for a specific event or user segment. Use User Lookup to dig into a specific user's event stream, raw event payloads, and individual property details. **Note:** when validating against other tools, pay close attention to whether uniques (Amplitude counts both unique devices + users) or event totals are being compared, and to any event time zone differences.

## Lesson: Quiz (Check Your Understanding)

*Extracted programmatically from the inline quiz lesson's `items` array.*

**Q1. Avery is planning the agenda for instrumentation support sessions with their customer. They confirm the ingestion method and review the Amplitude schema. What third topic or pillar should they cover at these sessions that's not included in the other two topics?**
- ☑ **(correct)** Review best practices
- ☐ Go over user identification and session tracking
- ☐ Identify any blockers and resolution paths for data ingestion

**Q2. Your customer wants to collect all the behavioral data like Clicks, Page Views, Screen Views in their product. They also want to bring in additional data from a CRM and other databases which is not available on the client side. What is the right data ingestion method for this customer?**
- ☑ **(correct)** Hybrid
- ☐ Client-side
- ☐ Server-side
- ☑ **(correct)** Data layer

*(Note: this question's extracted data marks two answers — "Hybrid" and "Data layer" — as correct, consistent with the question describing both a need for client-side behavioral tracking and server-side/CRM data integration, which the course's reference table maps to both the Hybrid and Data Layer methods.)*

**Q3. A customer has a CDP and an existing data structure in place. What is the right data ingestion method for this customer?**
- ☑ **(correct)** Data layer
- ☐ Client-side
- ☐ Server-side
- ☐ Hybrid

**Q4. You've kicked off the QA phase with your customer. You need to validate Amplitude event and user counts against your customer's internal system. Which validation tool should you use?**
- ☑ **(correct)** Event Segmentation chart
- ☐ Amplitude Event Explorer
- ☐ User Lookup

## Lesson (Practice, optional): Your Turn: Send data to Amplitude

Practice sending data to Amplitude using the HTTP API to send three event requests, following instructions in a linked doc. Framed as a good exercise for business strategy/engagement-manager type roles to build empathy/intuition for what it means to send data into Amplitude; technical roles are directed instead to get hands-on SDK practice via the separate "Implementing Analytics Technical Track" course (Task 15 in this catalog). Learners can use the partner-training org for this exercise but won't be able to verify their input there (not an admin in that org) — a sandbox org destination project is suggested instead so the data can be checked.

## Lesson: Course Feedback (optional)

Standard optional feedback survey lesson — not course content.

---

### IMPL-4 Summary / Explanation

IMPL-4 moves from planning (Scope: KPIs and taxonomy) into execution — actually getting instrumented data flowing into Amplitude. Its central decision framework is the four data-ingestion methods (Client-side, Server-side, Hybrid, Data Layer), each mapped to a specific customer situation: pure behavioral/UI tracking calls for client-side; backend-only data calls for server-side; a need for both calls for Hybrid; and an existing CDP/data-layer investment calls for the Data Layer method — tested directly and repeatedly in the quiz. The course also introduces a three-pillar structure for running "instrumentation support sessions" with a customer's engineering team (confirm ingestion method, review the Amplitude schema, review best practices), reinforced by the sorting exercise. The QA/Validation lesson closes the phase with a practical distinction implementers are expected to apply: use the Event Explorer (or the Chrome extension) for real-time, in-the-moment validation of one's own triggered events, but use the Event Segmentation chart specifically when cross-checking aggregated Amplitude counts against a customer's other internal systems or tools — a distinction the quiz tests directly, and one where a data-discrepancy investigation should always also account for uniques-vs-totals counting differences and time zone mismatches.

---

# PART 5: IMPL-5 Rollout [2024]

**Estimated time:** 40 minutes

## About This Course

*Note: same "temporarily re-opened as of June 2026" banner as the prior IMPL courses.*

This foundational course provides an overview of the Rollout phase of an implementation project, including dashboarding.

After taking this course you'll be able to:
- Explain the goals and required participants of the Dashboarding session
- Translate customer use cases (business goals) into Amplitude chart types, dashboards, and notebooks
- Build charts to address a business question
- Share Amplitude dashboarding best practices to drive adoption
- Answer common customer questions about this phase (e.g. implementation readout, CSAT)

---

## Lesson: Rollout & Dashboarding (4 min)

**[Video embedded, 4 min]** — no transcript exposed.

**Linked resource: "Industry Best Practices"** — *"Check out our industry-specific best practices guides to see sample use cases and business questions, a recommended taxonomy, and complementary dashboards you can use for your implementation, each one tailored to meet the specific needs of the following sectors: e-commerce, fintech, publications, streaming media, B2B, and healthcare."* (`https://amplitude.com/docs/data/data-planning-playbook#next-steps`) — this is the same Industry Best Practice Guides resource referenced earlier in IMPL-3.

## Lesson: Summary (2 min)

**[Video embedded, 2 min]** — recap video with no additional on-page text content beyond the embed itself.

## Lesson: Quiz (Check Your Understanding)

*Extracted programmatically from the inline quiz lesson's `items` array.*

**Q1. At which session do you confirm with the customer that their data in Amplitude answers the scoped business questions or KPIs?**
- ☑ **(correct)** Dashboarding session
- ☐ Implementation readout
- ☐ Data governance workshop

**Q2. True or false: you should always plan to deliver thorough foundational training for the customer at the dashboarding session.**
- ☑ **(correct)** False
- ☐ True

**Q3. True or false: you should build all the charts in advance of the dashboarding session so that you can show the customer how Amplitude is answering their KPIs.**
- ☑ **(correct)** False
- ☐ True

## Lesson (Practice): Your Turn: Dashboarding

Build 3 charts for any 3 KPIs in the Implementation Workbook for AmpliTunes. After saving each chart, select the "More" drop-down menu and set it to "Unlisted." Organize the charts into a dashboard. Add chart URLs to Column E in the Implementation Scope tracker, corresponding to the KPI each one answers.

## Lesson: Course Feedback (optional)

Standard optional feedback survey lesson — not course content.

---

### IMPL-5 Summary / Explanation

IMPL-5 closes out the four-phase implementation lifecycle (Kickoff → Scope → Send in Data → Rollout) with the Dashboarding session — the point at which the customer's now-flowing data is proven out against the KPIs scoped all the way back in IMPL-2. The quiz's two true/false questions push back against two tempting but incorrect instincts: delivering exhaustive foundational training during the dashboarding session (marked false — the session should stay focused on demonstrating the KPIs, not serve as a full training event), and fully pre-building every chart before the session rather than building at least some of them live/collaboratively with the customer (also marked false). Read together with IMPL-3's and IMPL-5's shared reference to the "Industry Best Practice Guides," this course reinforces that dashboarding work should lean on Amplitude's sector-specific templates (e-commerce, fintech, publications, streaming media, B2B, healthcare) rather than building every chart from scratch. This is also the final graded checkpoint before the path's capstone project, which the "Your Turn: Dashboarding" exercise directly rehearses using the same AmpliTunes workbook exercise learners have been building since IMPL-2.

---

# PART 6: AI-first Implementation Methodology 2026 Updates

**Estimated time:** 90 minutes

## About This Course

This course is for Certified Delivery Partners to get up to speed on the new AI-first Implementation Methodology updates made in early 2026.

After taking this course you'll be able to apply the updated AI-first methodology:
- Correctly sequencing Week 0 activities
- Securing exec sign-off before instrumentation begins
- Delivering all five AI deliverables
- Consolidating multi-product technical walkthroughs
- Scheduling the Data Governance Workshop during instrumentation
- Uses the new implementation roadmap to orient customers and colleagues to the new approach
- Uses the updated Partnership Kickoff Deck

**IMPORTANT METHODOLOGY NOTE ON THIS COURSE'S QUIZ DATA:** This course's final "Certification Renewal Quiz" was found, upon structural inspection, to have a data inconsistency not seen in any other course in this catalog: for most questions, the per-answer `correct: true` flag and the `corrects` array point to a *different* answer option than the question's own authoritative single `correct` (answer-ID) field and its `feedbackCorrect` text. In every case of this mismatch, the `feedbackCorrect` text explicitly explains why a specific option is right — and that option matches the authoritative single `correct` ID field, not the per-answer flag. The quiz reproduction below uses the `feedbackCorrect`-verified answer as correct in every case; a note flags each question where this mismatch occurred, since it means the "obvious" first-listed option is a deliberately plausible-sounding **wrong** answer for most of these scenario-based questions.

---

## Lesson: Introduction

**What's Changing — and Why It Matters to You.** If you've delivered an Amplitude implementation in the last year or two, some of what you know is still accurate. But three things have converged to change the way we work:
- Amplitude now sells full-platform SKUs — customers are implementing multiple products from day one, not adding them later.
- AI agents are now a standard part of every engagement, not a premium add-on.
- Misalignment at the executive level is one of the most consistent causes of implementations that don't land at renewal.

These three forces are why the methodology has changed. This course covers five specific updates to apply on every new engagement going forward. This is explicitly **not** a re-certification — it won't re-teach taxonomy-building or KPI alignment sessions; it covers only what is new.

**Linked resource:** "Full Platform Methodology Launch deck" — source material for this course's content (`https://docs.google.com/presentation/d/1glT7awCXmPiQ_oTJCIDX_wGK9h-BxCtm/view`).

**[Video 0.1: "Now and Beyond with AI"]** — Alex Ho opens with the bigger picture: what Amplitude's AI-first direction means for how customers expect to work with their implementation partners.

**[Video 0.2: "Why are we changing?"]** — Alex Ho walks through the forces that made the old methodology insufficient for where Amplitude and its customers are headed.

**[Video 0.3: "Summary of Changes"]** — Kelly Casanova walks through the five changes at a high level (detailed further in later modules).

*Clarification on Exec Sign-off: the exec sign-off is required for Emerging Enterprise and Major Enterprise accounts. Velocity accounts have a different process where this is not a hard requirement.*

**Written summary of the five changes:**
1. **Week 0 is now a formal pre-project phase.** Four specific requirements must be confirmed before kickoff begins. These replace the value map in the pre-kickoff process.
2. **Executive sign-off before instrumentation.** The Executive Business lead (EB) must align on use cases and KPI scope before technical work begins. Required for Enterprise accounts (Emerging & Majors); for other accounts it's a strong expectation, not a hard blocker, but skipping it puts the engagement at risk.
3. **Five AI deliverables are now standard on every engagement**, not optional add-ons, applying regardless of implementation package (with one scope-based exception).
4. **Technical walkthroughs should be consolidated for multi-product implementations** — happening in the same week where possible, not in siloed sessions weeks apart. (For subco implementations, Add-On SKUs are assigned.)
5. **The Data Governance Workshop moves earlier** — now during the instrumentation phase, not after production launch, since AI agents depend on clean taxonomy from the start.

*A note on iteration: AI-driven workflows can evolve quickly; enablement material will be updated as the methodology develops.*

## Lesson: Week 0: The New Pre-Project Phase

**Before Kickoff: What Needs to Be True.** In the previous methodology, implementation began at kickoff — that's no longer the case. Week 0 is now a formal pre-project phase: a set of four things that need to be confirmed before walking into the kickoff meeting.

**[Video: "Week 0: Pre-Project Requirements"]** — Kelly Casanova walks through what Week 0 looks like in practice and why each requirement matters.

**JOB AID — Week 0 Checklist.** Week 0 is complete when all four of the following are confirmed:
1. **AI legal approval.** The customer's legal team has reviewed and approved the use of Amplitude AI features (a new requirement driven by enterprise legal processes around AI usage — don't assume it's been handled, confirm it explicitly). *"Done" looks like:* written confirmation from the customer's legal or procurement team that AI features are approved for use.
2. **Engineering alignment across all products.** The engineering team is aware of and aligned on the full scope of products being implemented, not just the first one in the queue — especially important for multi-product engagements where different engineers may own different products. *"Done" looks like:* the engineering lead can confirm who owns instrumentation for each product in scope and has seen the architectural diagram.
3. **Product priority and sequencing confirmed.** The customer has confirmed which products are being implemented and in what order, driving the project plan and determining which technical walkthroughs to schedule first. *"Done" looks like:* a documented project plan or scope agreement showing product sequence, signed off by the project lead.
4. **Architectural diagram validated.** The pre-sales architectural diagram has been reviewed and confirmed accurate before kickoff — this replaces the value map as the primary alignment tool at this stage. *"Done" looks like:* the TSM has provided the pre-sales diagram and the customer's technical lead has confirmed it reflects their actual stack.

**Linked resources:** "Week 0 Checklist" (part of the AI-First Implementation Quick Reference), "Architectural Diagrams" (sample simple/complex pre-sales diagrams), "Project Plan Priorities" (sample documented project plan showing product sequence).

**Embedded knowledge check (select all that apply): "Which of the following are required Week 0 items?"**
- ☑ **(correct)** AI legal approval
- ☐ Value map review
- ☑ **(correct)** Engineering alignment across all products
- ☐ Define use cases with the customer
- ☑ **(correct)** Product priority and sequencing confirmed
- ☑ **(correct)** Architectural diagram validated

*Feedback: value map review and defining use cases are NOT part of Week 0 — both happen after Week 0 is complete. The value map has been replaced by the architectural diagram as the pre-kickoff alignment tool, and use case development happens during kickoff/scoping once these four requirements are confirmed.*

## Lesson: Executive Sign-Off Before Instrumentation

**Getting the Right People Aligned Before Technical Work Begins.** A recurring pattern shows up at renewal: an implementation that went smoothly technically, but the executive sponsor doesn't feel Amplitude delivered what they bought, because use cases and success criteria were never validated with them. Executive sign-off before instrumentation is the checkpoint designed to prevent this.

**[Video: "Executive Sign-Off Before Instrumentation"]** — Kelly Casanova covers what sign-off looks like in practice, when it happens, and what to do when it can't be obtained. *(Note: the video refers to a "CSM" role — CSMs are now TSMs, Technical Success Managers.)*

**Who Owns This Conversation?** In a standard Amplitude implementation, the Amplitude TSM leads the executive sign-off conversation — the TSM is the primary Amplitude contact during implementation, responsible for executive alignment, platform adoption, and keeping the engagement on track. The partner Engagement Manager's (EM's) role is to prepare the use case summary and scoping context that informs that communication. In the Velocity Segment, there is no TSM assigned — the partner EM shares use cases directly with the Amplitude AE and proceeds accordingly.

**Embedded knowledge check 1 (multiple choice): "You're three weeks into a new engagement. The EB hasn't responded to the Use Case sign-off, and the Amplitude TSM suggests proceeding with instrumentation. What do you do?"**
- ☐ Don't begin instrumentation — exec sign-off is required before any technical work can start.
- ☑ **(correct)** Proceed, but document that sign-off was not obtained and flag the risk to the TSM.
- ☐ Proceed — exec sign-off is a best practice but has no real impact on implementation quality.

*Feedback: exec sign-off is a strong expectation, not a hard blocker — you shouldn't hold up a project indefinitely waiting for an EB to respond, but proceeding silently creates risk. Documenting the gap and flagging it to the TSM keeps the issue visible.*

**Embedded knowledge check 2: "The customer's Procurement lead has confirmed AI approval and signed off on the implementation scope. The EB has not been contacted. Is this sufficient?"**
- ☐ Yes — executive-level approval satisfies the requirement.
- ☑ **(correct)** No — the EB specifically needs to align on the use cases because they own the business outcome.
- ☐ It depends on whether the Procurement lead has budget authority.

*Feedback: Procurement approval covers legal/commercial (AI usage, budget, contracts) — necessary but not sufficient. Exec sign-off is specifically about business-outcome alignment, owned by the EB.*

**Embedded knowledge check 3: "In an Enterprise segment Amplitude implementation, who leads the executive sign-off conversation?"**
- ☐ The partner's Engagement Manager.
- ☑ **(correct)** The Amplitude TSM, with the partner EM providing scoping and technical context.
- ☐ The Amplitude Account Executive.

*Feedback: the TSM owns this conversation; the partner EM prepares supporting content. Exception: in the Velocity Segment (no TSM), the partner EM works directly with the AE.*

## Lesson: Five AI Deliverables: Now Standard on Every Engagement

**AI Is No Longer Optional.** Previously, AI features were something partners introduced when asked or when there was time. Now every Amplitude implementation includes five AI deliverables as standard, regardless of package size or product scope — not add-ons.

**[Video: "AI Deliverables Overview"]** — Kelly Casanova introduces the five deliverables and why they're now baseline.

**[Video: "Goals of the Agent Rollout for Admins Training"]** — Kelly covers what this (new) training is, how it differs from the Admin Starter Pack, and what partners need to do to prepare.

**Linked video resource:** "Agent Rollout for Admins video" (45 min) — Professional Services team member Xin Cao walks through an early version of the training (`https://amplitude.wistia.com/medias/t6i2uy748t`). Additional AI capability training available at academy.amplitude.com.

**Linked resource:** "AI Deliverables at a Glance" reference table — what each deliverable is, who owns it, when it happens, and scope conditions (part of the AI-First Implementation Quick Reference).

**Embedded knowledge check 1 (select all that apply): "Which of the following are standard AI deliverables required on every Amplitude implementation?"**
- ☑ **(correct)** Agent Rollout for Admins Training
- ☐ Implementation Readout
- ☑ **(correct)** AI Context Layer
- ☐ Autocapture SDK Installation
- ☑ **(correct)** Global Agent Configuration + Dashboard Build
- ☑ **(correct)** Dashboard Agent Setup
- ☑ **(correct)** Session Replay Agent

*Feedback: those are the five. Session Replay Agent is the only one with a scope condition (applies only when Session Replay is in scope); the other four are required regardless of package or product mix. Implementation Readout is a real milestone but not an AI deliverable; Autocapture SDK Installation is a real technical activity but not an AI deliverable, and is no longer the default recommendation for enterprise customers (see the Autocapture guidance update below).*

**Embedded knowledge check 2: "You're mid-engagement and production data has just gone live. Which AI deliverable should you focus on right now?"**
- ☐ Agent Rollout for Admins Training
- ☐ AI Context Layer setup
- ☑ **(correct)** Global Agent Configuration + Dashboard Build
- ☐ Data Governance Workshop

*Feedback: the Global Agent configuration and dashboard build (along with Dashboard Agent setup) happen at production launch, when there's actual data to work with. Agent Rollout for Admins Training happens earlier (Weeks 3-4); AI Context Layer is set up before production launch; Data Governance Workshop is a separate workstream during instrumentation, not an AI deliverable.*

**Embedded knowledge check 3: "A customer's implementation scope does not include Session Replay. Which of the five standard AI deliverables is affected?"**
- ☐ None — all five deliverables are required regardless of scope.
- ☑ **(correct)** The Session Replay Agent only — the other four remain required.
- ☐ Both the Session Replay Agent and the AI Context Layer, because context relies on replay data.

*Feedback: Session Replay Agent is the only scope-conditional deliverable. AI Context Layer is not dependent on Session Replay data — it draws on the customer's broader analytics context.*

## Lesson: Technical Walkthroughs: Consolidate for Multi-Product Implementations

**Multi-Product Implementations: Schedule Walkthroughs Together.** The old pattern scheduled each product's technical walkthrough as that product entered instrumentation — often weeks apart — leaving engineering teams to piece together how everything fits together on their own. The new goal: schedule all technical walkthroughs in the same week where possible.

**[Video 4.1]** — Kelly explains the reasoning and how to handle it when the customer's schedule makes consolidation difficult. *Key nuance: this is a "goal" to work toward, not a hard requirement that blocks the project if unachievable.*

**Embedded knowledge check 1: "A customer is implementing Analytics, Session Replay, and Guides and Surveys. How should you schedule the technical walkthroughs?"**
- ☐ Schedule each walkthrough when that product enters the instrumentation phase — typically 2-4 weeks apart.
- ☑ **(correct)** Aim to schedule all three walkthroughs within the same week, or as close together as possible.
- ☐ Hold a single combined walkthrough only if the same engineering team owns all three products.

*Feedback: same-week consolidation is the goal regardless of team ownership — engineering teams need to hear the full architecture story together to understand cross-product dependencies from the start. If the same week isn't achievable, get as close as possible and document why.*

**Embedded knowledge check 2: "The customer's engineering lead tells you they can only attend one product walkthrough per week due to sprint commitments. What's your best response?"**
- ☐ Respect their constraints — schedule walkthroughs in separate weeks as requested.
- ☐ Escalate to the TSM to require attendance at a consolidated session.
- ☑ **(correct)** Explain why a consolidated walkthrough benefits their team and work together on a schedule that gets as close to the same week as possible.

*Feedback: this is a goal, not a rule — you can't force consolidation, and escalating to require attendance risks damaging the relationship. Explain the benefit (avoiding integration surprises later) and work toward the closest achievable option; document if it truly can't be done.*

## Lesson: Data Governance Workshop: Move It Earlier

**Data Governance Workshop: During Instrumentation, Not After Launch.** Previously scheduled after production launch (once there was real data to look at), which created a consistent problem: governance issues surfaced once live users were already in the product, making fixes expensive and disruptive. The new timing is during instrumentation — Weeks 5-8, before data flows at scale — because AI agents depend on clean, governed taxonomy from the moment data starts flowing.

**[Video: "Data Governance Workshop: Move It Earlier"]** — Kelly explains the old timing, the problem it created, and why moving the workshop earlier is now non-negotiable. *Key rationale to remember: AI agents need clean taxonomy from day one.*

**Embedded knowledge check 1: "A new Analytics implementation is in Week 4. Test data has been sent to the development project and looks clean. When should the Data Governance Workshop be scheduled?"**
- ☑ **(correct)** Now — during the instrumentation phase, before production launch.
- ☐ After production launch, once there is real data to govern.
- ☐ At the end of the engagement, as part of the Implementation Readout.

*Feedback: Week 4 (test data in, taxonomy taking shape) is exactly right — there's still time to catch governance issues before they become production problems.*

**Embedded knowledge check 2: "What is the primary reason the Data Governance Workshop was moved earlier in the engagement?"**
- ☐ To reduce overall project duration and improve time to value.
- ☐ To give the customer more time to implement governance policies.
- ☑ **(correct)** AI agents depend on a clean, governed taxonomy from the time data starts flowing — poor governance directly degrades AI output quality.

*Feedback: reducing project duration is a real secondary benefit, but it's not why this change was made — the primary driver is AI's dependency on clean taxonomy from day one.*

## Lesson: Updates to the Partnership Kickoff Deck

**The Updated Kickoff Deck: What Changed and Why It Matters.** The Partnership Kickoff deck is the primary tool for aligning customers on the implementation process at the start of every engagement. The updated version reflects everything covered in this course — Week 0, exec sign-off, AI deliverables woven throughout, and the new implementation roadmap.

**Linked resource:** "Updated Partnership Kickoff Deck" (`https://docs.google.com/presentation/d/1KjjIF5LyT5W9F3HI9VAPZ8KUqDnBNLaauLCR-1GB0P4/edit`).

**[Video: "Overview of Kickoff Deck Updates"]** — Kelly opens with a high-level summary of what's changed.

**[Video: "Implementation Roadmap Slides"]** (~7 min, the longest clip in the course) — Kelly walks through the updated roadmap slides in detail, including new multi-product versions. *Note: Subco partners are only responsible for delivering the implementations they're assigned — e.g. a customer may have Session Replay in scope, but the subco partner may only be assigned Analytics and Guides and Surveys.*

**[Video: "Architecture Alignment"]** — Kelly covers the architecture alignment slide, what it replaces (the value map), and how to use it with customers.

**[Video: "Project Planning Priorities"]** — Kelly walks through the (new) project planning priorities slide and how it helps set customer expectations on sequencing and resource involvement upfront.

**Embedded knowledge check: "A colleague who hasn't seen the updated Partnership Kickoff deck asks what changed. Which of the following is the most accurate summary?"**
- ☐ The deck now includes an AI section at the end covering the five standard AI deliverables.
- ☑ **(correct)** The deck reflects a new pre-kickoff phase, replaces the value map with an architectural diagram, and shows AI deliverables woven throughout the roadmap rather than added at the end.
- ☐ The main change is a new implementation checklist that replaces the project plan slide.

*Feedback: the updated deck reflects three interconnected shifts — Week 0, the value-map-to-architectural-diagram swap, and AI woven throughout the roadmap rather than bolted onto the end.*

## Lesson: Before You Take the Quiz: Resources and a Note on Autocapture

**Your Reference Materials.** Reference materials to keep handy on real engagements:
- **JOB AID: New Implementation Roadmap** (2-page reference) — Page 1: Week 0 Checklist (the four requirements plus links to sample diagrams/project plan); Page 2: AI Deliverables at a Glance (all five deliverables with owner, timing, scope conditions).
- **AI-First Implementation Quick Reference** (`https://docs.google.com/document/d/1dLgdCEZX0ifmY6d5ZqS2bOCiTzCG9UxTiPTuGYlBr2Y/view`).
- **Implementation Roadmap Slides** — individual roadmap slides for 1-product, 3-product, and 4-product implementations (`https://docs.google.com/presentation/d/1KjjIF5LyT5W9F3HI9VAPZ8KUqDnBNLaauLCR-1GB0P4/view`).

**Autocapture Guidance Update.** Autocapture is **no longer the default recommendation for enterprise customers**. In previous training, Autocapture was presented as a strong default starting point; that guidance has been updated. Amplitude is finding Autocapture is not always the best fit for enterprise implementations — the project team (EM + SA) should now make a judgment call based on the customer's specific context, tech stack, and instrumentation goals. This doesn't take Autocapture off the table — it remains valid for customers who want faster time to value or want to learn their data before committing to precision tracking — but it should now be a **considered** recommendation, not an automatic one. If unsure, discuss with the Amplitude SA or TSM before the technical walkthrough.

**Linked resource:** "Updated Implementation Workbook" — key updates: Week 0 tab, updated roadmap, AI deliverables column (`https://docs.google.com/spreadsheets/d/1RyHS_ylpR5NY5iZKIte_LvhO1MPBP1NGwJ4rwZG9BzE/view`).

## Lesson: Certification Renewal Quiz

*Extracted structurally, with the `correct`-field/`feedbackCorrect`-text cross-check methodology described in the course-level note above (the per-answer `correct:true` flag was unreliable for this specific quiz and is NOT what is reproduced below).*

**Q1.** Your team is preparing to onboard a new enterprise customer implementing Analytics and Session Replay. You have confirmed product priorities, validated the architectural diagram, and received engineering alignment. What still needs to happen before kickoff can proceed?
- ☐ Schedule the KPI alignment session with the customer's business lead.
- ☑ **(correct)** Confirm AI legal approval from the customer's legal or procurement team.
- ☐ Complete the value map review with the sales team.

*Feedback: three of four Week 0 requirements are in place — the missing one is AI legal approval, a new requirement that should be confirmed explicitly, not assumed.*

**Q2.** You're two days away from kickoff. Engineering alignment is confirmed, AI legal approval is in place, and the architectural diagram has been validated. The customer's project lead tells you product implementation sequencing hasn't been formally documented yet but expects to confirm it in the kickoff meeting itself. What do you do?
- ☐ Proceed with kickoff as planned — product sequencing can be confirmed during the meeting.
- ☐ Postpone kickoff until product sequencing is formally documented.
- ☑ **(correct)** Proceed with kickoff, note that product sequencing is still pending, and flag it to the TSM so it gets resolved in the meeting and documented immediately after.

*Feedback: Week 0 requirements are strong expectations, not hard blockers — with three of four confirmed and the fourth days from resolution, postponing is unnecessary; proceed, flag the gap, document it.*

**Q3.** You're four weeks into an engagement. The EB attended the kickoff meeting but has not responded to the use case summary the TSM sent for sign-off two weeks ago. The TSM suggests moving forward with instrumentation. What's the right response?
- ☐ Agree — the EB attended kickoff, which constitutes sufficient alignment.
- ☐ Disagree — instrumentation cannot begin until the EB has formally signed off on the use case summary.
- ☑ **(correct)** Agree to proceed, but ask the TSM to document the outstanding sign-off and continue pursuing it actively while instrumentation begins.

*Feedback: EB attendance at kickoff is a good start but not the same as sign-off; the TSM should keep pursuing sign-off while instrumentation proceeds, with the gap documented.*

**Q4.** A customer's legal team has approved AI usage and the EB has signed off on the use cases. Before instrumentation begins, the EB is replaced by a new executive who says they want to review the scope before proceeding. What do you do?
- ☐ Proceed with instrumentation — the original EB's sign-off is on record and legally sufficient.
- ☑ **(correct)** Pause instrumentation and work with the TSM to get the new EB aligned on the use cases before proceeding.
- ☐ Ask the new EB to confirm AI legal approval since the previous sign-off may no longer be valid.

*Feedback: exec sign-off exists to ensure the person who owns the business outcome is aligned — a new, unbriefed EB is exactly the misalignment risk this requirement prevents; get them up to speed quickly with the TSM.*

**Q5.** You're running a subco engagement and there is no Amplitude TSM assigned. The EB needs to sign off on the use cases before instrumentation begins. What's the correct approach?
- ☐ Wait for an Amplitude TSM to be assigned before pursuing exec sign-off.
- ☑ **(correct)** The partner EM shares the use cases directly with the Amplitude AE and proceeds accordingly.
- ☐ Skip exec sign-off for Velocity Segment customers — it's not required without a TSM.

*Feedback: in the Velocity Segment (no TSM), the partner EM shares use cases with the Amplitude AE directly — exec sign-off doesn't disappear as a requirement, the process just adapts.*

**Q6.** A colleague is preparing for a new Analytics-only implementation and asks which AI deliverables they need to plan for.
- ☑ **(correct)** Agent Rollout for Admins Training, AI Context Layer, Global Agent Configuration + Dashboard Build, and Dashboard Agent Setup — four deliverables, since Session Replay Agent doesn't apply.
- ☐ All five — AI deliverables are required regardless of product scope.
- ☐ Global Agent Configuration + Dashboard Build and Dashboard Agent Setup only — the others are optional for smaller implementations.

*(This is the one question in the quiz where the per-answer flag and the authoritative field agreed.)*

**Q7.** An engagement is in Week 3. The taxonomy is being finalized and the engineering team has just completed their technical walkthrough. Which AI deliverable should be happening right now?
- ☐ Global Agent Configuration + Dashboard Build.
- ☑ **(correct)** Agent Rollout for Admins Training.
- ☐ AI Context Layer setup.

*Feedback: Agent Rollout for Admins Training happens in Weeks 3-4, exactly when the taxonomy is being finalized and engineering is already engaged; Global Agent and AI Context Layer come later.*

**Q8.** You're mid-engagement and about to set up the AI Context Layer. The customer's SA asks what data the context layer draws on.
- ☐ It draws on Session Replay footage to build context around user behavior.
- ☑ **(correct)** It draws on the customer's analytics context — use cases, taxonomy, and goals — to help agents give tailored answers.
- ☐ It is automatically populated by Amplitude based on the customer's event data once production data goes live.

*Feedback: the AI Context Layer is set up with customer-specific context (use cases, taxonomy, goals), not Session Replay data, and requires deliberate configuration before production launch.*

**Q9.** A customer is implementing Analytics and Web Experiment. The Analytics technical walkthrough is scheduled for Week 2. The Web Experiment team says their engineer can't attend until Week 5. What's the best course of action?
- ☐ Proceed with the Analytics walkthrough in Week 2 and schedule Web Experiment separately in Week 5 as requested.
- ☐ Delay the Analytics walkthrough to Week 5 so both products can be covered together.
- ☑ **(correct)** Explain to the Web Experiment engineer why consolidated walkthroughs benefit their team and work toward a schedule that's closer to Week 2 — even if Week 5 is ultimately what's achievable.

*Feedback: the goal is same-week consolidation where possible; make the case for it first rather than accepting the gap without discussion.*

**Q10.** You've successfully consolidated technical walkthroughs for a three-product implementation into the same week. At the end of the session, the customer's engineering lead says they felt overwhelmed by the volume of information and would have preferred separate sessions. How do you respond?
- ☐ Apologize and offer to schedule follow-up sessions for each product separately.
- ☑ **(correct)** Acknowledge their feedback, offer a follow-up Q&A session to address any gaps, and note for future engagements that this customer prefers a different approach.
- ☐ Explain that consolidated walkthroughs are now required and separate sessions are no longer available.

*Feedback: consolidation is a goal, not a rigid rule; acknowledge feedback, offer a practical follow-up, and capture the preference for future engagements without undoing the consolidation benefit.*

**Q11.** A partner EM asks when to schedule the Data Governance Workshop on a new Analytics implementation. The customer's engineering team is currently sending data to the development project.
- ☑ **(correct)** Now — while data is going into the development project, so governance issues can be caught before production launch.
- ☐ After production launch, once there is enough real data to make the governance conversation meaningful.
- ☐ During the rollout phase, alongside the foundational training sessions.

*(Another question where the per-answer flag and authoritative field agreed.)*

**Q12.** A customer's project lead pushes back on scheduling the Data Governance Workshop during instrumentation, preferring to wait until after launch when the team has more context about the data. How do you respond?
- ☐ Agree — the customer knows their team best, and post-launch governance is still better than none.
- ☑ **(correct)** Explain that post-launch governance is possible but means AI agents will start working with ungoverned data from day one, which directly affects output quality — and offer to keep the workshop focused and efficient so it doesn't feel like a burden during instrumentation.
- ☐ Explain that the Data Governance Workshop is a contractual requirement and cannot be moved.

*Feedback: this is the consultative response — explains the real consequence rather than just citing policy, and addresses the customer's underlying bandwidth concern with a practical solution.*

**Q13.** You're about to use the updated Partnership Kickoff Deck with a customer for the first time. A colleague who used the old deck last month asks what's different.
- ☐ The deck is largely the same but includes a new AI section at the end and an updated timeline slide.
- ☑ **(correct)** The deck now opens with a Week 0 slide, replaces the value map with an architectural diagram, and shows AI deliverables integrated throughout the roadmap rather than added at the end.
- ☐ The main structural change is a new implementation checklist that gives customers a clearer view of what's expected of them.

*Feedback: the three most significant changes are the Week 0 formalization, the value-map-to-architectural-diagram replacement, and AI woven into the roadmap from the start.*

## Lesson: Next Steps

*"You've completed AI-First Implementation: Certification Renewal. Your Delivery Certification has been renewed. You'll receive a confirmation email shortly. The methodology will continue to evolve as Amplitude's AI capabilities develop — we'll update this course as needed and let you know when something changes that affects your engagements. In the meantime, the AI-First Implementation Quick Reference and the resources linked throughout this course are your go-to references on new projects. Questions or feedback? Reach out to partner-enablement@amplitude.com."*

---

### AI-first Implementation Methodology — Summary / Explanation

This course functions as a 2026 patch to the IMPL-1 through IMPL-5 methodology covered earlier in this path, driven by three converging forces: full-platform SKU sales (multi-product from day one), AI agents becoming standard rather than premium, and a recognition that executive-level misalignment — not technical execution — is the most consistent cause of implementations that fail to renew. Its five updates layer directly onto the four-phase lifecycle taught earlier: a new **Week 0** pre-project phase (four gate items — AI legal approval, engineering alignment, product sequencing, architectural diagram — replacing the value map as the pre-kickoff artifact) now precedes Kickoff; **executive sign-off** becomes an explicit, TSM-owned checkpoint before instrumentation (Send in Data) begins; **five AI deliverables** (Agent Rollout for Admins Training, AI Context Layer, Global Agent Configuration + Dashboard Build, Dashboard Agent Setup, and the scope-conditional Session Replay Agent) are woven across the engagement timeline rather than bolted on; multi-product **technical walkthroughs** should be consolidated into the same week as a goal (not a hard rule); and the **Data Governance Workshop** — previously covered as following production launch in the earlier IMPL courses — now moves into the instrumentation phase itself (Weeks 5-8), specifically because AI agents inherit whatever taxonomy quality exists when data starts flowing. A secondary but explicit change is that **Autocapture is no longer the default enterprise recommendation** — it remains valid but must now be a deliberate, context-based decision by the EM/SA team rather than an automatic starting point, nuancing the "Autocapture Hybrid" framing taught back in IMPL-1. The course's scenario-based certification quiz repeatedly rewards a specific judgment pattern over its 13 questions: prefer proceeding-with-documentation over rigid blocking, and prefer consultative explanation (making the case, addressing the underlying concern) over either silent compliance or citing policy — reflecting a partner-enablement philosophy that treats these five changes as strong expectations to reason about in context, not bureaucratic checkboxes.

---

# PART 7: Implementation Capstone Project (Analytics) April 2026

**Estimated time:** 5 hours (4-6 hours including a 20-minute presentation and preparation time)

*This item is a graded, hands-on capstone assignment rather than passive lesson content — it is not a standard Rise-based course (no `#scorm_content_frame` was present; it is a plain assignment/exercise page with a file-upload submission mechanism), so it is documented here as "About this assignment" content rather than full lesson extraction.*

## About This Exercise

Welcome! In this exercise, you'll demonstrate that you can successfully implement the Amplitude platform. After you submit a recording, an Amplitude team member will provide feedback within 4 weeks.

## Instructions (reproduced in full)

**Show us you're ready to implement Amplitude!**

1. First, review the "Analytics Implementation Capstone Project April 2026" prompt document. Determine if you will submit a recording or schedule a time to present live.
2. Submit content below depending on your chosen presentation format:
   1. **If you are recording yourself**, submit the video file below.
   2. **If you are presenting live**, submit a relevant file below (e.g. presentation deck) **before** your Zoom meeting! You must upload something in order for this course to be marked "Complete" and to receive your badge.

**If you opt to submit a recording for asynchronous review, you'll need to allow up to 4 weeks for a team member to review your work.** Scheduling a live presentation is recommended instead, because it gives the trainer a chance to ask questions and for the learner to clarify anything (a prompt provides instructions to schedule a live Zoom meeting).

When the team marks this course complete, learners receive an email inviting them to accept their **Certified Amplitude Delivery Partner badge**.

*Note: if the partner's company uses Microsoft, the capstone project prompt is also accessible via a "Spekit Partner Hub" link (external, Microsoft-specific access route).*

## Linked Prompt Document: "Analytics Implementation Capstone Project 2026" (external Google Slides deck, embedded preview — not fully reproduced here as it is an external, partner-facing working document)

Legible content from the embedded preview:

**Overview.** *"Your goal is to work through the main phases of an Amplitude Analytics implementation and present your recommendations to an Amplitude team member. We expect this project to take about 4-6 hours to complete."*

**Capstone Project example:** a link to an "AmpliTunes" exemplary project is referenced (noted in the source document as "to be added after permission received from partner learners" — i.e., a placeholder pending permission from the learners whose example project it showcases).

*(This document is the same underlying prompt whose structure — using the AmpliTunes fictional media-streaming customer, building on the Implementation Workbook, KPIs, and taxonomy developed across the IMPL-2/IMPL-3/IMPL-5 "Your Turn" practice exercises in this path — is consistent with the recurring AmpliTunes exercises used throughout IMPL-2, IMPL-3, and IMPL-5 above.)*

## Lesson: Feedback on capstone project experience

Standard feedback survey lesson — not course content. (The page also displayed unrelated account-specific navigational chrome — "You have completed the quiz! Your responses have been submitted. Your score will be available after all your responses have been graded. Elapsed time: 1 week, 3 days" — which is this learner account's own progress/grading status, not course content, and is noted here only for completeness per instruction to discard nothing, not as instructional material.)

---

### Capstone Project Summary / Explanation

The capstone is the culminating, graded deliverable of the "Implementing Amplitude Analytics" path: rather than teaching new material, it asks the learner to actually perform an end-to-end implementation exercise — working through the main phases of an Amplitude Analytics implementation (mirroring Kickoff, Scope/KPIs, Scope/Taxonomy, Send in Data, and Rollout/Dashboarding as taught in IMPL-1 through IMPL-5) — and then present the resulting recommendations to a live Amplitude team member, either via a scheduled Zoom presentation or an uploaded recording. This directly builds on the recurring "AmpliTunes" practice exercises seeded throughout IMPL-2 ("Your turn: Develop KPIs"), IMPL-3 ("Your turn: Build a Taxonomy"), and IMPL-5 ("Your Turn: Dashboarding") — learners who completed those practice exercises along the way should already have most of the raw material (KPIs, taxonomy, and charts/dashboard) needed for this final presentation. Successful completion and review earns the learner the Certified Amplitude Delivery Partner badge, formally closing out this learning path.

---

## Combined Path Summary: Implementing Amplitude Analytics

Taken as a whole, this 7-part learning path trains a delivery partner through one complete, realistic Amplitude implementation lifecycle, layered twice: once as the "classic" four-phase methodology (IMPL-1 Kickoff/Overview → IMPL-2 Scope/KPIs → IMPL-3 Scope/Taxonomy → IMPL-4 Send in Data → IMPL-5 Rollout/Dashboarding), each phase pairing a conceptual video lesson with a scored knowledge check and an ungraded "Your Turn" hands-on exercise using a consistent fictional customer (AmpliTunes) and a shared "Implementation Workbook" artifact that accumulates KPIs, taxonomy, and dashboard links across courses — and then a second time as a 2026 methodology update layer (the AI-first Implementation Methodology course), which does not replace the earlier phases but inserts new gates and deliverables into them: a Week 0 pre-project phase before Kickoff, executive sign-off before Send in Data/instrumentation, five standard AI deliverables spread across the engagement, consolidated multi-product technical walkthroughs, and an earlier-scheduled Data Governance Workshop during instrumentation rather than after launch. The path closes with a graded capstone project that asks the learner to actually execute this full lifecycle once, live, using the same AmpliTunes-style exercise materials built up during the practice exercises, in exchange for the Certified Amplitude Delivery Partner badge. A recurring cross-cutting theme worth flagging across the whole path is data governance and PII handling (introduced in IMPL-3's taxonomy-building content and echoed in the "Essentials of Data Management" course elsewhere in this catalog), and a second recurring theme is the shift from purely technical execution toward business-alignment and stakeholder-management skills (value drivers, KPI alignment conversations, executive sign-off, consultative pushback-handling) — reflecting Amplitude's own stated rationale that executive misalignment, not technical shortfalls, is the leading cause of implementations that fail to renew.

