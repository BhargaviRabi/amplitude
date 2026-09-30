"""Canonical content model for the AmpliStore 2.0 capstone.

Single source of truth. The workbook, deck, architecture diagram, chart
specifications and consistency report are all generated from this file, so the
artifacts cannot drift apart.

Naming style decision (documented in output/README.md):
  Events     : Title Case, verb+noun / noun+verb, human readable
  Properties : Title Case, consistent across every event that carries the same
               information
Rationale: the official 2026 Implementation Workbook 'Taxonomy Best Practices'
sheet requires verb+noun, "as human friendly as possible", and explicitly
prefers "Onboarding: Captured Billing Info" OVER "onboarding.captured_billing_info".
"""

SCENARIO = {
    "name": "AmpliStore 2.0",
    "industry": "E-commerce (D2C apparel & accessories)",
    "reference_app": "Zara (zara.com)",
    "platform": "Web (desktop + mobile browser)",
    "categories": ["Men's clothing", "Women's clothing", "Jewelry"],
    "source": "Capstone PDF, 'Scenario: E-Commerce (AmpliStore 2.0)'",
}

# ---------------------------------------------------------------------------
# ALIGNMENT / WEEK 0 - four pre-project requirements (Capstone PDF: "Identify
# the four pre-project requirements for your mock scenario")
# ---------------------------------------------------------------------------
ALIGNMENT_REQUIREMENTS = [
    {
        "id": "R1",
        "name": "Business goals and success criteria",
        "confirm": [
            "Which business outcome matters most this fiscal year?",
            "Is purchase conversion the primary objective, or is it AOV / retention?",
            "Is product discovery a known pain point, and what evidence exists today?",
            "Is checkout abandonment a known issue, and is it worse on mobile browser?",
            "How will success be measured, and against what current baseline?",
        ],
        "mock_assumption": (
            "MOCK ASSUMPTION (not customer-confirmed): the primary objective is to "
            "improve purchase conversion by improving product discovery and reducing "
            "checkout friction."
        ),
        "owner": "Executive Advocate / Business Lead",
    },
    {
        "id": "R2",
        "name": "Stakeholders and ownership",
        "confirm": [
            "Executive Advocate - overall sponsor and budget owner, attends EBRs",
            "Business Lead - early power user, drives adoption and value",
            "Project Lead - manages the Amplitude instance, Amplitude's main POC",
            "Technical Lead / Engineering Lead - owns instrumentation and data accuracy",
            "Analytics users / power users - merchandising, growth, CRM analysts",
        ],
        "mock_assumption": (
            "Role definitions are taken verbatim from the official 2026 Kickoff Deck "
            "'[Customer] Amplitude Leads' slide. Named individuals are TO CONFIRM."
        ),
        "owner": "Project Lead",
    },
    {
        "id": "R3",
        "name": "Data and technical architecture",
        "confirm": [
            "Web technology and release process for AmpliStore Web",
            "Existing analytics implementation and whether a tag manager / CDP is in play",
            "Amplitude project structure (Dev / Staging / Prod) and taxonomy sharing",
            "SDK vs API vs warehouse-import responsibilities per data domain",
            "Backend order system that is authoritative for completed orders and revenue",
            "Data warehouse (Snowflake per the pre-sales architecture) and access model",
            "Downstream destinations (Braze for engagement; Snowflake for enriched export)",
            "User identification approach for anonymous, authenticated and cross-device",
            "Development / staging / production environment separation",
        ],
        "mock_assumption": (
            "Architecture is taken from the OFFICIAL AmpliStore pre-sales architecture "
            "diagram in the Capstone PDF (p.7): Amplishop web -> Browser SDK -> Amplitude; "
            "Snowflake backend -> warehouse import -> Amplitude; Amplitude -> Braze "
            "(cohort sync) and Amplitude -> Snowflake (data export)."
        ),
        "owner": "Technical Lead / Engineering Lead",
    },
    {
        "id": "R4",
        "name": "Scope and priority",
        "confirm": [
            "Product / platform priority (AmpliStore Web, then mobile browser parity)",
            "Top 2-3 Amplitude use cases for the implementation phase",
            "10-15 supporting business questions to validate by launch",
            "Event scope - the prioritised events that answer those questions",
            "KPI scope - the 5-6 KPIs that will be reported at launch",
            "Chart and dashboard scope for the launch readout",
            "Launch target date and any seasonal freeze windows",
            "Engineering availability, sprint cadence and release train",
        ],
        "mock_assumption": (
            "Scope below is our recommendation for the mock scenario; launch date and "
            "engineering availability are TO CONFIRM and are not invented here."
        ),
        "owner": "Project Lead / Business Lead",
    },
]

# ---------------------------------------------------------------------------
# DISCOVERY - use cases, business questions, KPIs
# ---------------------------------------------------------------------------
USE_CASES = [
    {
        "id": "UC1",
        "name": "Product Discovery Optimization",
        "goal": ("Understand how users discover products and which discovery behaviours "
                 "lead to product engagement and purchase."),
        "challenge": ("Users struggle to find relevant products; unclear which discovery "
                      "path (browse, search, filter) actually leads to purchase."),
    },
    {
        "id": "UC2",
        "name": "Purchase Funnel Optimization",
        "goal": ("Understand conversion from product view through cart, checkout and "
                 "completed purchase."),
        "challenge": ("Drop-off between product view, cart and checkout is not measurable "
                      "today, so investment cannot be targeted."),
    },
    {
        "id": "UC3",
        "name": "Checkout Optimization",
        "goal": ("Identify where users abandon checkout and which segments experience the "
                 "greatest friction."),
        "challenge": ("Checkout friction is suspected, especially on mobile browser and for "
                      "guest checkout, but the abandonment step is unknown."),
    },
]

# 15 supporting business questions, each mapped to a use case and a KPI.
BUSINESS_QUESTIONS = [
    ("Q1",  "UC1", "K5", "What percentage of users who search for a product go on to view a product detail page?"),
    ("Q2",  "UC1", "K5", "Do users who search convert to purchase differently from users who browse without searching?"),
    ("Q3",  "UC1", "K5", "Which searches return zero results, and do those users abandon the session?"),
    ("Q4",  "UC1", "K2", "Which filters are associated with stronger product engagement and add-to-cart rate?"),
    ("Q5",  "UC1", "K2", "Which product categories have the strongest add-to-cart rate?"),
    ("Q6",  "UC1", "K1", "Do users who view reviews on the product detail page purchase at a different rate?"),
    ("Q7",  "UC2", "K1", "What percentage of product viewers complete a purchase?"),
    ("Q8",  "UC2", "K2", "What percentage of product viewers add an item to cart?"),
    ("Q9",  "UC2", "K1", "Where is the largest drop-off in the purchase funnel?"),
    ("Q10", "UC2", "K1", "Does purchase conversion differ between mobile browser and desktop?"),
    ("Q11", "UC2", "K4", "What proportion of users who add to cart never complete a purchase?"),
    ("Q12", "UC3", "K3", "What percentage of checkout starters complete an order?"),
    ("Q13", "UC3", "K3", "Which checkout step - shipping or payment - has the highest abandonment?"),
    ("Q14", "UC3", "K3", "Do guest and registered users complete checkout at different rates?"),
    ("Q15", "UC3", "K6", "What is average order value by category, by device type and by account type?"),
]

