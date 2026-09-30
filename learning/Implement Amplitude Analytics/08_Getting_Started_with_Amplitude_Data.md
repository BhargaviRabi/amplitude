# Getting Started with Amplitude Data

**Type:** On-demand course | **Time commitment:** 40 minutes (curriculum overview lists 35 min of lesson content, with the ability to stop and start as needed)

---

## About This Course

Amplitude Data brings data management functionalities to a centralized hub to help you maintain a clean, high-quality source of truth for your analytics data.

This course will introduce you to Amplitude Data's basic data ingestion, data planning, and data governance functionalities. You will learn to connect data sources to Amplitude, make changes to your product's tracking plan, and set rules for managing your schema. If you're a developer who wants to learn more about the implementation tools offered by Amplitude Data, be sure to check out Amplitude's developer documentation.

While it's not necessary to have specific knowledge of Amplitude Analytics, be sure you're familiar with event-based analytics before getting started with this course.

**By the end of this course, you will be able to:**
- Set up a new data project and connect data sources and destinations
- Navigate key parts of the Amplitude Data user interface
- Make changes to your product's analytics tracking plan
- Collaborate on your event tracking strategy without leaving Amplitude Data
- Set rules for managing your tracking plan
- Validate your data collection
- Manage your tracking plan and enrich your data
- Interpret the event statuses surfaced automatically by Amplitude Data

**Who this course is right for:** Anyone setting up a new data project in Amplitude Data who is already familiar with event-based analytics.

**Time commitment:** 40 minutes, with the ability to stop and start as needed.

---

## SECTION: Introduction to Amplitude Data

### Lesson 1 — Data Management in Amplitude (4 min)

Amplitude Data is a centralized hub for data management and governance. Before diving into the specifics of using this product, this lesson looks at what data management is and the main functionalities of Amplitude Data.

**[Video: "Intro to Amplitude Data", 2 min 07 sec]** — introduces Amplitude Data. (No on-page transcript available.)

**Data management with Amplitude Data** — you can think of Amplitude Data as having four interrelated parts to its functionality (presented as an interactive flashcard activity):
- **Data Planning** — Proactively managing data quality by planning which events and properties to track based on the goals of the business.
- **Data Ingestion** — Bringing in data from various data sources, such as SDKs, APIs, warehouses, and more.
- **Data Governance** — Setting and enforcing practices for ensuring high data quality.
- **Data Federation** — Sending data to downstream destinations like marketing technology.

**Who is Amplitude Data for?** Different people and teams are involved in different parts of data management (presented as an interactive card activity — "Which category do you best fit into? Depending on your organization you may find yourself in one or more of these roles"):
- **Data governors** — Who they are: data analysts, technical product managers, data engineering leads. What they care about: Setting and enforcing internal standards for maintaining high-quality data.
- **Data consumers** — Who they are: product managers, marketers, anyone who uses data. What they care about: Getting the events and properties they need instrumented so they can do analyses and uncover insights to support their decision-making.
- **Data implementers** — Who they are: developers, other technical users. What they care about: Fast, simple, painless analytics instrumentation.

### Lesson 2 — Navigating the Amplitude Data Interface (3 min)

Before getting into the functionalities of Amplitude Data, this lesson covers how to navigate through the product. The areas of the product visited on a day-to-day basis may differ depending on role (data governor, data consumer, or data implementer). A simple workflow is introduced here that also serves as a roadmap through the rest of the course.

**[Video: "Navigating the Amplitude Data UI", 5 min 18 sec]** — walks through navigating the Amplitude Analytics/Data UI. (No on-page transcript available.)

