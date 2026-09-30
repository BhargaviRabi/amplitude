# Amplitude Analytics Capstone 2026 — Detailed Execution Plan for Claude Code

> **Purpose:** Give this file to Claude Code in VS Code so it can execute as much of the Analytics Implementation Capstone Project 2026 as possible.
>
> **Source basis:** This plan is based on the uploaded Capstone PDF, the official 2026 Implementation Workbook, and the official 2026 Partnership Kickoff Deck. Do not replace the official template structure with an invented one.

---

# 0. YOUR ROLE

You are Claude Code acting as an implementation consultant / technical partner.

Your objective is to produce a high-quality, internally consistent capstone for:

- **Scenario:** AmpliStore 2.0
- **Industry:** E-commerce
- **Reference app:** Zara (use ASOS instead only if the user chooses it)
- **Primary platform:** Web
- **Important traffic dimension:** Mobile browser
- **Customer model:** D2C apparel/accessories
- **Core categories:** Men's clothing, women's clothing, jewelry

The Capstone requires three deliverables:

1. Completed Implementation Workbook
2. Partnership Kickoff presentation using the official 2026 Kickoff Deck template
3. Amplitude charts/dashboards in the partner-training organization

The capstone says the demo dataset in the partner-training organization is for taxonomy/chart reference only and must **not simply be replicated**. Our recommendations must be our own. 

---

# 1. FIRST: INSPECT THE WORKSPACE

Before changing anything:

```bash
pwd
find . -maxdepth 4 -type f | sort
```

Identify:

- official workbook `.xlsx`
- official kickoff deck `.pptx`
- capstone PDF
- training materials
- architecture diagrams
- any Amplitude-related files
- any existing customer/product information

Create:

```text
amplitude-capstone/
├── source/
├── working/
├── output/
├── notes/
└── validation/
```

Do NOT overwrite the original official templates.

Copy them into `working/` before editing.

---

# 2. SOURCE-OF-TRUTH RULES

Use the sources in this priority order:

1. Official uploaded 2026 templates/training materials
2. Capstone PDF
3. User-provided scenario decisions
4. Reasonable mock-scenario assumptions
5. General Amplitude knowledge only where the source materials do not specify something

Clearly label assumptions.

Never fabricate:

- real customer data
- numerical baselines
- Amplitude chart URLs
- partner-training access
- credentials
- implementation status
- AI deliverable names if the official training material does not provide them

If something is unavailable, write `TBD / Requires Confirmation` rather than inventing it.

---

# 3. UNDERSTAND THE OFFICIAL CAPSTONE REQUIREMENTS

The Capstone PDF requires:

## Deliverable 1 — Implementation Workbook

Complete:

- Alignment tab
- KPIs / Scope Tracker tab
- Events tab
- Event Properties
- User Properties
- AI deliverables plan

The workbook also contains supporting tabs that may be useful for QA, integrations, governance, project mapping, etc.

## Deliverable 2 — Partnership Kickoff

Use the official 2026 Kickoff Deck template and present as though the reviewer is the customer's executive sponsor.

## Deliverable 3 — Amplitude Charts

Build charts in the partner-training organization and walk through them live. Screenshots alone are not sufficient.

Passing score is **17/18**.

---

# 4. TARGET RUBRIC

Optimize the entire project for Level 3 in these six areas:

## A — Implementation process

Be able to explain:

- Alignment / Week 0
- Discovery
- Technical Scoping
- Instrumentation
- Enablement and Rollout

Explain the goal of each phase and the role of the implementation team.

## B — Amplitude fundamentals

Explain the Amplitude features used and, more importantly, the value they provide to AmpliStore.

## C — Discovery

Create excellent, well-scoped KPIs based on product value drivers and pain points.

## D — Technical Scoping

Translate customer use cases into an event taxonomy following best practices.

The AI deliverables plan must be complete and correctly sequenced.

## E — Instrumentation

Discuss:

- SDKs
- HTTP API
- data sources
- destinations
- user identification
- ingestion method
- tradeoffs

The rubric specifically expects understanding of HTTP API, SDKs, Snowflake, BigQuery and S3.

## F — Enablement and Rollout

Translate use cases into useful Amplitude charts and dashboards and explain dashboarding best practices.

---

# 5. PROJECT DECISION: AMPLISTORE

Use the following mock business context:

AmpliStore is a D2C retailer selling apparel and accessories across:

- Men's clothing
- Women's clothing
- Jewelry

Customer journeys include:

- product discovery
- search
- filtering
- product detail/reviews
- add to cart
- checkout
- guest checkout
- registered-user checkout
- registration/login
- order management

Web is the main platform and mobile browsers are a significant traffic source.

Do not invent revenue, conversion, customer counts or other numeric baselines.

---

# 6. STEP 1 — ALIGNMENT / WEEK 0

The official Kickoff deck has a Goal Alignment section with:

- Challenges
- Critical Business Use Case
- KPIs

The capstone asks for **four pre-project requirements**.

Use these four for the mock scenario:

## Requirement 1 — Business goals and success criteria

Confirm:

- What business outcome is most important?
- Is conversion the primary objective?
- Is product discovery a major pain point?
- Is checkout abandonment a known issue?
- How will success be measured?

Mock assumption:

> Primary objective: improve purchase conversion by improving product discovery and reducing checkout friction.

