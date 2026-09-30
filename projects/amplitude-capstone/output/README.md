# AmpliStore 2.0 — Analytics Implementation Capstone 2026

## Scenario

**AmpliStore 2.0** — D2C e-commerce retailer selling apparel and accessories across men's
clothing, women's clothing and jewelry. Web-based, with mobile browsers a significant traffic
source. Customers browse and filter by category, view product detail pages with ratings and
reviews, add to cart, and check out as guest or registered user.

**Reference app:** Zara (zara.com) — used for the product walkthrough that justifies the taxonomy.

## Scope

Product discovery, the purchase funnel, and checkout — three use cases, 15 business questions,
six KPIs, a 16-event taxonomy, and eight charts feeding one executive dashboard.

| Use case | Goal |
|---|---|
| UC1 Product Discovery Optimization | Understand how users discover products and which discovery behaviours lead to purchase |
| UC2 Purchase Funnel Optimization | Understand conversion from product view through cart, checkout and completed purchase |
| UC3 Checkout Optimization | Identify where users abandon checkout and which segments experience the most friction |

## Deliverables

| File | What it is |
|---|---|
| `AmpliStore_Implementation_Workbook.xlsx` | The official 2026 workbook, populated. All 18 original sheets preserved; two sheets added (`Alignment (Week 0)`, `AI Deliverables Plan`) because the capstone requires deliverables the template has no tab for. |
| `AmpliStore_Partnership_Kickoff.pptx` | The official 2026 kickoff deck, populated. 38 slides. Template structure and design untouched. |
| `AmpliStore_Architecture.png` | Architecture diagram, based on the official AmpliStore pre-sales diagram in the Capstone PDF (p.7). Embedded on the deck's architecture slide. |
| `AmpliStore_Chart_Specifications.md` | All eight charts specified in full, with live URLs for the five that were built and evidence for the three that could not be. |

Supporting material lives alongside:

- `../notes/` — the canonical content model everything is generated from, the demo-taxonomy
  mapping, and the verified chart build results
- `../validation/` — consistency report, QA checklist, unresolved items, and the re-runnable check
- `../source/` — untouched copies of the official templates and the extracted official diagrams
- `../working/` — working copies used during the build

## Amplitude work completed

Built and verified in the **partner-training** org, project **Amplistore 2.0 (E-commerce 2024)**
(ID 616592), saved to Bhargavi Devi's Space:

| Chart | URL |
|---|---|
| C1 — Purchase Funnel (Product View to Order) | https://app.amplitude.com/analytics/partner-training/chart/p18njvdl |
| C3 — Product Discovery Funnel (Search to Order) | https://app.amplitude.com/analytics/partner-training/chart/xke4q1vb |
| C4 — Purchase Conversion by Device | https://app.amplitude.com/analytics/partner-training/chart/4dcotsr6 |
| C5 — Add-to-Cart Rate by Product Category | https://app.amplitude.com/analytics/partner-training/chart/rppyxd6k |
| C8 — Cart Abandonment (Cart Add to Order) | https://app.amplitude.com/analytics/partner-training/chart/44t450ks |
| **Dashboard — AmpliStore Executive Analytics** | https://app.amplitude.com/analytics/partner-training/dashboard/t125gcku |

Every chart was re-opened after saving and confirmed for project, events, step order, conversion
window, grouping and saved status.

**Three charts could not be built.** The demo project genuinely lacks the required events or
properties, and nothing was substituted to force them to render:

- **C2 Checkout Funnel** — no checkout sub-step events exist (no shipping/payment equivalents)
- **C6 Average Order Value** — no order-total property; `$revenue` is present but unpopulated
- **C7 Guest vs Registered** — no populated account-type property; `userType` last saw data in
  March 2025

Each gap is evidenced in the chart specification. These are demo-dataset limitations, not
taxonomy flaws — and they make a good point to raise with the reviewer, because instrumenting
those events is exactly what the taxonomy recommends.

## Three things this project keeps separate

Confusing these is the easiest way to mislead a reviewer, so they are labelled everywhere:

| | What it is | Where it lives |
|---|---|---|
| **1. Recommended implementation taxonomy** | What we recommend AmpliStore actually instruments — 16 Title Case events with defined properties and types. Unchanged by whatever the demo project contains. | Workbook → `Events and Event Properties`, `User Properties` |
| **2. Demo taxonomy used to construct charts** | Event names that already exist in the partner-training project, used only so charts can be demonstrated live against real volume. Not a recommendation. | `../notes/demo_event_mapping.md` |
| **3. Identified instrumentation / data gaps** | Analyses the demo project cannot support that our taxonomy would. Findings, not design failures. | Chart spec → *Instrumentation and data gaps*; workbook → `Taxonomy and Data QA` |