KPIS = [
    {
        "id": "K1",
        "name": "Purchase Conversion Rate",
        "use_case": "UC2",
        "value_driver": "Monetization > Path to Purchase: grow revenue by converting more of the existing traffic that already reaches a product page.",
        "optimization_area": "Understand where users drop between product discovery, cart, checkout and completed order, so investment can be directed at the step with the largest measured drop-off.",
        "question": "What percentage of users who view a product complete an order?",
        "definition": ("Unique users with Order Completed divided by unique users with Product Viewed, "
                       "within a 7-day conversion window, counted on a user basis."),
        "events": ["Product Viewed", "Product Added to Cart", "Checkout Started", "Order Completed"],
        "window": "7-day conversion window, user-level",
        "chart": "AmpliStore | Purchase Funnel (Product View to Order)",
        "chart_id": "C1",
        "priority": "P0",
        "notes": ("Denominator is Product Viewed, not all site visitors, so the metric isolates "
                  "shopping intent. Do not mix with a session-based denominator."),
    },
    {
        "id": "K2",
        "name": "Add-to-Cart Rate",
        "use_case": "UC1",
        "value_driver": "Monetization > Path to Purchase: convert product interest into cart creation.",
        "optimization_area": "Understand how effectively product detail pages and discovery paths turn interest into cart adds, by category and by device.",
        "question": "How effectively do product views lead to cart creation?",
        "definition": ("Unique users with Product Added to Cart divided by unique users with "
                       "Product Viewed, within a 1-day conversion window."),
        "events": ["Product Viewed", "Product Added to Cart"],
        "window": "1-day conversion window, user-level",
        "chart": "AmpliStore | Add-to-Cart Rate by Category and Device",
        "chart_id": "C5",
        "priority": "P0",
        "notes": "Segment by Category and by device to answer Q4, Q5.",
    },
    {
        "id": "K3",
        "name": "Checkout Completion Rate",
        "use_case": "UC3",
        "value_driver": "Monetization > Path to Purchase: recover revenue already in the cart by removing checkout friction.",
        "optimization_area": "Identify which checkout step shows the highest measured abandonment, and whether completion rates differ between guest and registered checkout.",
        "question": "How many checkout starters complete an order?",
        "definition": ("Unique users with Order Completed divided by unique users with "
                       "Checkout Started, within a 1-day conversion window."),
        "events": ["Checkout Started", "Shipping Info Added", "Payment Info Added", "Order Completed"],
        "window": "1-day conversion window, user-level",
        "chart": "AmpliStore | Checkout Funnel (Checkout Start to Order)",
        "chart_id": "C2",
        "priority": "P0",
        "notes": "Segment by Checkout Type (guest vs registered) to answer Q14.",
    },
    {
        "id": "K4",
        "name": "Cart Abandonment Rate",
        "use_case": "UC2",
        "value_driver": "Monetization > Path to Purchase: quantify the revenue sitting in abandoned carts and size the remarketing opportunity.",
        "optimization_area": "Size the abandoned-cart audience so it can be actioned through the Braze cohort sync already in the architecture.",
        "question": "What proportion of users who add products to cart fail to complete a purchase?",
        "definition": ("1 minus (unique users with Order Completed divided by unique users with "
                       "Product Added to Cart), within a 7-day conversion window."),
        "events": ["Product Added to Cart", "Order Completed"],
        "window": "7-day conversion window, user-level",
        "chart": "AmpliStore | Cart Abandonment (Cart Add to Order)",
        "chart_id": "C8",
        "priority": "P1",
        "notes": ("Complement of the cart-to-order conversion step. State the window explicitly - "
                  "a 1-day and a 7-day cart abandonment rate are different metrics."),
    },
    {
        "id": "K5",
        "name": "Product Discovery Conversion",
        "use_case": "UC1",
        "value_driver": "Monetization > Path to Purchase: assess whether search and filtering are associated with stronger progression toward purchase.",
        "optimization_area": "Compare progression to purchase for search-initiated and browse-initiated journeys, and quantify how often searches return zero results. Any difference observed is correlational.",
        "question": "How effectively do discovery behaviours lead to purchase?",
        "definition": ("Unique users with Order Completed divided by unique users with "
                       "Product Searched, within a 7-day conversion window; compared against "
                       "the same measure for users who browse without searching."),
        "events": ["Product Searched", "Product Viewed", "Product Added to Cart", "Order Completed"],
        "window": "7-day conversion window, user-level",
        "chart": "AmpliStore | Product Discovery Funnel (Search to Order)",
        "chart_id": "C3",
        "priority": "P0",
        "notes": ("Comparison is correlational. A difference between searchers and non-searchers "
                  "does not establish that search causes conversion - state this to stakeholders."),
    },
    {
        "id": "K6",
        "name": "Average Order Value",
        "use_case": "UC2",
        "value_driver": "Monetization > Upsell and Cross-sell: grow revenue per order rather than only order count.",
        "optimization_area": "Understand which categories, devices and account types produce higher-value orders to guide merchandising and promotion.",
        "question": "What is the average monetary value of completed orders?",
        "definition": ("Average of Order Completed.Total Amount over the analysis period. "
                       "Sourced from the Snowflake warehouse import so the figure reconciles "
                       "with finance."),
        "events": ["Order Completed"],
        "window": "Reported per calendar period; no conversion window applies",
        "chart": "AmpliStore | Average Order Value by Category, Device and Account Type",
        "chart_id": "C6",
        "priority": "P1",
        "notes": ("Use the warehouse-imported Total Amount as authoritative. No baseline value is "
                  "asserted here - baselines require real data."),
    },
]

# ---------------------------------------------------------------------------
# PRODUCT FLOWS  (official 'Product Flows Tracker (optional)' sheet: 4 flows,
# 5 milestone rows each)
# ---------------------------------------------------------------------------
PRODUCT_FLOWS = [
    ("Product Discovery Flow", ["Category Viewed", "Product Searched", "Filter Applied",
                                "Product Viewed", "Review Viewed"]),
    ("Purchase Flow",          ["Product Viewed", "Product Added to Cart", "Cart Viewed",
                                "Checkout Started", "Order Completed"]),
    ("Checkout Flow",          ["Cart Viewed", "Checkout Started", "Shipping Info Added",
                                "Payment Info Added", "Order Completed"]),
    ("Account & Order Management Flow", ["Account Created", "Login Completed",
                                         "Order Viewed", "Return Requested"]),
]

