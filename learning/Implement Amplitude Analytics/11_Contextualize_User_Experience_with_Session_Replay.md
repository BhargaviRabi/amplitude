# Contextualize User Experience with Session Replay

**Type:** On-demand course | **Time commitment:** Not separately listed on the catalog card (single-lesson course)

---

## About This Course

In this course you'll learn how to access and interpret your user sessions to quickly zoom into your data to efficiently discover, troubleshoot, and validate product issues. Replays can help you understand the user experience even when there are gaps in your event instrumentation.

In this course, you'll walk through several examples of how to use this powerful tool as well as learn how replays are collected and how and why to modify replay settings.

**NOTE:** You must have purchased and installed Session Replay in order to use it. Please see Amplitude's Developer Docs for installation instructions.

---

## Lesson: Gain Qualitative Context with Session Replay (4 min)

*Note: this lesson displays a notice that Session Replay needs to be enabled in the learner's Amplitude organization in order to complete the exercises in the lesson.*

**Gain qualitative context.** By pairing qualitative insights with your quantitative data, Session Replay gives you a clearer view of the customer journey, so you can gain insights into behavior, friction, and missed opportunities. With Session Replay, you can:
- Watch users navigate key marketing flows
- Spot signs of frustration or confusion
- Validate hypotheses from funnel analysis
- See whether landing pages are engaging users
- Surface bugs or UX blockers that might otherwise go unnoticed

**How capture works.** A session replay plays like a video, but Amplitude isn't recording your screen. It captures the page's DOM, the elements and every change to them, plus your clicks, scrolls, and inputs, and rebuilds the session in your browser when you hit play.

This keeps replays light and lets Amplitude mask sensitive fields like passwords before they ever leave the page. It also means anything outside the DOM, like canvas, WebGL, or a cross-origin iframe, can't be rebuilt, so when you see a blank stretch in a replay, that's usually why.

When a number moves, the replay shows you the cause behind it. Session Replay lives under Experience Analytics, next to the rest of your behavioral data.

**Example: Your add-to-cart funnel is leaking.** For Amplistore, half the people who add an item never reach checkout, and fewer than one in twenty finish the purchase. The funnel shows you where they drop off. To see why, you watch the session itself.

One shopper added items to the cart, reached the billing form, and left without buying.

Session Replay captures the actual session: every click, scroll, and input, alongside the event timeline your instrumentation already records. You watch what the user did instead of guessing at it.

**[Video: "Session Replay - AI Led", Amplitude Academy / Wistia embed]** — demonstrates watching an actual Amplistore session replay of the add-to-cart drop-off scenario described above, alongside the event timeline. (No on-page transcript available; exact runtime not exposed in the page data.)

*"Every product has sessions where a user hits a wall and leaves. You can open one in your own data by asking Global Agent:"*

**✨ Try it out:** *"Show me session replays where users showed frustration before dropping off"* (presented as a clickable prompt link to Amplitude's Global Agent / AI assistant).

**Frustration signals.** The player showed you what the user did. Amplitude also detects four specific kinds of frustration on its own and marks them on the timeline as signals. This section embeds an interactive third-party widget ("Session Replay: Frustration Signals") with four info cards — reproduced in full below:

| Signal | Description |
|---|---|
| **Rage click** | Rapid repeated clicks on the same element. The user expected a response that didn't come. |
| **Dead click** | Click on an element that isn't interactive. Something that looks like a button or link but doesn't respond. |
| **Error click** | Click that triggered a JavaScript error in the session. The interaction caused something to break. |
| **Form abandonment** | User started filling a form and left without submitting. Intent was there; completion wasn't. |

*"Thanks for completing this course! Click 'Next' to share your feedback on this course by completing a short survey."*

## Feedback

This course ends with a "We'd love your feedback" survey lesson — navigational/administrative, not course content.

---

## Summary / Explanation

This short course positions Session Replay as the qualitative counterpart to Amplitude's quantitative analytics: where a funnel or chart tells you *that* users are dropping off at a certain step, Session Replay lets you watch an actual recorded session to understand *why*. The technical explanation of how capture works is a key detail — because Amplitude reconstructs sessions from DOM snapshots and diffs (not a screen recording), it can mask sensitive fields like passwords, but it also means content outside the standard DOM (canvas, WebGL, cross-origin iframes) can't be replayed, which explains occasional blank stretches in a replay. The lesson's worked example (the "Amplistore" add-to-cart funnel leak) shows the intended workflow: notice a drop-off in a quantitative funnel, then open the actual session replay of an affected user to see the specific point of friction — in this case, a shopper who reached the billing form and left. The four "frustration signals" (rage click, dead click, error click, form abandonment) extend this from a manual, one-session-at-a-time review into something Amplitude can detect and surface automatically across many sessions, timestamped directly on the replay timeline. The lesson also demonstrates a lightweight AI/agent workflow — using a natural-language prompt to Amplitude's Global Agent ("Show me session replays where users showed frustration before dropping off") to surface relevant replays without manually filtering session lists.
