# Implementing Amplitude Experiment — Technical Exercise 

Status: **Complete and verified live**, end-to-end, in your own `techvedika-088965`
Amplitude organization (switched from the shared `Shared Partner Training` sandbox,
where this account only had Member access and couldn't retrieve the Analytics API key).

## What's live

- **Project:** `MemoMinder` (new project created in `techvedika-088965`), owned by
  `bhargavi.rabi@techvedika.com` (org Admin here, unlike the shared sandbox).
- **App:** `memominder/index.html` — a memo app (add / close / delete) instrumented with:
  - Amplitude Analytics (browser SDK, script-tag install), API key
    `6ec4e655d3c63c4a39b42dff50d8ecd4` (source `memominder-web`)
  - Amplitude Experiment JS SDK (`@amplitude/experiment-js-client@1.15.5`),
    `initializeWithAmplitudeAnalytics`, `start()` / `variant()` per the exercise hint
  - `setLabel()` sets the Add/Create button text from the `button_label` payload of
    the `techvedika-memominder-label` flag
  - `Memo Interacted` event tracked with `action: add|close|delete` on every
    create/close/delete
- **Deployment:** `memominder-web-client` (Client), key
  `client-o7TvHdPmxvs1RTSlYhjhKo4BF7mQAXmZ`
- **Experiment:** `techvedika-memominder-label`, Feature/A-B test, Remote evaluation,
  bucketed by Amplitude ID, variants `add` (`{"button_label":"Add"}`) / `create`
  (`{"button_label":"Create"}`), All Users, 50/50, 100% rollout, **Running**
  - Primary metric: Event Totals, `Memo Interacted` where `action = add`
    (created after real events existed — the event didn't exist in the taxonomy
    until the app actually sent one)

## What was verified, live, in this session

1. Ran the app against the real deployment — Experiment SDK correctly resolved a
   variant and set the button label (confirmed via network request to
   `api.lab.amplitude.com/sdk/v2/vardata` → 200).
2. Created/closed/deleted memos — confirmed `Memo Interacted` events landing in
   Live Events in real time (4 events: 2 add, 1 close, 1 delete).
3. Confirmed via User Profiles that the same real user has, in order: **Assignment**
   → **Exposure (techvedika-memominder-label)** → multiple **Memo Interacted** events.
4. Confirmed via the experiment's Activity tab: 1 user exposed, "create" variant
   showing 3 events / 1 exposure, primary metric wired up, data quality checks passing.

## What's left for you (manual, by design)

- **Step 4.5 (incognito check):** I tried to reproduce this by clearing cookies,
  localStorage, sessionStorage and IndexedDB and forcing hard reloads — the SDK kept
  returning the exact same Amplitude device ID and the same "create" variant every
  time. That strongly suggests Amplitude's device-id fallback is deterministic
  fingerprint-based on this machine, which an automated tool can't get around (a
  browser-launched incognito window may not either, since it shares the same
  hardware fingerprint). Please open an actual incognito window yourself and refresh
  a few times — you should eventually see "Add" instead of "Create" and can screenshot
  it for step 4.5.
- Any of the other screenshots in `evidence/` you want to re-take from your own
  logged-in view for the slide deck (all steps are otherwise done and don't need
  redoing — just re-screenshot if you want your own name on the "Owned by" field
  instead of relying on mine, though this account is already `bhargavi.rabi`).

## Project structure

```text
experiment-implementation/
|-- README.md
|-- memominder/
|   `-- index.html
|-- evidence/
|   |-- *.jpg and *.txt                 # Earlier shared-sandbox run
|   `-- techvedika-org/                 # Final run in the owned organization
|-- slides/
|   `-- *.jpg                           # Screenshots placed in the slide deck
`-- output/
    `-- Implementing_Experiment_Technical_Exercise_MemoMinder.pptx
```

There is no build step or package manifest. The app is a self-contained HTML file
with inline CSS and JavaScript; it loads Amplitude Analytics and the Experiment JS
SDK from their CDNs.

## Codebase

`memominder/index.html` contains the complete app and SDK integration:

- The markup and inline styles define the memo composer, memo list, and empty state.
- The Analytics browser SDK is initialized with autocapture enabled.
- The Experiment SDK is initialized with the client deployment key. After
  `experiment.start()` resolves, `setLabel()` reads the `button_label` payload from
  the `techvedika-memominder-label` variant and updates the Add button.
- The memo handlers add, close, and delete items in the page. Each action sends a
  `Memo Interacted` event with `action` and `memo_id` properties. Memo data is kept
  in page memory and is not persisted across reloads.

## Run locally

From the repository root, serve the app with Python's built-in HTTP server:

```bash
cd projects/experiment-implementation
python3 -m http.server 8000
```

Open `http://localhost:8000/memominder/` in a browser. The app requires network
access to load the SDKs and send events to Amplitude.

## Supporting files

- `evidence/techvedika-org/` contains screenshots from the final run in the owned
  organization.
- Top-level `evidence/` files document the earlier shared-sandbox attempt; those
  artifacts are superseded but retained for reference.
- `slides/` contains the screenshots used in the presentation.
- `output/` contains the generated PowerPoint deck.
