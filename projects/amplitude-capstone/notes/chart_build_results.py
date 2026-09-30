"""Live Amplitude build results - verified in the partner-training org on 2026-08-27.

Org:     partner-training
Project: Amplistore 2.0 (E-commerce 2024)  (ID 616592)
Space:   Bhargavi Devi's Space (private)
Owner:   Bhargavi Devi

Every URL below was re-opened and verified after saving: correct project, correct
events in correct order, correct conversion window, correct grouping, status "Saved".
"""

BASE = "https://app.amplitude.com/analytics/partner-training"

BUILT = {
    "C1": {
        "name": "C1 — AmpliStore | Purchase Funnel (Product View to Order)",
        "url": f"{BASE}/chart/p18njvdl",
        "type": "Funnel Analysis",
        "demo_events": ["View Item Details", "Add to Cart", "Checkout", "Place Order"],
        "window": "7 days, unique users, steps in order",
        "grouping": "None - All Users (headline funnel)",
        "verified": True,
    },
    "C3": {
        "name": "C3 — AmpliStore | Product Discovery Funnel (Search to Order)",
        "url": f"{BASE}/chart/xke4q1vb",
        "type": "Funnel Analysis",
        "demo_events": ["Search for Items", "View Item Details", "Add to Cart", "Place Order"],
        "window": "7 days, unique users, steps in order",
        "grouping": "None - All Users",
        "verified": True,
    },
    "C4": {
        "name": "C4 — AmpliStore | Purchase Conversion by Device",
        "url": f"{BASE}/chart/4dcotsr6",
        "type": "Funnel Analysis, grouped",
        "demo_events": ["View Item Details", "Place Order"],
        "window": "7 days, unique users",
        "grouping": "Device family (Amplitude SDK default user property)",
        "verified": True,
    },
    "C5": {
        "name": "C5 — AmpliStore | Add-to-Cart Rate by Product Category",
        "url": f"{BASE}/chart/rppyxd6k",
        "type": "Funnel Analysis, grouped",
        "demo_events": ["View Item Details", "Add to Cart"],
        "window": "1 day, unique users",
        "grouping": "Product Category (event property)",
        "verified": True,
    },
    "C8": {
        "name": "C8 — AmpliStore | Cart Abandonment (Cart Add to Order)",
        "url": f"{BASE}/chart/44t450ks",
        "type": "Funnel Analysis",
        "demo_events": ["Add to Cart", "Place Order"],
        "window": "7 days, unique users",
        "grouping": "None - All Users",
        "verified": True,
    },
}

NOT_BUILT = {
    "C2": {
        "name": "C2 — AmpliStore | Checkout Funnel (Checkout Start to Order)",
        "reason": (
            "The partner-training demo project contains no checkout sub-step events. There is a "
            "'Checkout' event but nothing equivalent to Shipping Info Added or Payment Info Added, "
            "so the shipping-versus-payment abandonment split cannot be measured."
        ),
        "verified_absent": "Searched the project's 105 events for 'checkout', 'shipping', 'payment'. Only 'Checkout' and 'Checkout custom event test' exist.",
        "decision": "Specification only. NOT fabricated.",
        "why_it_matters": (
            "This is the single most valuable gap to close for a real AmpliStore. Without those two "
            "events, 'checkout is broken' cannot be narrowed to a step, so engineering cannot be "
            "pointed at a specific fix. Instrumenting them is a concrete Phase 1 recommendation."
        ),
    },
    "C6": {
        "name": "C6 — AmpliStore | Average Order Value",
        "reason": (
            "No order-value property exists on the demo purchase events. 'Place Order' carries only "
            "$location_lat, $location_lng, Custom Event Property 6 and Source. 'Complete Purchase' "
            "carries $price and $quantity (both typed String) and a $revenue property that is marked "
            "Unexpected with a single recorded occurrence - effectively unpopulated."
        ),
        "verified_absent": "Inspected all 23 properties on 'Complete Purchase' and all 4 on 'Place Order'; checked $revenue's USED BY - one event, unpopulated.",
        "decision": (
            "Specification only. Averaging $price would produce average ITEM price, not average ORDER "
            "value - a different metric answering a different question. Not substituted."
        ),
        "why_it_matters": (
            "AOV is a headline monetization KPI. Its absence in the demo underlines the "
            "recommendation that order total be sourced from the backend (Snowflake warehouse "
            "import) as a typed numeric property, not inferred client-side."
        ),
    },
    "C7": {
        "name": "C7 — AmpliStore | Guest vs Registered Checkout Completion",
        "reason": (
            "No populated account-type property exists. The only candidate, user property 'userType', "
            "was first and last seen on 29 Mar 2025 - a single day over a year ago - and has zero "
            "30-day queries. 'Plan Type' exists and is populated but describes a subscription plan, "
            "not guest-versus-registered checkout."
        ),
        "verified_absent": "Searched all 72 user properties for account / guest / member / type. Only Device Type, Device type, Plan Type, userType matched; none usable.",
        "decision": (
            "Specification only. Plan Type was NOT substituted - it is a different concept and using "
            "it would silently answer a different question."
        ),
        "why_it_matters": (
            "The scenario explicitly supports guest and registered checkout, so Checkout Type is a "
            "required property in our taxonomy. The demo's lack of it is exactly the kind of gap the "
            "taxonomy design is meant to prevent."
        ),
    },
}

