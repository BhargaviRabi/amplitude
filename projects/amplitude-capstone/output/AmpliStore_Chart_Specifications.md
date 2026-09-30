# AmpliStore 2.0 — Chart Specifications

**Scenario:** AmpliStore 2.0 (E-commerce) · **Reference app:** Zara · **Platform:** Web (desktop + mobile browser)

**Amplitude org:** `partner-training` · **Project:** `Amplistore 2.0 (E-commerce 2024)` (ID 616592)

**Space:** Bhargavi Devi's Space (private) · **Built and verified:** 2026-08-27


---

## Three things this document keeps separate

Please read this before any figure below.

| | What it is | Where it lives |
|---|---|---|
| **1. Recommended implementation taxonomy** | What we recommend AmpliStore actually instruments. 16 events, Title Case, with defined properties and types. This is our deliverable and it is **unchanged** by whatever the demo project happens to contain. | Workbook → `Events and Event Properties`, `User Properties` |
| **2. Demo taxonomy used to construct charts** | The event names that already exist in the partner-training project. Used **only** so the charts can be demonstrated live against real volume. Not a recommendation. | `notes/demo_event_mapping.md`, and the *Demo events used* line on each built chart below |
| **3. Identified instrumentation / data gaps** | Places where the demo project cannot support an analysis our taxonomy would support. These are findings, not failures of the design. | The *Instrumentation and data gaps* section at the end of this document |

The Capstone states the demo dataset is a reference for taxonomy and chart-building and must not simply be replicated. Our recommendations are therefore our own.


---

## How to talk about the numbers in this document

> Observed in the Amplitude partner-training organization, project 'Amplistore 2.0 (E-commerce 2024)', over the last 7 days as at 2026-08-27. This is a training dataset provided for taxonomy and chart-building reference. It does not represent AmpliStore 2.0 performance and must not be quoted as a business baseline.


Every figure in this document is an observation about a **training dataset**. None of it is an AmpliStore baseline, a target, or a commitment. Deliberately, **no figure from these charts appears anywhere in the Implementation Workbook** — the workbook records definitions, not values.


When quoting any figure, state the conversion window and the population alongside it. A conversion rate without its window and denominator is not a metric.


---

## Summary

| ID | Chart | Status | Amplitude URL |
|---|---|---|---|
| C1 | Purchase Funnel (Product View to Order) | **Built & verified** | https://app.amplitude.com/analytics/partner-training/chart/p18njvdl |
| C2 | Checkout Funnel (Checkout Start to Order) | **Specification only — data gap** | Not available |
| C3 | Product Discovery Funnel (Search to Order) | **Built & verified** | https://app.amplitude.com/analytics/partner-training/chart/xke4q1vb |
| C4 | Purchase Conversion by Device | **Built & verified** | https://app.amplitude.com/analytics/partner-training/chart/4dcotsr6 |
| C5 | Add-to-Cart Rate by Category and Device | **Built & verified** | https://app.amplitude.com/analytics/partner-training/chart/rppyxd6k |
| C6 | Average Order Value by Category, Device and Account Type | **Specification only — data gap** | Not available |
| C7 | Guest vs Registered Checkout Completion | **Specification only — data gap** | Not available |
| C8 | Cart Abandonment and Abandoner Cohort | **Built & verified** | https://app.amplitude.com/analytics/partner-training/chart/44t450ks |

**Dashboard:** AmpliStore Executive Analytics — https://app.amplitude.com/analytics/partner-training/dashboard/t125gcku (contains C1, C3, C4, C5, C8)


5 of 8 charts built. 3 could not be built because the demo project genuinely lacks the required events or properties. Nothing was substituted to force a chart to render — substituting a near-enough property would have silently answered a different business question.


---


## C1 — Purchase Funnel (Product View to Order)

- **Chart:** AmpliStore \| Purchase Funnel (Product View to Order)
- **Use Case:** UC2 — Purchase Funnel Optimization
- **Business Question:** Where do users drop before purchase, and does that differ by device?
- **KPI:** Purchase Conversion Rate (K1)
- **Chart Type:** Funnel Analysis
- **Starting Event:** Product Viewed
- **Steps (recommended taxonomy):** Product Viewed → Product Added to Cart → Checkout Started → Order Completed
- **Filters:** Internal User = false
- **Segmentation:** All Users (headline funnel). Device breakdown is deliberately kept in C4 to avoid a redundant chart.
- **Conversion window / definition:** 7-day conversion window, user-level, ordered steps
- **Supporting questions answered:** Q7, Q9, Q10
    - Q7: What percentage of product viewers complete a purchase?
    - Q9: Where is the largest drop-off in the purchase funnel?
    - Q10: Does purchase conversion differ between mobile browser and desktop?