Label this as a mock assumption, not customer-confirmed fact.

## Requirement 2 — Stakeholders and ownership

Identify:

- Executive Advocate
- Business Lead
- Project Lead
- Technical Lead / Engineering Lead
- Analytics users / power users

The official deck identifies these customer roles and describes their responsibilities.

## Requirement 3 — Data and technical architecture

Confirm:

- web technology
- analytics implementation
- Amplitude project structure
- SDK/API usage
- backend order system
- data warehouse
- data destinations
- user identification approach
- development/staging/production environments

## Requirement 4 — Scope and priority

Confirm:

- product/platform priority
- top 2–3 use cases
- 10–15 supporting business questions
- event scope
- KPI scope
- chart/dashboard scope
- launch target
- engineering availability

---

# 7. STEP 2 — USE CASE ALIGNMENT

The official deck says Use Case Alignment should identify:

- 2–3 initial Amplitude use cases
- 10–15 supporting business questions

For AmpliStore, use these 3 primary use cases:

## Use Case 1 — Product Discovery Optimization

Goal:

> Understand how users discover products and which discovery behaviors lead to product engagement and purchase.

## Use Case 2 — Purchase Funnel Optimization

Goal:

> Understand conversion from product view through cart, checkout and completed purchase.

## Use Case 3 — Checkout Optimization

Goal:

> Identify where users abandon checkout and which segments experience the greatest friction.

---

# 8. SUPPORTING BUSINESS QUESTIONS

Create 10–15 questions.

Recommended set:

1. What percentage of product viewers add an item to cart?
2. What percentage of cart users begin checkout?
3. What percentage of checkout starters complete a purchase?
4. Where is the largest drop-off in the purchase funnel?
5. Does conversion differ between mobile web and desktop?
6. Which product categories have the strongest add-to-cart rate?
7. Which categories have the strongest purchase conversion?
8. Do users who search convert differently from users who browse without search?
9. Which filters are associated with stronger product engagement?
10. Do users who view reviews have different purchase behavior?
11. Do guest and registered users have different checkout completion rates?
12. What is average order value by category?
13. What is average order value by device type?
14. Do returning users convert differently from new users?
15. Where are checkout users most likely to abandon?

Do not claim answers unless the demo data actually supports them.

---

# 9. STEP 3 — KPIs

Use a small, focused set.

Recommended six:

1. Purchase Conversion Rate
2. Add-to-Cart Rate
3. Checkout Completion Rate
4. Cart Abandonment Rate
5. Product Discovery Conversion
6. Average Order Value

For every KPI, document:

- Value Driver
- Areas for Optimization
- KPI / Metric
- In Taxonomy?
- Validated?
- Autocapture?
- Chart or Metric
- Chart Link
- Additional Notes
- Priority
- Link to Experiment, if applicable

These match the official `Analytics KPIs` sheet structure.

---

# 10. KPI DEFINITIONS

## KPI 1 — Purchase Conversion Rate

Business question:

> What percentage of users who enter the purchase journey complete an order?

Recommended implementation:

```text
product_viewed
→ product_added_to_cart
→ checkout_started
→ order_completed
```

Define the exact funnel population and conversion window in the workbook.

Do not mix incompatible denominator definitions.

## KPI 2 — Add-to-Cart Rate

Question:

> How effectively do product views lead to cart creation?

Potential definition:

```text
users with product_added_to_cart
/
users with product_viewed
```

State the conversion window.

## KPI 3 — Checkout Completion Rate

Question:

> How many checkout starters complete an order?

```text
users with order_completed
/
users with checkout_started
```

## KPI 4 — Cart Abandonment Rate

Question:

> What proportion of users who add products fail to complete a purchase?

Document the exact window/definition.

## KPI 5 — Product Discovery Conversion

Question:

> How effectively do discovery behaviors lead to purchase?

Potential journey:

```text
product_searched
→ product_viewed
→ product_added_to_cart
→ order_completed
```

## KPI 6 — Average Order Value

Question:

> What is the average monetary value of completed orders?

Use `order_completed.total_amount` or the authoritative transaction value.

Do not invent values.

---

# 11. STEP 4 — COMPLETE THE PRODUCT FLOWS TRACKER

The official workbook includes:

`Product Flows Tracker (optional)`

Use it because it makes the presentation easier.

Add critical flows:

## Flow 1 — Product Discovery

```text
Landing / Category
→ Search or Browse
→ Filter
→ Product Detail
```

## Flow 2 — Purchase

```text
Product Detail
→ Add to Cart
→ Cart
→ Checkout
→ Shipping
→ Payment
→ Order Complete
```

## Flow 3 — Account

```text
Registration
→ Login
→ Account
→ Orders
```

## Flow 4 — Order Management

```text
Order History
→ Order Detail
→ Return Request
```

Keep the flow milestones aligned with actual events.

---

# 12. STEP 5 — EVENT TAXONOMY

The official deck recommends instrumenting roughly the top prioritized events that relate to the questions.

Do NOT track every UI click.

Use business-action-oriented events.

Recommended starting taxonomy:

## Discovery

```text
product_viewed
product_searched
category_viewed
filter_applied
```

## Product evaluation

```text
review_viewed
```

## Cart

