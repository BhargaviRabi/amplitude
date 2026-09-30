# Move Faster with Amplitude Agents

**Type:** On-demand course | **Time commitment:** 20 minutes

---

## About This Course

Amplitude's AI Analytics Platform uses the Global Agent, an intelligent copilot, to democratize customer intelligence across your organization. Analytics no longer needs to be a specialized skill, as the Global Agent can understand your customer data, answer complex questions, and perform deep analysis through natural language. This course teaches you how to use this chat interface to quickly create and analyze charts, moving from a hypothesis to a validated answer in minutes. The Agent actively investigates root causes for drop-offs and changes, analyzing user properties, behavior patterns, and product context. By the end, you'll be able to leverage the Global Agent to get expert insights, reduce time spent on manual analysis, and instantly take action — such as creating cohorts or setting up experiments — directly from your analysis.

**By the end of this course, you will be able to:**
- Use the Global Agent's natural language interface to quickly create and analyze charts.
- Leverage the Global Agent to identify the underlying reasons for changes and drop-offs in key business metrics.
- Get expert-level insights and reduce time spent on manual analysis.
- Instantly take action from your analysis, such as creating cohorts or setting up experiments.

**You should take this course if:**
- You are an Amplitude user who wants to accelerate time-to-insight.
- You want to leverage natural language to answer complex questions about customer behavior.
- You are ready to use AI to perform deep analysis and take immediate action, such as creating cohorts or experiments.

---

## SECTION: Introduction to Amplitude Analytics

### Lesson 1 — Overview: Amplitude's Agents (1 min)

Amplitude's AI Platform consists of three parts.

**[Video: "Agents Overview", 1 min 07 sec]** — (No on-page transcript available; the three parts it covers are summarized below.)

- **Global Agent** — Understands your customer data and can answer questions, perform analysis, and execute tasks through natural language. This is a chat interface available on every page.
- **Specialized Agents** — Amplitude's specialized autonomous agents can run continuously in the background and assist by monitoring dashboards, analyzing session replays, and running experiments — taking action to drive growth.
- **MCP** — The same MCP that powers the Global Agent is available as a connection layer, making Amplitude's customer intelligence available in any AI tool that supports MCP.

The rest of the course looks at each of these three parts more closely.

### Lesson 2 — Move Faster with the Global Agent (7 min)

Amplitude's Global Agent lets you interact with your data using natural language via in-product Chat. You no longer need to start each analysis from scratch or group-by endless properties to find what was responsible for a given impact.

**[Video: "Global Agent", 1 min 07 sec]** — shows how AI helps you get started, gain immediate insight into a dashboard, and dive deep into an analysis. (No on-page transcript available.)

**Use Cases for Global Agent** — common ways to start unlocking AI analytics immediately:
- **Descriptive analytics:** "How many weekly active users did we have last week?"
- **Root-cause analysis (why?):** "Why did checkout conversion drop last week?"
- **Reporting:** "Create a weekly KPI dashboard for WAU, purchase conversion, and revenue for the last 8 weeks."
- **Driving feature adoption:** "Create a cohort of users who haven't engaged with X feature and design a guide to target them."
- **Understanding data:** "What does the event checkout_started mean, and what properties usually come with it?"
- **Optimizing campaigns:** "Which acquisition channel drove the highest 7-day retention for new users last month?"
- **Governing data:** "Which high-usage events have missing descriptions or have duplicate meanings?"
- **Quantifying business impact:** "What was the impact of the new onboarding flow on LTV?"
- **Churn prevention:** "Build a cohort of users likely to churn based on declining usage over the last 4 weeks."

### Lesson 3 — Accessing Amplitude's MCP Server (2 min)

You may want to access your Amplitude data using natural language outside of Amplitude, or using third-party tools — you can do that using the same MCP server that powers Amplitude's Global Agent.

**What is Model Context Protocol (MCP)?**

You can access your Amplitude data using natural language whether you're working within Amplitude or through third-party tools. Amplitude provides access to the same industry-standard Multi-Channel Protocol (MCP) server that powers Global Agent. This is made possible by connecting to Amplitude's global and specialized agents via the MCP server protocol, which supports seamless data exchange. Some integrations are available out of the box, while others may require additional technical setup.

- **Bring your own model** — If you have a highly negotiated contract with a model provider (e.g., OpenAI, Anthropic), you may prefer to stay with only that model. This gives you more control over high-level system prompts, for example to limit what data can be queried by users.
- **Multi-data source integration** — You can combine various data sources (such as Salesforce, HubSpot, and Amplitude) to address data questions. This is most effective when the solution requires drawing data from all three sources, manipulating it, and providing the results to an LLM for analysis or a specialized Amplitude Agent.

### Lesson 4 — Automate Tasks with Specialized Agents (10 min)

Amplitude's always-on, specialized agents focus on some of the highest-leverage workflows: monitoring dashboards, analyzing session replays, and optimizing website conversion through experimentation. Agents work by synthesizing data from different parts of your Amplitude account — analytics, session replay, experimentation, guides and surveys — so the more you're already using Amplitude to analyze user behavior, the more context your Agents will have to work with.