- **Expected Interpretation:** Shows the relative size of the drop-off at each step of the purchase journey, so the step with the largest measured decrease can be prioritised. Interpretation requires the conversion window and population to be stated alongside any figure quoted.
- **Dashboard:** AmpliStore Executive Analytics
- **Status:** Built and verified in the partner-training org
- **Amplitude URL:** https://app.amplitude.com/analytics/partner-training/chart/p18njvdl
- **Demo events used (demo taxonomy, not our recommendation):** View Item Details → Add to Cart → Checkout → Place Order
- **As configured:** 7 days, unique users, steps in order; grouping: None - All Users (headline funnel)

  **Demo-data observation — training data, not an AmpliStore baseline:**

  Within the configured demo-data funnel, 10,341 users recorded View Item Details. 94.8% of those users progressed to Add to Cart, 56.2% to Checkout, and 26.2% to Place Order. The largest step-to-step decrease observed was between Add to Cart and Checkout. Any figure quoted from this chart must be accompanied by the conversion window (7 days) and the population (users who recorded View Item Details).

  | Step / Segment | Users | Conversion |
  |---|---|---|
  | View Item Details | 10,341 | 100% |
  | Add to Cart | 9,807 | 94.84% |
  | Checkout | 5,812 | 56.2% |
  | Place Order | 2,708 | 26.19% |


## C2 — Checkout Funnel (Checkout Start to Order)

- **Chart:** AmpliStore \| Checkout Funnel (Checkout Start to Order)
- **Use Case:** UC3 — Checkout Optimization
- **Business Question:** Which checkout step has the highest abandonment?
- **KPI:** Checkout Completion Rate (K3)
- **Chart Type:** Funnel Analysis
- **Starting Event:** Checkout Started
- **Steps (recommended taxonomy):** Checkout Started → Shipping Info Added → Payment Info Added → Order Completed
- **Filters:** Internal User = false
- **Segmentation:** Checkout Type (guest vs registered)
- **Conversion window / definition:** 1-day conversion window, user-level, ordered steps
- **Supporting questions answered:** Q12, Q13, Q14
    - Q12: What percentage of checkout starters complete an order?
    - Q13: Which checkout step - shipping or payment - has the highest abandonment?
    - Q14: Do guest and registered users complete checkout at different rates?
- **Expected Interpretation:** Isolates shipping-step versus payment-step friction. A large guest-vs-registered gap at the shipping step points at forced account creation.
- **Dashboard:** AmpliStore Executive Analytics
- **Status:** Specification only — blocked by an identified data gap
- **Amplitude URL:** Not available
- **Why not built:** The partner-training demo project contains no checkout sub-step events. There is a 'Checkout' event but nothing equivalent to Shipping Info Added or Payment Info Added, so the shipping-versus-payment abandonment split cannot be measured.
- **How this was verified:** Searched the project's 105 events for 'checkout', 'shipping', 'payment'. Only 'Checkout' and 'Checkout custom event test' exist.
- **Decision:** Specification only. NOT fabricated.
- **Why this gap matters for AmpliStore:** This is the single most valuable gap to close for a real AmpliStore. Without those two events, 'checkout is broken' cannot be narrowed to a step, so engineering cannot be pointed at a specific fix. Instrumenting them is a concrete Phase 1 recommendation.


## C3 — Product Discovery Funnel (Search to Order)

- **Chart:** AmpliStore \| Product Discovery Funnel (Search to Order)
- **Use Case:** UC1 — Product Discovery Optimization
- **Business Question:** Does search effectively move users toward purchase?
- **KPI:** Product Discovery Conversion (K5)
- **Chart Type:** Funnel Analysis
- **Starting Event:** Product Searched
- **Steps (recommended taxonomy):** Product Searched → Product Viewed → Product Added to Cart → Order Completed
- **Filters:** Internal User = false
- **Segmentation:** Results Count = 0 vs Results Count > 0 (null-result searches)
- **Conversion window / definition:** 7-day conversion window, user-level, ordered steps
- **Supporting questions answered:** Q1, Q3
    - Q1: What percentage of users who search for a product go on to view a product detail page?
    - Q3: Which searches return zero results, and do those users abandon the session?