```text
product_added_to_cart
product_removed_from_cart
cart_viewed
```

## Checkout

```text
checkout_started
shipping_info_added
payment_info_added
order_completed
```

## Account

```text
account_created
login_completed
```

## Orders

```text
order_viewed
return_requested
```

Only keep an event if it supports an actual scoped business question/KPI.

---

# 13. EVENT NAMING RULES

Use one consistent naming scheme.

Recommended style:

```text
object_action
```

Examples:

```text
product_viewed
product_added_to_cart
checkout_started
order_completed
```

Do not mix:

```text
ProductViewed
productViewed
PRODUCT_VIEWED
product_view
```

Consistency is more important than cosmetic naming.

Avoid UI-specific names such as:

```text
red_button_clicked
pdp_button_clicked
checkout_component_clicked
```

unless the business question genuinely concerns that UI component.

---

# 14. STEP 6 — EVENTS AND EVENT PROPERTIES SHEET

The official workbook sheet is:

`Events and Event Properties`

Its columns are:

1. Filter: Example & Defaults
2. Event Category
3. Event Name
4. Business Question
5. Trigger + Event Description
6. Property Type
7. Property Name
8. Sample Values
9. Property Description
10. Platform
11. Implemented?

Populate this structure.

One event may occupy multiple rows because it can have multiple properties.

---

# 15. EVENT DEFINITIONS

Create detailed definitions.

## product_viewed

Trigger:

> User opens a product detail page.

Properties:

- product_id
- product_name
- category
- subcategory
- brand
- price
- currency
- availability
- rating

Business questions:

- Which products/categories receive engagement?
- Which product views lead to cart?
- How does product engagement differ by device?

Platform:

`Web`

Implemented:

`No` unless actual implementation exists.

---

## product_searched

Trigger:

> User submits a product search.

Properties:

- search_term
- results_count
- category
- filters_active
- sort_option

Questions:

- Do search users convert differently?
- Which searches return zero results?
- Does search lead to product engagement?

---

## category_viewed

Properties:

- category
- subcategory
- product_count

---

## filter_applied

Properties:

- filter_type
- filter_value
- category
- results_count

---

## review_viewed

Properties:

- product_id
- rating_average
- review_count

---

## product_added_to_cart

Properties:

- product_id
- category
- quantity
- unit_price
- currency
- cart_value

---

## product_removed_from_cart

Properties:

- product_id
- quantity
- unit_price
- cart_value

---

## cart_viewed

Properties:

- cart_item_count
- cart_value
- currency

---

## checkout_started

Properties:

- cart_value
- item_count
- currency
- checkout_type
- account_type

Potential `checkout_type`:

```text
guest
registered
```

---

## shipping_info_added

Properties:

- shipping_method
- country
- cart_value

Do not store unnecessary personal data.

---

## payment_info_added

Properties:

- payment_method

Never store:

- card number
- CVV
- password
- authentication secrets

---

## order_completed

This is a critical business event.

Properties:

- order_id
- total_amount
- currency
- item_count
- payment_method
- shipping_method
- coupon_code
- checkout_type

Recommended authoritative source:

`Backend`

Reason:

> Completed order and revenue are authoritative business outcomes and should be sourced from the transaction system where possible.

---

## account_created

Properties:

- account_type
- acquisition_source, if legitimately available

---

## login_completed

Properties:

- login_method
- account_type

---

## order_viewed

Properties:

- order_id
- order_status
- order_value

---

## return_requested

Properties:

- order_id
- return_reason
- item_count

Avoid unnecessary personally identifiable information.

---

# 16. STEP 7 — USER PROPERTIES

The official workbook sheet is:

`User Properties`

Its columns are:

1. Sample vs Default Tracking
2. Property Name
3. Question
4. Property Description
5. Sample Values
6. Platform
7. Implemented?

Potential properties:

## account_type

Values:

```text
guest
registered
```

## country

Values:

```text
US
```

Use only if appropriate to the scenario and privacy requirements.

## preferred_category

Potential values:

```text
mens
womens
jewelry
```

## customer_segment

Potential values:

```text
new
returning
loyal
```

## loyalty_status

Potential values:

```text
new
standard
loyal
```

## registration_date

Use only if useful to a real use case.

Do not put event-specific information into user properties simply because it exists.

---

# 17. STEP 8 — USER IDENTIFICATION

The official Kickoff deck says the Engineering Kickoff should cover:

- data ingestion methods
- Amplitude schema
- session tracking
- data management
- User Identification strategy

For AmpliStore propose:

## Anonymous users

Do not assign a permanent authenticated User ID before authentication/identification.

## Authenticated users

After login/registration, identify the user using a stable internal customer identifier.

Avoid email address as the primary analytics User ID when a stable internal ID exists.

Document:

- anonymous identity behavior
- authenticated identity behavior
- identity transition
- logout behavior
- cross-device considerations

Do not claim this has been implemented unless it actually has.

---

# 18. STEP 9 — INSTRUMENTATION APPROACH

The capstone asks you to recommend:

- Precision tracking OR
- Hybrid

Recommended:

# Hybrid

Reason:

### Frontend / SDK

Use for:

- product views
- searches
- category views
- filters
- cart behavior
- checkout progression

### Backend / HTTP API

Use for:

- order completed
- refunds
- returns
- authoritative transaction outcomes