# ---------------------------------------------------------------------------
# TECHNICAL SCOPING - event taxonomy
# Each event: (category, name, business_question, trigger, platform, source,
#              [(property_type, property_name, sample_values, description)])
# 'source' records where the event is instrumented from - this is what makes the
# hybrid ingestion recommendation concrete rather than abstract.
# ---------------------------------------------------------------------------
EVENTS = [
    {
        "category": "Discovery",
        "name": "Product Viewed",
        "question": "What percentage of product viewers add an item to cart?",
        "trigger": "When a user opens a product detail page (PDP). Fires once per PDP view, including PDPs reached from search, category browse or a direct link.",
        "platform": "Web Only",
        "source": "Browser SDK",
        "kpis": ["K1", "K2"],
        "properties": [
            ("Event Property", "Product ID",   "SKU-10093, SKU-44120",              "Stable catalogue identifier for the product"),
            ("Event Property", "Product Name", "Ribbed Knit Midi Dress",            "Display name of the product"),
            ("Event Property", "Category",     "womens, mens, jewelry",             "Top-level merchandising category"),
            ("Event Property", "Subcategory",  "dresses, knitwear, earrings",       "Second-level merchandising category"),
            ("Event Property", "Brand",        "AmpliStore, AmpliStore Studio",     "Brand or sub-brand of the product"),
            ("Event Property", "Price",        "49.90, 129.00",                     "Displayed unit price at time of view, numeric"),
            ("Event Property", "Currency",     "USD",                               "ISO 4217 currency code of the displayed price"),
            ("Event Property", "Availability", "in stock, low stock, out of stock", "Stock state shown to the user at view time"),
            ("Event Property", "Rating Average", "4.3",                             "Average review rating displayed on the PDP, numeric"),
        ],
    },
    {
        "category": "Discovery",
        "name": "Product Searched",
        "question": "Do users who search convert differently from users who browse without searching?",
        "trigger": "When a user submits a search query from the site search bar and a results page is returned.",
        "platform": "Web Only",
        "source": "Browser SDK",
        "kpis": ["K5"],
        "properties": [
            ("Event Property", "Search Term",    "gold hoop earrings, linen shirt", "Raw query string submitted by the user"),
            ("Event Property", "Results Count",  "0, 24, 312",                      "Number of products returned; 0 identifies null-result searches"),
            ("Event Property", "Category",       "womens, mens, jewelry, all",      "Category scope the search was run within"),
            ("Event Property", "Filters Active", "size:M, colour:black",            "Filters already applied when the search was submitted, list"),
            ("Event Property", "Sort Option",    "relevance, price asc, newest",    "Sort order applied to the result set"),
        ],
    },
    {
        "category": "Discovery",
        "name": "Category Viewed",
        "question": "Which product categories have the strongest add-to-cart rate?",
        "trigger": "When a user opens a category or product listing page.",
        "platform": "Web Only",
        "source": "Browser SDK",
        "kpis": ["K2"],
        "properties": [
            ("Event Property", "Category",      "womens, mens, jewelry",      "Top-level merchandising category viewed"),
            ("Event Property", "Subcategory",   "dresses, knitwear, earrings","Second-level merchandising category viewed"),
            ("Event Property", "Product Count", "48, 120",                    "Number of products displayed in the listing"),
        ],
    },
    {
        "category": "Discovery",
        "name": "Filter Applied",
        "question": "Which filters are associated with stronger product engagement?",
        "trigger": "When a user applies a filter on a category or search results page. One event per filter applied.",
        "platform": "Web Only",
        "source": "Browser SDK",
        "kpis": ["K2"],
        "properties": [
            ("Event Property", "Filter Type",   "size, colour, price, material", "Dimension the user filtered on"),
            ("Event Property", "Filter Value",  "M, black, under 50",            "Value selected for that dimension"),
            ("Event Property", "Category",      "womens, mens, jewelry",         "Category the filter was applied within"),
            ("Event Property", "Results Count", "0, 18, 96",                     "Number of products remaining after the filter"),
        ],
    },
    {
        "category": "Product Evaluation",
        "name": "Review Viewed",
        "question": "Do users who view reviews have different purchase behaviour?",
        "trigger": "When the review section of a product detail page becomes visible to the user, or the user opens the reviews tab.",
        "platform": "Web Only",
        "source": "Browser SDK",
        "kpis": ["K1"],
        "properties": [
            ("Event Property", "Product ID",     "SKU-10093",  "Product whose reviews were viewed"),
            ("Event Property", "Rating Average", "4.3",        "Average review rating displayed, numeric"),
            ("Event Property", "Review Count",   "128",        "Number of reviews available for the product"),
        ],
    },
    {
        "category": "Cart",
        "name": "Product Added to Cart",
        "question": "What percentage of product viewers add an item to cart?",
        "trigger": "When a user successfully adds a product to the cart and the cart confirms the addition.",
        "platform": "Web Only",
        "source": "Browser SDK",
        "kpis": ["K2", "K4"],
        "properties": [
            ("Event Property", "Product ID", "SKU-10093",             "Product added to the cart"),
            ("Event Property", "Category",   "womens, mens, jewelry", "Category of the product added"),
            ("Event Property", "Quantity",   "1, 2",                  "Units added in this action, numeric"),
            ("Event Property", "Unit Price", "49.90",                 "Price per unit at time of add, numeric"),
            ("Event Property", "Currency",   "USD",                   "ISO 4217 currency code"),
            ("Event Property", "Cart Value", "149.70",                "Total cart value after the addition, numeric"),
        ],
    },
    {
        "category": "Cart",
        "name": "Product Removed from Cart",
        "question": "What proportion of users who add products fail to complete a purchase?",
        "trigger": "When a user removes a product from the cart.",
        "platform": "Web Only",
        "source": "Browser SDK",
        "kpis": ["K4"],
        "properties": [
            ("Event Property", "Product ID", "SKU-10093", "Product removed from the cart"),
            ("Event Property", "Quantity",   "1",         "Units removed in this action, numeric"),
            ("Event Property", "Unit Price", "49.90",     "Price per unit at time of removal, numeric"),
            ("Event Property", "Cart Value", "99.80",     "Total cart value after the removal, numeric"),
        ],
    },
    {
        "category": "Cart",
        "name": "Cart Viewed",
        "question": "What percentage of cart users begin checkout?",
        "trigger": "When a user opens the cart page or the cart drawer.",
        "platform": "Web Only",
        "source": "Browser SDK",
        "kpis": ["K4"],
        "properties": [
            ("Event Property", "Cart Item Count", "3",      "Number of line items in the cart, numeric"),
            ("Event Property", "Cart Value",      "149.70", "Total cart value at view time, numeric"),
            ("Event Property", "Currency",        "USD",    "ISO 4217 currency code"),
        ],
    },
    {
        "category": "Checkout",
        "name": "Checkout Started",
        "question": "What percentage of checkout starters complete a purchase?",
        "trigger": "When a user enters the first step of the checkout flow from the cart.",
        "platform": "Web Only",
        "source": "Browser SDK",
        "kpis": ["K3"],
        "properties": [
            ("Event Property", "Cart Value",    "149.70",            "Cart value entering checkout, numeric"),
            ("Event Property", "Item Count",    "3",                 "Number of line items entering checkout, numeric"),
            ("Event Property", "Currency",      "USD",               "ISO 4217 currency code"),
            ("Event Property", "Checkout Type", "guest, registered", "Whether the user is checking out as a guest or signed in"),
            ("Event Property", "Account Type",  "guest, registered", "Account state of the user at checkout start"),
        ],
    },
    {
        "category": "Checkout",
        "name": "Shipping Info Added",
        "question": "Which checkout step has the highest abandonment?",
        "trigger": "When a user successfully submits the shipping step of checkout.",
        "platform": "Web Only",
        "source": "Browser SDK",
        "kpis": ["K3"],
        "properties": [
            ("Event Property", "Shipping Method", "standard, express, store pickup", "Shipping option chosen"),
            ("Event Property", "Country",         "US",                              "Destination country code only - no street address, name or postcode is sent"),
            ("Event Property", "Cart Value",      "149.70",                          "Cart value at the shipping step, numeric"),
        ],
    },
    {
        "category": "Checkout",
        "name": "Payment Info Added",
        "question": "Which checkout step has the highest abandonment?",
        "trigger": "When a user successfully submits the payment step of checkout. No payment credentials are captured.",
        "platform": "Web Only",
        "source": "Browser SDK",
        "kpis": ["K3"],
        "properties": [
            ("Event Property", "Payment Method", "card, paypal, apple pay, klarna", "Payment type selected. Never send card number, CVV, expiry or any authentication secret."),
        ],
    },
    {
        "category": "Checkout",
        "name": "Order Completed",
        "question": "What percentage of users who enter the purchase journey complete an order?",
        "trigger": "When the order is confirmed as placed by the transaction system. Sourced from the backend, not the confirmation page, so revenue reconciles with finance and survives a browser close on the thank-you page.",
        "platform": "Web Only",
        "source": "Snowflake warehouse import (backend, authoritative)",
        "kpis": ["K1", "K3", "K4", "K6"],
        "properties": [
            ("Event Property", "Order ID",        "ORD-2026-004412",         "Unique order identifier from the transaction system"),
            ("Event Property", "Total Amount",    "149.70",                  "Order total actually charged, numeric - authoritative revenue figure"),
            ("Event Property", "Currency",        "USD",                     "ISO 4217 currency code"),
            ("Event Property", "Item Count",      "3",                       "Number of line items in the order, numeric"),
            ("Event Property", "Payment Method",  "card, paypal, apple pay", "Payment type used to settle the order"),
            ("Event Property", "Shipping Method", "standard, express",       "Shipping option purchased"),
            ("Event Property", "Coupon Code",     "SPRING10, none",          "Promotion code applied, or none"),
            ("Event Property", "Checkout Type",   "guest, registered",       "Whether the order was placed as guest or signed in"),
        ],
    },
    {
        "category": "Account",
        "name": "Account Created",
        "question": "Do guest and registered users have different checkout completion rates?",
        "trigger": "When a user completes registration and an account is successfully created.",
        "platform": "Web Only",
        "source": "Browser SDK",
        "kpis": ["K3"],
        "properties": [
            ("Event Property", "Account Type",       "registered",                "Account state after creation"),
            ("Event Property", "Acquisition Source", "organic, paid search, email","Marketing source of the registration where legitimately available"),
            ("User Property",  "Account Type",       "guest, registered",         "Set to registered on account creation - see User Properties sheet"),
        ],
    },
    {
        "category": "Account",
        "name": "Login Completed",
        "question": "Do returning users convert differently from new users?",
        "trigger": "When a user successfully authenticates. This is the point at which the Amplitude User ID is set.",
        "platform": "Web Only",
        "source": "Browser SDK",
        "kpis": ["K3"],
        "properties": [
            ("Event Property", "Login Method", "email, google, apple", "Authentication method used"),
            ("Event Property", "Account Type", "registered",           "Account state after authentication"),
        ],
    },
    {
        "category": "Order Management",
        "name": "Order Viewed",
        "question": "Where are checkout users most likely to abandon?",
        "trigger": "When a user opens an order detail page from order history.",
        "platform": "Web Only",
        "source": "Browser SDK",
        "kpis": [],
        "properties": [
            ("Event Property", "Order ID",     "ORD-2026-004412",                    "Order being viewed"),
            ("Event Property", "Order Status", "processing, shipped, delivered, returned", "Fulfilment status shown to the user"),
            ("Event Property", "Order Value",  "149.70",                             "Value of the order being viewed, numeric"),
        ],
    },
    {
        "category": "Order Management",
        "name": "Return Requested",
        "question": "Which categories have the strongest purchase conversion?",
        "trigger": "When a user submits a return request for one or more items in an order.",
        "platform": "Web Only",
        "source": "Snowflake warehouse import (backend, authoritative)",
        "kpis": [],
        "properties": [
            ("Event Property", "Order ID",      "ORD-2026-004412",                  "Order the return relates to"),
            ("Event Property", "Return Reason", "size, quality, changed mind, damaged", "Reason selected by the user from a fixed list"),
            ("Event Property", "Item Count",    "1",                                "Number of items being returned, numeric"),
        ],
    },
]

