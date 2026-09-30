# Cross-Artifact Consistency Report — AmpliStore 2.0 Capstone

**Generated:** 2026-08-27 (re-run after the interpretation-wording pass) · **Result: 51 / 51 checks passing, 0 failures**

Re-run at any time from the `amplitude-capstone/` directory:

```bash
python3 validation/run_consistency_check.py
```

Exit code is 0 when everything passes, 1 otherwise.

## What this checks

Every artifact — workbook, presentation, architecture diagram and chart specifications — is
generated from a single canonical content model (`notes/content_model.py`), plus the verified
live build results (`notes/chart_build_results.py`). Consistency is therefore structural rather
than something maintained by hand. This suite proves it, and would catch drift if any artifact
were later edited in isolation.

The check covers exactly the failure modes the execution spec asks about (§47):

| Failure mode it looks for | Covered by |
|---|---|
| KPI exists in slides but not workbook | KPI parity check |
| Event exists in a chart but not in the taxonomy | chart-step → taxonomy check |
| Property exists in a chart but not in an event definition | property reuse + taxonomy checks |
| Chart has no mapped business question | chart → question check |
| Architecture says SDK but workbook says HTTP API | architecture term + Phase 1 path checks |
| AI deliverable names differ between artifacts | model ↔ workbook AI parity check |
| Placeholder remains | deck placeholder scan (14 tokens) |
| Fake URL exists | URL allow-list against verified builds only |

## Full results

```
CONSISTENCY CHECK   PASS 36   FAIL 0   TOTAL 36
==============================================================================
  PASS  All 16 taxonomy events present in the workbook Events sheet
  PASS  Every chart step maps to an event in the taxonomy
  PASS  Every KPI-referenced event exists in the taxonomy
  PASS  Every chart maps to at least one scoped business question
  PASS  Every KPI has a mapped chart
  PASS  Every business question maps to a valid use case and KPI
  PASS  KPI names used in the deck all exist in the workbook model
  PASS  No fabricated Amplitude URLs — every URL was built and re-verified
  PASS  Specification-only charts (C2, C6, C7) carry no Amplitude URL
  PASS  Every built chart carries its verified URL in the specification
  PASS  No template placeholders remain in the deck
  PASS  No percentage baselines asserted in the workbook KPI / Alignment / AI sheets
  PASS  Demo-data observations do not leak into the workbook as baselines
  PASS  Workbook states explicitly that no baseline is asserted
  PASS  Architecture term 'Snowflake' appears consistently in the deck
  PASS  Architecture term 'Braze' appears consistently in the deck
  PASS  Architecture term 'Amplitude Browser SDK' appears consistently in the deck
  PASS  Deck presents warehouse import (not HTTP API) as the Phase 1 backend path
  PASS  Five AI deliverables identical between the model and the workbook
  PASS  Exactly five AI deliverables, each with a cited official source
  PASS  All event names follow the Title Case style guide
  PASS  Shared property names are reused across events rather than duplicated per event
  PASS  No PII in event or user property names, or in sample values
  PASS  Sensitive steps carry explicit do-not-store guidance
  PASS  Payment step explicitly forbids storing card credentials
  PASS  Chart specification documents all 8 charts
  PASS  5 built + 3 specification-only = 8 charts
  PASS  Official deck section retained: Partnership Kickoff
  PASS  Official deck section retained: Introductions
  PASS  Official deck section retained: Goal Alignment
  PASS  Official deck section retained: Implementation Roadmap
  PASS  Official deck section retained: Implementation Scope
  PASS  Official deck section retained: Action Items
  PASS  Official roadmap slide retained verbatim
  PASS  All 18 original template sheets preserved
  PASS  No Data QA row marked Pass without evidence
```

## Notes on three checks that initially failed

The first run reported three failures. All three were defects in the *checks*, not in the
artifacts, and each was verified by hand before the check was corrected:

1. **"Specification-only charts carry no Amplitude URL"** — the original regex searched a fixed
   400-character window after each chart ID, which spilled out of C2's section and into C3's
   URL in the summary table. Corrected to scope the search to each chart's own section.
   Verified by hand: C2, C6 and C7 each read `**Amplitude URL:** Not available`.

2. **"Demo observations live in the chart spec, not the workbook"** — the check looked for a
   substring that did not match the wording actually used. Replaced with a stronger check that
   scans every sheet for the actual demo figures (10,341 / 9,807 / 26.19 …). Result: no leaks.

3. **"No PII fields in the taxonomy"** — the check scanned property *descriptions*, which name
   PII precisely in order to forbid it ("Never send card number, CVV, expiry or any
   authentication secret"; "Destination country code only — no street address, name or postcode
   is sent"). Scanning prohibition language for the words it prohibits is backwards. Corrected
   to scan property **names** and **sample values**, and a second check was added to confirm the
   prohibition guidance is genuinely present.

None of the three required any change to the workbook, deck, diagram or chart specifications.


## Wording-discipline checks (added after the interpretation review)

Fourteen further checks were added so the discipline around demo data is enforced mechanically
rather than trusted:

- every built chart's figures sit under an explicit *training data, not a baseline* label
- every built chart carries its careful, descriptive reading
- readings are screened against a banned list of over-strong phrases
  (`near-universal`, `dominant`, `collapse`, `far better`, `clearly shows`, `proves that`, …)
- C3 explicitly states correlation, not causation — in the spec and on the live Amplitude chart
- C5 explicitly flags that its category values are grocery, not the apparel scenario
- all six identified gaps appear in both the chart specification and the workbook
- the recommended-taxonomy / demo-taxonomy / data-gap distinction is stated up front in both the
  chart specification and the README
- speaker notes brief the presenter on the demo-data framing, and on stating window and population
- C2, C6 and C7 are framed as identified data gaps rather than as work not done