**Using Agents** — Start by defining a goal for your Agent, like improving conversion or boosting feature adoption. The Agent uses your Amplitude data to identify patterns and make recommendations you can approve for it to act on. Instead of manually checking dashboards or scrubbing through replays, these agents run continuously in the background, surface insights, and prepare recommended actions for you to approve.

- **Dashboard Monitoring Agent** — Continuously analyzes your selected dashboards, looks for meaningful changes in key metrics, and runs root-cause analysis to explain what's driving those shifts (e.g., segments, channels, or mix changes). Pushes clear summaries and recommended next steps into Amplitude, Slack, or email when it finds something.
  *Example use cases:*
  - *Monitor core product KPIs without manual reporting* — Point the Agent at your product health or North Star dashboard (signups, activation, retention, revenue). It summarizes the most important week-over-week and month-over-month changes plus likely drivers, instead of you assembling that story by hand before every standup or QBR.
  - *Catch conversion drops and anomalies early* — Configure the Agent on a funnel or growth dashboard (e.g., trial-to-paid, checkout completion, onboarding completion) so it flags unusual drops, highlights the segments most affected, and ties changes to any recent releases or campaigns.
  - *Automate stakeholder updates in Slack or email* — Schedule the Agent to send regular summaries to a Slack channel or distribution list, giving PMs, marketers, and executives a digest of key movements and suggested follow-ups without anyone needing to log into Amplitude first.

- **Session Replay Agent** — Automatically watches hundreds of sessions across your funnels or critical events, identifies friction patterns, curates representative replays, and recommends targeted fixes — an organized, insight-ready "highlight reel" instead of manual sampling and guessing.
  *Example use cases:*
  - *Diagnose funnel drop-off with qualitative evidence* — When you see a quantitative drop-off in a funnel step (e.g., payment, signup verification, account setup), the agent analyzes sessions at that step, surfaces common friction behaviors (scrolling loops, form errors, rage-clicks), and curates a short playlist to review with designers and engineers to align on the root cause.
  - *Improve mobile UX and accessibility* — Direct the agent to focus on mobile sessions for key flows (onboarding, checkout, content consumption) so it can detect issues like tap targets that are too small, keyboard overlays hiding fields, or confusing navigation.
  - *Reduce support tickets by fixing "hot paths"* — Have the agent analyze sessions for users who trigger "contact support," "cancel," or other high-risk events, then summarize the most common confusing interactions and show example sessions you can use to prioritize UX fixes, in-product guides, or experiments to deflect future tickets.

- **Website Conversion Agent** — Analyzes user behavior on your website, develops hypotheses, designs and configures experiments, generates page variants (including HTML/CSS/JavaScript for web experiments), launches tests with your approval, and measures results to recommend roll-outs or next iterations.
  *Example use cases:*
  - *Continuously optimize key landing pages* — Point the agent at your primary acquisition or pricing pages to monitor conversion performance, propose hypotheses (e.g., unclear value prop, weak CTA placement), and generate test variants; with your approval it runs experiments and reports back which variant wins and by how much.
  - *Fix checkout and sign-up friction* — Use output from the Session Replay Agent (e.g., identified form or error-state friction) as input context so the Website Conversion Agent can design A/B tests that adjust layout, copy, or validation patterns, then measure whether those changes actually reduce drop-off at critical steps like payment or account creation.
  - *Test messaging and layout without engineers* — For campaign pages or new product announcements, have the agent generate multiple variants (headline, hero layout, trust indicators, social proof) and manage the experiment lifecycle, iterating on a hypothesis quickly and confidently without engineering or design resources.

**Common AI questions**

- *Are models trained using customer data?* No. Amplitude does not train AI Models on any customer's data for Amplitude AI Agents. Agents learn from general best practices from the latest foundation models (interaction patterns, accessibility standards, design practices) plus Amplitude's own expertise layered in via system prompts developed from working with thousands of teams.
- *How do Agents learn and know what to do?* Each Agent builds up its own memory from a customer's database about your specific product and what works for your users. This knowledge stays completely separate and secure for each customer. Over time, Agents are expected to get smarter as their underlying models improve, as Amplitude refines its approach, and as they learn more about your particular business.
- *What models power Agents?* Amplitude uses a combination of models from OpenAI and AWS Bedrock, plus many specialized tools and sub-Agents for different tasks (analysis, running experiments, creating guides). Most orchestration, memory, and session management is supported by Amplitude's backend, so Agents behave like product analytics specialists rather than AI generalists.

---

## Feedback

This course ends with a "We'd Love Your Feedback" survey lesson — navigational/administrative, not course content.

---

## Summary / Explanation

This short course is the AI-agent counterpart to "Getting Started with Amplitude Analytics." It breaks Amplitude's AI platform into three pieces: the **Global Agent** (an on-demand, chat-based copilot available on every page that can build charts, investigate root causes, and take action from natural-language prompts), the **specialized always-on Agents** (Dashboard Monitoring, Session Replay, and Website Conversion — each watching a specific surface, surfacing insights automatically, and proposing actions for you to approve), and the **MCP server** (the same protocol layer that powers the Global Agent, exposed so third-party AI tools — or your own chosen model provider — can query Amplitude data directly, optionally blended with other data sources like Salesforce or HubSpot). The throughline is that none of this is trained on customer data — each agent instead builds a private, per-customer memory on top of general foundation-model best practices and Amplitude's own system-prompt expertise.