# ---------------------------------------------------------------------------
# USER PROPERTIES  (user-level state only; nothing event-specific)
# ---------------------------------------------------------------------------
USER_PROPERTIES = [
    ("Account Type", "Do guest and registered users behave differently?",
     "Current account state of the user. Set to registered on Account Created and on Login Completed.",
     "guest, registered", "Web Only", "No", "Browser SDK"),
    ("Loyalty Status", "Do loyalty members convert and spend differently?",
     "Loyalty tier held by the user, maintained by the CRM and synced through the warehouse import.",
     "none, standard, loyal", "Web Only", "No", "Snowflake warehouse import"),
    ("Preferred Category", "Does a user's dominant category predict conversion or AOV?",
     "Dominant purchase category over the trailing 12 months, computed in the warehouse - not set client-side.",
     "mens, womens, jewelry", "Web Only", "No", "Snowflake warehouse import"),
    ("Registration Date", "Do recently registered users convert differently from long-tenured ones?",
     "Date the account was created, used for tenure analysis and cohorting.",
     "2026-03-14", "Web Only", "No", "Browser SDK"),
    ("Total Orders Completed", "How many lifetime orders has this user placed?",
     "Incremental user property, increased by one on each Order Completed. Best practice for milestone events per the Taxonomy Best Practices sheet.",
     "0, 1, 7", "Web Only", "No", "Snowflake warehouse import"),
    ("Internal User", "Can internal and QA traffic be excluded from analysis?",
     "Flag for AmpliStore staff and QA accounts so they can be filtered out of every chart.",
     "true, false", "Web Only", "No", "Browser SDK"),
]

