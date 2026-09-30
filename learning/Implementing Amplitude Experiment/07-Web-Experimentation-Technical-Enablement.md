# Web Experimentation: Technical Enablement

**Source:** Amplitude Partner Training — [Web Experimentation: Technical Enablement](https://trainingpartners.amplitude.com/web-experimentation-technical-enablement)

**Subtitle:** "Learn about what Web Experimentation means for technical roles"

This is a standalone course. Curriculum lists it as 5 minutes, but that figure covers only the "Check your understanding" quiz — the main lesson itself runs across 7 sub-lessons totaling roughly 73 minutes of video (17+23+9+3+13+2+6), consistent with the course's real scope.

## About this course (verbatim)

> Learn about what Web Experimentation means for technical roles.
>
> This course is designed to help technical roles to:
> - Use an understanding of web fundamentals to talk about Web Experimentation
> - Explain how implementation differs at a high level with Web Experiment
> - Explain how the visual editor, code editor, and script work
> - Address common customer questions and objections
>
> Looking for the slide deck? Check your partner resource area (Highspot for resellers; Gdrive folder for Solution Partners.)
>
> Time commitment: ~1 hour

## Format note

Like "Web Experimentation: Implementation Enablement," this course's main lesson is presented as a series of narrated slide-deck videos (7 lessons under one heading, "Web Experimentation: Technical Enablement"), rather than as interactive Rise text content.

**Important — video availability:** Only the first 2 of the 7 lesson videos actually played back in this browsing session. Lessons 3 through 7 all displayed a **"Media not found."** placeholder in the video player, meaning the underlying video file/link is broken on the training platform itself. This appears to be a hosting issue with the course, not a restriction of any kind — the lesson titles, order, and durations are all still visible in the curriculum, but the video content for those 5 lessons could not be captured because the platform itself could not serve it.

---

## Lesson 1 of 7: Web fundamentals (17 min)

**Video** (17:47) — slide titled **"Local Storage vs Session Storage"** (under section header "Web Fundamentals"):

> - **Local Storage**
>   - **Storage Duration**: Data persists indefinitely until manually cleared by the user or programmatically.
>   - **Scope**: Shared across all tabs and windows for the same domain.
> - **Session Storage**
>   - **Storage Duration**: Data persists on[ly for the current] session and is cleared when the tab or window is closed. *(a few words in the middle of this line are obscured by the video player's play-button overlay in the captured frame)*
>   - **Scope**: Data is confined to the spec[ific tab or window wher]e it was set. The session begins when the tab or window is opened and ends when i[t's closed — data is only av]ailable during this period and is not shared across tabs or windows. *(same obstruction as above)*

> **Explanation:** This lesson establishes the browser-storage fundamentals a technical partner needs before talking about how Web Experimentation actually works client-side: Amplitude's Web Experiment SDK relies on this same local-storage/session-storage distinction to remember which variant a visitor has been bucketed into (persistent across visits vs. only for the current browser session), which is foundational context for the "Implementation" and "How the script works" lessons that follow.

---

## Lesson 2 of 7: Implementation (23 min)

**Video** (23:31) — slide titled **"Stand-alone Web Experiment Script"** (under section header "Implementation"):

> - Only loads and initializes the Web Experiment SDK
> - Should be used by existing customers who already have analytics (Amplitude or 3rd party) implemented on their site
>   - Works with any versions of am[plitude and other] analytics-browser SDKs which also integration with feature analytics. *(obscured mid-line by the video player's play-button overlay; wording approximate)*
> - Can be loaded sync or async + anti-f[licker] *(same obstruction)*
> - Replace `API_KEY` with the project A[PI key] *(same obstruction)*

Code snippets shown on the slide:

```
US: <script src="https://cdn.amplitude.com/script/API_KEY.experiment.js"></script>
EU: <script src="https://cdn.eu.amplitude.com/script/API_KEY.experiment.js"></script>
```

> **Explanation:** This slide is describing the "stand-alone" installation path for the Web Experiment SDK — i.e., loading just the experimentation script (as opposed to a combined Analytics+Experiment script) via a `<script>` tag, with a region-specific CDN URL (US vs. EU data residency) and the customer's own project API key substituted into the URL. The "should be used by existing customers who already have analytics implemented" bullet indicates this is the recommended path specifically for customers who don't need Amplitude's script to also set up analytics — it's experimentation-only.

---

## Lessons 3–7: content unavailable ("Media not found")

The following lessons are listed in the curriculum with their titles and durations, but their video content returned a **"Media not found"** error in the player and could not be captured:

- **Lesson 3 of 7: How the visual editor works (9 min)**
- **Lesson 4 of 7: How the code editor works (3 min)**
- **Lesson 5 of 7: How the script works (13 min)**
- **Lesson 6 of 7: Common customer questions and objections (2 min)**
- **Lesson 7 of 7: Demo, Q&A (6 min)**

> **Explanation (inference from titles and course objectives only):** Based on the "About this course" learning objectives ("Explain how the visual editor, code editor, and script work" / "Address common customer questions and objections"), Lessons 3–5 almost certainly walk through Web Experimentation's three ways of building a variant — the point-and-click visual editor, the raw code editor, and directly editing the underlying experiment script — progressing from least to most technical. Lesson 6 would cover objection-handling talking points for technical roles fielding customer pushback, and Lesson 7 is presumably a live demo recording plus Q&A. None of this is confirmed content, however — it is offered only as context for why these lessons are sequenced this way, not as a substitute for the actual (currently inaccessible) video content.

### Check your understanding / Feedback (not reproduced)

The course also includes a 5-minute "Scenario Questions (Check your understanding)" quiz and an optional "Course feedback" form, neither of which is reproduced here.

---

*End of file for "Web Experimentation: Technical Enablement."*
