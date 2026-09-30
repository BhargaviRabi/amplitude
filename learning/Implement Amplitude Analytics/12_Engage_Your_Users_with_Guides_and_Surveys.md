# Engage Your Users with Guides and Surveys

**Type:** On-demand course | **Time commitment:** 30 minutes

---

## About This Course

Do you want to drive adoption, increase engagement, and collect valuable insights without disrupting the user experience?

In this course, you'll learn to use Amplitude's Guides and Surveys to build and launch targeted messaging that guides users, encourages feature adoption, and collects valuable feedback.

Whether you're designing a product tour, onboarding flow, or customer feedback survey, this course provides you with the tools and best practices to create effective and user-friendly in-product experiences.

**By the end of this course, you'll be able to:**
- Identify the key functions of Guides and Surveys and how they support the user experience
- Create and launch engaging, well-structured guides and surveys
- Leverage targeting and behavioral insights to ensure the right users see the right message at the right time
- Develop an effective content strategy for Guides and Surveys that engages users at the right moment to drive adoption and support long-term retention

**You should take this course if:**
- You want to learn more about engaging users in your product.
- You have taken the *Create, Analyze, and Activate User Groups with Behavioral Cohorts* course.

---

## Section: Introduction

### Lesson 1 — Overview of Amplitude's Guides and Surveys (3 min)

Amplitude's Guides and Surveys enable teams to deliver in-product messages, walkthroughs, and feedback requests. Whether you're a product manager, marketer, or growth professional, Guides and Surveys help you guide users, drive adoption, and gather valuable insights.

**[Video: "Engage Your Users with Guides and Surveys", 1 min 45 sec, Amplitude Academy / Wistia]** — an overview of Guides and Surveys. (No on-page transcript available.)

**Also Available: The Resource Center (optional).** Guides and Surveys also include the Resource Center. While not covered in depth in this course, the Resource Center is a complementary feature designed for persistent, in-product support. If you're interested in offering centralized guidance alongside your targeted guides and surveys, explore the course *Deliver Targeted Guidance and Support with a Resource Center*.

In this course, you'll learn to use Guides and Surveys, see examples, and pick up tips for engaging users.

## Section: Explore the Guides and Surveys Interface

### Lesson 2 — Build: Create Your Content (5 min)

The Guides and Surveys interface is divided into three main sections that each play a crucial role in building, targeting, and analyzing your content. This lesson uses an interactive tabbed overview of the three sections:

- **Build** — Create your content. Use Amplitude's responsive Guides and Surveys builder interface to customize the content, design, and flow of your guide or survey.
- **Setup** — Target your users. Define who will see your guide or survey, where it will appear, and when it should trigger.
- **Insights** — Analyze the results. View out-of-the-box analytics to evaluate the performance of your guides and surveys and drive meaningful action.

**Build: Create your content.** The builder interface is the responsive workspace where you'll create the content of your guide or survey. It includes customizable settings that let you tailor the experience to your business needs. This lesson uses a numbered, hotspot-based labeled-graphic diagram of the builder interface — each hotspot is reproduced below:

1. **Application type** — This icon shows the type of application the guide is built for. If your project has multiple application types enabled, you can choose which one to use when creating a new guide or survey.
2. **Form factor** — Select your guide's form factor, or the layout style for how the guide appears. All templates and blank guides include the following form factors:
   - **Modal**: A large, centered pop-up with a background mask to draw the user's attention.
   - **Popover**: A less intrusive alternative to modals that you can position in a corner of the screen.
   - **Pin**: Pins are attached to a specific interface element. Pins are ideal for product tours, announcements, or surveys that guide users through sequential steps.
   You can access and use additional specialty form factors through the corresponding template; these include **banners**, **checklists**, and **tooltips**.
3. **Content formatting options** — Guides and Surveys support customizable free-text content with various formatting options. You can apply bold, italics, emojis, bulleted and numbered lists, and hyperlinks.
4. **Add block** — Add blocks to your guide or survey:
   - **Buttons**: Navigate steps, link to URL, interact with UI elements, trigger actions, or show another guide/survey.
   - **Images & Videos**: Make your message more engaging with visuals.
   *Note: Surveys include additional user input block options.*