# Deliberately NOT added as custom user properties, and why. This is a scoping
# decision the reviewer should see, not an omission.
USER_PROPERTIES_DELIBERATELY_EXCLUDED = [
    ("Country", "Already provided by the Amplitude SDK default 'Country' user property (GeoIP). "
                "Adding a custom duplicate would trip the 'duplicated across event and user properties' QA check."),
    ("Device Type / Platform", "Already provided by Amplitude SDK defaults. Mobile-browser vs desktop "
                               "segmentation uses the default Device Family / Platform properties."),
    ("Customer Segment (new / returning / loyal)", "Overlaps with Loyalty Status and with Amplitude's "
                                                   "built-in new-vs-returning behavioural cohorts. One "
                                                   "well-defined property beats two overlapping ones."),
    ("Email address / name / shipping address", "PII with no analytical use case in the scoped questions."),
]

# ---------------------------------------------------------------------------
# AI DELIVERABLES PLAN
#
# PROVENANCE - read this before presenting:
# The Capstone PDF requires "which of the five standard AI deliverables apply to
# this scenario and when each would be delivered". The PDF does not name them.
# No file in this workspace prints a list under the literal heading "the five
# standard AI deliverables".
#
# The five below are NOT invented. Each is quoted verbatim from the official
# 2026 Partnership Kickoff Deck, slide 16 ("Implementation roadmap: Core
# Analytics"), which contains exactly five AI activities, and each is
# independently corroborated by a row in the official 2026 Implementation
# Workbook 'Project Plan Gantt View' sheet. Phase and week are the official
# roadmap's own sequencing, not ours.
#
# ACTION REQUIRED: confirm the canonical names against Partner Academy training
# before presenting. See validation/unresolved_items.md.
# ---------------------------------------------------------------------------
AI_DELIVERABLES = [
    {
        "n": 1,
        "official_name": "Confirm legal approval on AI functionality",
        "deck_source": "Kickoff Deck slide 16, Alignment / Week 0 column",
        "workbook_source": "Project Plan Gantt View, row 12 note: 'Align on org usage and approval of AI features'",
        "phase": "Alignment",
        "timing": "Week 0 - at or immediately after kickoff",
        "owner": "Customer (Executive Advocate + Legal/Privacy) with Amplitude support",
        "applies": "Yes",
        "scenario_rationale": (
            "AmpliStore is D2C retail handling order and customer data. Legal and privacy sign-off "
            "on AI features is a hard prerequisite - every later AI deliverable is blocked until it "
            "lands, which is why it is also carried as a project risk."
        ),
        "exit_criteria": "Written approval on AI feature usage; decision recorded on admin-only vs org-wide rollout.",
    },
    {
        "n": 2,
        "official_name": "AI admin walkthrough",
        "deck_source": "Kickoff Deck slide 16, Technical scoping column",
        "workbook_source": "Project Plan Gantt View, row 15: 'AI Agents Walkthrough Training for Admins'",
        "phase": "Technical Scoping",
        "timing": "Weeks 3-4 - alongside event taxonomy design",
        "owner": "Amplitude, with the customer's Project Lead and Technical Lead attending",
        "applies": "Yes",
        "scenario_rationale": (
            "Sequenced with taxonomy design on purpose: admins learn what AI agents need from the "
            "data model while the AmpliStore taxonomy is still being shaped, so event and property "
            "descriptions are written to be AI-legible rather than retrofitted."
        ),
        "exit_criteria": "Admins can configure agent access and permissions; AI governance owner named.",
    },
    {
        "n": 3,
        "official_name": "Send data to production and set up AI context",
        "deck_source": "Kickoff Deck slide 16, Prod launch column",
        "workbook_source": "Project Plan Gantt View, row 30: 'Set up Context and Global Agent'",
        "phase": "Instrumentation to Launch",
        "timing": "Weeks 9-10 - immediately after production data lands",
        "owner": "Customer (Technical Lead) with Amplitude support",
        "applies": "Yes",
        "scenario_rationale": (
            "AI context must be grounded in real production data. For AmpliStore the context needs "
            "the category taxonomy (mens/womens/jewelry), the guest-vs-registered checkout "
            "distinction, and the fact that Order Completed is warehouse-sourced and authoritative "
            "for revenue - otherwise an agent may answer revenue questions from client-side data."
        ),
        "exit_criteria": "Production project populated; business context uploaded; event and property descriptions complete.",
    },
    {
        "n": 4,
        "official_name": "AI dashboards and set up Global Agent",
        "deck_source": "Kickoff Deck slide 16, Prod launch column",
        "workbook_source": "Project Plan Gantt View, rows 28-29: 'Build reports in Amplitude' (note: 'Use Global Agent to build out key reporting') and 'Set up Dashboard Agent'",
        "phase": "Launch",
        "timing": "Weeks 9-10 - after AI context is in place",
        "owner": "Shared - Amplitude builds with the customer's Business Lead",
        "applies": "Yes",
        "scenario_rationale": (
            "This is where the eight scoped charts and the AmpliStore Executive Analytics dashboard "
            "are built and validated, and where the Dashboard Agent is pointed at that dashboard. "
            "Deliberately after #3: an agent configured before context exists produces confident "
            "answers from an incomplete data model."
        ),
        "exit_criteria": "Executive dashboard live and validated against the scoped business questions; Global Agent answering them in context.",
    },
    {
        "n": 5,
        "official_name": "Foundational training for Analytics and AI",
        "deck_source": "Kickoff Deck slide 16, Enablement and rollout column",
        "workbook_source": "Project Plan Gantt View, rows 31/35: 'Foundational Training'",
        "phase": "Enablement and Rollout",
        "timing": "Weeks 11-14",
        "owner": "Amplitude delivers; customer nominates the audience",
        "applies": "Yes",
        "scenario_rationale": (
            "Merchandising, growth and CRM analysts are the day-to-day audience. Training closes the "
            "loop: they learn to interrogate the funnel themselves rather than queue requests, which "
            "is what makes the implementation stick after the engagement ends."
        ),
        "exit_criteria": "Trained user cohort able to build their own charts and use Global Agent; data governance owner handed over.",
    },
]