Benefits:

- frontend provides behavioral context
- backend provides authoritative transaction data
- better reliability for revenue/order metrics

Tradeoffs:

- more coordination
- event identity/deduplication considerations
- more engineering ownership

---

# 19. DATA SOURCES AND DESTINATIONS

The official rubric expects discussion of:

- HTTP API
- SDKs
- Snowflake
- BigQuery
- S3

Create the workbook's `Integrations Tracker` entries only for systems that are relevant to the proposed architecture.

Potential architecture:

```text
Web Application
      |
      | Amplitude SDK
      v
Amplitude

Order / Transaction Backend
      |
      | HTTP API
      v
Amplitude

Amplitude
      |
      | Export / downstream integration
      v
Warehouse / Storage / BI
      |
      +-- Snowflake
      +-- BigQuery
      +-- S3
```

Clearly label these as proposed/mock architecture where appropriate.

---

# 20. STEP 10 — OFFICIAL WORKBOOK SHEETS TO USE

The official workbook contains these sheets:

```text
Project Plan Gantt View
Implementation Plan Checklist
Product Flows Tracker (optional)
Analytics KPIs
(Analytics KPI Guidelines)
Events and Event Properties
User Properties
Question Tracker
Integrations Tracker
Amplitude Project Mapping
Bulk Update Event Schema (Import)
Bulk Update Property Groups (Import)
Taxonomy and Data QA
Accounts
Taxonomy Best Practices
Ampl Project Mapping
Governance QA
Project Migration Plan
```

For this capstone, prioritize:

1. Product Flows Tracker
2. Analytics KPIs
3. Events and Event Properties
4. User Properties
5. Integrations Tracker
6. Taxonomy and Data QA
7. Question Tracker
8. Amplitude Project Mapping

Do not corrupt or unnecessarily modify unrelated operational/migration sheets.

---

# 21. ANALYTICS KPI GUIDELINES

Use the official workbook's KPI guidelines.

Do not create vague KPIs.

Avoid statements such as:

> "Understand customer behavior."

Instead make the KPI measurable and tied to a specific product decision.

Good:

> "What percentage of product viewers add a product to cart?"

Better:

> "Did mobile product viewers have a lower add-to-cart rate than desktop users during the selected analysis period?"

Keep KPIs tied to actual business questions.

---

# 22. STEP 11 — AI DELIVERABLES PLAN

The capstone explicitly requires the five standard AI deliverables and their sequencing.

IMPORTANT:

The Capstone PDF available here does **not** list the five names.

The Kickoff Deck does contain current AI-related content, including Global Agent, AI dashboards, AI context, AI admin walkthrough, and related activities, but it does not provide a definitive five-item list in the extracted material.

Therefore:

1. Search all uploaded training materials for the official five names.
2. If found, use the exact official names.
3. If not found, do NOT invent names.
4. Create a clearly marked `AI Deliverables — Requires Official Training Definition` section.
5. Explain what can be sequenced based on the official roadmap without falsely naming missing deliverables.

Relevant official roadmap activities include:

- Confirm legal approval on AI functionality
- AI admin walkthrough
- AI dashboards and set up Global Agent
- Send data to production and set up AI context
- Foundational training for Analytics and AI

---

# 23. AI SEQUENCING LOGIC

Where official definitions are available, sequence AI work around:

## Alignment

- confirm AI scope
- confirm legal/privacy approval
- identify stakeholders

## Discovery

- identify AI-supported business questions
- identify priority dashboards/questions

## Technical Scoping

- determine required event/property context
- prepare taxonomy for AI usefulness
- identify metadata/data governance requirements

## Instrumentation

- send development data
- validate data quality
- prepare production data

## Launch / Enablement

- AI dashboards
- Global Agent setup
- AI context
- foundational training
- governance/maintenance

Do not claim any AI capability is enabled until actually configured.

---

# 24. STEP 12 — AMPLITUDE FEATURES TO EXPLAIN

The presentation should explain customer value, not just product names.

For AmpliStore:

## Funnel

Value:

> Identify where users drop between discovery, cart, checkout and purchase.

## Segmentation / User analysis

Value:

> Compare conversion across device, category, account type and other meaningful dimensions.

## Retention

Value:

> Understand whether users return after initial engagement or purchase.

## Cohorts

Value:

> Create reusable audiences such as high-value purchasers, search users or checkout abandoners.

## Dashboards

Value:

> Give business stakeholders a repeatable view of the highest-value metrics and trends.

## Global Agent

Use only the official wording/capabilities supported by the provided 2026 deck/training material.

The official deck describes Global Agent as an in-product AI analyst that can analyze questions in context and work with events, funnels, cohorts, experiments and session replay.

Do not invent unsupported capabilities.

---

# 25. STEP 13 — CHART PLAN

The capstone requires live charts in the partner-training organization.

Create these chart specifications before opening Amplitude.

## Chart 1 — Purchase Funnel

```text
product_viewed
→ product_added_to_cart
→ checkout_started
→ order_completed
```

Question:

> Where do users drop before purchase?

---

## Chart 2 — Checkout Funnel

```text
checkout_started
→ shipping_info_added
→ payment_info_added
→ order_completed
```

Question:

> Which checkout step has the highest abandonment?

---

## Chart 3 — Product Discovery Funnel