5. **Add another step** — You can build multistep tours, announcements, and surveys. Choose a modal, popover, or pin form factor for each new step.
6. **Visualizing your content** — View a responsive, visual preview of your guide. *Note: To preview in your product, use the Preview button at the top of the screen.*
7. **Edit Theme** — Select Edit Theme to adjust the design of your guide. Choose a pre-created theme or create a custom one.
8. **Form factor positioning** — Position your selected form factor. Modals are centered by default, but you can adjust the placement of a popover or set a target in your interface for a pin.
9. **Form factor: more options** — Use this menu to customize the settings for an individual step in your guide or survey. Options include layout and formatting, animation, and visibility controls. The available settings vary depending on the form factor selected (modal, popover, or pin).
10. **Settings** — Additional guide settings include:
    - **Searchable**: Makes the guide discoverable in other areas of Amplitude, including the Resource Center.
    - **Dismissible**: Lets users close the guide at any time.
    - **Snooze**: Lets users temporarily dismiss the guide, with customizable snooze duration options.
    - **Show all steps**: Displays the total number of steps for guides with multiple steps.
11. **Experiment** — You can dynamically generate an A/B test or multi-armed bandits to test which user engagements are most effective. (Cross-reference course: *Getting Started with Amplitude Guides and Surveys Experimentation*.)
12. **Preview, Publish, and Save** — Use these buttons to manage your guide or survey:
    - **Preview**: Enter your product URL to preview the guide or survey in your interface.
    - **Draft**: Save as a draft, publish, test, or schedule a future publication.
    - **Save**: Save changes to your guide or survey. Some settings require saving before they take effect.
    - **More Options**: After saving, additional actions become available. You can duplicate a guide, share a link, view version history, or create a template.

**Guides and Surveys for mobile applications (optional).** While the examples in this course focus on guides and surveys built for web applications, you can use Guides and Surveys for mobile applications. To enable Guides and Surveys in a mobile app, install the mobile SDK (iOS SDK referenced; requires iOS 15+, Swift 5.9+, Amplitude iOS Swift SDK 1.13.0+) and then enable the apps you want to support at the project level. Refer to the Amplitude Documentation for further support instrumenting Guides and Surveys for your mobile application.

**Choose the right template.** When you create a new guide or survey, you'll notice the option to begin from a template. These templates are a great starting point, especially if you're new to building in-product engagement, because they offer suggested form factors and blocks to help effectively structure your guide or survey. This lesson uses an expandable-row list of templates:

**Guide Templates:**
- **Announcement** — A large message that communicates important information. Common use cases: announcing upcoming events like webinars or conferences; notifying users about scheduled maintenance or downtime; encouraging users to take action (e.g., upgrading their plan or enabling a feature); communicating account-related updates (e.g., payment issues, usage limits exceeded). By default, the announcement template includes a modal form factor, so the message will display in the center of your interface with a mask.
- **Banner** — A full-width, persistent message displayed at the top or bottom of the interface. Common use cases: delivering important but less intrusive announcements; providing alerts for scheduled maintenance or downtime; highlighting account-related updates like overdue payments; sharing one-time messages for major updates or promotions.
- **Product Tour** — A multi-step, interactive walkthrough that guides users through a feature or process. Common use cases: onboarding new users with a step-by-step guide; helping users navigate a new or updated interface; proactively guiding users through critical workflows; responding to common "How do I do X?" questions. The tour template begins with a modal form factor that will display in the center of the screen and then includes pins you can use to anchor to critical sections of your interface.
- **Tooltip** — A persistent, hover-based message that provides extra context or quick tips. Common use cases: offering explanatory information about a button, feature, or setting; reducing confusion without interrupting the user's workflow. Tooltips can appear on hover or click, so choose what best suits your users. Anchoring a tooltip works in your product/application the same way as a pin anchor.
- **Checklist** — A step-by-step progress tracker that guides users through onboarding or product activation. Common use cases: onboarding new users; guiding users through feature activation; encouraging engagement by breaking tasks into small, achievable steps.