# ---------------------------------------------------------------------------
# INSTRUMENTATION
# ---------------------------------------------------------------------------
INSTRUMENTATION = {
    "recommendation": "Hybrid",
    "headline": (
        "Hybrid: Amplitude Browser SDK for behavioural events, Snowflake warehouse import for "
        "authoritative order and revenue data."
    ),
    "why": [
        "Behavioural context lives in the browser. Search terms, filters applied, PDP views, cart "
        "activity and checkout step progression only exist client-side; the SDK captures them with "
        "session and attribution context attached automatically.",
        "Revenue must reconcile with finance. Order Completed and Total Amount are authoritative "
        "business facts, so they come from the transaction system of record via the Snowflake "
        "warehouse import shown in the official pre-sales architecture - not from the browser, "
        "where a closed tab, an ad blocker or a failed beacon silently loses an order.",
        "Precision-only tracking would leave the checkout and discovery experience unmeasurable. "
        "Warehouse-only would leave revenue trustworthy but the funnel blind.",
    ],
    "frontend_scope": ["Product Viewed", "Product Searched", "Category Viewed", "Filter Applied",
                       "Review Viewed", "Product Added to Cart", "Product Removed from Cart",
                       "Cart Viewed", "Checkout Started", "Shipping Info Added",
                       "Payment Info Added", "Account Created", "Login Completed", "Order Viewed"],
    "backend_scope": ["Order Completed", "Return Requested"],
    "tradeoffs": [
        ("Coordination cost", "Two teams instrument one taxonomy. Mitigated by a single shared "
                              "tracking plan in Amplitude Data and one naming style guide."),
        ("Identity stitching", "Warehouse-sourced orders must carry the same User ID the browser "
                               "sets at login, or orders detach from the behavioural funnel. This is "
                               "the single highest-risk item in the plan and is tracked as Q2 and R2."),
        ("Latency", "Warehouse import is batch, so orders arrive later than client-side events. "
                    "Acceptable for funnel and AOV reporting; not acceptable for real-time "
                    "triggering, which is why the Braze cohort sync is the action path."),
        ("Deduplication", "Server-sourced events need a unique insert_id so a replayed batch does "
                          "not double-count revenue."),
    ],
    "http_api_position": (
        "The HTTP V2 API is the alternative to warehouse import for backend events and is the right "
        "choice when order events are needed in minutes rather than hours - for example to trigger a "
        "real-time abandonment journey. We recommend warehouse import for Phase 1 because the "
        "official AmpliStore architecture already lands orders and revenue in Snowflake, so import "
        "reuses a governed, finance-reconciled dataset instead of standing up and maintaining a new "
        "server-side event pipeline. If latency requirements tighten, HTTP V2 can be added for "
        "Order Completed without changing the taxonomy - the event and property contract is identical."
    ),
    "autocapture": (
        "Browser SDK autocapture (sessions, page views, form starts/submissions, file downloads, "
        "marketing attribution) is enabled to provide baseline coverage and attribution from day one. "
        "The 16 scoped events are custom-instrumented, because autocaptured clicks cannot carry the "
        "commerce context - Product ID, Category, Cart Value - that every scoped question depends on."
    ),
}

USER_IDENTIFICATION = {
    "anonymous": (
        "Anonymous shoppers carry the SDK-generated Device ID only. No User ID is set before "
        "authentication. Setting a provisional User ID on an anonymous visitor is the single most "
        "common cause of unmergeable identities in Amplitude."
    ),
    "authenticated": (
        "On Account Created and Login Completed, set the Amplitude User ID to the stable internal "
        "customer identifier from the commerce platform. Not the email address: emails change, are "
        "PII, and are frequently re-used across guest orders."
    ),
    "transition": (
        "Amplitude merges the pre-login anonymous Device ID history with the User ID on first "
        "identify, so a browse-then-register session stays one user in the funnel."
    ),
    "logout": (
        "On logout, reset so a subsequent shopper on a shared device is not attributed to the "
        "previous user. This starts a new anonymous Device ID rather than reusing the old one."
    ),
    "guest_checkout": (
        "Guest checkout is the hard case and must be explicitly decided. A guest order has no "
        "authenticated User ID at the time of purchase. Recommendation: do not back-fill a User ID "
        "onto guest sessions; report guest conversion on a Device ID basis and use the Checkout Type "
        "property to segment. If the business needs guest orders attributed to a known customer "
        "record, that is a warehouse-side join, not a client-side identity change."
    ),
    "cross_device": (
        "Cross-device stitching works only for authenticated users. Mobile-browser-to-desktop "
        "journeys by anonymous shoppers will appear as two users; state this limitation when "
        "presenting device comparisons rather than letting stakeholders over-read the numbers."
    ),
    "warehouse_join": (
        "Warehouse-imported Order Completed rows must carry the same internal customer identifier "
        "used as the Amplitude User ID, plus a unique insert_id for deduplication."
    ),
    "status": "PROPOSED - not implemented. Confirmation is tracked as open question Q2.",
}

# ---------------------------------------------------------------------------
# DATA SOURCES AND DESTINATIONS
# Grounded in the OFFICIAL AmpliStore pre-sales architecture, Capstone PDF p.7.
# ---------------------------------------------------------------------------
SOURCES = [
    {
        "name": "AmpliStore Web (desktop + mobile browser)",
        "method": "Amplitude Browser SDK",
        "detail": "track() / identify(); autocapture enabled for sessions, page views, forms and attribution",
        "scope": "In scope - Phase 1",
        "official": True,
        "events": "14 behavioural events across discovery, cart, checkout and account",
    },
    {
        "name": "Order / transaction backend",
        "method": "Snowflake warehouse import",
        "detail": "Orders, revenue and returns imported from the customer's Snowflake instance",
        "scope": "In scope - Phase 1",
        "official": True,
        "events": "Order Completed, Return Requested",
    },
    {
        "name": "Order / transaction backend (low-latency alternative)",
        "method": "HTTP V2 API",
        "detail": "Server-side event ingestion with insert_id deduplication. Considered and not selected for Phase 1 - see instrumentation rationale.",
        "scope": "Alternative - evaluated, not in Phase 1 scope",
        "official": False,
        "events": "Order Completed (if near-real-time triggering becomes a requirement)",
    },
]