```text
product_searched
→ product_viewed
→ product_added_to_cart
→ order_completed
```

Question:

> Does search effectively move users toward purchase?

---

## Chart 4 — Conversion by Device

Compare:

```text
mobile web
desktop
tablet
```

Question:

> Does mobile web underperform desktop?

---

## Chart 5 — Conversion by Category

Compare:

```text
men's
women's
jewelry
```

Question:

> Which categories have the strongest purchase behavior?

---

## Chart 6 — Search vs Non-Search

Compare downstream behavior for:

- users who search
- users who do not search

Question:

> Does search usage correlate with stronger product engagement/purchase?

Do not claim causation from a simple comparison.

---

## Chart 7 — Guest vs Registered Checkout

Compare:

```text
guest
registered
```

Question:

> Does account type correlate with checkout completion?

---

## Chart 8 — AOV

Analyze:

- average order value
- by category
- by device
- by account type where meaningful

---

# 26. CHART → KPI TRACEABILITY

For every chart add:

- Chart name
- Business question
- KPI
- Use case
- Chart type
- Events
- Filters
- Segments
- Expected insight
- Dashboard
- Status
- Actual Amplitude URL, only after the chart really exists

Never create fake URLs.

---

# 27. STEP 14 — BUILD THE EXECUTIVE DASHBOARD

Recommended dashboard structure:

```text
AmpliStore Executive Analytics
--------------------------------

Purchase Conversion | Add-to-Cart | Checkout Completion | AOV

Purchase Funnel

Checkout Funnel

Conversion by Device | Conversion by Category

Search Effectiveness | Guest vs Registered
```

Prioritize readability.

Avoid filling one dashboard with too many unrelated charts.

Every chart must answer a business question.

---

# 28. STEP 15 — COMPLETE TAXONOMY AND DATA QA

The official workbook contains `Taxonomy and Data QA`.

Use it to document expected validation.

Important checks include:

- anonymous users should not receive permanent authenticated User IDs
- authenticated users should have a unique User ID
- development and production should be separated
- naming should be consistent
- event definitions should be documented
- properties should have appropriate types
- taxonomy should answer the implementation questions
- unnecessary properties should be avoided
- critical transaction data should be validated

Where actual production data is unavailable:

Use:

`N/A — Mock scenario / not yet instrumented`

Do not mark data QA as `Pass` without evidence.

---

# 29. STEP 16 — QUESTION TRACKER

Use `Question Tracker` for unresolved items.

Examples:

| Question | Priority | Status | Owner |
|---|---|---|---|
| What is the final user identification strategy? | P0 | Open | Technical Lead |
| Which backend system is authoritative for order completion? | P0 | Open | Engineering |
| Which warehouse is available for downstream export? | P1 | Open | Data Team |
| Which mobile web flows are in Phase 1 scope? | P1 | Open | Business Lead |
| Which AI deliverables are required by the official training scope? | P0 | Open | Implementation Lead |

Do not leave important assumptions hidden.

---

# 30. STEP 17 — OFFICIAL KICKOFF DECK STRUCTURE

Use the official deck.

The extracted official deck includes these major sections:

1. Partnership Kickoff
2. Introductions
3. Goal Alignment
4. Implementation Roadmap
5. Implementation Scope
6. Action Items

Use the actual template slide order and design.

Do not redesign the entire deck unnecessarily.

---

# 31. DECK — SLIDE CONTENT

## Cover

Replace:

- Presenter Name
- Title / Company
- Date
- Customer name/logo if appropriate

Use:

`AmpliStore 2.0`

---

## Introductions

Use the official Amplitude role structure where appropriate:

- Technical Success Manager
- Customer Success Architect
- Account Executive

For the mock customer side:

- Executive Advocate
- Business Lead
- Project Lead
- Technical Lead

Use mock names only if necessary and clearly treat them as mock roles.

---

## Goal Alignment

Populate:

| Challenges | Critical Business Use Case | KPIs |
|---|---|---|
| Product discovery and conversion opportunities | Product Discovery Optimization | Product Discovery Conversion, Add-to-Cart Rate |
| Drop-off through cart/checkout | Purchase Funnel Optimization | Purchase Conversion Rate, Cart Abandonment |
| Checkout friction | Checkout Optimization | Checkout Completion Rate |

---

# 32. IMPLEMENTATION ROADMAP SLIDE

The official deck's roadmap describes:

## Alignment — Week 0

- Project kickoff
- Confirm legal approval on AI functionality
- Confirm timeline
- Confirm lead roles/responsibilities
- Align on data sources/methods

## Discovery — Weeks 1–2

- Confirm and executive-business signoff on Analytics use cases
- Customer product walkthrough
- AI dashboards / Global Agent setup planning as applicable
- Product/use-case alignment

## Technical Scoping — Weeks 3–4

- Design event taxonomy
- Technical walkthrough
- AI admin walkthrough
- Align instrumentation approach

## Instrumentation — Weeks 5–8

- Send data to development
- Validate test data
- Data Governance Workshop

## Launch / later implementation — Weeks 9–10

- Production launch
- Send production data
- Set up AI context
- Build/validate dashboards

## Enablement and Rollout — Weeks 11–14

- Foundational Analytics/AI training
- Data governance
- Implementation readout
- Rollout

