# (Soon to be retired/updated) Web Experimentation: Implementation Enablement

**Source:** Amplitude Partner Training — [Web Experimentation: Implementation Enablement](https://trainingpartners.amplitude.com/web-experimentation-implementation-enablement)

**Note on course status:** The course title itself is prefixed "(Soon to be retired/updated)" on the training site, indicating Amplitude expects to replace or retire this course.

This is a standalone course. Time commitment: **~1.25 hours** (curriculum shows 80 minutes total: a 75-minute main lesson plus a 5-minute "Check your understanding" scenario quiz).

## About this course (verbatim)

> This course will give you an overview of Web Experimentation and how it impacts roles in a Professional Services team that implements Amplitude.
>
> This course is designed to help Professional Services roles to:
> - Explain what Web Experimentation means for EMs (Engagement Managers)
> - Describe the impact to the Implementation Process and collateral
> - Explain changes to Customer Billing and A/A Test Process
> - Explain the implications for technical roles (e.g. Solution Architects)
>
> Looking for the slide deck? Check your partner resource area (Highspot for resellers; Gdrive folder for Solution Partners.)
>
> Time commitment: ~1.25 hours

## Format note

Unlike the other courses in this training program, this course is presented as a **recorded internal training webinar**: each lesson is a single screen-recorded video of an Amplitude presenter walking through a slide deck (their webcam appears picture-in-picture in the top-right corner of each video), rather than an interactive Rise-style text lesson. There is no separate on-page narrative text for these lessons — the content lives entirely inside the videos. Below, each lesson's visible title slide and bullet content (captured from the video frame) is transcribed, since the specific spoken narration cannot be transcribed from a static frame capture. The course is organized into 5 video lessons under 2 headings: "Implications for Engagement Managers" and "Implications for Technical Roles."

---

## Lesson 1 of 5: Background (2 min)

**Video:** A recorded presentation opening on an **"Agenda"** slide, with the presenter (badge reads "Channing Benson | S...") narrating over a shared Google Slides deck. The agenda lists:

1. Background
2. Engagement Implications
3. Technical Implications
4. Resources

> **Explanation:** This lesson is the shortest at 2 minutes and is purely a table-of-contents/agenda-setting video for the rest of the course — it previews the same 3 topic areas (Background, Engagement Implications, Technical Implications) that make up the remaining 4 lessons, plus a "Resources" section that (based on the rest of the course) appears to correspond to the "Looking for the slide deck?" pointer given in the About-this-course text (Highspot for resellers, Google Drive for Solution Partners) rather than to a separate on-platform lesson.

---

## Lesson 2 of 5 (heading: "Implications for Engagement Managers"): What this means for Engagement Managers (11 min)

**Video** (10:55) — slide titled **"What Does This Mean for EMs?"** (under section header "Engagement Implications"):

> - In general, no drastic changes.
> - Engagements with only web experimentation or feature experimentation engagements.
> - Some customer scenarios will require tailoring the customer's priorities:
>   - Existing feature experimentation customer adding web experimentation
>   - Simultaneous purchase of both web and feature experimentation
>   - Clarify use case selection - what distinguishes experiments done with web from experiments done with feature?

> **Explanation:** The headline message for Engagement Managers is reassurance — day-to-day EM work doesn't change much with the addition of Web Experimentation. The real nuance shows up in mixed engagements: a customer who already has Feature Experimentation and is now adding Web Experimentation, or a brand-new customer buying both products at once, both need the EM to help the customer draw a clear line between "this test belongs in Web Experimentation" vs. "this test belongs in Feature Experimentation."

---

## Lesson 3 of 5: Impact to Implementation Process and collateral (12 min)

**Video** (12:16) — slide titled **"Collateral Changes"** (under "Engagement Implications"):

> - New Instrumentation Walkthrough deck for W[eb Experimentation]
>   - Also includes info on defining variants (*rest of this line is obscured by the video-player's play-button overlay in the captured frame*)
> - New Implementation Workbooks for different [scenarios]:
>   - Web experimentation only (Core and Co[re+ tiers, inferred])
>   - Web and Feature experimentation (Con[verged/combined engagement, inferred])

> **Explanation:** The practical takeaway here is a documentation/collateral change, not a process change: Professional Services gets a dedicated Instrumentation Walkthrough deck for Web Experimentation (which also covers how to define variants) and new versions of the Implementation Workbook are split by scenario — one for customers buying Web Experimentation alone, and one for customers buying both Web and Feature Experimentation together.

---

## Lesson 4 of 5: Changes to Customer Billing and A/A Test Process, Edge Cases (15 min)

**Video** (15:06) — slide titled **"A/A Test Process Change (Impressions)"** (under "Engagement Implications"), shown as a two-column comparison:

**Feature Experimentation column:**
> - Customer pays for Product SKU
> - Customer does not pay for Exposures
> - Customer can run A/A tests at full Production volume with no implication
> - **PS RECO:** Run A/A tests in Prod as part of implementation

**Web Experimentation column** *(partially obscured by the video-player's play-button overlay in the captured frame; reconstructed from the visible fragments)*:
> - Customer pays for Product SKU
> - Customer pays for Impressions
> - Any test that runs in any environment will consume impressions
> - **PS RECO:** Only run A/A tests in Prod if the customer pushes for us to:
>   - We can still do QA in Dev and Prod
>   - Gradual Prod traffic rollout (start at 0%)
>   - Restrict the duration (1-2 weeks max)

> **Explanation:** This is the most commercially important slide in the course. The core billing difference is that Feature Experimentation bills by Product SKU and doesn't charge for exposures, so a full-production-volume A/A test costs the customer nothing extra — hence the PS recommendation to just run A/A tests in Prod as standard practice. Web Experimentation, in contrast, bills for impressions, and *any* test running in *any* environment (including an A/A test) consumes (and therefore costs) impressions — hence the much more conservative PS recommendation: avoid running A/A tests in Prod unless the customer specifically insists, do QA in Dev/Prod instead, and if you must run one in Prod, ramp traffic gradually from 0% and cap the duration at 1–2 weeks to limit the cost impact.

---

## Lesson 5 of 5 (heading: "Implications for Technical Roles"): Technical Implications (7 min)

**Video** (7:14) — slide titled **"Be Aware!"** (under "Technical Implications"):

> - *Currently* all web experiments are evaluated l[ocally / — rest of this line obscured by the video-player's play-button overlay in the captured frame]
> - $Impression events are NOT free
> - No navigation while editing variants
>   - Tests with changes on separate pages should be separate experiments
>   - Fallback option is for customer to build new page nodes on their end and run as a Split URL test instead

> **Explanation:** This lesson is aimed at technical implementation roles (e.g., Solution Architects) and flags three "gotchas" specific to Web Experimentation: (1) currently, web experiments are evaluated in a way the presenter calls out as a "be aware" caveat (the exact wording is cut off in the captured frame, but based on context this is very likely calling out client-side/local evaluation as the current mechanism); (2) impression events carry a real dollar cost, reinforcing the billing point from Lesson 4; and (3) the Web Experimentation visual editor does not support navigating between pages while editing variants, so a test that needs changes on more than one page has to be split into separate per-page experiments, or the customer can build the additional page(s) into their own site and run a Split URL test instead.

### Check your understanding / Feedback (not reproduced)

Following the 5 video lessons, the course includes a 5-minute "Scenario Questions (Check your understanding)" quiz and an optional "Course feedback" form. Neither is reproduced here, consistent with the rest of this training-content set (quiz/assessment content is not taught content, and reproducing it would capture this learner's personal quiz-attempt data).

---

*End of file for "Web Experimentation: Implementation Enablement."*