- **Expected Interpretation:** Measures how often searches return zero results and whether search-initiated journeys reach purchase at a different rate from browse-initiated ones. Any difference is correlational: it does not establish that searching causes conversion, because intent and population composition are not controlled for.
- **Dashboard:** AmpliStore Executive Analytics
- **Status:** Built and verified in the partner-training org
- **Amplitude URL:** https://app.amplitude.com/analytics/partner-training/chart/xke4q1vb
- **Demo events used (demo taxonomy, not our recommendation):** Search for Items → View Item Details → Add to Cart → Place Order
- **As configured:** 7 days, unique users, steps in order; grouping: None - All Users

  **Demo-data observation — training data, not an AmpliStore baseline:**

  Within the configured demo-data funnel, 10,285 users recorded Search for Items. 99.5% progressed to View Item Details, 94.3% to Add to Cart, and 36.4% to Place Order. The end-to-end rate observed for this search-initiated funnel (36.4%) is higher than the rate observed for the product-view-initiated funnel in C1 (26.2%). IMPORTANT: these are two separately configured funnels with different starting populations. The difference is CORRELATIONAL and does NOT establish that searching causes users to purchase. Users who search may already arrive with stronger purchase intent; intent, traffic source, and population composition are not controlled for here. Establishing causation would require a controlled experiment.

  | Step / Segment | Users | Conversion |
  |---|---|---|
  | Search for Items | 10,285 | 100% |
  | View Item Details | 10,238 | 99.54% |
  | Add to Cart | 9,694 | 94.25% |
  | Place Order | 3,743 | 36.39% |


## C4 — Purchase Conversion by Device

- **Chart:** AmpliStore \| Purchase Conversion by Device
- **Use Case:** UC2 — Purchase Funnel Optimization
- **Business Question:** Does mobile browser underperform desktop on purchase conversion?
- **KPI:** Purchase Conversion Rate (K1)
- **Chart Type:** Funnel Analysis, conversion over time
- **Starting Event:** Product Viewed
- **Steps (recommended taxonomy):** Product Viewed → Order Completed
- **Filters:** Internal User = false
- **Segmentation:** Device Family: mobile browser, desktop, tablet
- **Conversion window / definition:** 7-day conversion window, user-level
- **Supporting questions answered:** Q10
    - Q10: Does purchase conversion differ between mobile browser and desktop?
- **Expected Interpretation:** The scenario states mobile browsers are a significant traffic source. If a material difference between device families is measured, it would indicate where to investigate first. A difference in observed rates is correlational and would need further investigation before being attributed to the device experience.
- **Dashboard:** AmpliStore Executive Analytics
- **Status:** Built and verified in the partner-training org
- **Amplitude URL:** https://app.amplitude.com/analytics/partner-training/chart/4dcotsr6
- **Demo events used (demo taxonomy, not our recommendation):** View Item Details → Place Order
- **As configured:** 7 days, unique users; grouping: Device family (Amplitude SDK default user property)

  **Demo-data observation — training data, not an AmpliStore baseline:**

  Within the configured demo-data funnel, observed View Item Details to Place Order conversion ranged from 41.2% to 44.6% across the six device families present (Apple iPhone, Apple iPad, Samsung Galaxy Phone, Windows PC, Google Nexus Tablet, HTC Phone). No material difference between device families was observed in this training dataset. This is an observation about demo data only and indicates nothing about how AmpliStore's mobile browser experience would actually perform.

  | Step / Segment | Users | Conversion |
  |---|---|---|
  | Apple iPhone | 4,715 | 41.51% |
  | Apple iPad | 1,952 | 42.11% |
  | Samsung Galaxy Phone | 655 | 42.29% |
  | Windows PC | 512 | 41.21% |
  | Google Nexus Tablet | 471 | 41.19% |
  | HTC Phone | 471 | 44.59% |