## Instrumentation and data gaps identified

Six gaps were found by inspecting the partner-training demo project. Each is verified in the
tool, and each maps to something the recommended taxonomy already addresses:

| # | Gap |
|---|---|
| G1 | Checkout sub-step events unavailable — blocks C2 and step-level checkout diagnosis |
| G2 | Reliable numeric order total unavailable — blocks C6 and KPI 6 (AOV) |
| G3 | Guest / registered indicator unavailable — blocks C7 and the UC3 account-type analysis |
| G4 | `Product Category` demo values are grocery, not the apparel/jewelry of the scenario |
| G5 | Duplicate / overlapping purchase events (`Place Order` and `Complete Purchase`) |
| G6 | Numeric commerce properties have data-quality and type issues (`$price`, `$quantity` typed String) |

Full detail, including how each was verified, is in `AmpliStore_Chart_Specifications.md` and the
workbook's `Taxonomy and Data QA` sheet.

## How to talk about the numbers

> Observed in the Amplitude partner-training organization, project
> 'Amplistore 2.0 (E-commerce 2024)', over the last 7 days as at 2026-08-27. This is a training
> dataset provided for taxonomy and chart-building reference. It does not represent AmpliStore 2.0
> performance and must not be quoted as a business baseline.

Say that once before the live chart walkthrough and it covers every number that follows. It is
also written into every chart description and the dashboard description in Amplitude, and it is
in the speaker notes on the Action Items slide.

Two specific cautions to state out loud:

- **C3 is correlational.** The search-initiated funnel and the product-view-initiated funnel in C1
  are separately configured funnels with different starting populations. A difference between them
  does **not** establish that searching causes purchasing — searchers may simply arrive with
  stronger intent. Intent, traffic source and population composition are not controlled for.
  Establishing causation would require a controlled experiment.
- **C5 proves configuration, not category insight.** Its category values are grocery, not
  AmpliStore's apparel and jewelry.

## Major assumptions

All of these are mock-scenario assumptions, labelled as such in the artifacts:

1. **Primary objective** — improve purchase conversion by improving product discovery and
   reducing checkout friction. Flagged for the executive sponsor to confirm or redirect.
2. **Ingestion** — hybrid: Browser SDK for behaviour, Snowflake warehouse import for
   authoritative orders and revenue. Taken from the official pre-sales architecture rather than
   invented. HTTP V2 API evaluated and documented as the low-latency alternative.
3. **Event naming** — Title Case, verb+noun, human readable, per the official workbook's own
   Taxonomy Best Practices sheet. Independently corroborated by the demo project, whose events
   are `Add to Cart`, `View Item Details`, `Place Order`.
4. **User identification** — User ID set only at authentication, using the internal customer
   identifier, never the email address. Guest checkout reported on a Device ID basis.
5. **Scope** — Analytics + Global Agent only. Session Replay, Guides & Surveys and Experiment
   are deliberately excluded so nothing is implied as committed.
6. **Roles** — defined from the official deck; all individual names are `TBD`.

## What is NOT asserted

No conversion rate, revenue figure, AOV, customer count, engineering availability or launch date
appears anywhere as an AmpliStore baseline. The live charts display partner-training demo data;
those figures are recorded as demo observations in the chart specification and are deliberately
kept out of the workbook. No Data QA row is marked `Pass` — every row reads `N/A`, because
nothing is instrumented and there is no evidence to support a pass.

## External work remaining

The capstone is **not complete** until these happen, and none can be done from here:

1. Fill in presenter title and company on the deck cover (currently `TBD`)
2. Confirm the canonical names of the five AI deliverables against Partner Academy
3. Present the kickoff live with camera on, or record a 20-minute version
4. Walk through the charts **live** in the partner-training org — screenshots are explicitly
   not sufficient
5. Submit the deck and workbook in the Partner Academy course before the review meeting
6. Book the 60-minute review slot
7. Receive the rubric and, on a pass, the badge

See `../validation/unresolved_items.md` for the full list.

## Verification

```bash
cd amplitude-capstone
python3 validation/run_consistency_check.py
```

36 checks, currently all passing. Every artifact is generated from one canonical content model,
so consistency is structural rather than maintained by hand.
