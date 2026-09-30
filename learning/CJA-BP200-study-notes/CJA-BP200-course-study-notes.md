# CJA Business Practitioner — study notes

Source: [Adobe Customer Journey Analytics Business Practitioner Professional](https://certification.adobe.com/courses/1062), course CJA-BP200, B2C focus. Reviewed September 29, 2026.

## Scope and limitations

The selected page contains one course with six modules. This package covers those six modules, not the whole Adobe catalog or other enrolled courses.

These files contain concise original summaries, explanations, and invented practice examples. They do not reproduce all Adobe course content and are not a complete export, transcript, or official certification guide.

The module overviews and summaries were reviewed, along with selected lesson sections in Modules 1 and 2. Not every lesson, interactive detail, or video was reviewed. All six modules showed closing resources locked behind a final quiz. No quizzes were answered. Viewing pages updated some lesson progress in Adobe's player.


---

# Module 1: Understanding CJA

Course: Adobe Customer Journey Analytics Business Practitioner Professional (CJA-BP200, B2C).

[Open the module](https://certification.adobe.com/courses/playScorm/1333/1062)

## Study summary

Customer Journey Analytics (CJA) helps practitioners examine customer activity across channels. Its connection to Adobe Experience Platform supports analysis of data originating in digital and offline systems. Looking at these sources together can reveal patterns that isolated reports miss.

The module introduces segmentation, visualization, configurable reporting, and timely analysis. It connects these capabilities to personalization, collaboration, and adapting analytics as an organization grows.

Campaign applications include evaluating a launch, following up with interested shoppers, and choosing a better time to communicate. The central idea is to turn observed behavior into a testable business decision.

## Explanation and original example

Imagine a bicycle retailer. A customer reads a product guide on a phone, asks a question through support, and purchases in a shop. A website-only report cannot explain the entire sequence. An analysis using appropriately connected records can investigate whether guide readers subsequently buy, and whether support helps them decide.

Start with a question: “Do customers who read the sizing guide return fewer bicycles?” Then define the relevant audience, purchase period, and return measure. Compare like-for-like groups. An observed difference is a reason to investigate; it does not by itself establish that reading the guide caused fewer returns.

## Practice

- Choose a business outcome, such as repeat purchases.
- Identify the interactions needed to understand it.
- Write one decision that the analysis could change.
- Identify missing data that could distort your conclusion.

## Coverage

These are original study notes based on reviewed introductory sections and the module summary, not a complete transcript. Some interactive sections and the embedded video were not fully reviewed. The quiz was not answered; closing resources were locked behind it.


---

# Module 2: Exploring CJA Components

[Open the module](https://certification.adobe.com/courses/playScorm/1460/1062)

## Study summary

Analysis Workspace is a place to investigate questions and assemble an analysis. Panels organize work; tables and visualizations present results. Guided analysis offers structured starting points, while the project table of contents helps navigate larger projects.

The main analytical components are dimensions, metrics, segments or filters, and date ranges. The Data Dictionary helps users understand component definitions consistently.

The module distinguishes exploration from dashboards that communicate selected indicators to an audience. Its dashboard lessons cover choosing relevant information, adjusting layout and filters, saving views, and sharing useful results with different teams.

## Explanation and original example

Suppose you want to compare orders across devices:

| Component | Example | Question it answers |
|---|---|---|
| Dimension | Device category | Which group? |
| Metric | Orders | How many? |
| Segment/filter | Customers in the selected market | Whose activity? |
| Date range | The previous complete month | During which period? |

The same orders metric can tell a different story when the audience or period changes. Keep those choices explicit when sharing a result.

A useful executive view might show the trend in orders, a comparison with the previous period, and a short interpretation. An investigation for a product team might need additional breakdowns. Choose the amount of detail based on the decision the reader needs to make.

## Practice

Sketch a dashboard for a support manager. Give each chart a purpose, define its metric, and state its date range. Remove any chart that does not support a decision.

## Coverage

These are original study notes based on the workspace sections and module summary reviewed. They are not a complete transcript or a verified click-by-click product tutorial. Dashboard lesson details, videos, and all interactions were not fully reviewed. The quiz was not answered; closing resources were locked behind it.


---

# Module 3: Data Analysis Fundamentals

[Open the module](https://certification.adobe.com/courses/playScorm/1335/1062)

## Study summary

The module covers three stages: understanding the data, interpreting it, and communicating findings. Its data lesson introduces source types, integration, and stitching across systems. Knowing how records are structured matters when interpreting a combined customer journey.

The analysis lesson addresses metrics, dimensions, chart selection, trends, and indicators that help users interpret results. The communication lesson focuses on organizing an analysis, curating a workspace, sharing insights, and choosing an appropriate export format for the audience.

## Explanation and original worked example

Suppose a shop records 240 orders across 8,000 sessions in one period, and 300 orders across 12,000 sessions in another. For a deliberately defined “orders per session” measure:

```text
Period A: 240 / 8,000 × 100 = 3.0%
Period B: 300 / 12,000 × 100 = 2.5%
```

Orders increased by 25%, yet orders per session fell. Both statements are true. Counts describe volume; rates help compare performance relative to opportunity. This example is invented and is not a prescribed CJA metric definition.

A line chart can show how the rate changes over time. A bar chart can compare selected groups. A table can provide the precise values behind either chart. Explain the denominator and analysis period so the audience understands the comparison.

## Practice

Write a four-sentence finding: the question, the evidence, an uncertainty, and a proposed next action. Then check that the supporting chart actually shows the evidence you cite.

## Coverage

These original notes are based on the module overview and summary. Detailed lesson interactions and videos were not reviewed. They are not a complete transcript. The quiz was not answered; closing resources were locked behind it.


---

# Module 4: Business Use Cases

[Open the module](https://certification.adobe.com/courses/playScorm/1336/1062)

## Study summary

Useful analysis begins with a business question. An observation reports what happened; an actionable insight connects evidence to an objective and helps someone decide what to do.

The module discusses applications involving app engagement, journeys spanning multiple channels, and call-center demand. It connects findings to key performance indicators and stresses communicating results to stakeholders and measuring the effect of subsequent action.

## Explanation and original example

Observation: “Support contacts increased last week.”

Investigation: Break the increase down by topic, customer group, and relevant journey step. Check whether the increase reflects more customers, more contacts per customer, or a change in recording.

Possible insight: “Delivery-status questions account for most of the increase, and affected customers often visited the tracking page first.” This is a hypothesis to validate, not proof that the page caused the calls.

Proposed action: Test clearer delivery information. Define success as fewer delivery-status contacts per shipped order, while monitoring customer satisfaction. Assign an owner and review the result after a specified period.

## Reusable analysis template

```text
Business objective:
Question to investigate:
Population and period:
Metric and definition:
Observed evidence:
Alternative explanations:
Proposed action and owner:
Success measure:
Review date:
```

## Practice

Take a dashboard observation and fill in the template. If you cannot identify an action or a person who would use the finding, refine the business question.

## Coverage

These original notes are based on the module overview and summary. Detailed scenarios, interactive lessons, and videos were not reviewed. They are not a complete transcript. The quiz was not answered; closing resources were locked behind it.


---

# Module 5: Troubleshooting Common Issues

[Open the module](https://certification.adobe.com/courses/playScorm/1337/1062)

## Study summary

This module separates data problems from reporting problems. Its examples of possible data issues include inconsistent schemas, missing collection tags, and time-zone differences. It introduces validating collection with Adobe's debugger tools.

For dashboards, the module highlights filters, attribution, persistence, and component configuration as settings that can influence results. It also emphasizes keeping issue records, collaborating on diagnosis, maintaining dashboards, and using Adobe support resources.

## Explanation and original diagnostic exercise

Suppose a revenue chart becomes blank. Treat “blank” as a symptom rather than immediate proof that sales stopped.

1. Record the report, period, selected population, and expected result.
2. Check whether the problem affects one chart or other views too.
3. Compare the current selections with a previously working view.
4. Ask the data owner whether the expected records are arriving.
5. Change one diagnostic variable at a time and record the result.

This is a general reasoning exercise, not a verified CJA administration procedure. A collection check and a report check examine different points in the process; evidence at one point does not establish that every later stage is correct.

## Issue-report template

```text
Symptom and first observed time:
Affected report and settings:
Expected versus actual result:
Scope: one user, one view, or multiple views?
Recent relevant changes:
Checks performed and outcomes:
Evidence available to the responsible team:
Owner and next investigation step:
```

## Practice

List three possible explanations for a sudden drop in a metric. For each, identify one observation that would support it and one that would weaken it.

## Coverage

These original notes are based on the module overview and summary. Detailed lessons, debugger demonstrations, and interactive material were not reviewed. They are not a complete transcript. The quiz was not answered; closing resources were locked behind it.


---

# Module 6: Maximizing the Value of CJA

[Open the module](https://certification.adobe.com/courses/playScorm/1338/1062)

## Study summary

The final module introduces deeper analytical approaches: pathing, funnels, retention, segmentation, attribution, and AI-assisted insights. It emphasizes selecting a method that suits the business question.

Its implementation lesson addresses stakeholder involvement, strategic goals, governance, responsibility, and training. Sustained value depends on people being able to trust and use the analysis, as well as having the technology available.

## Explanation and original examples

| Analytical question | General approach | Example to investigate |
|---|---|---|
| What routes do people take? | Path analysis | Steps before a support request |
| Where does a defined sequence lose people? | Funnel analysis | Progress from registration to first order |
| Do people come back? | Retention analysis | Return activity after a first purchase |
| Which groups behave differently? | Segmentation | New versus established customers |
| How is credit assigned to interactions? | Attribution | Contribution assigned to marketing touchpoints |

A funnel starts with a sequence you specify. A path investigation explores routes people actually follow. Retention requires an explicit definition of returning: another visit, another purchase, or another meaningful action. Those definitions change the interpretation.

Attribution is a way of assigning credit under chosen rules or models. Treat the resulting allocation as an analytical perspective; it does not by itself prove causal impact.

## Original adoption exercise

Choose one recurring business decision. Name the person responsible for it, define the measures they need, and identify who maintains those definitions. Set up a review cadence and a way to record which decisions changed because of the analysis. This makes adoption observable rather than equating it with the number of dashboards created.

## Coverage

These original notes are based on the module overview and summary. Detailed technique demonstrations and implementation lessons were not reviewed. They are not a complete transcript. The quiz was not answered; closing resources were locked behind it.