## C5 — Add-to-Cart Rate by Category and Device

- **Chart:** AmpliStore \| Add-to-Cart Rate by Category and Device
- **Use Case:** UC1 — Product Discovery Optimization
- **Business Question:** Which categories and filters turn product views into cart adds most effectively?
- **KPI:** Add-to-Cart Rate (K2)
- **Chart Type:** Funnel Analysis, segmented
- **Starting Event:** Product Viewed
- **Steps (recommended taxonomy):** Product Viewed → Product Added to Cart
- **Filters:** Internal User = false
- **Segmentation:** Category: mens, womens, jewelry; secondary split by Device Family
- **Conversion window / definition:** 1-day conversion window, user-level
- **Supporting questions answered:** Q4, Q5, Q8
    - Q4: Which filters are associated with stronger product engagement and add-to-cart rate?
    - Q5: Which product categories have the strongest add-to-cart rate?
    - Q8: What percentage of product viewers add an item to cart?
- **Expected Interpretation:** Shows whether measured add-to-cart rates differ by category, which would indicate where to investigate merchandising or product-page experience. Differences observed are a starting point for investigation, not a diagnosis.
- **Dashboard:** AmpliStore Executive Analytics
- **Status:** Built and verified in the partner-training org
- **Amplitude URL:** https://app.amplitude.com/analytics/partner-training/chart/rppyxd6k
- **Demo events used (demo taxonomy, not our recommendation):** View Item Details → Add to Cart
- **As configured:** 1 day, unique users; grouping: Product Category (event property)

  **Demo-data observation — training data, not an AmpliStore baseline:**

  Within the configured demo-data funnel, observed View Item Details to Add to Cart conversion ranged from 90.2% to 91.4% across the five populated Product Category values, plus a 3-user '(none)' group at 66.7%. IMPORTANT: the demo values are grocery categories (Protein, Pantry, Dairy, Cleaning, Produce), not the men's clothing, women's clothing and jewelry categories in the AmpliStore 2.0 scenario. These figures therefore cannot be read as category insight for AmpliStore. The chart demonstrates that the analysis is correctly configured; it does not describe AmpliStore's categories.

  | Step / Segment | Users | Conversion |
  |---|---|---|
  | Protein | 3,345 | 90.19% |
  | Pantry | 2,866 | 90.93% |
  | Dairy | 1,578 | 90.56% |
  | Cleaning | 1,289 | 90.77% |
  | Produce | 1,260 | 91.43% |
  | (none) | 3 | 66.67% |


## C6 — Average Order Value by Category, Device and Account Type

- **Chart:** AmpliStore \| Average Order Value by Category, Device and Account Type
- **Use Case:** UC2 — Purchase Funnel Optimization
- **Business Question:** What is average order value, and which segments produce higher-value orders?
- **KPI:** Average Order Value (K6)
- **Chart Type:** Event Segmentation - average of a numeric property
- **Starting Event:** Order Completed
- **Steps (recommended taxonomy):** Order Completed
- **Filters:** Internal User = false
- **Segmentation:** Category, Device Family, Checkout Type
- **Conversion window / definition:** Reported per calendar period
- **Supporting questions answered:** Q15
    - Q15: What is average order value by category, by device type and by account type?
- **Expected Interpretation:** Guides merchandising and promotion. Uses the warehouse-sourced Total Amount so the figure reconciles with finance.
- **Dashboard:** AmpliStore Executive Analytics
- **Status:** Specification only — blocked by an identified data gap
- **Amplitude URL:** Not available
- **Why not built:** No order-value property exists on the demo purchase events. 'Place Order' carries only $location_lat, $location_lng, Custom Event Property 6 and Source. 'Complete Purchase' carries $price and $quantity (both typed String) and a $revenue property that is marked Unexpected with a single recorded occurrence - effectively unpopulated.
- **How this was verified:** Inspected all 23 properties on 'Complete Purchase' and all 4 on 'Place Order'; checked $revenue's USED BY - one event, unpopulated.
- **Decision:** Specification only. Averaging $price would produce average ITEM price, not average ORDER value - a different metric answering a different question. Not substituted.
- **Why this gap matters for AmpliStore:** AOV is a headline monetization KPI. Its absence in the demo underlines the recommendation that order total be sourced from the backend (Snowflake warehouse import) as a typed numeric property, not inferred client-side.


