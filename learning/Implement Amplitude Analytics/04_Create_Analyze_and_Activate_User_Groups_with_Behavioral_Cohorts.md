# ✨ Create, Analyze, and Activate User Groups with Behavioral Cohorts

**Type:** On-demand course | **Time commitment:** 16 minutes

---

## About This Course

We all fall into certain groupings with other individuals, whether based on our location, behaviors, or demographics. The same is true for your customers — for example, your users might fall into groups such as users in Singapore who attended a webinar you hosted last month, or users who have spent at least $20 in your product in the past 7 days.

Amplitude allows you to group users who share a trait or a set of traits into cohorts. Those cohorts can then be used in the segmentation module in Amplitude charts, synced to a third-party destination, or compared to another user group to deepen your understanding of how certain groups of users engage with your product.

**By the end of this course, you'll be able to:**
- Describe what cohorts are and how they function in Amplitude
- Differentiate between segments and cohorts and identify when to use each
- Create custom behavioral cohorts using Global Chat, the cohort builder, Microscope, and CSV upload
- Use behavioral cohorts to perform targeted analyses across the Amplitude platform
- Configure cohort syncing to downstream destinations

**You should take this course if:** You have taken a foundational training with the Amplitude team, or "Getting Started with Amplitude Analytics."

---

## SECTION: Introduction

### Lesson 1 — What are Cohorts? (3 min)

**Overview of cohorts**

Amplitude's cohorts help you create and analyze custom user groups based on shared behaviors or properties. Cohorts are useful when you want to compare one group of users to another, focus your analysis on a specific group, or take targeted action based on user behavior.

**[Video: "What Are Cohorts?", 1 min 44 sec]** — overview of cohorts in Amplitude. (No on-page transcript available.)

*Note: This course focuses on behavioral cohorts — user groups based on past actions. Amplitude also offers predictive cohorts, built using predictions about future behavior; learn more in the course "Create and Analyze Predictive Cohorts."*

**Cohorts vs. segments**

If you're familiar with Amplitude's chart builder, you've likely used the "Segment by" module to filter and compare users. This raises the question: when should you use a segment, and when should you create a cohort?

- A **cohort** is a saved group of users who meet certain criteria.
- A **segment** is a filter, or set of filters, applied inside a chart. Segments don't create a reusable group of users; they control which users display in that chart's results. You can save a segment, which saves the filter setup, not the user group itself.

| Scenario | Use a... | Because... |
|---|---|---|
| You want to apply a simple, one-time filter to analyze a subset of users in a chart. | Segment | Segments are created directly in the chart and are ideal for one-time comparisons. |
| You want to filter a chart for users who did something in each bucket of the chart. | Segment | Segments support "in each" logic based on the chart's interval (daily, weekly, monthly). |
| You want to reuse a simple set of segment filters across multiple charts. | Saved segment | Saved segments can be reused across charts, but if you change the definition later, you'll need to reapply the updated segment filter in each chart. |
| You need the same group of users across charts and want the definition to stay up to date automatically. | Cohort | Most cohorts are dynamic by default, so they update automatically wherever they're applied. |
| You want to define users with nuanced counting rules. | Cohort | Cohorts support more detailed logic, including event sequencing, "did not" and "or" conditions, and refined counting rules (e.g., requiring an event on distinct days within a set period). |
| You plan to activate users in other tools (like an external messaging, ad, or data platform). | Cohort | Only cohorts can be synced to external tools for activation or follow-up. |
| You want to build a new group based on a previously defined one. | Cohort | You can layer conditions or refine existing cohorts to create more specific user groups. |
| You plan to target users in Amplitude Experiment or Guides or Surveys. | Cohort (recommended) | While you can apply segment filters during setup, cohorts offer the most flexibility when you want a reusable audience across Amplitude products. |

## SECTION: Create Cohorts

### Lesson 2 — Create Cohorts (4 min)

**Create custom cohorts** — you can create cohorts in several different ways:
- Use natural language to build a cohort using Global Chat
- Define a cohort using the cohort builder
- Save a cohort from Microscope
- Import a cohort from a CSV file

**Additional resources:**
- For more on the cohort builder, including specific explanations of the various event-counting options, refer to the Amplitude Documentation on defining a new cohort.
- For more on creating cohorts from Microscope, refer to the Amplitude Documentation on creating cohorts with Microscope.

## SECTION: Take Action

### Lesson 3 — Take Action on Your Cohorts (3 min)

**Use your cohorts** — now that you know how to access your cohorts, this lesson explores how to use them throughout the Amplitude platform. The **Target Users** button on the cohort details page shows the various ways you can use cohorts:

- Apply cohorts to charts to perform targeted analyses on specific user groups
- Use cohorts in A/B testing and feature flags with Amplitude Experiment
- Target specific cohorts with Guides and Surveys for timely, relevant in-product messaging and support
- Sync cohorts to downstream destinations to further activate user groups