DESTINATIONS = [
    {
        "name": "Braze",
        "method": "Cohort sync",
        "detail": "Engagement platform - cart abandonment and promotional journeys",
        "scope": "In scope - Phase 1",
        "official": True,
        "audiences": "Cart abandoners, high-value purchasers, search-led non-converters",
    },
    {
        "name": "Snowflake",
        "method": "Data export",
        "detail": "Enriched behavioural data returned to the warehouse for blending with order and margin data",
        "scope": "In scope - Phase 1",
        "official": True,
        "audiences": "Event export, not audience sync",
    },
    {
        "name": "Amazon S3",
        "method": "Data export",
        "detail": "Raw event export to object storage",
        "scope": "Potential downstream destination / out of Phase 1 scope",
        "official": False,
        "audiences": "N/A",
    },
    {
        "name": "BigQuery",
        "method": "Data export",
        "detail": "Warehouse export - relevant only if AmpliStore adopts GCP alongside Snowflake",
        "scope": "Potential downstream destination / out of Phase 1 scope",
        "official": False,
        "audiences": "N/A",
    },
]

AMPLITUDE_PROJECTS = [
    ("AmpliStore Web", "Dev",     "AmpliStore web taxonomy", "[Dev] AmpliStore Web",     "Web"),
    ("AmpliStore Web", "Staging", "AmpliStore web taxonomy", "[Staging] AmpliStore Web", "Web"),
    ("AmpliStore Web", "Prod",    "AmpliStore web taxonomy", "[Prod] AmpliStore Web",    "Web"),
    ("Snowflake order import", "Dev",  "AmpliStore web taxonomy", "[Dev] AmpliStore Web",  "Web"),
    ("Snowflake order import", "Prod", "AmpliStore web taxonomy", "[Prod] AmpliStore Web", "Web"),
]