DASHBOARD = {
    "name": "AmpliStore Executive Analytics",
    "url": f"{BASE}/dashboard/t125gcku",
    "charts_in_order": ["C1", "C3", "C4", "C5", "C8"],
    "verified": True,
}

# Demo-data observations. NOT AmpliStore baselines - see README and workbook.
DEMO_OBSERVATIONS = {
    "window": "Last 7 days as observed on 2026-08-27",
    "C1": [("View Item Details", 10341, "100%"), ("Add to Cart", 9807, "94.84%"),
           ("Checkout", 5812, "56.2%"), ("Place Order", 2708, "26.19%")],
    "C3": [("Search for Items", 10285, "100%"), ("View Item Details", 10238, "99.54%"),
           ("Add to Cart", 9694, "94.25%"), ("Place Order", 3743, "36.39%")],
    "C4": [("Apple iPhone", 4715, "41.51%"), ("Apple iPad", 1952, "42.11%"),
           ("Samsung Galaxy Phone", 655, "42.29%"), ("Windows PC", 512, "41.21%"),
           ("Google Nexus Tablet", 471, "41.19%"), ("HTC Phone", 471, "44.59%")],
    "C5": [("Protein", 3345, "90.19%"), ("Pantry", 2866, "90.93%"), ("Dairy", 1578, "90.56%"),
           ("Cleaning", 1289, "90.77%"), ("Produce", 1260, "91.43%"), ("(none)", 3, "66.67%")],
    "C8": [("Add to Cart", 9568, "100%"), ("Place Order", 3764, "39.34%")],
}


# ---------------------------------------------------------------------------
# DEMO-DATA READINGS
#
# Careful, descriptive wording for every figure observed in the partner-training
# project. These are observations about a TRAINING DATASET. They are not
# AmpliStore performance, not a baseline, not a commitment, and not evidence of
# cause and effect. Use this wording verbatim when presenting.
# ---------------------------------------------------------------------------
DEMO_DATA_CAVEAT = (
    "Observed in the Amplitude partner-training organization, project "
    "'Amplistore 2.0 (E-commerce 2024)', over the last 7 days as at 2026-08-27. "
    "This is a training dataset provided for taxonomy and chart-building reference. "
    "It does not represent AmpliStore 2.0 performance and must not be quoted as a "
    "business baseline."
)

DEMO_READINGS = {
 "C1": (
   "Within the configured demo-data funnel, 10,341 users recorded View Item Details. "
   "94.8% of those users progressed to Add to Cart, 56.2% to Checkout, and 26.2% to "
   "Place Order. The largest step-to-step decrease observed was between Add to Cart "
   "and Checkout. Any figure quoted from this chart must be accompanied by the "
   "conversion window (7 days) and the population (users who recorded View Item Details)."
 ),
 "C3": (
   "Within the configured demo-data funnel, 10,285 users recorded Search for Items. "
   "99.5% progressed to View Item Details, 94.3% to Add to Cart, and 36.4% to Place Order. "
   "The end-to-end rate observed for this search-initiated funnel (36.4%) is higher than "
   "the rate observed for the product-view-initiated funnel in C1 (26.2%). "
   "IMPORTANT: these are two separately configured funnels with different starting "
   "populations. The difference is CORRELATIONAL and does NOT establish that searching "
   "causes users to purchase. Users who search may already arrive with stronger purchase "
   "intent; intent, traffic source, and population composition are not controlled for here. "
   "Establishing causation would require a controlled experiment."
 ),
 "C4": (
   "Within the configured demo-data funnel, observed View Item Details to Place Order "
   "conversion ranged from 41.2% to 44.6% across the six device families present "
   "(Apple iPhone, Apple iPad, Samsung Galaxy Phone, Windows PC, Google Nexus Tablet, "
   "HTC Phone). No material difference between device families was observed in this "
   "training dataset. This is an observation about demo data only and indicates nothing "
   "about how AmpliStore's mobile browser experience would actually perform."
 ),
 "C5": (
   "Within the configured demo-data funnel, observed View Item Details to Add to Cart "
   "conversion ranged from 90.2% to 91.4% across the five populated Product Category "
   "values, plus a 3-user '(none)' group at 66.7%. "
   "IMPORTANT: the demo values are grocery categories (Protein, Pantry, Dairy, Cleaning, "
   "Produce), not the men's clothing, women's clothing and jewelry categories in the "
   "AmpliStore 2.0 scenario. These figures therefore cannot be read as category insight "
   "for AmpliStore. The chart demonstrates that the analysis is correctly configured; it "
   "does not describe AmpliStore's categories."
 ),
 "C8": (
   "Within the configured demo-data funnel, 9,568 users recorded Add to Cart and 39.3% "
   "progressed to Place Order within the 7-day window. The complement, 60.7%, is the "
   "cart abandonment rate observed for this training dataset over that window. "
   "A cart abandonment rate is only meaningful alongside its window: a 1-day and a 7-day "
   "figure are different metrics."
 ),
}

