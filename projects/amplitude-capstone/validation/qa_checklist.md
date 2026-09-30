# QA Checklist — AmpliStore 2.0 Capstone

Completed against §45 and §46 of the execution specification. Each item is marked with what
was actually verified, not merely intended.

## Workbook QA

### Alignment
- [x] Four pre-project requirements documented — `Alignment (Week 0)` sheet, R1–R4, each with the
      questions to confirm, an owner, and an explicitly labelled mock assumption
- [x] Challenges documented — three, one per use case, carried identically onto the deck's Goal Alignment slide
- [x] 2–3 use cases documented — three (UC1 Product Discovery, UC2 Purchase Funnel, UC3 Checkout)
- [x] 10–15 business questions documented — 15, each mapped to a use case and a KPI
- [x] Stakeholders documented — 9 roles across AmpliStore, Amplitude and the partner; all names `TBD`
- [x] Dependencies documented — Question Tracker, 13 open items with priority and owner

### KPIs
- [x] 5–6 focused KPIs — six
- [x] Each tied to a business question — verified programmatically
- [x] Each tied to events — verified programmatically against the taxonomy
- [x] Each tied to a chart — verified programmatically
- [x] No invented baseline numbers — verified by scanning every sheet for percentage patterns and
      for the specific demo figures; zero leaks
- [x] Conversion window stated for every KPI — 7-day purchase, 1-day add-to-cart, stated in the
      Additional Notes column and on every chart description

### Events
- [x] Event names consistent — 16 events, Title Case verb+noun, verified programmatically
- [x] Business meaning clear — every event carries a business question
- [x] Trigger defined — every event has a trigger description plus its instrumentation source
- [x] Properties defined — 65 property rows across 16 events
- [x] Platform defined — `Web Only` throughout (no native app in scope)
- [x] Implementation status honest — every row `No`; nothing is claimed as implemented

### User Properties
- [x] User-level only — six properties, all describing user state
- [x] Data types and sample values given
- [x] No unnecessary PII — verified programmatically on names and sample values
- [x] Exclusions documented — four properties deliberately NOT tracked, each with a reason
      (notably `Country`, which would duplicate the Amplitude SDK default)

### AI
- [x] Five deliverables identified from official materials — each quoted verbatim from Kickoff deck
      slide 16 and corroborated by a `Project Plan Gantt View` row
- [x] Correct sequence — Alignment → Technical Scoping → Launch → Launch → Enablement
- [x] No fabricated names — provenance and the confirmation caveat are stated on the sheet itself
- [x] No AI capability claimed as enabled

### Instrumentation
- [x] Precision vs hybrid decision — Hybrid, with rationale
- [x] SDK / API / warehouse roles defined per event
- [x] User identification strategy — seven scenarios including the guest-checkout edge case
- [x] Sources and destinations — Integrations Tracker populated; out-of-scope items marked as such
- [x] HTTP API, Snowflake, BigQuery and S3 all addressed (rubric E)

## Presentation QA
- [x] Official 2026 template retained — 38 slides, all six official sections intact
- [x] Official roadmap slide retained verbatim rather than replaced with a competing timeline
- [x] No `Presenter Name` placeholder
- [x] No `[Customer]` placeholder
- [x] No `XX` dates — all target dates read `TBD` deliberately
- [x] No leftover internal instructions ("Example ONLY", "Delete if not applicable", etc.)
- [x] Consistent terminology with the workbook
- [x] Same KPI definitions as the workbook
- [x] Same event names as the workbook
- [x] Architecture matches the instrumentation strategy — both show warehouse import as the
      Phase 1 backend path with HTTP API marked out of scope
- [x] AI section matches the workbook
- [x] Risks and action items concrete, with owners
- [x] Executive narrative — speaker notes added to seven pivotal slides
- [x] Only committed products shown — Session Replay, Guides & Surveys and Experiment rows removed

## Chart QA (for the five charts actually built)
- [x] Correct event names — verified against the demo taxonomy before building
- [x] Correct order of funnel steps — re-opened and confirmed after saving
- [x] Correct conversion window — 7-day on C1/C3/C4/C8, 1-day on C5, each confirmed in the UI
- [x] Correct segmentation — C4 by Device family, C5 by Product Category; C1 deliberately ungrouped
- [x] Correct project — every chart confirmed in `Amplistore 2.0 (E-commerce 2024)`
- [x] Saved status confirmed on every chart
- [x] URLs captured only after the chart was verified to exist
- [x] No misleading metric definitions — C3 and C7 carry explicit correlation-not-causation caveats

## Dashboard QA
- [x] Chart titles understandable — each names the question it answers
- [x] Chart purpose clear — every chart's description carries use case, KPI, question and window
- [x] Related charts grouped — funnel → discovery → device → category → abandonment
- [x] No redundant charts — device analysis lives only in C4, not duplicated onto C1
- [x] Business questions represented — all 15 map to at least one chart
- [x] Not overcrowded — five charts, one screen of narrative
- [x] Empty tiles avoided — C2, C6, C7 deliberately excluded rather than shown broken

## Honesty checks
- [x] No fabricated Amplitude URLs — allow-list check against verified builds only
- [x] No fabricated metrics or baselines
- [x] No unsupported implementation claims
- [x] No invented names, dates or engineering availability
- [x] Original template files untouched — MD5 verified before and after


## Interpretation discipline (added after review)

- [x] No over-strong readings of demo data — readings screened against a banned-phrase list, enforced in the validation suite
- [x] Every demo figure labelled as a training-data observation, in the chart spec, in all 5 Amplitude chart descriptions, and in the dashboard description
- [x] No demo figure appears in the workbook — verified programmatically against the actual values
- [x] C3 search comparison stated as correlational, not causal, in three places (chart spec, live chart description, speaker notes)
- [x] C5 category-value mismatch flagged in three places
- [x] Recommended taxonomy / demo taxonomy / data gaps kept explicitly separate in the chart spec and README
- [x] Six instrumentation and data gaps documented in both the chart spec and the workbook
- [x] C2, C6, C7 retained as data gaps — no substitute property used for any of them
- [x] All unknown person names remain TBD — none invented
- [x] Speaker notes brief the presenter to state window and population with every rate quoted