## C7 — Guest vs Registered Checkout Completion

- **Chart:** AmpliStore \| Guest vs Registered Checkout Completion
- **Use Case:** UC3 — Checkout Optimization
- **Business Question:** Does account type correlate with checkout completion?
- **KPI:** Checkout Completion Rate (K3)
- **Chart Type:** Funnel Analysis, segmented
- **Starting Event:** Checkout Started
- **Steps (recommended taxonomy):** Checkout Started → Order Completed
- **Filters:** Internal User = false
- **Segmentation:** Checkout Type: guest vs registered
- **Conversion window / definition:** 1-day conversion window, user-level
- **Supporting questions answered:** Q14
    - Q14: Do guest and registered users complete checkout at different rates?
- **Expected Interpretation:** Compares measured checkout completion for guest and registered checkout. Correlational only: a difference may reflect the smoothness of the registered path, or simply that registered users arrive with higher intent. Do not present as causal.
- **Dashboard:** AmpliStore Executive Analytics
- **Status:** Specification only — blocked by an identified data gap
- **Amplitude URL:** Not available
- **Why not built:** No populated account-type property exists. The only candidate, user property 'userType', was first and last seen on 29 Mar 2025 - a single day over a year ago - and has zero 30-day queries. 'Plan Type' exists and is populated but describes a subscription plan, not guest-versus-registered checkout.
- **How this was verified:** Searched all 72 user properties for account / guest / member / type. Only Device Type, Device type, Plan Type, userType matched; none usable.
- **Decision:** Specification only. Plan Type was NOT substituted - it is a different concept and using it would silently answer a different question.
- **Why this gap matters for AmpliStore:** The scenario explicitly supports guest and registered checkout, so Checkout Type is a required property in our taxonomy. The demo's lack of it is exactly the kind of gap the taxonomy design is meant to prevent.


## C8 — Cart Abandonment and Abandoner Cohort

- **Chart:** AmpliStore \| Cart Abandonment and Abandoner Cohort
- **Use Case:** UC2 — Purchase Funnel Optimization
- **Business Question:** What proportion of cart builders never purchase, and how large is that audience?
- **KPI:** Cart Abandonment Rate (K4)
- **Chart Type:** Funnel Analysis + saved Cohort
- **Starting Event:** Product Added to Cart
- **Steps (recommended taxonomy):** Product Added to Cart → Order Completed
- **Filters:** Internal User = false
- **Segmentation:** Cart Value bands; Device Family
- **Conversion window / definition:** 7-day conversion window, user-level
- **Supporting questions answered:** Q11
    - Q11: What proportion of users who add to cart never complete a purchase?
- **Expected Interpretation:** Sizes the abandoned-cart audience and saves it as a cohort for the Braze sync already present in the architecture, turning the metric into a campaign.
- **Dashboard:** AmpliStore Executive Analytics
- **Status:** Built and verified in the partner-training org
- **Amplitude URL:** https://app.amplitude.com/analytics/partner-training/chart/44t450ks
- **Demo events used (demo taxonomy, not our recommendation):** Add to Cart → Place Order
- **As configured:** 7 days, unique users; grouping: None - All Users

  **Demo-data observation — training data, not an AmpliStore baseline:**

  Within the configured demo-data funnel, 9,568 users recorded Add to Cart and 39.3% progressed to Place Order within the 7-day window. The complement, 60.7%, is the cart abandonment rate observed for this training dataset over that window. A cart abandonment rate is only meaningful alongside its window: a 1-day and a 7-day figure are different metrics.

  | Step / Segment | Users | Conversion |
  |---|---|---|
  | Add to Cart | 9,568 | 100% |
  | Place Order | 3,764 | 39.34% |


---

## Instrumentation and data gaps identified in the partner-training project

Each gap below was verified in the tool, not assumed. Each maps to something our recommended taxonomy already addresses — which is the point worth making to the reviewer.


### G1 — Checkout sub-step events unavailable

- **What was found:** The demo project has a 'Checkout' event but no equivalent of Shipping Info Added or Payment Info Added. Checkout abandonment cannot be narrowed to a step.
- **Impact:** Blocks chart C2 and KPI 3 diagnosis.
- **How our recommended taxonomy addresses it:** Our taxonomy instruments Shipping Info Added and Payment Info Added as separate events.