**Survey Templates:**
- **User feedback survey (free-form)** — A text-based survey where users can provide open-ended feedback. Common use cases: capturing qualitative insights about user experiences; collecting feedback on why users are confused.
- **Rating survey** — A quick-response survey using stars, numbers, or emojis to measure user sentiment. Common use cases: gathering fast, quantitative feedback on a feature or experience; measuring user satisfaction in a lightweight way.
- **NPS survey** — A Net Promoter Score (NPS) survey asks users to rate their likelihood of recommending a product on a 0-10 scale. Common use cases: measuring overall customer happiness and loyalty; tracking user satisfaction over time. *Important: You'll want to be mindful of survey placement. For example, if you trigger an NPS survey for users who appear confused, the ratings may be lower than a representative sample.*
- **Banner survey** — Display a rating or NPS survey as a full-width, persistent survey at the top or bottom of the interface. Common use cases: measuring overall customer satisfaction in a lightweight, persistent format; collecting feedback on a feature or experience without disrupting the user journey.
- **Tooltip survey** — Display a rating survey as a tooltip anchored to a specific element in your product interface. Common use cases: collecting feedback on new features; measuring satisfaction with a specific workflow or task; asking quick usability questions at key points in the interface.

*Note: You can save any guide or survey you create as a reusable template. This helps you maintain consistency and save time.*

Each template is designed for a specific purpose, whether informing users, guiding them through a process, or collecting feedback, but they also allow for customization. You can adjust the settings to fit your unique needs.

**A guide or a survey?** This lesson includes a comparison table:

| Guides | Surveys |
|---|---|
| Informational messages that provide instructions or insights | Interactive messages that include block options that collect **user input** |
| **Use a guide to:** communicate an important update; walk users through a process; provide additional context or tooltips; highlight key actions users should take | **Use a survey to:** gather feedback; measure user satisfaction; collect insights about a feature or experience |
| **Examples:** Announcements, product tours, tooltips, and banners | **Examples:** Rating scales, NPS surveys, and free-text feedback forms |

Before you start building, ask yourself: **Do I want user input?** If yes, a survey is likely the best tool. If not, a guide is likely the better choice.

After building your content in the builder interface, you'll use the Setup tab to strategically target the right users at the right time.

### Lesson 3 — Setup: Target Your Users (3 min)

Generic, untargeted pop-ups can disrupt the user experience and create friction rather than engagement. Therefore, strategically targeting your users is critical to the success of your guides and surveys. This lesson uses a 3-tab component covering three questions to ask when implementing strategic, intentional targeting:

- **WHO?** — Who are the users for whom the guide is relevant?
- **WHERE?** — What page or place in your product is the guide relevant?
- **WHEN?** — When do you want to show the guide in the context of the user's session?

The *Setup* tab in Guides and Surveys helps you target the right users based on who they are, where they are, and what they need. This lesson uses a hotspot diagram of the Setup tab — each hotspot is reproduced below:

- **Targeting** — Choose whether your guide or survey will be shown to all users or a specific audience. In most cases, leveraging Amplitude's cohorts is the best way to strategically target the right users. *Note: Cohort membership is not instantaneous. Allow time for users to enter a cohort before expecting them to see your guide or survey.*
- **User segments** — Create a targeted user segment by filtering by user properties or selecting an existing cohort. If you need a new cohort, select *Create Cohort* to define a custom audience.
- **Trigger: When** — Select criteria for when this experience will appear, such as after a fixed time interval, after another element appears, or when another event is tracked. Smart triggers detect when Amplitude identifies task completion, rage, or confusion.
- **Trigger: Where** — Choose *Any page* or *On specific pages* to include or exclude specific URLs. URL options: match exact URLs, patterns, contains, starts with, ends with, or regex. *Temporarily hide if*: Prevents an in-progress guide or survey from reappearing on irrelevant pages.
- **Priority** — Set the priority for your guide. When multiple guides or surveys qualify to appear, the one with the highest priority displays first.
- **Limits** — You can stop showing a guide or survey once a user has completed all steps. If you choose not to stop showing the guide when dismissed, you can set a cooldown period to delay when it reappears, which prevents it from displaying too frequently.
- **Localization** — Display guides and surveys in multiple languages without creating separate versions. Use *Manage languages* to open project-level settings, where you can enable localization, choose a default language, define available languages, and set fallback behavior.
- **Test users** — Use this option to test your guide or survey in a live environment before publishing. Add specific users or cohorts as testers to see exactly how the content will appear. Only those test users will be able to view the guide or survey while it is in testing mode.

After you've completed the targeting, you're ready to save and publish your guide or survey. Once published, insights will start to accumulate, and you can begin to analyze the impact.

### Lesson 4 — Insights: View Your Results (2 min)

**Out-of-the-box insights.** Once your guide or survey is published, you can view out-of-the-box analytics and start tracking engagement.

