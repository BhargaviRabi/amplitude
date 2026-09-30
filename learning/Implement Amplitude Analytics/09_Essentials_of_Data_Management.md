# Essentials of Data Management

**Type:** Learning path (5 courses + introduction + final assessment) | **Total time commitment:** ~122 minutes of lesson content (31 + 50 + 10 + 21 + 10 min across the five courses)

---

## About This Learning Path

**Audience:** This learning path is designed for all roles involved in the process of taxonomy design, instrumentation, and governance.

This series of five courses is designed to take you through the cycle of data creation and introduce frameworks, resources, and essential Amplitude tools to help you be successful at each step. You will go through the Fundamentals of Data Taxonomy Design, Instrumenting Your Data Taxonomy, Getting Started with Autocapture and Visual Labeling, Data Governance and Maintenance Best Practices, and the Data Access Controls: Classify and Manage Your Data courses. The "Getting Started with Amplitude Data" course is not a prerequisite for this learning path; however, the Amplitude Data product will be referenced as a tool where appropriate.

By the end of this learning path, you will have a solid foundation for getting and maintaining useful data into Amplitude, including knowledge of the following:

**Part 1: Fundamentals of Data Taxonomy Design**
- Different ways to approach what events and properties to track
- Best practices for how to design a good taxonomy
- How to teach and learn your taxonomy

**Part 2: Instrumenting Your Data Taxonomy**
- Ways you can send data to Amplitude
- How Amplitude resolves anonymous users
- Why and how to set User IDs
- How to set and update user properties
- High-level strategies for validating and debugging instrumentation

**Part 3: Getting Started with Autocapture and Visual Labeling**
- How to enable and configure Autocapture
- How to use visual labeling to track click events
- When to use Autocapture versus precision tracking

**Part 4: Data Governance and Maintenance Practices**
- The data governor's three broad areas of ownership as recommended by Amplitude
- Methods to scale taxonomy education at your organization so new consumers of data can quickly begin to create their own analyses
- Methods to establish instrumentation standards that will help preserve data cleanliness and usability
- How to audit your data health to identify inaccurate or unhelpful data

**Part 5: Data Access Controls: Classify and Manage Your Data**
- How to classify data in Amplitude
- How to grant data access to the right members of your organization

---

## Introduction

**[Video: "Essentials of Data Management", learning path introduction]** — Amplitude Academy–branded introduction video for the learning path. (No on-page transcript available; no separate text content on this page beyond the title card.)

---

# Part 1: Fundamentals of Data Taxonomy Design

**Type:** On-demand course | **Time commitment:** 30–31 minutes

## About This Course

Data taxonomy design is the process of planning out the user actions and attributes that you will track as events and properties in Amplitude. It is one of the most critical steps in implementing Amplitude and well worth the upfront time and effort that goes into it. A well-designed taxonomy will help you build meaningful analyses and deepen the value you get from the data you send to Amplitude, while also remaining easy to learn and maintain.

What makes for a good taxonomy and how do you create one? While taxonomy design can vary between organizations and verticals, this course offers universal guiding principles and frameworks that you can use to design the taxonomy of the first few critical paths through your product.

This course is best suited for individuals who are already familiar with event-based analytics and are tasked with thinking strategically about first-time taxonomy design.

**In this course, you will learn:**
- Why good data taxonomy design matters
- Different ways to approach what events and properties to track
- Best practices for how to design a good taxonomy
- How to teach and learn your taxonomy

**You should take this course if:** You are already familiar with event-based analytics, are responsible for instrumenting Amplitude, and/or you have completed the Getting Started with Amplitude Analytics learning path.

## SECTION: Introduction to Data Taxonomy Design

### Lesson 1 — Reviewing Events and Properties (4 min)

Welcome to Fundamentals of Data Taxonomy Design. One of the most important steps in getting started with Amplitude is designing your data taxonomy — this is the language of events, properties, and users that allows you to build analyses in Amplitude. In this course you will: talk about why your data taxonomy matters and recap how events and properties relate to asking questions in Amplitude; explore different frameworks for figuring out what to track in Amplitude; go over how to teach and learn your data taxonomy.

Before getting started, this lesson talks about what is meant by a "taxonomy" for your data and why it matters, and reviews events and properties in relation to a data taxonomy.

**[Video: "What is a Taxonomy Abridged", 2 min 54 sec]** — (No on-page transcript available.)

### Lesson 2 — Using Autocapture and Precision Tracking

There are two main data tracking strategies available in Amplitude: Autocapture and precision tracking.
- **Autocapture** (also known as auto-tracking) refers to a way of automatically collecting a predefined set of events and properties in a standardized taxonomy using the Amplitude SDKs.
- **Precision tracking** (also known as manual tracking or code-based tracking) refers to manually planning and instrumenting events, event properties, and user properties in your code that are specifically tailored to your business needs and desired analyses.

**A combined approach:** Amplitude recommends starting with Autocapture to get your first few event types in quickly with minimal engineering resources — the Browser SDK 2 lets you capture sessions, page views, clicks, form interactions, file downloads, marketing attributions, and element interactions (visual labeling can be used to navigate your site to create new click events); the iOS Swift SDK and Android-Kotlin SDK capture application installs and upgrades, sessions, and screen views. Beyond this, you need precision tracking to capture the full, rich context of a user interaction with custom properties — this requires thinking through analytical questions and business use cases, maintaining a robust taxonomy, and committing engineering resources. This course is mainly focused on strategies for precision tracking, though many of the taxonomy design principles covered also apply to visually-labeled autocaptured events.

*(Cross-reference: "Get Started with Autocapture and Visual Labeling" — learn how to bring event data into Amplitude and start surfacing insights fast. This corresponds to Part 3 of this learning path.)*

The following lessons provide guiding practices on how to best approach a precision tracking strategy.

### Lesson 3 — Determining What to Track (5 min)

Before you can begin instrumentation, it's important to think about the types of questions you want to answer with data — this influences the insights you uncover and future actions you take in Amplitude. There is no need to track every action in your product or come up with every single question ahead of time for your data to be valuable; rather, consider what job data does in your organization.

**[Video: "Determining what to track", 2 min 46 sec]** — (No on-page transcript available.)

**How should you think about what to track?** Understanding how Amplitude defines events, properties, and activities is key to using the platform to gain insights.

**Ask yourself what job data will do for you.** One way to brainstorm the questions you want to answer with data is to ask what the primary job of analytics is in your organization — what business objectives do you hope to meet, and how do those translate to questions you would ask in Amplitude? The lesson includes a diagram with four frames of reference and example questions (all categories may be equally important, but picking a couple areas to initially brainstorm helps create focus):

| I need data to... | I have questions/want to do things like: |
|---|---|
| **...report on metrics I care about.** | How is my North Star metric trending? What is my ACV? Total revenue? What is my DAU? How are my KPIs tracking? |
| **...know what's happening & why.** | What critical paths do users take through my product? What is my aha moment? How many people reach it? What step do users drop out of my funnel? What is my stickiest feature? |
| **...make decisions.** | Should I deprecate this feature? Do I have a usability issue? What product levers can I use to improve retention? Do I need to rethink my pricing model? |
| **...help me take action.** | Send a message to a select group of users; Integrate with a 3rd party; Automate a process; Run an experiment; Build a model |

**Focus on critical actions and paths through your product.** When in doubt, focus on leveraging data to learn what's happening in your product: How are users navigating your product? When do you know they've gotten value? At what point does a transaction happen between your business and your user? Instrumenting events that make up key user flows and points of value exchange can help investigate questions about conversion, retention, revenue, and engagement. As a rule of thumb, you should always track:
- **A defined sequence of steps in your product.** This could be something like a tutorial flow or an onboarding sign-up flow.
- **Paths leading to critical actions being completed in your product.** This is closely related to your product's promise — what do users expect to be able to accomplish, and what paths lead to that moment?
- **Paths leading to purchase or monetization.** This includes things like upgrading a plan, converting from a free trial to paid subscription, and going through a checkout flow.

### Lesson 4 — Turning Questions into Events and Properties (3 min)

Once you have determined the questions you want to answer with your data, you have to think about how to build those analyses in Amplitude — reconstructing your questions as events and properties to track for your product.

**Scenario: Taxonomy for an ecommerce business.** Imagine working at an ecommerce company in the early stages of implementing Amplitude, with a few key questions determined as the immediate focus:
- What is my monthly Average Order Value (AOV)?
- How do I improve my cart abandonment rate?
- Where in my checkout flow do users drop off?

**Focus on one question.** Consider just the first question — tracking monthly AOV, calculated as Total Revenue / Number of Orders. What events and properties would be needed to see this metric?

**Identify actions.** An event is an action that happens in the product that you care about (user-triggered or passive, like a notification). What action is associated with AOV? Revenue is generated when a user goes through the whole checkout flow and successfully places their order — there's the action: **Order Completed**. From there, you could work backwards through the checkout flow to find other important actions, like creating a new account, adding an item to a cart, or browsing an item category.