### G2 — Reliable numeric order total unavailable

- **What was found:** 'Place Order' carries no order-value property. 'Complete Purchase' carries $revenue, but it is marked Unexpected with a single recorded occurrence, so it is effectively unpopulated.
- **Impact:** Blocks chart C6 and KPI 6 (Average Order Value).
- **How our recommended taxonomy addresses it:** Our taxonomy defines Order Completed.Total Amount as a required numeric property sourced from the transaction system of record.

### G3 — Guest / registered indicator unavailable

- **What was found:** No populated account-type property exists. The only candidate, user property 'userType', was first and last seen on 29 Mar 2025 and has zero 30-day queries. 'Plan Type' is populated but describes a subscription plan, which is a different concept.
- **Impact:** Blocks chart C7 and the guest-versus-registered analysis in UC3.
- **How our recommended taxonomy addresses it:** Our taxonomy defines Checkout Type (guest, registered) as an event property on Checkout Started and Order Completed, plus Account Type as a user property.

### G4 — Product Category demo values do not match the apparel scenario

- **What was found:** The demo project's Product Category values are grocery categories (Protein, Pantry, Dairy, Cleaning, Produce), not the men's clothing, women's clothing and jewelry categories in the AmpliStore 2.0 scenario.
- **Impact:** Chart C5 is structurally correct but its category labels are demo artefacts and carry no meaning for AmpliStore.
- **How our recommended taxonomy addresses it:** Our taxonomy defines Category with values mens, womens, jewelry, and Subcategory beneath it.

### G5 — Duplicate / overlapping purchase events

- **What was found:** The demo project contains both 'Place Order' (30-day volume 39,636) and 'Complete Purchase' (35,208), which record the same user action. Amplitude's own Data Assistant flags this class of issue as CRITICAL because it splits a metric across two events.
- **Impact:** Any purchase metric built on one event silently excludes the other. We standardised every chart on 'Place Order' so all five charts share one definition.
- **How our recommended taxonomy addresses it:** Our taxonomy defines a single Order Completed event, and the Taxonomy and Data QA sheet carries an explicit check for exactly this failure.

### G6 — Numeric commerce properties have data-quality and type issues

- **What was found:** $price and $quantity on 'Complete Purchase' are typed as String rather than numeric. $location_lat / $location_lng appear on purchase events where they carry no analytical purpose. Several commerce properties are marked Unexpected, meaning they are not in the tracking plan.
- **Impact:** String-typed values cannot be aggregated, so revenue and basket-size analysis is not possible without remediation.
- **How our recommended taxonomy addresses it:** Our taxonomy specifies data types explicitly and the planned QA includes a type-correctness check before production sign-off.

---

## Dashboard — AmpliStore Executive Analytics

**URL:** https://app.amplitude.com/analytics/partner-training/dashboard/t125gcku

**Audience:** Executive Advocate, Business Lead, merchandising and growth leads


**Charts, in presentation order:**

1. C1 — AmpliStore \| Purchase Funnel (Product View to Order)
2. C3 — AmpliStore \| Product Discovery Funnel (Search to Order)
3. C4 — AmpliStore \| Purchase Conversion by Device
4. C5 — AmpliStore \| Add-to-Cart Rate by Product Category
5. C8 — AmpliStore \| Cart Abandonment (Cart Add to Order)

**Narrative the dashboard follows:** headline purchase funnel → discovery funnel → device breakdown → category breakdown → cart abandonment. Each answers one scoped question.


**Dashboarding best practices applied:**

- One question per chart. If a chart needs a paragraph to explain, it is two charts.
- Order top-to-bottom as headline KPIs, then where the loss happens, then who it happens to.
- Name charts as the question they answer, not the chart type used.
- Apply Internal User = false consistently so every number on the dashboard shares a population.
- State the conversion window on funnel charts - a 1-day and a 7-day funnel are different metrics.
- Keep it to one screen of scroll for executives; depth belongs in linked charts, not this board.
- Assign an owner and a review cadence, or the dashboard rots within a quarter.

**Deliberately kept off this dashboard:** C2, C6 and C7, because they could not be built from real data. An executive dashboard with three empty tiles is worse than one with five that work.