*(The next lesson digs deeper into syncing cohorts to downstream destinations.)*

### Lesson 4 — Sync Your Cohorts to Downstream Destinations (6 min)

Exporting cohorts to downstream destinations allows you to act on your behavioral insights. Once you've built a cohort, you can sync it to external tools — such as ad networks, attribution providers, or marketing automation platforms — for timely and targeted activation. This lesson covers confirming a destination is connected, creating a sync, and managing sync settings within Amplitude.

**Example: Sync a cohort for re-engagement**

**[Video: "Use Case: Sync a Cohort for Re-Engagement", 3 min 42 sec]** — demonstrates syncing a cohort for re-engagement. (No on-page transcript available.) While watching, consider the various ways your team can use cohort syncs to act on insights uncovered in your analysis.

**Connect to a destination** — Before you can start syncing cohorts, check that your destination of choice is connected by navigating to the data destinations area of Amplitude. If you don't see your destination of choice, add it using the **Add Destination** button on that screen. *Note: Adding new destinations might be managed by another team at your organization.* You can connect a new destination from the integrations catalog in the Data section of Amplitude — search or filter for an integration, or browse by category, and filter by "Cohorts" to see destinations you can send Amplitude cohorts to. You can also find all of Amplitude's current available integrations at amplitude.com/integrations. For step-by-step guidance, refer to the Amplitude Documentation on destination integrations.

**Create your cohort sync** — once your destination is connected, you can start a cohort sync from two places:
- **Option 1: Cohort Details** — From a specific cohort's details page, click the **Target Users** button, then choose the destination for your sync.
- **Option 2: Syncs** — Create a sync from **Syncs** within the Users section of Amplitude, where all existing syncs for your project are listed. Click **Create Sync**, choose **Cohort Sync**, select the cohort you want to sync, then click **Next** — this takes you into the same setup flow as syncing from the cohort's detail page.

After selecting your sync destination, define the cadence of the sync. Once you make your sync cadence selection, click **Sync** to complete the setup.

**Review the two types of syncs** — you can set up both one-time and scheduled syncs in Amplitude:
- **One-time sync** — also known as ad hoc syncs, on-demand syncs, or manual syncs. Useful for one-off campaigns and audience testing.
- **Scheduled syncs** — also known as recurring or automated syncs. Useful for ongoing campaigns set to recur at a daily, hourly, or real-time cadence.

**Review and manage syncs** — once created, you can view and manage a sync from the **Syncs** section, which includes a table with relevant information for each sync in your project:
- **Destination** — where the sync is exporting data.
- **Cadence** — whether the sync happened just once or recurs on a cadence.
- **Last synced at** — the date of the last sync.
- **Sync (name)** — clicking the name takes you to the cohort details page, landing on the Syncs tab, where you can view additional details, check sync history (including any errors), manually trigger a sync, or edit the existing sync cadence.

## SECTION: Conclusion

### Summary and Additional Resources

**Summary:**
- You can create behavioral cohorts using Global Chat, the cohort builder, Microscope, or CSV upload. Each method offers different advantages depending on your data and analysis needs.
- Use cohorts to power targeted analysis across Amplitude — apply them in charts and target them with experiments, guides, and surveys.
- Sync cohorts to downstream tools to take action on your insights. One-time or automated syncs let you activate your audiences in messaging, ad, and data platforms.
- Behavioral cohorts support strategic goals across teams. Whether you're focused on retention, engagement, feature adoption, or conversion, cohorts help you personalize interventions and measure impact.

**Additional resources:**
- Amplitude Documentation: Define a new cohort; Create cohorts with Microscope, file import, or the Segmentation module; Destination catalog
- Amplitude Academy: Create and Analyze Predictive Cohorts; Getting Started with Amplitude Feature Experiment; Engage Your Users with Guides and Surveys
- Amplitude Website: Data and Marketing Integrations

*"Thanks for completing this course! You've reached the end of Create, Analyze, and Activate User Groups with Behavioral Cohorts. Click 'Next' to share your feedback on this course by completing a short survey."*

---

## Summary / Explanation

This course zooms in on one Amplitude concept — the **cohort** — and covers it end to end. It starts by disambiguating cohorts from segments (a cohort is a saved, typically dynamic, reusable group of users defined by nuanced rules; a segment is a one-off filter scoped to a single chart), then walks through the four ways to build a cohort (Global Chat / natural language, the cohort builder, saving from Microscope, or CSV import), the four places a cohort gets used (charts, Experiment, Guides & Surveys, and downstream syncs), and finally the mechanics of syncing a cohort to an external destination (ad networks, attribution tools, marketing automation) as either a one-time or a recurring sync, plus how to monitor and manage those syncs afterward. The throughline is a funnel: define the group → analyze/target with it inside Amplitude → activate it outside Amplitude.