Use the exact official roadmap slide where possible rather than creating a competing timeline.

---

# 33. IMPLEMENTATION SCOPE SLIDES

The official deck includes:

## Business Use Cases to Architecture Alignment

The template says to replace the example with the architecture diagram from sales.

For this mock scenario, use our proposed architecture diagram and label it:

`Mock Architecture — Proposed for Capstone`

Do not present it as a real customer's architecture.

---

# 34. DATA SOURCES & DESTINATIONS SLIDE

Populate:

## Sources

Example:

- Web application → Amplitude Browser SDK
- Order/transaction backend → HTTP API

## Destinations

Only include relevant proposed destinations:

- Snowflake
- BigQuery
- S3

If not actually required by the mock scope, mark as:

`Potential downstream destination / out of Phase 1 scope`

---

# 35. PROJECT ROLES & RESPONSIBILITIES

Use the official table:

| Activity | Amplitude | Implementation Partner |
|---|---|---|
| Project Management / Updates | Owner/Support as applicable | Owner as assigned |
| Use Case Discovery | Owner | Support |
| Event Taxonomy Design | Owner | Support |
| Instrumentation/Data Ingestion | Shared | Shared |
| Data Audit/Validation | Owner | Support |
| Dashboarding | Owner | Support |
| End User Training | Owner | Support |

Adapt based on the role you are presenting.

Do not falsely claim Amplitude/partner responsibilities that are not agreed.

---

# 36. PROJECT PLANNING PRIORITIES

Use the official `Project Planning - Priorities` slide.

For AmpliStore:

### Customer Product Priority

1. AmpliStore Web
2. Mobile Web
3. Account / Order Management

### Amplitude Product Priority

1. Analytics + Global Agent
2. Other products only if actually in scope

Do not add Session Replay, Guides & Surveys, Experiment, etc. as implementation commitments unless the scenario requires them.

---

# 37. ENGINEERING RESOURCING

Answer the official deck questions:

- Same engineering team across all products?
- Different teams per product?
- Sprint/release cycle?

For the mock scenario use:

`To Confirm`

unless training materials specify otherwise.

Do not invent engineering availability.

---

# 38. IMPLEMENTATION PLAN & CHECKLIST

The official deck contains an implementation checklist with:

- Align on use cases
- Align on instrumentation approach
- Complete taxonomy
- Conduct technical walkthroughs
- Send dev data
- QA dev data
- Conduct Data Governance
- Promote to production
- Launch reports
- Launch Global Agent
- Conduct training
- Roll out Amplitude

Use the checklist to ensure no major phase is forgotten.

---

# 39. RISKS / DELAYS

Populate the official slide with realistic mock risks.

Recommended:

## Risk 1 — Engineering resource availability

Impact:

Could delay taxonomy implementation and dev data delivery.

## Risk 2 — User identity strategy not finalized

Impact:

Could cause identity fragmentation and inaccurate cross-device/user reporting.

## Risk 3 — Privacy/legal approval for AI

Impact:

Could delay AI configuration and rollout.

Keep these as potential risks, not confirmed customer issues.

---

# 40. ACTION ITEMS / CLOSE

The official deck's closing section asks for concrete next steps.

Use:

1. Schedule product walkthrough
2. Confirm top 2–3 use cases
3. Confirm KPI scope
4. Confirm technical lead and engineering resources
5. Confirm user identification strategy
6. Confirm ingestion architecture
7. Review taxonomy
8. Send development data
9. Schedule recurring implementation meetings
10. Prepare initial AI/business context where applicable

Assign:

- Owner
- Action
- Target timing
- Dependency

---

# 41. PRODUCT WALKTHROUGH PREPARATION

The official deck asks the customer to prepare a 20-minute product demo focused on key user flows.

For the mock Zara reference walkthrough, demonstrate:

1. Category browsing
2. Search
3. Filtering
4. Product details
5. Reviews
6. Add to cart
7. Cart
8. Checkout
9. Guest/registered flow
10. Account/order history

Use this walkthrough to justify the taxonomy.

---

# 42. PRESENTATION TALK TRACK

Do not read the spreadsheet.

Use this narrative:

```text
Business goal
    ↓
Customer pain point
    ↓
Use case
    ↓
KPI
    ↓
Business question
    ↓
Event taxonomy
    ↓
Instrumentation
    ↓
Amplitude chart
    ↓
Decision/action
```

Example:

> "Our primary objective is to improve purchase conversion. We therefore scoped the purchase journey from product discovery through completed order. The funnel allows the team to identify where customers drop, while device and category segmentation show whether the problem is concentrated in a specific experience."

---

# 43. LIVE AMPLITUDE WORK

If you have authorized access to the partner-training organization:

1. Open the correct scenario/project.
2. Inspect demo taxonomy only as a reference.
3. Do not copy the taxonomy blindly.
4. Build the recommended charts.
5. Validate event/property names against your workbook.
6. Save each chart with a meaningful name.
7. Add the real chart link to the workbook.
8. Add the chart to the dashboard.
9. Test the dashboard.
10. Prepare a live walkthrough.

If you do NOT have access:

Create the chart specifications and leave:

`Chart Link = Pending — must be created in partner-training org`

Never fabricate URLs.

---

# 44. CHART QA

For every actual chart verify:

- correct event names
- correct order of funnel steps
- correct conversion window
- correct filters
- correct segmentation
- correct project/environment
- no accidental test data
- no misleading metric definition

For every dashboard verify:

- chart titles are understandable
- chart purpose is clear
- KPIs are visible
- related charts are grouped
- no redundant charts
- business questions are represented

---

# 45. FINAL WORKBOOK QA

Before finalizing:

## Alignment

- [ ] Four pre-project requirements
- [ ] Challenges
- [ ] 2–3 use cases
- [ ] 10–15 questions
- [ ] Stakeholders
- [ ] Dependencies

## KPIs

- [ ] 5–6 focused KPIs
- [ ] Each tied to a business question
- [ ] Each tied to events
- [ ] Each tied to a chart
- [ ] No invented baseline numbers

## Events

- [ ] Event names consistent
- [ ] Business meaning clear
- [ ] Trigger defined
- [ ] Properties defined
- [ ] Platform defined
- [ ] Implementation status honest

## User Properties

- [ ] User-level only
- [ ] Data types clear
- [ ] Values defined
- [ ] No unnecessary PII

## AI

- [ ] Official five deliverables identified if source exists
- [ ] Correct sequence
- [ ] No fabricated names

## Instrumentation

- [ ] Precision vs hybrid decision
- [ ] Rationale
- [ ] SDK/API
- [ ] user identification
- [ ] sources
- [ ] destinations

---

# 46. FINAL PRESENTATION QA

Check:

- [ ] Official template retained
- [ ] No placeholder `[Customer]`
- [ ] No placeholder `Presenter Name`
- [ ] No `XX` dates unless intentionally marked TBD
- [ ] Consistent terminology
- [ ] Same KPI definitions as workbook
- [ ] Same event names as workbook
- [ ] Architecture matches instrumentation strategy
- [ ] AI section matches workbook
- [ ] Risks and action items are clear
- [ ] Executive narrative is understandable

---

# 47. CONSISTENCY CHECK

Create a machine-readable comparison between:

```text
Workbook KPIs
Workbook Events
Workbook Properties
Presentation KPIs
Presentation Events
Architecture
Chart Specifications
```

Flag:

- KPI exists in slides but not workbook
- Event exists in chart but not taxonomy
- Property exists in chart but not event definition
- Chart has no mapped business question
- Architecture says SDK but workbook says HTTP API
- AI deliverable names differ
- Placeholder remains
- fake URL exists

---

# 48. FILES TO CREATE

Final output:

```text
output/
├── AmpliStore_Implementation_Workbook.xlsx
├── AmpliStore_Partnership_Kickoff.pptx
├── AmpliStore_Architecture.png
├── AmpliStore_Chart_Specifications.md
└── README.md
```

Validation:

```text
validation/
├── consistency_report.md
├── qa_checklist.md
└── unresolved_items.md
```

---

# 49. README CONTENT

The README must include:

## Scenario

AmpliStore 2.0

## Reference app

Zara

## Scope

Product discovery, purchase funnel, checkout.

## Major assumptions

List every mock assumption.

## Deliverables created

List files.

## External/manual work remaining

Especially:

- Amplitude chart creation if no authenticated access
- real chart links
- presentation/recording
- Partner Academy submission
- reviewer scheduling

## Known limitations

State exactly what could not be verified.

---

# 50. DO NOT CLAIM COMPLETION TOO EARLY

There are two meanings of "complete":

## Local artifact complete

The workbook, deck, architecture and documentation have been created and validated.

## Capstone complete

Requires:

- actual Amplitude charts in partner-training org
- live/recorded presentation
- submission
- reviewer assessment

Claude Code can potentially handle the first category.

It cannot claim the second category unless the external steps were actually completed.

---

# 51. EXPECTED EXECUTION ORDER

Claude Code should execute in this order:

```text
1. Inspect workspace
2. Inspect official workbook
3. Inspect official kickoff deck
4. Inspect training materials
5. Identify official AI deliverables
6. Copy templates to working/
7. Choose/confirm AmpliStore + Zara
8. Define four Alignment requirements
9. Define 3 use cases
10. Define 10–15 business questions
11. Define 5–6 KPIs
12. Populate Product Flows Tracker
13. Build KPI → Question → Event traceability
14. Build event taxonomy
15. Define event properties
16. Define user properties
17. Define user identification strategy
18. Define AI deliverables plan
19. Define instrumentation approach
20. Populate integrations/data sources
21. Create architecture diagram
22. Populate workbook
23. Build presentation from official template
24. Create chart specifications
25. Attempt authorized Amplitude chart creation if tools/access exist
26. Add real chart links only after successful creation
27. Run workbook QA
28. Run presentation QA
29. Run cross-artifact consistency QA
30. Produce final README
31. Show user exactly what remains manual
```

---

# 52. CLAUDE CODE START PROMPT

Use this after placing this `.md` file and the official templates in the VS Code workspace:

```text
Read `Amplitude_Capstone_Claude_Code_Instructions.md` completely before doing anything.

This is the execution specification for my Analytics Implementation Capstone 2026.

Now inspect the entire workspace and identify:
- official Implementation Workbook
- official Partnership Kickoff Deck
- Capstone PDF
- all training materials
- any architecture diagrams

Use the official templates as the source of truth.

Do NOT create a new workbook structure if the official workbook exists.
Do NOT redesign the official PowerPoint if the official template exists.

First produce an implementation plan based on the actual files you find.

Then execute the plan.

Primary scenario:
- AmpliStore 2.0
- Reference app: Zara

Use the detailed requirements in the MD file.

IMPORTANT:
- Find the official five AI deliverable names in the training materials.
- Do not invent them.
- Do not fabricate metrics.
- Do not fabricate Amplitude chart URLs.
- Do not claim partner-training access unless you actually have authorized access.
- Clearly separate confirmed information from mock assumptions.
- Preserve official template structure.
- Keep workbook, presentation, architecture and chart specifications consistent.

Create the requested output and validation files.

Before finishing, run a full consistency check and report:
1. files created
2. assumptions
3. unresolved items
4. Amplitude work completed
5. Amplitude work still requiring manual action
6. validation failures, if any
```

---

# 53. IF CLAUDE CODE CAN ACCESS AMPLITUDE

If an authorized browser/API/plugin integration is available, Claude should:

1. Verify it is operating in the correct partner-training organization.
2. Verify it is using the AmpliStore scenario.
3. Inspect demo data.
4. Map our proposed taxonomy to available demo events.
5. Build charts using the closest supported demo data.
6. Never change the implementation recommendations merely to match demo data.
7. Save charts.
8. Capture actual chart URLs.
9. Build the dashboard.
10. Test each chart.
11. Update the workbook's `Chart Links`.

Remember:

> Demo data is a reference for taxonomy/chart-building, not a real implementation. The capstone explicitly says not to simply replicate the demo taxonomy.

---

# 54. IF CLAUDE CODE CANNOT ACCESS AMPLITUDE

It should NOT stop the entire project.

Instead:

Create:

```text
output/AmpliStore_Chart_Specifications.md
```

For each chart include:

```text
Chart:
Use Case:
Business Question:
KPI:
Chart Type:
Starting Event:
Steps:
Filters:
Segmentation:
Expected Interpretation:
Status:
Amplitude URL:
```

Use:

```text
Status: Pending manual creation in partner-training org
Amplitude URL: Not available
```

Then continue with workbook, deck and architecture.

---

# 55. EXECUTIVE QUESTIONS TO PRACTICE

Prepare answers to:

### Why these KPIs?

They map directly to product discovery, conversion and checkout optimization.

### Why only 5–6 KPIs?

Because the implementation should prioritize measurable, actionable outcomes rather than create an unfocused metric catalog.

### Why not track every click?

Because business-action-based tracking provides more durable and useful analytics while reducing unnecessary data.

### Why hybrid?

Frontend events capture behavioral context; backend events provide authoritative transaction outcomes.

### Why backend for order completion?

Order completion and revenue are authoritative business transactions.

### What if the UI changes?

The taxonomy represents business actions rather than fragile UI component names.

### How will you validate data?

Through development instrumentation, QA, taxonomy validation, event/property checks, identity checks and reconciliation of critical transaction events.

### Why mobile-web segmentation?

Because the scenario explicitly states mobile browsers are a significant traffic source.

### Why guest vs registered?

Because the scenario explicitly supports both guest and registered checkout.

### How do the charts support business goals?

Each chart is mapped to a business question and KPI, allowing stakeholders to identify a measurable problem and make a product decision.

---

# 56. FINAL DEFINITION OF DONE

Do not report success until all applicable items are true:

- [ ] Official templates inspected
- [ ] Workbook populated
- [ ] Alignment complete
- [ ] 2–3 use cases documented
- [ ] 10–15 business questions documented
- [ ] KPIs documented
- [ ] Product flows documented
- [ ] Event taxonomy documented
- [ ] Event properties documented
- [ ] User properties documented
- [ ] User identification strategy documented
- [ ] AI deliverables identified from official materials, or explicitly marked unavailable
- [ ] Instrumentation approach documented
- [ ] Data sources/destinations documented
- [ ] Architecture diagram created
- [ ] Kickoff presentation completed
- [ ] Chart specifications completed
- [ ] Actual Amplitude charts created OR clearly marked pending
- [ ] Dashboard created OR clearly marked pending
- [ ] No fabricated URLs
- [ ] No fabricated metrics
- [ ] No unsupported implementation claims
- [ ] Workbook/presentation/taxonomy/chart consistency checked
- [ ] QA report generated
- [ ] Manual remaining actions listed

---

# 57. IMPORTANT SOURCE NOTES

The official Capstone states that:

- the project takes approximately 4–6 hours
- three deliverables are required
- the partner-training demo dataset is for reference, not replication
- a real app such as ASOS/Zara can be used for AmpliStore
- Alignment requires four pre-project requirements
- Discovery should establish KPI scope
- Technical Scoping requires event taxonomy and AI deliverables sequencing
- Instrumentation requires an ingestion recommendation and relevant data sources
- Enablement/Rollout requires actual Amplitude charts
- the presentation should be executive-sponsor oriented
- the passing score is 17/18

The official Kickoff Deck additionally provides the detailed 2026 roadmap, Goal Alignment structure, Implementation Scope structure, data source/destination section, project roles, implementation checklist, risk/action-item sections, and current AI/Global Agent material.

Use those official structures rather than inventing a different implementation methodology.