**An overview of Amplitude Data** — an interactive hotspot diagram ("Click on the hotspots below to learn about the different areas of Amplitude Data"):
- **Navigating to Amplitude Data** — To access your data management portal from anywhere in the product, simply click Data in the left navigation.
- **Data Home** — For data governors, the Amplitude Data homepage surfaces insights into the health and usage of your data.
- **Data Assistant (BETA)** — Data Assistant offers suggestions on how to improve the discoverability of your data by adding useful event metadata. The clarity and consistency of your data taxonomy increases your overall score.
- **Tracking Plan** — The Tracking Plan is your data source of truth — a living catalog that describes the events and properties you are currently tracking or are planning to track. It consists primarily of your catalog of Events, Properties, and Filters. You can also launch Visual Labeling to define your autocaptured click events. Groups will only be visible if you have the Accounts add-on.
- **Projects and Branches** — Be sure to choose the correct project and branch if you need to make changes to your Tracking Plan. Main contains your most up-to-date, "official" Tracking Plan; a branch is an isolated working area for you and your team to make changes, which can later be merged to main.
- **Activity Log** — Shows a log of all the recent changes made to your Tracking Plan.
- **Connections** — View your connected data sources and data destinations and debug ingestion issues; browse the Connections Catalog to add a new source or destination.
- **Settings** — Navigate to Amplitude Data's Settings page to set taxonomy naming conventions, require reviews, and manage integrations with existing tools.

## SECTION: Data Connections

### Lesson 3 — Setting Up Your Amplitude Data Project (3 min)

Setting up a new project is the first thing you'll need to do in order to start using Amplitude Data's data planning, governance, and developer tools. Typically, you should have one project for every application that you'll be collecting data for. This step is usually done by someone who has administrator permissions in your organization.

**How to configure a new project:** If you have Manager or Administrator privileges, you can configure a new project in your Organization Settings page.
1. Click Create Project in the Organization Settings page.
2. Name your project and add a description, if necessary. Be sure to indicate whether this is a development or production project.
3. Select users and assign them user roles, if necessary.

*Are you an Amplitude administrator? Learn more about setting user roles and managing permissions by taking the "Amplitude Analytics Admin Essentials" course.*

**Development and production environments** — Having separate environments allows you to test and validate your instrumentation before sending production data to Amplitude. Amplitude cannot retroactively modify your raw historical data, so the data you collect can't be modified if your instrumentation is wrong — that's why it's always good to have a staging environment for testing. Reviewed via two tabs:
- **Development** — Treat this as a testing environment; keep it separate from your production data; catch errors in your instrumentation.
- **Production** — Treat this as the "official" environment; use the data here for analysis and reporting; block or filter out internal users.

### Lesson 4 — Connecting Data Sources and Destinations (4 min)

**Overview of Events and User Data in Amplitude:** Now that you have set up your Amplitude Data project, it's time to bring data into your system. You use the Connections area of Amplitude Data to connect to various data sources and choose which destinations to send your data to.

*Note: the lesson video shows an older Amplitude user interface; the product functionality described remains the same.*

**[Video: "Connecting sources and destinations", 3 min 35 sec]** — (No on-page transcript available.)

**Manage your data connections** — the easiest way to get an overview of all of your data sources and destinations is through the Connections Overview page. Presented as an interactive hotspot diagram ("Click on the hotspots below to learn more about each part of this page"):
- **Data Sources** — Shows the total number of data sources connected to this project in the last 30 days; click to go to the Sources page.
- **Data Ingested** — Shows the ingested events over the last 30 days; click to go to your organization's Usage page to learn more about event usage.
- **Data Destinations & Data Exported** — Two tiles: number of data destinations connected to this project (left), and number of events exported in the last 14 days (right); click to go to the Destinations page.
- **Cohorts Synced** — Shows the total number of cohorts from this project that were synced in the last 30 days; click to go to the Syncs page in the Users section of Amplitude.
- **Configure your sources and destinations** — Clicking any of the data sources or destinations shown here will prompt you to set up and/or configure the specified data connection.
- **Add new sources or destinations** — Easily add new sources and destinations from the Connections Overview page by clicking Add more, which takes you to the Connections Catalog.

**Data Connections FAQ:**
- *When should I create a new data source?* A new data source should be created for every standalone part of your product that will send events to your analytics backend.
- *What is the Ampli Wrapper?* A dynamic, code-generated tracking library that offers type-safety, supports linting, and offers autocomplete among other helpful features — making it easy and convenient for developers to instrument the events in your tracking plan without errors.
- *What should I do after I create a new data source?* After creating and naming a new data source, reach out to a developer who will use the specific setup instructions provided to bring in the data associated with that source.

