# Unresolved Items — AmpliStore 2.0 Capstone

Everything here is genuinely open. Nothing on this list has been invented, guessed or
quietly filled in. Items are also tracked in the workbook's `Question Tracker` sheet.

## P0 — must be resolved before presenting

| # | Item | Why it matters | Owner |
|---|---|---|---|
| 1 | **Presenter title and company** on the deck cover | Currently `TBD`. Presenter name is set to Bhargavi Devi as instructed; title and company were deliberately not inferred from email, git or account data. | You |
| 2 | **Canonical names of the five standard AI deliverables** | Ours are quoted verbatim from the official 2026 roadmap (Kickoff deck slide 16) and corroborated by the workbook Gantt, but no supplied file prints them under the literal heading "the five standard AI deliverables". Confirm against Partner Academy before presenting. | You / Partner Enablement |
| 3 | **Named individuals for all project roles** | Every Amplitude-side and customer-side name is `TBD`. No names were invented. Fill in if your reviewer expects them, or present them as mock roles. | You |

## P1 — scenario decisions a real engagement would confirm at kickoff

| # | Item | Current state |
|---|---|---|
| 4 | Final user identification strategy, including guest checkout | Proposed in the Alignment sheet, not confirmed. Highest technical risk in the plan. |
| 5 | Authoritative backend system for order completion and revenue | Official pre-sales architecture shows Snowflake; assumed to be the system of record. |
| 6 | Whether `Checkout Type` (guest vs registered) will be instrumented in Phase 1 | Required by UC3 and chart C7. |
| 7 | Whether `Shipping Info Added` / `Payment Info Added` will be instrumented | Required by chart C2. |
| 8 | Authoritative order-total property and its data type | Required by KPI 6 (AOV) and chart C6. Must be numeric. Decision taken: C6 stays a documented gap (G2); Average Item Price was explicitly rejected as a substitute because it answers a different business question. |
| 9 | Launch target date and engineering sprint / release cycle | All dates are `TBD`. None invented. |
| 10 | Agreed conversion windows (7-day purchase, 1-day add-to-cart) | Proposed and applied consistently, not agreed. |
| 11 | Downstream destinations beyond Braze and Snowflake | S3 / BigQuery marked out of Phase 1 scope. |

## Known limitations — what could not be verified

- **No AmpliStore data exists.** AmpliStore 2.0 is a mock scenario. Nothing is instrumented, so
  every row of the workbook's `Taxonomy and Data QA` sheet is marked `N/A`, not `Pass`. A 16-item
  planned-QA table records what would be validated and when.
- **No baselines.** No conversion rate, revenue figure, customer count, AOV or engineering
  availability is asserted anywhere. The live charts display partner-training demo data; those
  figures are labelled demo observations in the chart specification and are deliberately kept
  out of the workbook.
- **Three of eight charts could not be built** because the demo project lacks the required events
  or properties. See `output/AmpliStore_Chart_Specifications.md` for the evidence behind each.
- **The demo dataset is not AmpliStore.** Its `Product Category` values are grocery
  (Protein, Pantry, Dairy, Cleaning, Produce), not the apparel and jewelry categories in the
  scenario. Chart C5 is structurally correct but its category labels are demo artefacts.

## External steps this work cannot complete

The capstone is not complete until these happen, and none of them can be done from here:

1. Present the kickoff live (camera on) to your reviewer, or record a 20-minute version.
2. Walk through the Amplitude charts **live** in the partner-training org — the capstone
   explicitly forbids relying on screenshots.
3. Submit the deck and workbook in the Partner Academy course *before* the meeting.
4. Book the 60-minute review slot via the Calendly link in the Capstone PDF.
5. Receive the completed rubric and, on a pass, the Certified Amplitude Delivery Partner badge.