- **Guide-Specific Insights** — View detailed performance metrics for an individual guide from its *Insights* tab.
- **Guides and Surveys Overview** — Use the *Overview* section to track the overall performance of all your project's guides and surveys and identify trends over time.

**Interested in deeper analysis?** For advanced reporting, use Amplitude's analytics tools to build custom charts and dashboards to further measure the impact of your guides and surveys. Since guides and surveys automatically trigger events when users interact with them, you can segment by these events or analyze them in charts, just like any other event in Amplitude.
- **As Events:** Treat them like any other event in Amplitude. For example, you can filter by users who have viewed, completed, or dismissed a guide or survey.
- **As User Properties:** Use them to segment users based on whether they have interacted with a specific guide or survey.

## Section: Use Cases

### Lesson 5 — Use Case: Accelerate Onboarding and Adoption (6 min)

Now that you're familiar with the core features of Guides and Surveys, let's explore key use cases that demonstrate their impact.

**[Video: "Use Case: Accelerate Onboarding and Adoption", 5 min 00 sec]** — demonstrates using a guide to accelerate onboarding and adoption. (No on-page transcript available.)

### Lesson 6 — Use Case: Prevent Churn with Personalized Support (4 min)

**[Video: "Use Case: Prevent Churn with Personalized Support", 3 min 35 sec]** — demonstrates using a survey to gather user input to enable personalized support and help reduce churn. (No on-page transcript available.)

## Section: Optimize Your Guides and Surveys Strategy

### Lesson 7 — Develop an Effective Content Strategy (7 min)

An individual guide or survey can drive engagement, but you'll likely find your messages are most effective when part of a larger, well-planned strategy. An effective Guides and Surveys content strategy requires strategic targeting and a series of well-timed interactions that align with your user's journey with your product or brand.

**Product adoption funnel.** The product adoption funnel is a useful framework for considering your user's journey. This model represents how users move from discovering your product or feature to becoming engaged, loyal customers. This lesson uses a hotspot diagram of the four-stage funnel — each stage is reproduced below:

- **Awareness** — Users are just discovering your product or brand. The goal is to introduce it in a way that highlights its benefits and relevance.
  - *Marketing Focus:* Users are exploring solutions and learning about your brand or product for the first time. Messaging should introduce value in a compelling, high-level way.
  - *Product Focus:* Users encounter your product or a new feature in-app. The goal is to highlight its relevance and benefits through in-product messaging.
- **Consideration** — Users have discovered the product or feature, but they haven't fully engaged with it yet. The goal is to encourage them to take meaningful action.
  - *Marketing Focus:* Users are evaluating whether the product is the right fit. They may be comparing options, reading case studies, or exploring benefits.
  - *Product Focus:* Users need contextual guides to engage, such as trying a feature, signing up for a trial, or completing a key setup step.
- **Conversion** — Users have engaged with the product or feature, but they may still need reinforcement to make it a habit or upgrade to a paid plan.
  - *Marketing Focus:* Users are primed to take the next step, such as purchasing, upgrading, or committing to the product. Messaging should highlight urgency and reinforce value.
  - *Product Focus:* Users are interacting more but may need additional encouragement to reach an "aha" moment where they see the full benefit.
- **Retention** — Even after users adopt your product or feature, continued engagement requires reinforcement. Without ongoing interaction, users may disengage or churn.
  - *Marketing Focus:* Users need continued engagement to stay loyal and expand their use of the product through upsells or advocacy.
  - *Product Focus:* The goal is to drive long-term adoption, encourage feature discovery, and prevent churn by reinforcing value over time.

Instead of taking a one-size-fits-all approach, both product and marketing teams can align their guides and surveys with the key adoption stages.

**Let's Look at an Example.** *"I'm a Product Manager focused on monetization. I want to convert free trial users into paying customers. I plan to identify where users are in their journey and target them with strategic messaging and engagement tactics."* This lesson walks through a 4-step interactive process card set showing how to apply the funnel to this scenario:

1. **Awareness: Introduce users to paid features**
   - *Goal:* Ensure users know why upgrading matters and introduce them to the benefits of premium features.
   - *Cohorts I Can Target:* Users who just signed up for a free trial; users who haven't interacted with premium features yet; users who haven't visited the pricing page.
   - *Guides and Surveys Content Strategy:* Banner announcement for all trial users ("Unlock premium insights! Upgrade now for advanced analytics and personalized reporting."); tooltip on locked features ("This feature is available on our Pro Plan—see how it can help you get deeper insights."); survey to gauge interest ("What's your top priority? A) Advanced reporting, B) Team collaboration, C) Faster workflows" — used to segment users for future targeting).
   - *What to Avoid:* Overloading these new users with a long, generic product tour. Instead, deliver targeted, contextual messaging.
2. **Consideration: Encourage users to engage with premium features**
   - *Goal:* Drive engagement with a key premium feature to showcase its value.
   - *Cohorts I Can Target:* Users who have clicked on a premium feature but didn't complete an action; users who have visited the pricing page but didn't upgrade; users who have completed the awareness stage (e.g., viewed feature pages or received onboarding emails).
   - *Guides and Surveys Strategy:* Pin guide on a locked feature ("Want to export reports? Upgrade to unlock seamless data sharing."); targeted survey to hesitant users ("You've explored our Pro Plan—what's holding you back from upgrading?" with multiple-choice answers and follow-up messaging based on responses).
   - *What to Avoid:* Assuming interest leads to conversion. Users need proof of value, so drive hands-on interactions.
3. **Conversion: Encourage users to upgrade**
   - *Goal:* Reinforce the value and urgency of upgrading.
   - *Cohorts I Can Target:* Users who have used a premium feature multiple times but haven't upgraded; users who have visited the upgrade page multiple times; users who have completed a full trial period without converting.
   - *Guides and Surveys Strategy:* Limited-time banner offer ("Upgrade in the next 48 hours and get 10% off your first month!"); modal with feature comparison ("You've used 80% of your free trial. See what's waiting for you in the Pro Plan!"); exit-intent survey ("What's stopping you from upgrading?" — e.g., if "Too expensive" is selected, trigger a discount offer).
   - *What to Avoid:* Offering a discount too early — test engagement first before incentivizing price drops.
4. **Retention: Keep paid users engaged**
   - *Goal:* Reinforce ongoing value and prevent churn.
   - *Cohorts I Can Target:* Users who have recently upgraded; long-time users who haven't engaged in key features; users who show signs of disengagement (e.g., haven't logged in recently).
   - *Guides and Surveys Strategy:* Survey post-upgrade ("What made you decide to upgrade?" — used to refine future messaging); onboarding checklist for paid features ("Get the most out of your Pro Plan—complete these three quick steps!"); tooltip nudges on underutilized features ("Haven't tried custom dashboards yet? See how they can help streamline your workflow!").
   - *What to Avoid:* Assuming users will explore on their own — keep engagement active and ongoing.

**Summary:** By aligning your messaging with the Product adoption funnel, you can engage users at the right moment, drive adoption, and support long-term retention.
- Identify the user's current stage using behavioral cohorts in Amplitude.
- Use targeted guides and surveys to move them forward, step by step.
- Reinforce your guides and surveys strategy through email, ads, and Customer Success for a multi-channel approach.

**Common pitfalls to avoid.** Beyond developing a strategy that aligns with your user's journey, it's important to be aware of common mistakes that can undermine your strategy. This lesson uses a 3-item accordion of pitfalls, each paired with a "Try this instead..." remedy:

1. **Prioritizing Product Updates Too Soon** — New users aren't interested in your latest feature release; they're focused on learning the basics. Introducing updates before users understand your product can lead to confusion and disengagement.
   - *Try this instead...* Align your messaging with where your users are in their journey with your product. Use Amplitude cohorts to target updates only to users who have completed key onboarding steps or engaged with core features.
2. **Cluttering the Interface** — Too many messages on your interface at one time create cognitive overload and reduce engagement.
   - *Try this instead...* Use built-in settings to help ensure guides remain helpful and non-disruptive: (1) **Priority** — control which guides or surveys appear first when multiple messages are eligible; (2) **Limits** — restrict how often a user sees a guide to prevent overwhelming them with too many messages; (3) **Global Throttling** — set an overall limit on how many guides or surveys a user can see within a given timeframe. By using these settings strategically, you can maintain a clean interface while still delivering impactful, well-timed messaging.