**Leverage Autocapture with Amplitude SDKs** — If you are bringing data into Amplitude using Amplitude SDKs, you will be able to track different types of data by default with autocapture. Autocapture is the fastest and easiest way to get data into Amplitude and requires minimal engineering effort once the SDK is initialized and configured. (More on autocapture and visual labeling is covered in a separate course.)
- *Read the docs:* Autocapture Documentation — learn more about what kinds of data can be autocaptured and how to configure your settings.
- *Watch the video:* "Visually label autocaptured events" — learn how to retroactively define your autocaptured click events.

## SECTION: The Tracking Plan: Your Analytics Source of Truth

### Lesson 5 — Leveraging the Tracking Plan (4 min)

In Amplitude Data, the Tracking Plan is a key feature that shows you all of your events and properties and acts as your analytics source of truth. This is what you use to learn about your schema, add and edit new events and properties, collaborate with your team, and surface errors. This lesson first covers how to navigate through the Tracking Plan.

*Note: the lesson video shows an older Amplitude user interface — for the updated Amplitude Data navigation, see the "Navigating the Amplitude Data Interface" lesson.*

**[Video: "Leveraging the Tracking Plan", 4 min 42 sec]** — (No on-page transcript available.)

**Traditional tracking plans vs. Amplitude Data's Tracking Plan:** A tracking plan is a document that outlines the events and properties you have or are planning to instrument in your analytics project. These usually live in spreadsheet templates or internal wiki pages, but often become outdated.

| Traditional tracking plans | Amplitude Data Tracking Plan |
|---|---|
| Static, can grow quickly outdated | Dynamic, easy to keep updated |
| Lives outside of Amplitude | Lives within Amplitude |
| Not easy to enforce governance rules | Surfaces errors in syntax and naming |
| Not easy to surface implementation errors | Overlays your event stream with your Tracking Plan and surfaces errors |
| Communication with developers isn't streamlined | Facilitates in-product communication with developers |

**Investigate issues with purpose-built views** — With the Tracking Plan's pre-built filters, you can directly validate your incoming data against your Tracking Plan. Choose Investigate Issues, and Amplitude will compare your current Tracking Plan with your event stream during a specified time window and surface all discrepancies. Data that does not match your Tracking Plan will be flagged as having an issue. Amplitude's event stream time window ranges from the past 5 minutes to the past 14 days; you can opt to look only at data sent to a specific branch. *(Includes an embedded walkthrough: "How to investigate data issues surfaced by Amplitude Data.")*

### Lesson 6 — Making Changes to Your Tracking Plan (4 min)

An analytics tracking plan should stay updated as you roll out new products and features. Amplitude Data's Tracking Plan lets you plan new events and properties and edit existing ones all without leaving Amplitude.

**[Video: "Making changes to the Tracking Plan", 3 min 37 sec]** — covers how to make common changes to your Tracking Plan, including: how and why you should create a branch; how to plan new events and properties; how to specify property rules. (No on-page transcript available.)

### Lesson 7 — Collaborating with Your Team Using the Tracking Plan (3 min)

Instrumenting analytics is often a team sport that brings together product managers, analysts, engineers, and other stakeholders. Amplitude Data offers several opportunities to easily connect with others in your organization for feedback and alignment without needing to leave the product.

**[Video: "Collaborating with your team using the Tracking Plan", 2 min 50 sec]** — covers ways to collaborate within Amplitude Data, including how to add comments, tag your team, and request approvals. (No on-page transcript available.)

## SECTION: Data Governance Basics

### Lesson 8 — Setting the Foundation for Data Governance (6 min)

Data governance can happen at the single product level or evolve into a multi-product strategy, depending on the maturity of the business. In many ways, all of Amplitude Data's capabilities mentioned in this course can be leveraged as part of an organization-wide governance practice, as well as within individual projects. This lesson focuses on data governance practices to put in place during the initial setup phase of Amplitude Data.

**Clean vs. messy data** — "garbage in, garbage out": if the data you collect and analyze is dirty, the insights you glean from it are unreliable.
- **Messy Data:** ⚠️ Inconsistent syntax · ⚠️ Punctuation and spelling errors · ⚠️ Duplicate data · ⚠️ Improper data types associated with a field · ⚠️ Wrong or outdated data
- **Clean Data:** ✅ Consistent syntax · ✅ Correct punctuation and spelling · ✅ Data is not duplicated · ✅ Inaccurate data is filtered or blocked · ✅ Data is up-to-date