**Identify attributes.** What extra context is needed for the Order Completed event to calculate AOV? Properties related to revenue, like `$price`, `$quantity`, and `$revenue`; also a unique `order_id` to track the transaction. No new user properties are needed for this particular question, but other event properties related to Order Completed and revenue metrics might include: `cart_size` (number of items in a cart), `cart_value` (total value of the user's cart), `total_discounts` (value of discounts applied to the total cart value).

**Your taxonomy unlocks the answers to more questions.** To track AOV, the decision is to instrument: **Order Completed** (a server-side event that triggers when a user successfully places a purchase), **`$revenue`** (an event property that tracks the total revenue of a purchase), and **`order_id`** (an event property that identifies each individual order). Focusing on one question can lead to other events and properties worth defining — and instrumenting the events/properties needed to answer just one question unlocks the ability to answer more questions. With just this one event and two properties, you can answer questions like: How does my monthly AOV compare to the same time last year? How many times on average do users place an order every month — are there any months that stand out? What proportion of users place an order two or more times a month? How does retention differ between users who return to place an order versus users who do not?

**Resources:** Help Center: Track Revenue.

## SECTION: Taxonomy Design Best Practices

### Lesson 5 — Three Guidelines for Designing Your Taxonomy (10 min)

As you continue exploring use cases and questions and coming up with events and properties to track, you should also strive to design your taxonomy thoughtfully.

**[Video: "Guidelines for designing your taxonomy", 1 min 55 sec]** — (No on-page transcript available.)

**Designing events for long-term usability and value.** Your taxonomy is the language that data users at your organization will use to build their queries and analyses. Keep three principles in mind: reflecting the world of your customers, making your data easy to learn, and defining events at the right degree of abstraction.

**1. How to reflect the world of your customers.** Your product exists to fulfill a specific purpose or goal for someone; that purpose is unlikely to change absent a major business pivot. Make sure your taxonomy captures behaviors related to what users want to accomplish. Best practices:
- **Specify an action.** Make sure your event name has a verb that indicates what the user accomplished or experienced when the event was triggered.
- **Use the language of your users.** Capturing the value your product offers using the language your users use keeps events/properties evergreen and survivable through redesigns, and helps new data users intuit what an event or property maps to.
- **Avoid basing event names on the product UI or code.** Unless testing specific designs, avoid naming critical events or critical paths with UI elements — interfaces can change rapidly, making it hard to figure out what an event is for.

*Example: Customer-centric event naming.* Scenario: defining an event that triggers when a user browses a music category for "AmpliTunes," a music streaming app.
- **"Top Nav Browse Button"** — Poor event name. 🚫 Uses lingo that may not be intuitive for everyone. 🚫 "Top Nav" refers to a UI part that could get redesigned; the browse button could also move. 🚫 No clear user goal or action specified.
- **"Category Browse Button Clicked"** — Okay event name. ✅ Uses the language of the user (a user may describe themselves clicking this button when recounting their flow). ✅ Specifies a clear action ("Clicked"). ✅ Reflects the user's goal of wanting to browse a category. ⚠️ Still references a button, a potentially changeable UI element — is "button clicked" adding crucial information or is it redundant? Also four words long; a shorter, simpler name is often better.
- **"Category Browsed"** — Good event name. ✅ Uses real-world language of the user, not jargon. ✅ Describes the user's goal. ✅ Specifies the action performed without referencing the product's interface.

*Resource: "Keeping the Customer Domain Front and Center" — Read more on reflecting the world of your customer in the Product Instrumentation Series by former Amplitude Product Evangelist John Cutler.*

**2. How to make your data easy to learn.** Adoption of data-driven practices and collaboration is easier if new data users can learn the taxonomy on their own. Take time to come up with a taxonomy style guide so events and properties are consistently named, intuitive, and informative. Best practices:
- **Maintain a consistent style** (case and punctuation) for all events and properties — e.g., Title Case for events and snake_case for properties. Use one style for events and a different one for properties for easy differentiation; consistency matters most.
- **For events, maintain a consistent syntax** that includes a noun and a verb (e.g., all events follow noun + verb or verb + noun order), helping map what event is triggered when an action is done.
- **Name properties such that you can intuit their data type** where possible — e.g., a boolean property could be named `is_subscriber`; a counter property could be named `num_purchases`. Optimize for readability first.
- **Maintain the same verb tense across all events** — Amplitude recommends past tense to indicate the event is triggered once the action is completed (e.g., "Category Browsed" preferred over "Category Browse"). Do not mix tenses.
- **Be concise in your naming.** The more concise, the easier the query is for others to read and comprehend — consider how to make an event name two words instead of five, while balancing conciseness against using the real-world language of the customer.

*Example: Stylistically consistent event naming.* A sample data taxonomy describing events/properties for an account setup flow, reviewed via numbered hotspots (organization's convention: events in Title Case with noun + verb syntax, verb in past tense; properties in snake_case):

| # | Event Name | Event Description | Event Property Name | Sample Property Values | Property Description |
|---|---|---|---|---|---|
| 1 | Homepage Viewed | Triggers when the user lands on the marketing home page | | | |
| 2 | Completed Account Creation | Triggers when the user clicks on "Create Account" button, starting the create account flow | | | |
| 3 | Account Info Submitted | Triggers when the user enters their profile info | | | |
| 4 | Account_Created | Triggers when the user successfully creates their account | account_type | email, facebook, twitter | Type of login used to create account |
| 5 | Verify Account | Triggers when the user verifies their account | verification_method | email, phone call, text | Method used to verify the account |

Hotspot feedback for each numbered item:
1. **Homepage Viewed** — Example of an event that adheres to the stylistic conventions set by this organization (Title Case, noun + verb, past tense; properties in snake_case).
2. **Completed Account Creation** — This event name is lengthy and can likely be simplified. It begins with a verb, which goes against the naming convention. It also sounds similar to the Account_Created event. This is a situation worth having a conversation about.
3. **Account Info Submitted** — No problems with this event. It follows all of the style and syntax conventions set for this taxonomy.
4. **Account_Created** — If we remove the underscore and make this "Account Created," it would fit the naming conventions of this taxonomy.
5. **Verify Account** — This event uses the opposite syntax (verb + noun) and is in present tense. To make this event more understandable and follow the style conventions, it could be renamed to "Account Verified."
6. **(Properties for Account_Created / Verify Account)** — Everything looks good with these properties!

While none of these event names are wrong individually, having hundreds of events and properties with no standard naming practice adds to a novice user's cognitive load — analytics risks becoming too difficult and time-consuming for anyone but the most tenured data analyst to leverage.

**3. How to define events at the right degree of abstraction.** An important part of taxonomy design is achieving the right degree of abstraction, or granularity — making sure events are not too general and not too specific. The right degree may depend on your product or what you decide to measure, and will likely require conversations with the engineer instrumenting events/properties. As a general rule, an event should be valuable on its own.

*Example of too general vs. too specific:* The event "Action Performed" is far too general — it tells you nothing without properties for context. Meanwhile, "Movie Watched: Family - Premium" packs too much information into a single event (Family = genre, Premium = plan) — to understand general movie viewership, you'd need a custom event combining all the too-specific "Movie Watched" events.

| Signals an event is Too General | Signals an event is Too Specific |
|---|---|
| Risk of exceeding event volume because of tracking too many actions at a high level. | Risk of hitting event/property limits because of instrumenting too many event types. |
| Generic event names make events hard to identify and use. | Sheer number of event types makes them hard to identify and use. |
| Requires instrumenting many properties to add context. | Requires creating many higher-level groupings via 'group-by' and custom events. |
| Difficult to maintain the number of properties. | Difficult to maintain the number of custom events. |
| Requires use of several 'where' clauses and filters to do an analysis. | Names are extremely long and difficult to use when the product gets redesigned. |
| Harder to leverage in Pathfinder and Funnels, i.e. charts that require analyzing unique steps. | Extreme detail causes you to lose sight of broader product usage insights. |
| Easier to instrument, but data is difficult to understand; usability is a major issue. | Time-consuming to instrument and data is difficult to understand; usability is a major issue. |

*Example: The "just right" event.* Scenario: a media streaming company where a critical path involves users clicking to view a movie's description. Three event/property combinations considered:
- **Page Viewed / `page_url`** — Triggers whenever a user lands on any product page; `page_url` stores the specific page URL. Too abstract (and violates customer-centricity): not valuable on its own; differentiating between pages requires filtering by `page_url`, making funnel charts cumbersome and hard to understand without knowing all page URLs.
- **Description Viewed / `content_title`** — Triggers when a user views a movie's description; `content_title` stores the movie title. Right level of abstraction: reflects the customer domain and follows stylistic best practices; the event alone can be leveraged in meaningful analyses.
- **"Mulan: Description Viewed"** (no properties) — Too specific: risks hitting event type limits depending on catalog size; taxonomy maintenance becomes difficult with so many event types; event name is long and unwieldy; measuring general behavior around viewing descriptions requires creating and maintaining one or more custom events.

**Resources:** Blog: "Keeping the Customer Domain Front and Center"; Help Center: "Limits: How much data can you send to Amplitude?"

### Lesson 6 — Industry-Specific Taxonomy Guides

If you're not sure where to start, Amplitude's Professional Services team publishes industry-specific implementation guides with recommended use cases and business questions to tackle, a proposed taxonomy, and an example dashboard:
- Ecommerce Implementation Guide
- FinTech Implementation Guide
- Print Media Implementation Guide
- Streaming Media Implementation Guide

### Lesson 7 — Teaching and Learning Your Data Taxonomy (8 min)

A major focus of this course is designing your data taxonomy so it's easy to learn and use for new users of data and of Amplitude. Beyond thoughtful upfront design, actions within the Amplitude product itself can ease the stress of learning this new data language:
- Adding descriptions to your events and properties, including what action in the product triggers the event.
- Creating a category and/or tags to group all events associated with a particular flow or part of the user journey together.
- Setting case rules for event and property names (can easily be set in Amplitude Data).
- Soliciting reviews from peers and engineers you plan to collaborate with in Amplitude Data.

**Teaching your taxonomy.** A hallmark of a real data-driven culture is having a practice of onboarding new teammates onto your data — introducing rituals like a data training program or a Q&A session with an internal expert.

*Cross-reference course: "Iterating on a Data-Informed Culture" — learn tips on how to build data culture at your organization with one of Amplitude's customers.*

**Learning your taxonomy.** What if you're new to learning your organization's data and don't have a way to learn it, or need to onboard a new teammate without a data dictionary to refer to? Amplitude's Event Explorer tool lets you see what events trigger as you interact with your own product.

**[Video: "Using Event Explorer to Learn Your Taxonomy", 8 min 05 sec]** — shows how people can learn their organization's taxonomy with Event Explorer. (No on-page transcript available.)

## SECTION: Conclusion

### Quiz

**Result on file:** Passed — 4 of 4 correct (100%). Elapsed time: 1 minute.

This quiz's "Show Answers" view marks correct options with a checked, bolded, green checkbox and incorrect options as unchecked, greyed out, and struck through. The correct answers are reproduced below.

1. **I want to investigate how users are moving through my newly implemented in-product onboarding flow. Which of these is an ideal event name to describe a user opting out of the onboarding flow?**
   - ☐ Skip Button Clicked
   - ☐ FTUE: Skipped
   - ☑ **Onboarding Skipped** *(correct)*

2. **True or False: To make sure I get the most value out of my data, I should start out tracking as many user actions as I can think of.**
   - ☐ True
   - ☑ **False** *(correct)*

3. **True or False: I should be careful of how granularly I instrument my events because I may run into event type limits.**
   - ☑ **True** *(correct)*
   - ☐ False

4. **Identify the user property that would help you answer the following question in Amplitude: In the past month, did more users upgrade their subscription plan via my web platform or my iOS app?**
   - ☐ 'Subscription Upgraded' - an action that triggers when a user completes the upgrade process
   - ☑ **'platform' - an attribute that contains the name of the platform the user is on when upgrading their subscription** *(correct)*
   - ☐ device ID - an identifier that denotes the device that a user is on when upgrading their subscription

### Summary and Additional Resources (1 min)

This course offered universal guiding principles and frameworks that you can use to design a data taxonomy for the first few critical paths through your product.

**Additional resources referenced in this course:** Help Center: Track Revenue; Help Center: Industry-Specific Best Practices; Help Center: Limits; Blog: "Use a Mixed-Pattern Approach to Instrumenting Your Product" (and other articles in this series); Blog: "Keeping the Customer Domain Front and Center"; Course: "Iterating on a Data-Informed Culture."

*"Thanks for completing this course! You've reached the end of Fundamentals of Data Taxonomy Design. Click 'Next' to share your feedback on this course by completing a short survey."*

## Feedback (Part 1)

This part ends with a "We'd Love Your Feedback" survey lesson — navigational/administrative, not course content.

---

# Part 2: Instrumenting Your Data Taxonomy

**Type:** On-demand course | **Time commitment:** 40–50 minutes

## About This Course

Once you have a data taxonomy designed with the business and product questions you have in mind to answer, you will need to instrument the events and properties into your codebase and then validate that your event tracking is occurring as expected. While most of the technical instrumentation details you'll need to know can be found in the Amplitude Developer Center, this course offers a deeper look at concepts that will help you in your instrumentation strategy, particularly if you're just starting out with your implementation of Amplitude.

**In this course, you will learn:**
- The various ways you can send data to Amplitude
- How Amplitude resolves anonymous users
- Why and how to set User IDs
- How to set and update user properties
- High-level strategies for validating and debugging instrumentation

**You should take this course if:**
- You collaborate with developers involved in the instrumentation of your taxonomy
- You've taken the Fundamentals of Data Taxonomy Design course
- You've taken Getting Started with Amplitude Data course

## SECTION: Introduction and Review

### Lesson 1 — The Data Creation Process (2 min)

Welcome to Instrumenting Your Data Taxonomy. This lesson reviews the steps of an ideal data creation cycle and identifies who is involved at each step.

**[Video: "Data Taxonomy and QA Intro", 1 min 17 sec]** — (No on-page transcript available.)

*Note: this course should be used alongside technical documentation found in the Amplitude Developer Center — relevant links are provided throughout the course, and it may help to have the Developer Center open in a separate browser window for reference.*

### Lesson 2 — Ways to Send Data to Amplitude (2 min)

How will you be sending data to Amplitude? If you haven't already, it may be worthwhile to review your data taxonomy and indicate the source of the events you want to track. Many customers send Amplitude both client- and server-side events, across multiple platforms. The Amplitude Developer Center has guides and detailed API documentation with all the details an engineer would need to instrument events/properties and ingest data from multiple sources:

- **SDK Quick Start** — Use Amplitude's native SDKs for client-side events (Typescript Browser SDK, Android Kotlin SDK, iOS SDK, and more).
- **Documentation** — Use the HTTP API for server-side events, letting you send data directly from your server to the Amplitude endpoint.
- **Sources Overview** — Integrate with third-party sources (a customer data platform or another tool in your growth stack), or ingest from cloud storage and warehouses (Snowflake, Google BigQuery, Amazon S3, and others).
- **Backfill guide** — Import historical data using the Batch Event Upload API to backfill historical data into Amplitude.

### Lesson 3 — Connecting Data Sources in Amplitude Data (5 min, optional)

*(Lesson title in the player: "Optional - Connecting Data Sources in Amplitude Data")*

In Amplitude Data, Amplitude's central hub for data management, you can directly connect and manage different data sources (and destinations). If you're new to Amplitude Data and haven't taken the "Getting Started with Amplitude Data" course, this lesson's video shows you how to add a new data source to your Amplitude Data project.

**[Video: "Connecting Sources and Destinations", 3 min 35 sec]** — (No on-page transcript available.)

## SECTION: First-time Instrumentation

### Lesson 4 — Instrumenting Events with Ampli (9 min, optional)

*(Lesson title in the player: "Optional - Instrumenting Events with Ampli")*

If you or the developer responsible for instrumentation will be using an Amplitude SDK and Amplitude Data, you may also want to leverage the Ampli Command Line Interface app. Ampli CLI and the Amplitude SDK work together to autogenerate a tracking library based on your Amplitude Data Tracking Plan. This library, the Ampli Wrapper, is a wrapper over the Amplitude SDK that provides type-safety, supports linting, and enables features like input validation. While not necessary for event tracking, it's a great way to reduce errors and ensure your code replicates the specifications of your Tracking Plan.

**[Video: "Instrumenting Events with the Ampli CLI", 8 min 51 sec]** — demonstrates how developers can instrument events with Amplitude Data and Ampli CLI. (No on-page transcript available.)

*Learn more about using Ampli CLI: most of Amplitude's SDKs are supported by Ampli CLI — details on getting started with Ampli and Ampli codegen for each SDK are in the Amplitude Developer Center.*

### Lesson 5 — Tracking Unique Users with Amplitude (13 min)

Your plan for tracking new event types, user properties, and event properties should typically unfold during the data taxonomy design phase, both when implementing Amplitude for the first time and during later rounds of instrumentation. Some properties are especially important to get right during initial implementation — the user ID is one such example. Incorrectly setting user IDs can result in inaccurate counts of unique users and skew your analyses.

**[Video: "Tracking Unique Users", 11 min 01 sec]** — covers when it is appropriate to set user IDs and best practices for doing so, and walks through several scenarios illustrating how the user ID, device ID, and Amplitude ID function together in counting unique users and resolving anonymous users across different devices. (No on-page transcript available.)

**Recap: Amplitude's identifiers.** Three key diagrams reviewed via an interactive carousel:

*Diagram 1 — Three identifiers.* Amplitude uses a system of three identifiers to resolve anonymous users and make sure unique user counts are as accurate as they can be:
- **DEVICE ID** — *Identifies a device.* Required; Amplitude sets this by default, but it's customizable.
- **USER ID** — *Identifies a unique user.* Optional, but recommended for users who are *not* anonymous in your product; set by the data implementer.
- **AMPLITUDE ID** — *Identifies a unique user.* Generated automatically; based on Device ID & User ID; requires *at least* a Device ID.

*Diagram 2 — Amplitude's default device IDs.* If you're using Amplitude SDKs, Amplitude automatically generates device IDs with the following default values. For iOS and Android, you may choose to use advertising identifiers as device IDs instead.

| Event source | Default device ID |
|---|---|
| iOS SDK | Identifier for Vendor (IDFV) |
| Other SDKs | Randomly generated UUID |
| HTTP V2 API | Hashed version of user ID (if not sent) |
| Batch Event Upload API | Hashed version of user ID (if not sent) |

Note that if you're using HTTP or Batch APIs, you must send either a device ID *or* a user ID along with your events.

*Diagram 3 — User ID dos and don'ts.* User IDs are configured by you. While not required, Amplitude recommends setting User IDs so it can generate the most accurate count of users.

| Do: | Do not: |
|---|---|
| ✅ Assign a user ID after a user is authenticated | 🚫 Assign a user ID to an anonymous user |
| ✅ Make sure a single identity in your system has only one unique user ID | 🚫 Assign a user ID that might change (e.g. email address) |
| ✅ Make sure the user ID is a string with minimum length of 5 | |
| ✅ Be aware that user IDs are case sensitive | |

**Knowledge check: true or false?** (Self-check flip cards — statement, then answer revealed.)
1. *"You should set user IDs for users who are not authenticated into your product."* — **False.** Setting User IDs for anonymous, or non-authenticated, users will cause Amplitude to double count users if they log in and become known.
2. *"You do not need both a device ID and user ID to generate an Amplitude ID."* — **True.** Amplitude only needs the device ID to generate the Amplitude ID; however, it is generally recommended that a user ID is also set.
3. *"If you use an Amplitude SDK, Amplitude will set the device ID automatically."* — **True.** The default device ID depends on the SDK used; you can also choose to set a custom device ID.

**Resources:** Help Center: Track unique users in Amplitude; Help Center: Set advertising identifiers as device IDs; Help Center: Setting up cross-domain tracking; Help Center: Assigning Amplitude IDs when no user ID is set.

### Lesson 6 — Updating Event and User Properties (8 min)

Knowing when to send and update your properties is critical to good instrumentation, since this can affect when those values are included in your analyses — particularly true for user properties because of how they are updated and applied to events.

**[Video: "Updating event and user properties", 4 min 54 sec]** — reviews event and user properties in the context of an event stream, then walks through two scenarios illustrating how the timing of a user property update matters. (No on-page transcript available.)

**Knowledge check: event properties and user properties.** An interactive drag-and-drop sorting activity: for each statement below, sort whether it is true for an event property, a user property, or both (statements as listed in the source, one presented at a time in the activity):
- Must be sent with the corresponding event
- Can be updated with the Identify API
- Found on the User & Account Lookup Page
- Can be tracked by Amplitude SDKs by default
- Persists across all events until updated
- Specific attribute of an event
- Specific attribute of a user
- Can be a custom property set by you

*(Categorization buckets: Event Property / User Property / Both. Per standard Amplitude semantics: "must be sent with the corresponding event," "specific attribute of an event" are Event Property; "can be updated with the Identify API," "found on the User & Account Lookup Page," "persists across all events until updated," "specific attribute of a user" are User Property; "can be tracked by Amplitude SDKs by default" and "can be a custom property set by you" are Both.)*

**Resources:** Help Center: All default user properties surfaced by Amplitude; Help Center: How Amplitude updates user properties; Help Center: Sending user properties with an event (via HTTP API).

## SECTION: Data Validation

### Lesson 7 — Validating Your Instrumentation (10 min)

Data validation and debugging should be a critical step in your instrumentation process. Any time you make a change to your taxonomy by adding new event or property types, make sure the data comes into Amplitude as expected. This lesson provides an overview of practices to minimize instrumentation errors and tools for debugging.

**Test in a separate development project.** Before sending data to Amplitude, set up separate development and production projects — a dev project lets you catch and debug errors without affecting your production data.

**Analyze your own event stream.** The Event Explorer feature (covered in the Fundamentals of Data Taxonomy Design course for learning/teaching your data taxonomy) can also be used to analyze your own event stream and see if newly instrumented event types are triggering properly.

**[Video: "Instrumentation Validation", 4 min 37 sec]** — demonstrates how to use Event Explorer, as well as the User & Account Lookup feature, to analyze your event stream and debug your analytics. (No on-page transcript available.)

**Leverage Amplitude Data and Ampli.** Amplitude Data offers proactive and reactive taxonomy management tools to help data implementers and data governors mitigate and resolve instrumentation errors:
- **Use Ampli to minimize instrumentation errors upfront.** The Ampli Wrapper sits on top of the Amplitude SDK and enables features like input validation and type-safety, adding a layer of quality control during instrumentation.
- **Use Ampli to verify your instrumentation against your Tracking Plan.** Ampli can lint your source code to make sure you're tracking all the events planned in your Tracking Plan correctly.
- **Validate your event stream against your Tracking Plan.** Amplitude Data monitors your event stream against your Tracking Plan and automatically surfaces anything broken or needing improvement in the form of statuses (covered further in a lesson of "Getting Started with Amplitude Data").

**Resources:** Amplitude Developer Center: Ampli CLI Commands; Amplitude Academy: Getting Started with Amplitude Data.

## SECTION: Conclusion

### Knowledge Check

**Result on file:** Passed — 4 of 4 correct (100%). Elapsed time: less than a minute. This quiz shows checkbox-marked correct answers plus per-question written feedback.

1. **Assume I assigned a user ID to a new anonymous user who just downloaded my mobile application. Once this user creates an account, I also set their account email address as their user ID. Which of the following happens as a result? Select all that apply.**
   - ☑ **If this user changes their email address, Amplitude will again count them as a different user.** *(correct)*
   - ☑ **Amplitude will count this user as two different users.** *(correct)*
   - ☑ **This user is also assigned two different Amplitude IDs.** *(correct)*
   - ☐ Amplitude will be able to merge this user's Amplitude IDs.
   - *Feedback: User IDs should only be assigned to authenticated users and they should not be set to anything that might change.*

2. **On April 6, 2022, when Brian triggers an action in the AmpliFit app, his `city` user property is logged as "London"; on June 15, 2022, when he triggers another action, this property value is updated to "Tokyo." On July 1, you build an Amplitude chart querying over the data between April 14 to June 14. What will the value of Brian's `city` user property be in this analysis?**
   - ☐ Tokyo
   - ☐ Both London and Tokyo
   - ☑ **London** *(correct)*
   - ☐ Not possible to determine
   - *Feedback: In Amplitude analyses, properties reflect the value they had during the time frame of your query. While the most recent value of Brian's city user property is Tokyo, during the time frame of the query, it was London.*

3. **Same scenario as Question 2. On July 1, you build an Amplitude chart querying over the data between April 14 to June 30. What will the value of Brian's `city` user property be in this analysis?**
   - ☑ **Both London and Tokyo** *(correct)*
   - ☐ London
   - ☐ Not possible to determine
   - ☐ Tokyo
   - *Feedback: In Amplitude analyses, properties reflect the value they had during the time frame of your query. During the time frame of this query, Brian's city user property had two values - London from April 14-June 14 and Tokyo from June 15-June 30.*

4. **Which of the following Amplitude tools can help with validating and debugging your instrumentation? Select all that apply.**
   - ☑ **Event Explorer** *(correct)*
   - ☑ **Ampli & Amplitude Data** *(correct)*
   - ☑ **User & Account Lookup** *(correct)*
   - ☐ Taxonomy API

### Additional Resources (1 min)

This course links to the following resources found in the Amplitude Help Center and the Amplitude Developer Center:
- **Data sources:** Amplitude SDK Quick Start Guide; HTTP V2 API; Batch Event Upload API; Data Backfill Guide.
- **Instrumentation:** Ampli Overview; Track Unique Users in Amplitude; User Properties and Event Properties; Identify API.
- **Data Validation:** Verifying Your Instrumentation with Ampli.

*"Thanks for taking this course! You've reached the end of Instrumenting Your Data Taxonomy. Please click 'Next' in the Academy lesson to complete the course and provide your feedback."*

## Feedback (Part 2)

This part ends with a "We'd Love Your Feedback" survey lesson — navigational/administrative, not course content.

---

# Part 3: Getting Started with Autocapture and Visual Labeling

**Type:** On-demand course | **Time commitment:** 10 minutes

## About This Course

Amplitude's Autocapture and visual labeling functionality is the fastest way to implement Amplitude and track the website clicks that matter to you. With minimal setup, you can capture all elements clicked and changed on your webpage with no additional engineering work. Then, you can visually label what clicks matter to you, directly from your webpage, and start using them in your analyses.

**By the end of this course, you will be able to:**
- Understand how Autocapture is enabled during Amplitude setup
- Understand what Autocapture is and how it differs from Amplitude's Precision Tracking
- Identify autocaptured events in Amplitude Data
- Use visual labeling to define an autocaptured click event
- Leverage a visually labeled event in an analysis
- Replace and repair a labeled event

**Who this course is for:** Product managers and marketing managers who are newly implementing Amplitude.

## Lesson: Getting Started with Autocapture and Visual Labeling (10 min)

With Amplitude Autocapture and visual labeling, you can begin tracking website clicks with minimal engineering set up — the fastest way to get started with data tracking and begin getting insights in Amplitude. This course covers common workflows and scenarios you may encounter while using Autocapture and visual labeling.

*Note: Amplitude's Autocapture and visual labeling functionality is rapidly evolving; this course will continue to expand as new features are added.*

**Overview: Autocapture and visual labeling.**

**[Video: "Use Autocapture and Visual Labeling to Track Website Clicks", 6 min 34 sec]** — a short overview of what Amplitude's Autocapture can track, how to use visual labeling, and how Autocapture differs from precision tracking, plus an end-to-end product demo. (No on-page transcript available. Note: this video may also appear in the Fundamentals of Data Taxonomy Design course.)

**Autocapture and visual labeling in context.** Autocapture and visual labeling may work in parallel — or replace — key workflows as you set up Amplitude and continue to evolve and govern your data taxonomy.

- **Enable Autocapture during Amplitude setup.** When setting up a new Amplitude account, Amplitude recommends pasting a short snippet into the `<head>` of every webpage you'd like to capture data from — this snippet automatically enables Autocapture and Session Replay. Beyond the setup phase, you can still enable Autocapture using the latest Browser SDK. *(The lesson includes a screenshot of a setup panel with step "2. Verify your installation in realtime" showing a "Listening" status indicator.)*

- **Not sure if you can use Autocapture for click tracking?** If you're a new Amplitude user but your organization has had Amplitude for a while, you may wonder how to check whether a specific project is using Autocapture and visual labeling for tracking website clicks. You can either: check for "Element Clicked" or "Element Changed" events in the Events table of Amplitude Data; check to see if your project has any labeled events by checking the Labeled Event tab; or try to launch Visual Labeling — if your site does not have the latest Browser SDK or Amplitude cannot detect any click events, you will see an error state (shown as a screenshot in the lesson).

- **Track click events with both Autocapture and precision tracking.** You can choose to track event data manually, automatically, or both. For web applications, Amplitude recommends using Autocapture with visual labeling to get started with tracking click events — this gets immediate value out of Amplitude's out-of-the-box reporting and helps you build your first few analyses. After your first few charts, you might want to ask deeper behavioral questions and analyze data across custom dimensions — that's where precision tracking brings additional value.
  - *A chart built with the labeled event "Add to Cart"* illustrates that Autocapture events have select default properties — "Add to Cart" is a visually labeled click event and "Page Title" is one of several event properties Autocapture captures by default; these properties relate to element interactions and the user's browser but don't add extra behavioral context.
  - *A chart built with the precisely tracked event "Add to Cart"* illustrates that precision tracking allows for custom properties — while Autocapture events are associated with default and custom user properties, precision tracking also lets you define your own event properties for richer behavioral analyses; in this example "Add to Cart" is manually tracked and "Promo Code Applied" is an event property storing the name of a discount code applied at checkout.

  A comparison table summarizes the key similarities and differences between Amplitude's Autocapture and Precision Tracking solutions:

  | Autocapture | Precision Tracking |
  |---|---|
  | Ideal when first getting started with Amplitude | Ideal when you want to answer more complex behavioral questions |
  | Available with Amplitude SDKs — leverage the Browser SDK with visual labeling for website click tracking | Offers more control over your data taxonomy |
  | Allows you to unlock insights in Amplitude's Web Analytics and Product Analytics spaces | Allows you to unlock insights in Amplitude's Web Analytics and Product Analytics spaces |
  | Captures a set of pre-defined event properties | Allows you to capture additional context behind your events with custom event properties |
  | Associated with all pre-defined and custom user properties | Associated with all pre-defined and custom user properties |
  | Requires no planning and minimal engineering resources | Requires planning and committed engineering resources |

  *Cross-reference course: "Supplement your use of Autocapture with precision tracking" — learn taxonomy design for precision tracking and instrumentation best practices in the Fundamentals of Data Taxonomy Design course (Part 1 of this learning path).*

**Iterate on and govern your labeled events.** Autocapture automatically tracks raw click events in addition to other types of data, while visual labeling gives those events specific definitions. As you iterate on your website and change its structure and design, you may need to make changes to your labeled events by replacing or repairing a definition. Regularly audit your labeled events to make sure they accurately represent the actions users take on your site.

- **Replace a labeled event.** You can replace the definition of a labeled event if you clicked an incorrect element during visual labeling, or need to choose a different element due to site changes. A replace resets the historical data associated with the event and may affect charts/analyses using it. To replace a labeled event definition: (1) Navigate to the Labeled Events tab of the Events table in Amplitude Data. (2) Select your labeled event. (3) Click Replace. (4) Navigate to your site via the Visual Labeler and choose the correct, new elements for this event. *(The lesson includes a screenshot illustrating that the Element Hierarchy property value changes in the labeled event definition when replaced.)*

- **Repair a labeled event.** You can repair the definition of a labeled event if you notice it's no longer receiving data and suspect a site change broke the visual labeling's reference to a specific element. Repairing adds a new definition to your labeled event, so the event maintains historical data for both definitions. To repair: (1) Click Repair. (2) Navigate to your site via the Visual Labeler and choose the correct definition for this event. *(The lesson includes a screenshot illustrating that a repair adds a new definition, including a new Element Hierarchy property value, below the old definition.)*

*For more information on how to leverage Autocapture and visual labeling, review Amplitude's documentation.*

*"Thanks for completing this course! You've reached the end of Getting Started with Autocapture and Visual Labeling. Click 'Next' to share your feedback on this course by completing a short survey."*

## Feedback (Part 3)

This part ends with a "We'd Love Your Feedback" survey lesson — navigational/administrative, not course content.

---

# Part 4: Data Governance and Maintenance Best Practices

**Type:** On-demand course | **Time commitment:** 20 minutes

## About This Course

Having ongoing practices to maintain your data health is critical for keeping your data clean, usable, and relevant for everyone in your organization. This responsibility typically falls to the data governor. Amplitude suggests that data governors take on the responsibilities of taxonomy education for new data consumers, while also establishing standards for instrumentation, and regularly auditing data health. This course offers tools and tactical practices for data governors to consider adopting in their organization.

**By the end of this course, you will be able to:**
- Begin designing a taxonomy onboarding session and a data dictionary to help with data education
- Incorporate practices that will lead to more consistent taxonomy instrumentation
- Leverage a data health checklist to audit your taxonomy on an ongoing basis

**You should take this course if:**
- You are a data governor or manager at your organization
- You have taken *Getting Started with Amplitude Data* and *Fundamentals of Data Taxonomy Design*

## Lesson 1 — The Data Creation Process (2 min)

Welcome to Data Governance and Maintenance Practices. Before we get started, let's review the steps of an ideal data creation cycle and identify who is involved at each step.

**[Video: "Data Governance and Maintenance Practices Intro", 2 min 05 sec]** — reviews the steps of an ideal data creation cycle and who is involved at each step. (No on-page transcript available.)

## Lesson 2 — Three Areas of Data Governance (5 min)

**Reflection: Data governance at your organization.** Amplitude recommends the individual or team responsible for data governance to own three closely-related areas of work: educating on the data taxonomy; setting and enforcing instrumentation standards; and maintaining data health.

*What activities do you or members of your team take that are related to each of these three areas of work? What are potential areas of improvement? Take a moment to reflect and then click the dropdown to see expert advice directly from Amplitude's Professional Services team.*

This lesson uses an interactive accordion with expert advice for each of the three areas:

**Scaling data taxonomy education.** When new data consumers get access to Amplitude, they will first need to learn the key event types, event properties, and user properties that correspond to your product's user actions and attributes. As a data governor, how can you help scale taxonomy education?

*Amplitude best practices:*
- **Create an easily accessible data dictionary** that defines your events and properties and indicates when they are triggered.
- **Run a taxonomy onboarding session** specific for new consumers of data. This might cover the event types and properties that correspond to critical user paths and funnels through your product and/or key metrics.
- **Design your taxonomy for usability.** When instrumenting new events and properties, make sure to adhere to a consistent syntax and style and use simple language. This will make it easier for new consumers of data to learn your events and properties.
- **Instill a cultural appreciation for data.** Find ways to celebrate and encourage data exploration throughout the broader organization. This might involve sharing success stories and spotlighting new users of data.
- **Build data trust** by communicating your processes and standards for data instrumentation. Even if not everyone in your organization will be instrumenting data themselves, they should be aware of how data comes into Amplitude, instrumentation standards, and the teams involved.

**Setting instrumentation standards.** As new features and products are developed, data governors should consider how new events and properties are instrumented. What processes might be put in place to help with continuous, consistent instrumentation?

- **Establish a data creation workflow** similar to the cycle introduced in the previous lesson. Consider which teams should be involved in determining what gets tracked and how.
- **Develop and enforce a consistent naming style and syntax.** Make sure that the standards for naming new event and property types are documented and communicated to all data implementers.
- **Add context to your events/properties in Amplitude Data** by including descriptions, categories, tags, to assist in taxonomy education.
- **Leverage branching and approvals in Amplitude Data** so your planned events and properties can be instrumented accurately.
- **Always make data validation part of the process.** Separate your development and production environments and make sure events and properties are triggering correctly using by using tools like Event Explorer and User Lookup.

**Maintaining data health.** When instrumentation is happening continuously across multiple teams, you may run into event volume issues or realize that some events are not being used regularly. Do you have a regular process for auditing your data health?

- **Review your events and properties at least quarterly.** Understand which event types have the most/least volume and which events are most/least queried.
- **Know when to hide, block, and delete events/properties** and establish a process for determining when to do each.

*In the next several sections, we will introduce resources and tips on how to put these practices in place using Amplitude.*

## Lesson 3 — Scaling Data Taxonomy Education (5 min)

**Your data onboarding checklist.** Amplitude recommends covering the following when running a taxonomy onboarding session for new data consumers:
- **Metrics** — What are the key metrics used across the organization, and how are they calculated?
- **Data sources and destinations** — Where does data come from (web, mobile, server-side, third-party integrations) and where does it flow to?
- **Critical events and paths** — What are the key events and user paths/funnels through the product that data consumers need to understand?
- **Key charts and analyses** — What are some example charts/analyses that showcase how to answer common business questions?
- **Finding help** — Who can new data consumers go to with questions (data governor, Slack channel, documentation, etc.)?

*Cross-reference course: "Iterating on a Data-Informed Culture" (featuring Patreon data leader Maura Church) — for more on scaling a data-informed culture across an organization.*

**Maintaining a data dictionary resource.** A data dictionary is a critical tool for scaling taxonomy education — it gives data consumers a self-serve reference for what events and properties mean. This lesson highlights three example formats:
- **Wiki** — e.g. Patreon's internal Dropbox Paper wiki, which provides extra context beyond a spreadsheet and documents quick-access use cases for common analyses.
- **Taxonomy spreadsheet** — a Google Sheet listing each event along with metadata columns such as Event Category and Event Description.
- **Amplitude Data** — event/property Description, Category, and Tags metadata entered directly in Amplitude Data, which is then surfaced in the chart builder and can be used for organizing and filtering the taxonomy.

**Learn your data taxonomy directly through Amplitude.** Beyond a separate data dictionary document, data consumers can also learn the taxonomy directly inside Amplitude using the Event Explorer tool. *Cross-reference video: "Use Event Explorer to Learn about Your Taxonomy."*

## Lesson 4 — Setting Instrumentation Standards (5 min)

As covered in the *Fundamentals of Data Taxonomy Design* and *Instrumenting Your Data Taxonomy* courses, maintaining a consistent process and set of standards during ongoing, iterative cycles of instrumentation is an important way to preserve data health and usability. Below are some practices you can consider putting in place during taxonomy instrumentation.

**Make instrumentation part of your product development cycle.** When a new feature or product is being developed, make sure teams take time to consider what new events or properties might need to be instrumented.
- Encourage teams to think about any new KPIs and business questions they need data to answer *ahead* of shipping the new feature.
- Data governors should document and socialize a process for nominating new events and properties. How does the decision get made and by whom?

**Maintain a descriptive and consistent syntax.** Your taxonomy is the language that users of data at your organization will leverage to build their analyses. Part of creating a usable taxonomy is using customer-centric, human-readable naming with consistent syntax.
- Data governors should establish and socialize a taxonomy style guide to all implementers of data. These style guidelines may also be denoted in the data dictionary or taxonomy planning document.
- Data governors should recommend anyone designing a taxonomy or instrumenting a new feature to review the course *Fundamentals of Data Taxonomy Design*.
- You can set event and property naming conventions directly in Amplitude. *(Illustrated with an animated screen-capture GIF, "Set Naming Conventions - with fade.gif", showing this workflow in the Amplitude Data UI.)*

**Make sure events include descriptions and categories.** As mentioned in the previous lesson, event descriptions and categories are surfaced in the chart builder, so your data users can find the events they're looking for quickly.
- Data governors may be involved in creating the categories and tags that show up in Amplitude.
- During the taxonomy planning phase, data governors should encourage implementers to include descriptions that specifically mention when the event is triggered.
- Event descriptions added in Amplitude Data can include rich text, images, code snippets and more. *(Illustrated with an animated screen-capture GIF, "Updating Event Description and Category.gif".)*

**Establish an engineering review process.** Once a team has planned new events and properties to be instrumented, either in Amplitude Data, or in another document, they should review their taxonomy with the engineer(s) who will be involved in the instrumentation.
- Data governors should help establish a 30-minute engineering review, in which the data implementer and taxonomy designers discuss the feasibility of the new events/properties. Make sure the team is prepared for compromises and adjustments.
- If taxonomy planning is undertaken in Amplitude Data, the comment feature below each event can help alert the appropriate team that it is time for an engineering review. Data governors should consider establishing practices on when/if conversations should take place using this feature. *(Illustrated with an animated screen-capture GIF, "Leaving a comment.gif".)*

**Establish a data validation process.** Data validation and QA testing should happen in a separate development environment, every time a new event or property is instrumented.
- Data governors should make sure data implementers — that is, the engineers involved in instrumentation — are aware of QA best practices.
- Data implementers should be recommended the *Instrumenting Your Data Taxonomy* course for specific QA tools and techniques.

## Lesson 5 — Auditing and Managing Your Data Health (3 min)

Regularly auditing the health of your data and taking care of issues in a timely manner can help maintain data quality and trust as your product evolves. When reviewing your data, the following checklist can be a useful tool to identify potential problems.

**Your data audit checklist.** Amplitude recommends auditing your data and addressing issues on at least a quarterly basis. During your audit, make note of the following:
- **Any events marked Invalid.** These events have data errors surfaced by Amplitude Data. You can investigate further by viewing the event's issue history. (Cross-reference: event statuses are covered in a lesson of the *Getting Started with Amplitude Data* course.)
- **Any events marked Unexpected.** These are events that have been ingested but are not in your Amplitude Data Tracking Plan.
- **Your project's instrumentation limits.** Amplitude has per-project instrumentation limits for event types, event properties, and user properties. How close are you to hitting these limits?
- **Your monthly event volume limit.** Your organization's monthly event volume limit varies according to your plan. Exceeding your event volume limit multiple times can result in your account being blocked — but Amplitude will alert you via email and through in-product notifications as you approach your limit.
- **Events with the most 30-day volume.** Are these events surprising? If an event is generating unusually high (or low) event volumes, it may be worth investigating in case this causes you to exceed your monthly event volume.
- **Events with the lowest 30-day queries.** What events are you ingesting that data users at your organization are not that interested in? The 30-Day Query volume offers insight into which events are leveraged most or least in analyses. You can investigate further by clicking into the event and viewing the "Used In" tab. Events with low or no 30-day queries may be candidates for hiding, blocking, or deletion.
- **Any duplicate events or properties.** If there are events or properties with similar names that only differ in syntax, double-check whether these data track the same user action or attribute. You may need to view the event/property descriptions and contact the creator of the events. If the events/properties are duplicated, you may be able to merge them into a single event.

**Leverage the Amplitude Data home screen.** The Amplitude Data home screen is purpose-built for data governors to get a quick, bird's-eye view of many of the issues outlined in the checklist above. Note that all of these items can also be surfaced in Amplitude Data by filtering the Tracking Plan and navigating to your project's Settings page — the home screen just serves to make this discovery easier. *(Illustrated with a screenshot, "data home screen 2.png", captioned "The Amplitude Data landing experience.")*

## Lesson 6 — Additional Resources (1 min, optional)

For additional resources related to the contents of this course, see the following:
- Getting Started with Amplitude Data
- Fundamentals of Data Taxonomy Design
- Instrumenting Your Data Taxonomy
- Iterating on a Data-Informed Culture
- Use Event Explorer to Learn About Your Taxonomy
- Verifying Your Instrumentation with Ampli

*"Thanks for taking this course! You've reached the end of Data Governance and Maintenance Practices. Please click 'Next' in the Academy lesson to complete the course and provide your feedback."*

## Feedback (Part 4)

This part ends with a "We'd Love Your Feedback" survey lesson — navigational/administrative, not course content.

---

# Part 5: Data Access Controls: Classify and Manage Access to Your Data

**Type:** On-demand course | **Time commitment:** 10 minutes

## About This Course

Amplitude administrators have the important task of balancing data accessibility with data security. With Amplitude's data access controls (DAC), Amplitude administrators can classify event and user properties and then create permission groups to manage exactly who can see the restricted data.

**By the end of this course, you will be able to:**
- Use the Amplitude UI to classify properties as PII, Sensitive, or Revenue
- Set up permission groups that grant data access to the right people at your organization
- State how DAC is enforced through the Amplitude product

**You should take this course if:**
- You are an Amplitude admin at your organization
- You have taken the Amplitude Admin Essentials course

## Lesson 1 — Data Access Controls (10 min)

Amplitude administrators have the important task of balancing data accessibility with data security. Teams should be able to view and analyze the data they need, but sensitive customer data should be appropriately protected in order to be compliant with privacy laws.

With Amplitude's data access controls (DAC), Amplitude administrators can classify event and user properties and then create permission groups to manage exactly who can see the restricted data.

*Note: Data Access Controls is available for free on select Amplitude plans.*

**Get started with DAC in three steps.** To leverage data access controls, first make sure you have admin privileges for your organization. This course will teach you how to classify data, set group-level permissions, and, finally, show you how DAC is enforced through the Amplitude product. *(Illustrated with an image, "three steps to DAC.png".)*

**Review user roles and permissions.** This course requires familiarity with Amplitude's admin role and other user roles, as well as permission groups. Referenced resources (shown as a button stack):
- **Take the Amplitude Admin Essentials course** — a short, interactive course on how to effectively administer Amplitude.
- **Understand Amplitude user roles** — documentation on what viewer, member, manager, and admin roles can accomplish in Amplitude.
- **Manage permissions at scale** — documentation on how to set up and use permission groups.

**Classify properties as PII, sensitive, or revenue.** Admins can classify user properties, event properties, and group properties into one of three restricted categories. This lesson uses an interactive tabbed component with the three category definitions:

- **Personally Identifiable Information (PII)** — Any data that can be used to identify someone. This includes data that can be used to directly identify an individual, as well as information that can be used in combination to identify an individual. *Examples of PII:* full name, physical address, health records and biometric data (e.g. fingerprints), driver's license number.
- **Revenue** — Sensitive business financial data that may be used for forecasting and reporting earnings.
- **Sensitive** — Any type of data that should not be broadly accessible to your Amplitude users, whether that is to maintain compliance with your data privacy laws or for other business reasons.

**Two ways to classify your data:**
- **Taxonomy API** — Programmatically classify your event properties, user properties, and group properties. This is best if you want to apply classifications in bulk. (See the Taxonomy API documentation for more information.)
- **Amplitude Data UI** — Navigate to each property individually and assign a classification through the Amplitude Data user interface. *This course covers only how to use DAC in the Amplitude Data UI.*

**Using Amplitude Data for data classification.** Let's take a look at how to assign a classification to a property using the Amplitude Data UI. *(You can enlarge each image by clicking on it.)* This lesson uses a 2-step "process" walkthrough with paired screenshots:

*Note: this step-by-step walkthrough contains an authoring placeholder ("Introduction"/"Summary" tab labels with Lorem-ipsum filler text — "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In purus velit, tincidunt ac nibh quis, sollicitudin varius libero. Nullam at mi felis. Donec a scelerisque augue, sit amet porttitor nibh. Suspendisse at lorem ut elit placerat blandit." — reproduced here verbatim as found in the source, per instructions to omit nothing.)*

1. **Navigate to your project's properties.** *(Screenshot: "Classify Step 1.png")* Make sure you are in the correct project and then navigate to the Properties table of Amplitude Data. To see what properties have already been classified, you can select to view the Classification column.
2. **Select the property and choose the classification.** *(Screenshot: "Classify Step 2.png")* Select a property to classify, but note that you cannot classify a property marked as Unexpected. Once you select your property, check the correct classification in the Classification dropdown. Note that a single property can be classified into multiple categories (for example, PII *and* sensitive).

After your data has been classified, it is time to make sure only the right groups of people have access to this restricted information. We can do this using permission groups in Amplitude.

**Set group-level permissions.** With Amplitude's permission groups, you can assign a group of Amplitude users the same level of project access (as a viewer, member, manager, or admin) and data access (PII, sensitive, and/or revenue) for one or more projects. Example walkthrough: creating a new group of users who have manager-level access to the AmpliShop project *and* can access all properties classified as sensitive. *(You can enlarge each image by clicking on it.)* This lesson uses a 4-step walkthrough, each paired with an animated screen-capture GIF:

1. **Navigate to Members & Groups settings.** *(GIF: "Permission Groups Step 1 - Navigate to Groups.gif")* You can manage permissions for users and groups in your organization settings. Note that you must be an admin to manage groups.
2. **Create a new group.** *(GIF: "Permission Groups Step 2 - New Group.gif")* In the Groups tab, click to add a new group. For easy management, be sure to give the group a name and/or description that makes it clear what the project and data access level is for that group.
3. **Set project access.** *(GIF: "Permission Groups Step 3 - Project Access.gif")* Assign this group manager-level access for AmpliShop by first selecting the AmpliShop project, and then changing the project role to manager.
4. **Set data access.** *(GIF: "Permission Groups Step 3 - Data Access.gif")* In the Data Access tab, assign access to sensitive data for this group, but continue to restrict access to PII and revenue data.
5. **Add members to the group.** *(GIF: "Permission Groups Step 4 - Add Members.gif")* Add users to the group by navigating to the Members tab and then click Save to save the group. If you do not see the user(s) you want in the drop down, you may have to first invite them as a new user.

**Understanding group vs. individual user permissions.** Users can be assigned roles individually or through a group. This means that the same user could potentially be assigned different permission levels. In this case, Amplitude will treat the user according to the *highest* level of permission they have. (Cross-reference: "example scenarios" in Amplitude's documentation on assigning user permissions.)

**Revoking data access.** In order to revoke or change access to PII, revenue, or sensitive data, you must remove the user from the appropriate permission group.

**View your DAC settings in one place.** As an Amplitude administrator, it can be useful to get a quick overview of your classifications in a central location. The DAC admin panel allows you to see how many users and groups have access to restricted data and how many properties have been classified per project. This lesson uses a labeled-graphic diagram ("DAC admin panel.png") with 3 numbered hotspots:

- **01 — DAC admin panel.** You can get a high-level overview of your data access controls settings by navigating to your organization settings.
- **02 — Groups and users with data access.** In this example, there are four permission groups and 190 individual users that have been granted access to data classified as Revenue.
- **03 — Properties that are restricted.** Event properties, user properties, and group properties can be classified into one of three restricted categories. In this example, 2 event properties have been classified as PII, 1 event property as Revenue, and 1 user property as Sensitive. These four properties can be considered "restricted" — analytics end-users who do not have the right data access will be blocked from viewing or using this data.

**How Amplitude enforces DAC in the UI.** What happens when an analytics end-user tries to access restricted data that they do not have permissions for in the Amplitude user interface? Be assured that these users will not be able to create or view any analyses with this data. This lesson illustrates each enforcement point with a screenshot:

- **Charts cannot be created with restricted data.** *(Screenshot: "Restricted properties in dropdown.png")* If a user does not have appropriate data access to a property, it will be labeled as *restricted* and cannot be selected in an analysis.
- **Charts with restricted data cannot be viewed.** *(Screenshot: "Chart with PII.png")* If a user does not have appropriate access to data used in a chart, they will be blocked from viewing the chart. They will also be provided details on which restricted property (or cohort) used in the analysis caused the chart to be blocked.
- **Dashboards, Notebooks, Spaces containing charts with restricted data can be viewed; *only* the charts containing restricted data will be blocked.** *(Screenshot: "Dashboard with PII Charts.png")* If a Dashboard, Notebook, and/or Space contains charts with restricted data, only that chart will be blocked from being viewed. For ease of collaboration and presentation, the rest of the content in a Dashboard, Notebook, or Space can be viewed.
- **Restricted properties cannot be viewed in User Profiles or Event Streams.** *(Screenshot: "Event Stream with restricted data.png")* If a user does not have appropriate data access to a property, that property will be labeled restricted in event streams and user profiles.
- **Cohorts built with restricted data cannot be viewed.** *(Screenshot: "Cohort with restricted data.png")* If a user does not have appropriate data access to the properties used in a cohort definition, they will not be able to preview the users of that cohort *or* see the size of the cohort.
- **Derived properties created with restricted properties cannot be used.** Derived properties inherit the classification of their underlying properties. Thus, users who do not have data access to a property will be restricted from using *and* creating derived properties that use that property.

**How Amplitude enforces DAC in exports.** DAC enforcement further extends to data that can be exported from Amplitude. In general, a user who does not have permissions for accessing restricted data will *not* be able to view this data in any kind of Amplitude export. This lesson illustrates with a 2-column gallery of screenshots:

- **Restricted user properties will be excluded in user downloads.** *(Screenshot: "Microscope Download Users.png")* If a user tries to perform Download Users via Microscope in a chart, the CSV export will exclude all properties they don't have access to.
- **Charts with restricted data will be excluded in Dashboard exports.** *(Screenshot: "Dashboard CSV Export.png")* If a user tries to perform Download chart CSVs from a Dashboard, the CSV export will exclude all charts they don't have access to.
- **Charts with restricted data cannot be viewed in Dashboard PDF/PNG exports.** *(Screenshots: "Dashboard PDF PNG Export.png" and a second "Dashboard with PII Charts.png")* If a user tries to perform Export > PNG or Export > PDF from a Dashboard, the PNG or PDF file will not show the charts they don't have access to.

**Test your knowledge.** Take the quiz on the next page to test your understanding of leveraging DAC in Amplitude.

*"Click 'Next' to continue to the next lesson. Click the 'Replay' button to restart this lesson."*

## Lesson 2 — Knowledge Check

**Result on file:** Passed — 4 of 4 correct (100%). Elapsed time: 1 minute.

This quiz's "Show Answers" view visually marks each option with a checkbox (checked/bolded/green = correct/selected; unchecked/greyed/struck-through = incorrect), which is reproduced below along with the per-question Feedback text where shown.

1. **True or False: When an Amplitude Dashboard contains a chart with restricted data, a user will be blocked from viewing the entire Dashboard unless they have access to that data.**
   - ☑ **False** *(correct)*
   - ☐ True

2. **Suppose Mary is in a permission group that grants manager-level project permissions and data access to PII, revenue, and sensitive data. You now want to revoke Mary's access to all restricted data. Which of the following actions should you take? Choose the best answer.**
   - ☐ Individually assign Mary member-level project permissions.
   - ☐ Remove Mary from your organization.
   - ☑ **Remove Mary from this permission group.** *(correct)*
   - *Feedback: Correct. The only way to revoke or adjust an individual's data access is to remove them from the permission group that grants them that access.*

3. **True or False: A user who does not have the right data access to a certain event property will not be able to select this event property when building a chart.**
   - ☑ **True** *(correct)*
   - ☐ False
   - *Feedback: A user will not be able to select restricted properties in the chart builder.*

4. **In order to classify data as PII, revenue, or sensitive, you must hold which user role in your organization?**
   - ☑ **admin** *(correct)*
   - ☐ manager
   - ☐ member

## Feedback (Part 5)

This part ends with a "We'd Love Your Feedback" survey lesson — navigational/administrative, not course content.

---

# Final Assessment: Essentials of Data Management

Take this assessment to check your understanding of taxonomy design, instrumentation, and data management best practices.

## Essentials of Data Management - Assessment (Quiz)

**Result on file:** Passed — 9 of 11 correct (81%). Elapsed time: 14 minutes.

This quiz's "Show Answers" view visually marks each option with a checkbox. For a correctly-answered question, the selected/correct option(s) appear checked, bolded, and green, while incorrect distractors appear unchecked and greyed/struck-through. For an *incorrectly*-answered question, the option(s) the quiz-taker actually selected but which were wrong appear checked with grey strikethrough text, while the true correct option(s) appear in green bold — even when unchecked (i.e., not selected). This distinction is reproduced below via `*(selected)*` and `*(correct)*` annotations.

1. **Assume you are designing a data taxonomy for AmpliChat, a B2B workplace instant messaging application similar to Slack and Microsoft Teams. Your business is currently focused on building a great free plan, with hopes of eventually converting free-plan customers to a paid enterprise plan. Which of the following describes the *best* strategy for tracking events and properties during your initial Amplitude implementation?**
   - I. Track events that correspond to users getting value out of your free product, like sending messages, uploading files, and creating channels.
   - II. Track events that correspond to users moving through your plan upgrade process, like interacting with the pricing page and submitting their credit card information.
   - III. Track events that correspond to every button click a user can perform within your product to make sure you'll have a thorough initial implementation.
   - IV. Track events that correspond to your product's onboarding flow, but don't track any user or event properties during your initial implementation.

   - ☐ I, III, IV
   - ☐ I, II, IV
   - ☑ **I, II** *(correct)*
   - ☐ I, III

2. **Assume you are instrumenting events for AmpliFlix, a media streaming platform similar to Netflix. Which of the following is an example of an event property you would need to instrument in order to answer the following question: In the last 30 days, which TV series was streamed most frequently?**
   - ☐ Episode Started — triggers when a user begins watching an episode
   - ☐ episodes_watched — stores the total number of episodes watched by a user
   - ☑ **series_title — stores the title of the TV series an episode belongs to** *(correct)*
   - ☐ Episode Ended — triggers when a user finishes or exits an episode

3. **Assume you are instrumenting events for an ecommerce site. Your business measures customer retention by looking at the proportion of users who return to make a repeat purchase within 30 days of their first purchase. Which of the following data types would you need to instrument to answer the following question: How does the retention of users who are 18-30 years old compare to that of users who are 31-45 years old? Select all that apply.**
   - ☑ **age_group — a user property that stores the age group of the user** *(correct)*
   - ☑ **Purchase Completed — an event that triggers after the user submits the order** *(correct)*
   - ☐ purchase_value — an event property that stores the total dollar value of the order
   - ☐ Cart Updated — an event that triggers after the user adds an item to the cart

4. **Your team has recently launched a community forum for your business. An important engagement metric that your team needs to report on is month-over-month growth — that is, the percentage increase in the number of new users that join the community each month. Based on Amplitude's data taxonomy design guidelines, what is the best name for the event you'll instrument to track new community sign-ups?**
   - ☐ New User Sign-up
   - ☐ Sign-up Button Clicked
   - ☑ **Community Joined** *(correct)*
   - ☐ Top Nav: joinButton

5. **The following is part of your business's data dictionary, which lists out the events and properties you are tracking along with their descriptions. The event and event properties enclosed by the black boxes correctly follow the taxonomy design conventions set by your team. With this in mind, how should the other event and property names be corrected? Select all that apply.**

   The lesson displays this as a screenshot of a data-dictionary table ("DM LP assessment - data dictionary example.png"), reproduced below as a Markdown table. Rows/cells outlined with a bold black box in the source (denoting names that already follow the team's taxonomy conventions) are marked *(boxed = follows convention)*:

   | Event Name | Trigger + Event Description | Event Property Name | Property Description |
   |---|---|---|---|
   | account_verified | When the user verifies their account | verification method | Method used to verify the account |
   | **Onboarding Step Completed** *(boxed = follows convention)* | Triggers when the user completes an onboarding step | **onboarding step** *(boxed = follows convention)* | The onboarding step the user has completed |
   | *(same event, cont'd)* | *(same trigger, cont'd)* | total genres favorited | At the favorite genres step, how many genres did the user favorite? |
   | *(same event, cont'd)* | *(same trigger, cont'd)* | **genres favorited** *(boxed = follows convention)* | What genres did the user favorite? |
   | Onboarding Completed | Triggers when the user completes all onboarding successfully | N/A | N/A |
   | Skipped onboarding | Triggers when the user clicks "Skip" to skip the onboarding experience | Last Onboarding Step | At which step did the user click to skip onboarding |
   | browse viewed | Triggers when the user views the main browse page | total titles shown | How much personalized content was the user shown? |
   | search completed | Triggers when the user performs a search | number of search results | Number of search results returned |
   | *(same event, cont'd)* | *(same trigger, cont'd)* | keywords | Keywords the user used |

   Answer options:
   - ☑ **The event property 'Last Onboarding Step' should be renamed 'last onboarding step'** *(correct — should match the lowercase, spaced convention used by "onboarding step" and "genres favorited")*
   - ☑ **The event 'account_verified' should be renamed Account Verified** *(correct — should match the Title Case, spaced convention used by "Onboarding Step Completed")*
   - ☐ The event 'search completed' should be renamed as 'Completed Search'
   - ☐ The event property 'total titles shown' should be renamed 'total_titles_shown'

6. **Amplitude leverages a system of three identifiers to resolve anonymous users — the device ID, the user ID, and the Amplitude ID. Which of the following statements are true about the User ID?**
   - I. User IDs are helpful in identifying a unique user.
   - II. User IDs are automatically generated by Amplitude.
   - III. User IDs should not be assigned to users who are not signed in.
   - IV. User IDs must be set to a value that can be changed later.

   - ☐ I, II
   - ☑ **I, III** *(correct)*
   - ☐ I, III, IV
   - ☐ I, II, III

7. **Let's say you are setting up a new Amplitude implementation for a music streaming application called AmpliTunes. Your current setup assigns a random numerical user ID to an anonymous user who uses your web application. Once this anonymous user logs into AmpliTunes and can be identified by Amplitude, they are assigned a *different* numerical user ID. Which of the following happens as a result?** — *(quiz-taker's answer was marked incorrect)*
   - ☐ Amplitude will assign this user the same Amplitude ID regardless of whether they are anonymous or logged in.
   - ☑ Amplitude will use this user's unique device ID to generate a merged Amplitude ID. *(selected — marked incorrect)*
   - ☐ **Amplitude will count this user as two different users, resulting in an inflated unique user count.** *(correct)*
   - ☐ Amplitude can merge this user's two different user IDs into a single user ID.
   - *Feedback: Because this user has been assigned two different user IDs (one before authentication and one after), this will result in the same user having two different Amplitude IDs, resulting in Amplitude counting this user as two unique users. For this reason, it is critical that users who are anonymous in your product are not assigned user IDs.*

8. **Which of the following methods can help you validate and debug your taxonomy instrumentation? Select all that apply.**
   - ☑ **Leverage automatic event validation with Amplitude Data.** *(correct)*
   - ☑ **Analyze your own event stream in Amplitude.** *(correct)*
   - ☐ Use auto-tracking for simple and accurate instrumentation.
   - ☑ **Use a separate development project for debugging.** *(correct)*

9. **Which of the following could be an important tactic for scaling data education at your organization?**
   - ☐ Limiting access to your data platform so new data users don't misinterpret your analyses.
   - ☐ Creating a Slack channel where data analysts answer other teams' business questions.
   - ☑ **Hosting an onboarding session that introduces new data users to your taxonomy and analytics platform.** *(correct)*
   - ☐ Siloing instrumentation to the data engineering team to limit bugs.

10. **Which of the following should you consider investigating on an ongoing basis to audit the health of your data? Select all that apply.** — *(quiz-taker's answer was marked incorrect)*
    - ☑ Events with the lowest 30-day volumes *(selected, shown in green)*
    - ☐ Events with the lowest 30-day queries *(unselected, shown in neutral/default color — not marked green)*
    - ☑ Events or properties that are being flagged as unexpected, invalid, or as having some other issue *(selected, shown in green)*
    - ☑ Your monthly event volume *(selected, shown in green)*

    *Note on this question: despite the header being marked "✖ Incorrect answer," all three selected options are rendered in the same green/checked styling normally used for correct answers, and none of the four options are shown with the strikethrough styling used elsewhere for wrong selections — so the screen does not visually indicate which specific option was mismarked. Based on the "Auditing and Managing Your Data Health" lesson content earlier in this learning path (Part 4, Lesson 5), the checklist explicitly names "events with the **lowest 30-day queries**" (not "lowest 30-day volumes") as one of the items to review — suggesting the intended correct combination is likely "lowest 30-day queries," "flagged events," and "monthly event volume," with "lowest 30-day volumes" being the distractor. This is offered as an inference from course content, not a definitive reveal from the quiz UI.*

11. **What ongoing processes should a data governor or data leader establish in order to make sure good instrumentation and design standards are maintained during rapid, iterative cycles of product development? Select all that apply.**
    - ☐ A process for creating new projects and workspaces as needed
    - ☑ **A process for reviewing the technical feasibility of a new event or property to be instrumented with engineers** *(correct)*
    - ☑ **A process for nominating new events and properties to be added to the taxonomy** *(correct)*
    - ☑ **A process for validating and debugging new data** *(correct)*

## Conclusion

If you did not successfully complete the assessment, feel free to retake it as many times as you need. You may find it helpful to review the content of the lessons in this path before attempting the assessment again, but that is not required.

If you did successfully complete the assessment, congratulations! Look for an email from "Amplitude via Credly" for instructions on how to accept your badge.

*"Click 'Next' to submit your feedback, or choose from one of the options below."* (Options shown: "Earn your next badge", "Find your next course".)

## Feedback (Final Assessment)

This ends with a "We'd love your feedback!" survey lesson — navigational/administrative, not course content.

---

## Summary / Explanation (Essentials of Data Management — Full Learning Path)

This five-part learning path takes a data taxonomy through its entire lifecycle. **Part 1 (Fundamentals of Data Taxonomy Design)** establishes the vocabulary and design principles — what to track, how to name events/properties consistently, and how to avoid taxonomies that are too general or too specific. **Part 2 (Instrumenting Your Data Taxonomy)** turns that design into working instrumentation — how data reaches Amplitude, how anonymous users are resolved into identified users via the three-identifier system (device ID, user ID, Amplitude ID), and how to validate that instrumentation is firing correctly. **Part 3 (Getting Started with Autocapture and Visual Labeling)** offers a faster, lower-engineering-effort alternative/complement to precision tracking for click events, plus how to maintain labeled events over time (replace vs. repair). **Part 4 (Data Governance and Maintenance Best Practices)** zooms out to the ongoing operational discipline required to keep a taxonomy healthy at scale — educating new data consumers, standardizing the instrumentation process, and running a recurring data-health audit. **Part 5 (Data Access Controls)** addresses the security/compliance dimension: classifying properties as PII, Revenue, or Sensitive, and using permission groups to control exactly who can see restricted data, with enforcement spanning charts, dashboards, cohorts, derived properties, and exports. The final Assessment ties all five parts together, testing taxonomy-design judgment (Q1, Q4, Q5), instrumentation/identifier concepts (Q2, Q3, Q6, Q7), validation practices (Q8), and governance/data-health practices (Q9, Q10, Q11) — the 9-of-11 result on file shows the taxonomy-design and instrumentation fundamentals were solid, with the two misses both landing on nuanced identifier-merging behavior (Q7) and the specific wording of the data-health checklist (Q10).
