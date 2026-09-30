# Demo taxonomy mapping — partner-training org

Verified live on 2026-08-27 in the Amplitude partner-training organization.

- **Org:** `partner-training`
- **Project:** `Amplistore 2.0 (E-commerce 2024)`
- **Project ID:** `616592`
- **Total events in project:** 105
- **Project event volume:** 3,433,169

## Why this table exists

The Capstone explicitly states the demo dataset is *"a reference for taxonomy and
chart-building — it is not meant to represent a real implementation. Do not simply
replicate what's already in the org."*

Our recommended taxonomy (see `content_model.py`) is therefore **unchanged** by what
the demo happens to contain. This table exists only to say which demo event each
chart is built on, so the charts can be demonstrated live against real data.

## Mapping

| Recommended event (our taxonomy) | Demo event used for charts | Demo source | 30-day volume | Usable |
|---|---|---|---|---|
| Product Viewed | `View Item Details` | Browser SDK + HTTP API | 450,530 | Yes |
| Product Searched | `Search for Items` | HTTP API | 404,535 | Yes |
| Product Added to Cart | `Add to Cart` | Browser SDK + HTTP API | 315,860 | Yes |
| Checkout Started | `Checkout` | Browser SDK + HTTP API | 89,538 | Yes |
| Category Viewed | `Browse by Category` | HTTP API | 53,168 | Yes |
| Review Viewed | `Rating Viewed` (aka `View Rating`) | HTTP API | 50,272 | Yes |
| Order Completed | `Place Order` | HTTP API | 39,636 | Yes |
| Cart Viewed | `View Cart` | Browser SDK | 2 | No — negligible volume |
| Filter Applied | *no demo equivalent* | — | — | No |
| Shipping Info Added | *no demo equivalent* | — | — | No |
| Payment Info Added | *no demo equivalent* | — | — | No |
| Product Removed from Cart | *no demo equivalent* | — | — | No |
| Account Created / Login Completed | *not confirmed in demo* | — | — | No |
| Order Viewed / Return Requested | *not confirmed in demo* | — | — | No |

## Consequences for the chart build

- **C2 (Checkout Funnel: Checkout Started → Shipping Info Added → Payment Info Added →
  Order Completed) cannot be built.** The demo has no checkout sub-step events. C2
  remains a specification. This is a limitation of the demo dataset, not of the proposed
  taxonomy — and it is worth stating to the reviewer, because instrumenting those two
  sub-steps is exactly what would make checkout abandonment diagnosable for a real
  AmpliStore.
- All other charts substitute the mapped demo event above.

## Naming-convention corroboration

The demo project's own events use Title Case with spaces (`Add to Cart`,
`View Item Details`, `Place Order`, `Browse by Category`). This independently supports
the naming decision taken from the official workbook's Taxonomy Best Practices sheet.

## Notable observation

The demo sources `Place Order` via **HTTP API**, i.e. server-side — consistent with our
recommendation that completed orders and revenue be sourced from the backend rather than
the browser. The official AmpliStore pre-sales architecture uses a Snowflake warehouse
import for the same data; both are backend paths, and the tradeoff between them is
discussed in the instrumentation section.