**[Video: "Setting the foundation for data governance", 3 min 20 sec]** — (No on-page transcript available.)

**Organize your Tracking Plan with the Data Assistant** — Amplitude's AI Data Assistant is a simple way to start organizing your Tracking Plan. On the Amplitude Data homepage, Data Assistant automatically surfaces quick and easy suggestions that improve your Tracking Plan's completeness, consistency, and cleanliness, reflected cumulatively in your Tracking Plan health score.
- *Add important metadata to your most relevant events* — Data Assistant's top suggestions for improving your Tracking Plan health score are found on the Data homepage; clicking a suggestion surfaces the data it applies to and lets you take action (add descriptions, categories, event owners).
- *Auto-generate relevant metadata* — Data Assistant can help generate event descriptions and suggest event owners and categories.
- *Keep your syntax consistent* — Data Assistant flags event and property names that violate your Tracking Plan's naming conventions and suggests naming that matches your specified syntax.

**How is the Tracking Plan health score calculated?** (Example shown: a health score of 84 out of 100.) The health score is calculated based on characteristics reflective of the Tracking Plan's overall completeness, consistency, and cleanliness, including: how consistently events/properties adhere to the proper casing and naming convention specified for the project; whether event descriptions, categories, and owners are specified; and whether deleted events are flagged as test events. Following Data Assistant's suggestions is expected to increase the health score over time.

**Event validation in Amplitude Data** — A big challenge for many teams is a lack of visibility into the state of their data collection; teams often rely on manual testing, broken charts, and instinct to validate their product analytics, which leaves teams lacking trust in their analytics. Amplitude Data monitors your existing event stream and surfaces inconsistencies, turning your tracking code into a living document so you know when something is broken or can be improved — issues are surfaced in the "Status" column of your Tracking Plan. Key features of Amplitude Data's event validation and observability capabilities:
- **Event validation time window** — Allows you to compare the event stream from the last 5 minutes to the last 14 days in your production or development environment against your most recent Tracking Plan; detected errors/discrepancies surface in the Issues column.
- **Issues column** — Shows data issues within the selected validation window and environment.
- **Event validation issue** — Indicates event data that is unexpected when compared to the Tracking Plan, during the specified event validation window and environment.
- **Status column** — Shows the status of the events being ingested in your Tracking Plan; the validation time window does not affect event statuses surfaced in this column.
- **Status: Unexpected** — Indicates an event that is not in your Tracking Plan.
- **Status: Live** — Indicates that an event is present in your Tracking Plan and is currently being ingested.
- **Actions on unexpected events** — Allows you to choose whether to block, delete, or add an unexpected event to your Tracking Plan.

### Lesson 9 — Transforming and Filtering Your Data (4 min)

Amplitude Data offers data governors several tools for cleaning up a Tracking Plan (covered in more detail in a separate data governance and maintenance course); this lesson briefly covers data transformations and drop/block filters. *Note: transformations is a paid feature.*

**Transform your event data structure** — Amplitude Data's transformations feature lets you transform data to correct common implementation mistakes, such as:
- Merging events, event properties, and user properties — useful if you have duplicate events, event types that use different syntax, or two similar events that are better tracked as a single event with distinguishing properties.
- Renaming user property and event property values that are misspelled and/or don't make sense.
- Hiding property values that you want to track but do not want appearing in charts.

**[Video: "Transformations", 1 min 15 sec]** — shows an example of setting up a transformation that merges two duplicate events into a single event. (No on-page transcript available.)

**Transformations FAQ:**
- *Why am I unable to create a transformation?* If the 'Transform' option can't be clicked or isn't visible, and you're certain your organization has access to this feature, check: you have the correct permissions (currently only admins and managers can create/modify/delete transformations); you're on the main branch of your Tracking Plan; you've published any pending changes.
- *Will a transformation change my raw data?* No — transformations are applied at query time, when a chart or cohort generates results; this does not affect the raw data.
- *Can transformations be applied retroactively?* Yes — you can create a transformation at any moment and apply it to all historical data.
- *Can I delete or modify a transformation?* Yes — transformations are not permanent; requires admin or manager-level permissions.
- *Can I transform a default Amplitude user property?* No — default Amplitude user properties (preceded by the Amplitude logo) cannot be transformed at this time.