# ---------------------------------------------------------------------------
# AMPLITUDE FEATURES - value to AmpliStore, not feature tourism
# ---------------------------------------------------------------------------
AMPLITUDE_FEATURES = [
    ("Funnel Analysis",
     "Shows exactly where shoppers drop between product view, cart, checkout and order, and how "
     "that differs by device and category. This is what turns 'checkout feels bad on mobile' into "
     "'X% of mobile users abandon at the payment step'.",
     ["C1", "C2", "C3"]),
    ("Segmentation",
     "Compares conversion across mobile browser vs desktop, category, and guest vs registered "
     "checkout - the three dimensions AmpliStore's scoped questions turn on.",
     ["C4", "C5", "C7"]),
    ("Cohorts",
     "Reusable audiences - cart abandoners, high-value purchasers, search-led non-converters - "
     "that sync to Braze through the destination already in the architecture, so an insight becomes "
     "a campaign without an engineering ticket.",
     ["C8"]),
    ("Retention Analysis",
     "Shows whether first-time purchasers come back, which is what separates a discount-driven spike "
     "from durable growth in a D2C business.",
     []),
    ("Dashboards",
     "One executive view of the scoped KPIs so the leadership team reads the same numbers weekly "
     "instead of commissioning ad-hoc pulls.",
     ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"]),
    ("Global Agent",
     "An in-product AI analyst that analyses questions in context, grounded in events, funnels, "
     "cohorts, experiments and session replay. For AmpliStore it lets merchandising ask 'why did "
     "jewelry conversion fall last week' without waiting on an analyst. "
     "(Description follows the official 2026 deck wording - no capabilities are claimed beyond it.)",
     []),
]

# ---------------------------------------------------------------------------
# CHART SPECIFICATIONS
# ---------------------------------------------------------------------------
CHARTS = [
    {
        "id": "C1",
        "name": "AmpliStore | Purchase Funnel (Product View to Order)",
        "use_case": "UC2", "kpi": "K1",
        "question": "Where do users drop before purchase, and does that differ by device?",
        "type": "Funnel Analysis",
        "steps": ["Product Viewed", "Product Added to Cart", "Checkout Started", "Order Completed"],
        "filters": "Internal User = false",
        "segments": "All Users (headline funnel). Device breakdown is deliberately kept in C4 to avoid a redundant chart.",
        "window": "7-day conversion window, user-level, ordered steps",
        "insight": ("Shows the relative size of the drop-off at each step of the purchase journey, so the "
                    "step with the largest measured decrease can be prioritised. Interpretation requires "
                    "the conversion window and population to be stated alongside any figure quoted."),
        "dashboard": "AmpliStore Executive Analytics",
        "answers": ["Q7", "Q9", "Q10"],
    },
    {
        "id": "C2",
        "name": "AmpliStore | Checkout Funnel (Checkout Start to Order)",
        "use_case": "UC3", "kpi": "K3",
        "question": "Which checkout step has the highest abandonment?",
        "type": "Funnel Analysis",
        "steps": ["Checkout Started", "Shipping Info Added", "Payment Info Added", "Order Completed"],
        "filters": "Internal User = false",
        "segments": "Checkout Type (guest vs registered)",
        "window": "1-day conversion window, user-level, ordered steps",
        "insight": ("Isolates shipping-step versus payment-step friction. A large guest-vs-registered gap "
                    "at the shipping step points at forced account creation."),
        "dashboard": "AmpliStore Executive Analytics",
        "answers": ["Q12", "Q13", "Q14"],
    },
    {
        "id": "C3",
        "name": "AmpliStore | Product Discovery Funnel (Search to Order)",
        "use_case": "UC1", "kpi": "K5",
        "question": "Does search effectively move users toward purchase?",
        "type": "Funnel Analysis",
        "steps": ["Product Searched", "Product Viewed", "Product Added to Cart", "Order Completed"],
        "filters": "Internal User = false",
        "segments": "Results Count = 0 vs Results Count > 0 (null-result searches)",
        "window": "7-day conversion window, user-level, ordered steps",
        "insight": ("Measures how often searches return zero results and whether search-initiated journeys "
                    "reach purchase at a different rate from browse-initiated ones. Any difference is "
                    "correlational: it does not establish that searching causes conversion, because "
                    "intent and population composition are not controlled for."),
        "dashboard": "AmpliStore Executive Analytics",
        "answers": ["Q1", "Q3"],
    },
    {
        "id": "C4",
        "name": "AmpliStore | Purchase Conversion by Device",
        "use_case": "UC2", "kpi": "K1",
        "question": "Does mobile browser underperform desktop on purchase conversion?",
        "type": "Funnel Analysis, conversion over time",
        "steps": ["Product Viewed", "Order Completed"],
        "filters": "Internal User = false",
        "segments": "Device Family: mobile browser, desktop, tablet",
        "window": "7-day conversion window, user-level",
        "insight": ("The scenario states mobile browsers are a significant traffic source. If a material "
                    "difference between device families is measured, it would indicate where to "
                    "investigate first. A difference in observed rates is correlational and would need "
                    "further investigation before being attributed to the device experience."),
        "dashboard": "AmpliStore Executive Analytics",
        "answers": ["Q10"],
    },
    {
        "id": "C5",
        "name": "AmpliStore | Add-to-Cart Rate by Category and Device",
        "use_case": "UC1", "kpi": "K2",
        "question": "Which categories and filters turn product views into cart adds most effectively?",
        "type": "Funnel Analysis, segmented",
        "steps": ["Product Viewed", "Product Added to Cart"],
        "filters": "Internal User = false",
        "segments": "Category: mens, womens, jewelry; secondary split by Device Family",
        "window": "1-day conversion window, user-level",
        "insight": ("Shows whether measured add-to-cart rates differ by category, which would indicate "
                    "where to investigate merchandising or product-page experience. Differences "
                    "observed are a starting point for investigation, not a diagnosis."),
        "dashboard": "AmpliStore Executive Analytics",
        "answers": ["Q4", "Q5", "Q8"],
    },
    {
        "id": "C6",
        "name": "AmpliStore | Average Order Value by Category, Device and Account Type",
        "use_case": "UC2", "kpi": "K6",
        "question": "What is average order value, and which segments produce higher-value orders?",
        "type": "Event Segmentation - average of a numeric property",
        "steps": ["Order Completed"],
        "filters": "Internal User = false",
        "segments": "Category, Device Family, Checkout Type",
        "window": "Reported per calendar period",
        "insight": ("Guides merchandising and promotion. Uses the warehouse-sourced Total Amount so the "
                    "figure reconciles with finance."),
        "dashboard": "AmpliStore Executive Analytics",
        "answers": ["Q15"],
    },
    {
        "id": "C7",
        "name": "AmpliStore | Guest vs Registered Checkout Completion",
        "use_case": "UC3", "kpi": "K3",
        "question": "Does account type correlate with checkout completion?",
        "type": "Funnel Analysis, segmented",
        "steps": ["Checkout Started", "Order Completed"],
        "filters": "Internal User = false",
        "segments": "Checkout Type: guest vs registered",
        "window": "1-day conversion window, user-level",
        "insight": ("Compares measured checkout completion for guest and registered checkout. Correlational "
                    "only: a difference may reflect the smoothness of the registered path, or simply "
                    "that registered users arrive with higher intent. Do not present as causal."),
        "dashboard": "AmpliStore Executive Analytics",
        "answers": ["Q14"],
    },
    {
        "id": "C8",
        "name": "AmpliStore | Cart Abandonment and Abandoner Cohort",
        "use_case": "UC2", "kpi": "K4",
        "question": "What proportion of cart builders never purchase, and how large is that audience?",
        "type": "Funnel Analysis + saved Cohort",
        "steps": ["Product Added to Cart", "Order Completed"],
        "filters": "Internal User = false",
        "segments": "Cart Value bands; Device Family",
        "window": "7-day conversion window, user-level",
        "insight": ("Sizes the abandoned-cart audience and saves it as a cohort for the Braze sync "
                    "already present in the architecture, turning the metric into a campaign."),
        "dashboard": "AmpliStore Executive Analytics",
        "answers": ["Q11"],
    },
]

DASHBOARD = {
    "name": "AmpliStore Executive Analytics",
    "audience": "Executive Advocate, Business Lead, merchandising and growth leads",
    "layout": [
        ("Row 1 - KPI tiles", ["Purchase Conversion Rate (K1)", "Add-to-Cart Rate (K2)",
                               "Checkout Completion Rate (K3)", "Average Order Value (K6)"]),
        ("Row 2 - Where do we lose people?", ["C1 Purchase Funnel", "C2 Checkout Funnel"]),
        ("Row 3 - Who is affected?", ["C4 Conversion by Device", "C5 Add-to-Cart by Category"]),
        ("Row 4 - Discovery and recovery", ["C3 Discovery Funnel", "C7 Guest vs Registered",
                                            "C8 Cart Abandonment"]),
    ],
    "best_practices": [
        "One question per chart. If a chart needs a paragraph to explain, it is two charts.",
        "Order top-to-bottom as headline KPIs, then where the loss happens, then who it happens to.",
        "Name charts as the question they answer, not the chart type used.",
        "Apply Internal User = false consistently so every number on the dashboard shares a population.",
        "State the conversion window on funnel charts - a 1-day and a 7-day funnel are different metrics.",
        "Keep it to one screen of scroll for executives; depth belongs in linked charts, not this board.",
        "Assign an owner and a review cadence, or the dashboard rots within a quarter.",
    ],
}

RISKS = [
    ("Engineering resource availability",
     "Taxonomy implementation and dev-data delivery could slip, pushing the launch date. "
     "Potential risk for planning - not a confirmed customer constraint."),
    ("User identity strategy not finalised",
     "If warehouse-imported orders do not carry the same User ID the browser sets at login, orders "
     "detach from the behavioural funnel and every conversion KPI understates. Highest-impact "
     "technical risk in the plan."),
    ("Privacy and legal approval for AI functionality",
     "AI deliverables 2-5 are all blocked until approval lands in Week 0, so a delay here compresses "
     "the entire AI track into the rollout window."),
]

ACTION_ITEMS = [
    ("Schedule product walkthrough (20 min demo of key user flows)", "Customer - Project Lead", "Within 1 week", "None"),
    ("Confirm top 2-3 use cases and executive sign-off", "Customer - Executive Advocate", "Week 1-2", "Product walkthrough"),
    ("Confirm KPI scope (6 KPIs proposed)", "Customer - Business Lead", "Week 1-2", "Use case sign-off"),
    ("Confirm technical lead and engineering resourcing", "Customer - Project Lead", "Week 0-1", "None"),
    ("Confirm user identification strategy, including guest checkout", "Customer - Technical Lead", "Week 0-1", "Engineering kickoff"),
    ("Confirm ingestion architecture and Snowflake import access", "Shared", "Week 1-2", "Engineering kickoff"),
    ("Confirm legal approval on AI functionality", "Customer - Executive Advocate + Legal", "Week 0", "None"),
    ("Review and sign off event taxonomy (16 events)", "Shared", "Week 3-4", "Use case sign-off"),
    ("Send data to development project", "Customer - Engineering", "Week 5-8", "Taxonomy sign-off"),
    ("Schedule recurring implementation meetings", "Amplitude / Partner", "Week 0", "None"),
    ("Gather initial AI business context for the priority project", "Customer - Business Lead", "Week 9-10", "Legal approval; production data"),
]