3. **Providing Too Much Information at Once** — Your product may have dozens of great features, but users don't need to learn them all immediately. Keep content digestible and introduce new features gradually as users progress through their journey with your product.
   - *Try this instead...* Use Guides and Surveys functionality to create digestible, well-timed content rather than long, complex tours: limit multi-step guides to 3-5 steps that lead users to critical events within your product; leverage cohorts to show messages based on user behavior; consider banners, tooltips, and checklists instead of lengthy tours to provide ongoing guidance.

## Section: Conclusion

### Lesson 8 — Summary and Additional Resources

**Additional resources.** For additional information on Guides and Surveys, see the following resources:

*Amplitude Documentation:*
- Guides and Surveys overview
- Guides and Surveys instrumentation (web and mobile)
- Guides and Surveys localization
- Guides and Surveys templates

*Amplitude Academy:*
- Deliver Targeted Guidance and Support with a Resource Center
- Create, Analyze, and Activate User Groups with Behavioral Cohorts
- Getting Started with Amplitude Guides and Surveys Experimentation

*"Thanks for completing this course! You've reached the end of Engage Your Users with Guides and Surveys. Click 'Next' to share your feedback on this course by completing a short survey."*

## Knowledge Check

**Result on file:** Passed — 3 of 3 correct (100%). Elapsed time: less than a minute.

This quiz's "Show Answers" view visually marks each option with a checkbox (checked/bolded/green = correct; unchecked/greyed/struck-through = incorrect), which is reproduced below along with the per-question Feedback text.

1. **True or False? The only functional difference between a guide and a survey is that surveys accept user input while guides do not.**
   - ☐ False
   - ☑ **True** *(correct)*
   - *Feedback: That's right! Guides and surveys have different templates because surveys can take additional input blocks. However, the form factors and styling are the same.*

2. **A product team launches a new feature and announces it with a guide that appears for all users as soon as they log in. After a week, they notice low engagement with the guide: many users quickly dismissed it. What is the most likely reason this guide was ineffective?**
   - ☐ The guide contained too much information about the feature.
   - ☐ The guide was not visually engaging enough.
   - ☑ **The guide was not strategically targeted to the right users at the right time.** *(correct)*
   - *Feedback: The guide targeted all users without considering their needs, behavior, or stage in the journey. A more effective approach would involve using behavioral data and cohorts to target users who would benefit from the feature.*

3. **How can you use Amplitude's behavioral insights to enhance the impact of your guide or survey?**
   - ☑ **Strategically target users with cohorts** *(correct)*
   - ☐ Limit the number of guides and surveys a user can see
   - ☐ Automatically choose the most popular form factor for a guide or survey
   - *Feedback: Amplitude's behavioral insights enable precise targeting based on user properties and cohorts. This ensures your content reaches the right users at the right time.*

## Feedback

This course ends with a "We'd love your feedback" survey lesson — navigational/administrative, not course content.

---

## Summary / Explanation

This course walks through Amplitude's Guides and Surveys feature end-to-end: what it is, how to build it, how to target it, how to measure it, and how to strategize with it. The core conceptual distinction — a guide is informational (no user input) while a survey is interactive (collects user input), with everything else (form factors, styling, templates) shared between them — is reinforced directly in the Knowledge Check. The Build/Setup/Insights three-tab structure mirrors the natural workflow of creating in-product engagement: first create the content (choosing a form factor — modal, popover, or pin — and populating it with blocks, or starting from a template matched to a use case like Announcement, Product Tour, or NPS survey), then target it precisely (the WHO/WHERE/WHEN framework, operationalized through Amplitude cohorts, page rules, and smart triggers), then measure its impact (through built-in Insights or by treating guide/survey interactions as ordinary Amplitude events and user properties for deeper analysis). The two use-case videos (onboarding/adoption and churn-prevention-via-survey) ground the feature in concrete scenarios, and the final "Develop an Effective Content Strategy" lesson ties everything together with the product adoption funnel (Awareness → Consideration → Conversion → Retention) — showing, via a single running example (a PM targeting free-trial-to-paid conversion), how the *content* and *targeting cohort* for a guide or survey should shift depending on which funnel stage a user is in. The three "common pitfalls" (updating users too soon, cluttering the interface, and front-loading too much information) all trace back to the same root cause the Knowledge Check emphasizes: engagement fails not because of bad design or copy, but because of poor targeting and timing — reinforcing that Priority, Limits, and Global Throttling settings, plus cohort-based targeting, are the primary levers for keeping in-product messaging effective rather than disruptive.