# ---------------------------------------------------------------------------
# IDENTIFIED INSTRUMENTATION AND DATA GAPS
# Found by reviewing the partner-training demo project. Each is a real finding
# worth raising with the reviewer, and each maps to a recommendation in our
# proposed taxonomy.
# ---------------------------------------------------------------------------
DATA_GAPS = [
 ("G1", "Checkout sub-step events unavailable",
  "The demo project has a 'Checkout' event but no equivalent of Shipping Info Added or "
  "Payment Info Added. Checkout abandonment cannot be narrowed to a step.",
  "Blocks chart C2 and KPI 3 diagnosis.",
  "Our taxonomy instruments Shipping Info Added and Payment Info Added as separate events."),
 ("G2", "Reliable numeric order total unavailable",
  "'Place Order' carries no order-value property. 'Complete Purchase' carries $revenue, but it "
  "is marked Unexpected with a single recorded occurrence, so it is effectively unpopulated.",
  "Blocks chart C6 and KPI 6 (Average Order Value).",
  "Our taxonomy defines Order Completed.Total Amount as a required numeric property sourced "
  "from the transaction system of record."),
 ("G3", "Guest / registered indicator unavailable",
  "No populated account-type property exists. The only candidate, user property 'userType', was "
  "first and last seen on 29 Mar 2025 and has zero 30-day queries. 'Plan Type' is populated but "
  "describes a subscription plan, which is a different concept.",
  "Blocks chart C7 and the guest-versus-registered analysis in UC3.",
  "Our taxonomy defines Checkout Type (guest, registered) as an event property on Checkout "
  "Started and Order Completed, plus Account Type as a user property."),
 ("G4", "Product Category demo values do not match the apparel scenario",
  "The demo project's Product Category values are grocery categories (Protein, Pantry, Dairy, "
  "Cleaning, Produce), not the men's clothing, women's clothing and jewelry categories in the "
  "AmpliStore 2.0 scenario.",
  "Chart C5 is structurally correct but its category labels are demo artefacts and carry no "
  "meaning for AmpliStore.",
  "Our taxonomy defines Category with values mens, womens, jewelry, and Subcategory beneath it."),
 ("G5", "Duplicate / overlapping purchase events",
  "The demo project contains both 'Place Order' (30-day volume 39,636) and 'Complete Purchase' "
  "(35,208), which record the same user action. Amplitude's own Data Assistant flags this class "
  "of issue as CRITICAL because it splits a metric across two events.",
  "Any purchase metric built on one event silently excludes the other. We standardised every "
  "chart on 'Place Order' so all five charts share one definition.",
  "Our taxonomy defines a single Order Completed event, and the Taxonomy and Data QA sheet "
  "carries an explicit check for exactly this failure."),
 ("G6", "Numeric commerce properties have data-quality and type issues",
  "$price and $quantity on 'Complete Purchase' are typed as String rather than numeric. "
  "$location_lat / $location_lng appear on purchase events where they carry no analytical "
  "purpose. Several commerce properties are marked Unexpected, meaning they are not in the "
  "tracking plan.",
  "String-typed values cannot be aggregated, so revenue and basket-size analysis is not "
  "possible without remediation.",
  "Our taxonomy specifies data types explicitly and the planned QA includes a type-correctness "
  "check before production sign-off."),
]