**Remove specific event data with filters** — If you find you are ingesting incorrect data, you can create block and drop filters in Amplitude Data:
- **Drop filters** let you remove specific event data from your charts at query time. These events are not deleted; they can be restored to your charts by editing or deleting the filter. Drop filters do not affect your event volume limit.
- **Block filters** block specific events or properties from being ingested, so this data cannot be recovered. Block filters are especially useful for blocking data by IP address.

## SECTION: Conclusion

### Quiz

**Result on file:** Passed — 4 of 4 correct (100%). Elapsed time: less than a minute.

This quiz's "Show Answers" view visually marks each option with a checkbox — correct options are shown checked, bolded, and in green; incorrect options are shown unchecked, greyed out, and struck through. The specific correct option(s) for each question are reproduced below.

1. **Which of the following is true about using branches in Amplitude Data? Select all that apply.**
   - ☑ **A branch is an isolated working area for you and your team to make changes to the Tracking Plan.** *(correct)*
   - ☐ All Tracking Plan changes must be made directly to the main branch.
   - ☑ **In order for the changes to your branch of the Tracking Plan to be reflected in the main branch, it must first be merged to the main branch.** *(correct)*

2. **How can you use Amplitude Data to maintain a clean data taxonomy? Select all that apply.**
   - ☑ **Set event and property naming conventions, like Title Case and snake_case** *(correct)*
   - ☑ **Set property rules, like whether or not a property is required for an event, what its min/max length is, and its data type** *(correct)*
   - ☑ **Add event categories and tags** *(correct)*

3. **In the following taxonomy, the event 'App Closed' follows the taxonomy design conventions set by this team. With this in mind, how should the other two events be corrected to maintain consistency? Select all that apply.**
   *(The question includes a screenshot of an Amplitude Data Events table listing three events: "Add Bank Account" [Category: Banking], "App Closed", and "ID process".)*
   - ☐ The event 'ID process' should be renamed 'ID processed'
   - ☑ **The event 'ID process' should be renamed and capitalized as 'ID Processed'** *(correct)*
   - ☑ **The event 'Add Bank Account' should be renamed 'Bank Account Added'** *(correct)*

4. **Which of the following actions must be done in Amplitude Data before you can begin building analyses in Amplitude Analytics? Select all that apply.**
   - ☐ Your Tracking Plan must be approved by the Amplitude administrator.
   - ☐ An event streaming destination must be configured.
   - ☑ **At least one data source must be configured.** *(correct)*

---

## Feedback

This course ends with a "We'd Love Your Feedback" survey lesson — navigational/administrative, not course content.

---

## Summary / Explanation

This course is the Amplitude Data counterpart to "Getting Started with Amplitude Analytics" — where that course teaches you to analyze data already in Amplitude, this one teaches you how that data gets there and how it stays trustworthy. It follows a natural lifecycle: first, **understand the four pillars** of data management (Planning, Ingestion, Governance, Federation) and learn the interface; then **set up a project** and **connect sources and destinations** to actually bring data in; then use the **Tracking Plan** as the analytics source of truth — reviewing it, editing it, and collaborating on it as a team; then apply **governance practices** (clean-data principles, the Data Assistant's health score, and automated event validation that flags "Unexpected" vs. "Live" events) to keep that Tracking Plan trustworthy over time; and finally **clean up problems after the fact** with transformations (query-time fixes that don't touch raw data) and drop/block filters (removing or blocking bad event data). The quiz reinforces several precise mechanics worth remembering: branches must be merged into main to take effect; a clean taxonomy relies on naming conventions, property rules, and categories/tags together; taxonomy consistency means both correct casing and clear, human-readable event names; and of the three Data-side prerequisites tested, only having at least one configured data source is strictly required before you can start building analyses in Amplitude Analytics.
