# Source for gershon.ai/articles. Edit here, then run: python3 _build/build_articles.py
# Each article: slug, app, url, title, dek, read, tag, body (list of blocks).
# Block types: ("h", text) heading, ("p", text) paragraph, ("ul", [items]) bullet list, ("q", text) pull quote.

DATE = "November 18, 2026"
AUTHOR = "Olivier Attia, Founder, Gershon Consulting"

ARTICLES = [
{
"slug": "why-we-built-gershon-ai",
"app": "Gershon.AI", "url": "https://gershon.ai/apps/", "tag": "Our story", "read": 5, "featured": True,
"title": "Why we built our own apps instead of buying more tools",
"dek": "Thirteen years of taking companies into the U.S. taught us where growth really leaks. So we built the apps to plug each leak, and turned them into a team of AI agents.",
"body": [
("p", "Since 2013, Gershon Consulting has had one job: give international companies a recurring sales pipeline in the United States. Not a strategy deck. Not a list of logos. Meetings with buyers, week after week."),
("p", "Doing that job for years, across industries, showed us the same pattern again and again. Companies rarely fail in the U.S. because their product is weak. They fail because the work between a good product and a signed U.S. customer is slow, manual and invisible. Nobody sees it slipping until the quarter is gone."),
("h", "The leaks we kept seeing"),
("ul", [
"Teams targeted the wrong buyers because nobody had mapped the U.S. market properly.",
"Travel budgets went to trade shows where the real decision-makers never walked the floor.",
"LinkedIn profiles stayed silent, so the first message to a prospect arrived cold.",
"Hot replies sat for days in a crowded inbox while the prospect moved on.",
"Warm introductions existed inside the network, but nobody knew who could make them.",
"Deals died of silence after a good first meeting.",
"Clients could not see, in one page, what their budget had actually produced.",
]),
("p", "Every one of those leaks costs a deal. Most of them were being handled with spreadsheets, sticky notes and good intentions. The off-the-shelf tools we tried each solved a slice, but none of them was built around the one outcome we are paid for: U.S. meetings."),
("h", "So we built the apps ourselves"),
("p", "One app per leak. ICP maps who to sell to. Events grades which U.S. shows are worth the trip. Publish and Social build a LinkedIn presence buyers recognise. Pulse and Radar start and triage the conversations. Sales keeps every deal moving. Client and Report prove the results. Around them sit the helpers: Talking Points to prepare every meeting, Welcome to onboard without forms, Gauge and Tools to check that the tools you pay for are really used."),
("p", "We use every one of these apps every day on real client campaigns. That is the point. They were not designed in a lab; they were designed by people who had to deliver meetings on Monday morning."),
("q", "AI does the volume. People own the judgment."),
("h", "Why that makes them powerful"),
("ul", [
"They share one goal. Each app hands its work to the next one, so the campaign gets sharper every week instead of starting over.",
"They run constantly. The agents behind them work around the clock, while our strategists in New York set direction and approve what goes out.",
"They are measurable. Every action leaves evidence, so results are shown, not claimed.",
]),
("p", "Today the apps work together as Gershon.AI: six AI agents, a Strategist, an Event Scout, a Writer, an SDR, a Closer's Copilot and an Analyst, steered by our team. The articles in this series explain each app, the problem that made us build it and what it changes for a company entering the U.S."),
("p", "If the U.S. is your next growth market, the fastest way to see what the apps can do for you is a 20-minute call with our team."),
]},

{
"slug": "icp",
"app": "ICP", "url": "https://icp.gershon.ai", "tag": "The Strategist", "read": 3,
"title": "ICP: your U.S. market launch analysis in minutes, not months",
"dek": "Enter a website. Get a 12-point U.S. launch analysis: who buys, who you compete with, where to meet them and how to reach them.",
"body": [
("h", "Why we built it"),
("p", "Every U.S. expansion we have run started with the same question: who exactly should we sell to? Most companies answer it with their home-market customer list and hope it translates. It rarely does. U.S. buyers are organised differently, titled differently and reached differently."),
("p", "We used to spend weeks of senior consulting time producing that answer by hand for each new client. That was too slow for the client and too expensive to give away to prospects who needed it before deciding anything. So we turned our method into an app."),
("h", "What it does"),
("ul", [
"Reads your website and your offer, the way a strategist would before a first meeting.",
"Builds a 12-point U.S. market launch analysis: ideal customer profiles, industries, company sizes, regions and the job titles that sign.",
"Maps the competition you will meet in the U.S. and how to position against it.",
"Points to the events and outreach channels where your buyers can actually be reached.",
]),
("h", "Why it is powerful"),
("p", "ICP compresses the first month of a U.S. launch into minutes. More importantly, it gives your team and ours one shared definition of the target. Every other Gershon app, from Events to Pulse, starts from that definition, so a better ICP makes every downstream action more precise."),
("p", "It is also honest. If your offer does not fit an obvious U.S. buyer yet, the analysis shows it, before you spend a dollar on travel or outreach."),
("h", "Who it is for"),
("p", "Founders and sales leaders weighing the U.S. as their next market, and teams already there who suspect they are talking to the wrong people."),
]},

{
"slug": "events",
"app": "Events", "url": "https://events.gershon.ai", "tag": "The Event Scout", "read": 3,
"title": "Events: stop flying to the wrong U.S. trade shows",
"dek": "From your ideal customer profile to a graded calendar of U.S. events, plus the exhibitors and CEOs worth meeting at each one.",
"body": [
("h", "Why we built it"),
("p", "A U.S. trade show is one of the biggest line items in an expansion budget: booth, flights, hotels, days away from the business. We watched clients pick events by reputation or habit, then come home with a bag of business cards and no meetings with real buyers."),
("p", "The problem was never effort. It was information. Nobody had checked, before booking, how many of the client's actual buyers would be in the room."),
("h", "What it does"),
("ul", [
"Takes your ICP and scans U.S. trade shows, conferences and industry events.",
"Grades each event on how well its audience matches your buyers, so you can rank them.",
"Pulls the exhibiting companies that fit your profile, with the CEO and decision-maker contacts worth meeting there.",
]),
("h", "Why it is powerful"),
("p", "Events turns a trade show from a gamble into a plan. You know which shows deserve your budget, and you arrive with a target list instead of hoping the right person walks past your booth. Meetings can be requested weeks before the doors open, which is when the best calendars fill up."),
("p", "Because it starts from the same ICP as the rest of the Gershon apps, the people you meet at the show flow straight into your LinkedIn outreach and follow-up afterwards. Nothing is lost when the event ends."),
("h", "Who it is for"),
("p", "Any company that spends money on U.S. events, or is about to, and wants each trip to produce pipeline."),
]},

{
"slug": "publish",
"app": "Publish", "url": "https://publish.gershon.ai", "tag": "The Writer", "read": 3,
"title": "Publish: a LinkedIn presence your U.S. buyers recognise before you write to them",
"dek": "Create, approve, schedule and publish LinkedIn posts in your voice, with a client validation step before anything goes live.",
"body": [
("h", "Why we built it"),
("p", "The single biggest difference between an outreach message that gets a reply and one that gets ignored is whether the recipient has seen your name before. Executives know this, yet their LinkedIn profiles stay quiet for months because writing, approving and posting takes time nobody has."),
("p", "Running content for many clients at once, we also needed something stricter than a shared document: a place where every post is drafted, checked by the client and published on schedule, with a record of who approved what."),
("h", "What it does"),
("ul", [
"Turns your expertise, interviews and existing material into LinkedIn posts written for U.S. buyers.",
"Plans a steady posting calendar for each person and company page.",
"Sends every post to the client for validation before it can go live.",
"Publishes on schedule and keeps a record of every action.",
]),
("h", "Why it is powerful"),
("p", "Publish makes consistency automatic. Your profile becomes the thing prospects check after receiving a message, and it answers the question they are really asking: is this company credible in my market?"),
("p", "The validation step matters as much as the writing. Nothing goes out in your name without your yes, which is how a busy CEO can stay visible without losing control of their voice."),
("h", "Who it is for"),
("p", "Founders, executives and company pages that need to be visible to U.S. buyers but cannot spend hours a week writing."),
]},

{
"slug": "social",
"app": "Social", "url": "https://social.gershon.ai", "tag": "The Writer", "read": 3,
"title": "Social: know which content earns attention before you post more",
"dek": "LinkedIn analytics and social performance dashboards that track reach, engagement and the inbound signals that matter.",
"body": [
("h", "Why we built it"),
("p", "Posting more is easy. Knowing what to post is not. Our clients kept asking the same questions: which topics actually reach U.S. buyers, what are competitors publishing, and is any of it turning into conversations?"),
("p", "LinkedIn's own statistics answer only part of that, one account at a time. We needed one view across every account we manage, and across the companies our clients compete with."),
("h", "What it does"),
("ul", [
"Collects posts and performance from the accounts and company pages you track.",
"Shows reach, engagement and inbound signals in clear dashboards.",
"Highlights which content gets the most attention, so the next post is better than the last.",
"Sends a weekly pack so the numbers come to you instead of the other way round.",
]),
("h", "Why it is powerful"),
("p", "Social closes the loop with Publish. What works is written more; what does not is dropped. Over a few weeks that feedback loop is the difference between a feed that people scroll past and one that starts conversations."),
("p", "It also shows what your competitors are doing on LinkedIn, so you can occupy the topics they ignore."),
("h", "Who it is for"),
("p", "Marketing and sales teams that publish on LinkedIn and want to know, with evidence, what is working."),
]},

{
"slug": "pulse",
"app": "Pulse", "url": "https://pulse.gershoncrm.com", "tag": "The SDR", "read": 3,
"title": "Pulse: no hot lead waits in a LinkedIn inbox again",
"dek": "LinkedIn and Sales Navigator inbox triage. Every conversation sorted Red, Orange or Green, so the interested prospects get an answer first.",
"body": [
("h", "Why we built it"),
("p", "Good outreach creates a new problem: replies. Hundreds of LinkedIn and Sales Navigator conversations pile up across accounts, and the one prospect who wrote \"yes, let's talk\" ends up buried between connection thank-yous and polite refusals."),
("p", "We saw real opportunities go cold simply because nobody answered for three days. In the U.S., three days is long enough for a prospect to take a meeting with someone else."),
("h", "What it does"),
("ul", [
"Reads every LinkedIn and Sales Navigator conversation across your accounts.",
"Sorts each one Red, Orange or Green according to how urgent and promising it is.",
"Puts the interested prospects at the top, ready for a reply or a meeting proposal.",
]),
("h", "Why it is powerful"),
("p", "Pulse turns an inbox into a to-do list ranked by revenue. Your team stops reading and starts answering. Speed to reply is one of the strongest predictors of a booked meeting, and Pulse makes speed the default."),
("p", "It also makes outreach measurable: you can see how many conversations are hot, warm or closed, instead of guessing from a scroll."),
("h", "Who it is for"),
("p", "Anyone running outbound on LinkedIn, especially across several accounts, who cannot afford to miss the reply that matters."),
]},

{
"slug": "radar",
"app": "Radar", "url": "https://radar.gershoncrm.com", "tag": "The SDR", "read": 3,
"title": "Radar: the warm intro beats the cold message",
"dek": "Warm introductions, mapped: Sources, Bridges, Prospects. See who in your network can introduce you to each buyer.",
"body": [
("h", "Why we built it"),
("p", "Every salesperson knows that an introduction from someone the buyer trusts beats any cold message. The problem is finding it. The path to a prospect often exists, through a former colleague, an investor, a partner, but it is hidden in hundreds of connections nobody has time to cross-check."),
("p", "We were doing that mapping by hand for clients, profile by profile. It worked, and it did not scale."),
("h", "What it does"),
("ul", [
"Starts from your Sources: the people and accounts in your own network.",
"Finds the Bridges: connections who know both you and the buyer.",
"Lines up the Prospects you can reach through each bridge.",
"Sends regular updates so new paths show up as your network grows.",
]),
("h", "Why it is powerful"),
("p", "Radar changes the first contact from \"you don't know me\" to \"a person you trust suggested we talk\". That shift raises reply rates and shortens sales cycles, especially with senior U.S. buyers who ignore cold outreach."),
("p", "It also makes your existing network work for you. Most companies already have more warm paths into the U.S. market than they think; Radar shows them."),
("h", "Who it is for"),
("p", "Founders and sales teams selling to senior decision-makers, where one introduction is worth a hundred cold messages."),
]},

{
"slug": "sales",
"app": "Sales", "url": "https://sales.gershon.ai", "tag": "The Closer's Copilot", "read": 3,
"title": "Sales: no deal dies of silence",
"dek": "A follow-up copilot on the sales pipeline. It surfaces every deal that needs a nudge and drafts the next touch.",
"body": [
("h", "Why we built it"),
("p", "Getting the first meeting is hard. Losing the deal after a great first meeting is painful, and it happens all the time. Not because the buyer said no, but because the follow-up slipped: a busy week, a forgotten promise, a proposal never chased."),
("p", "We run our own pipeline the same way we run our clients' campaigns, and we wanted a copilot that would never let a good conversation go quiet."),
("h", "What it does"),
("ul", [
"Watches the sales pipeline and flags every opportunity that has gone quiet.",
"Drafts the next follow-up for each one, based on where the deal stands and what was last said.",
"Makes sure every meeting ends with a clear next step and a date.",
]),
("h", "Why it is powerful"),
("p", "Sales turns follow-up from a memory exercise into a daily routine. Each morning there is a short list of deals to move and a draft ready for each. People still decide and send; the copilot makes sure nothing is forgotten."),
("p", "Combined with Pulse upstream, it closes the gap between \"interested\" and \"signed\", which is where most U.S. pipelines quietly leak."),
("h", "Who it is for"),
("p", "Founders and small sales teams carrying more opportunities than they can track in their head."),
]},

{
"slug": "client-report",
"app": "Client & Report", "url": "https://client.gershoncrm.com", "tag": "The Analyst", "read": 3,
"title": "Client and Report: proof, every week, on one page",
"dek": "A client portal with live dashboards and a one-pager generator that turns a month of campaign data into a client-ready report.",
"body": [
("h", "Why we built it"),
("p", "Clients who invest in U.S. growth deserve to know what their budget produced, without waiting for a monthly call or reading a twenty-tab spreadsheet. We also wanted to hold ourselves accountable in public: if the work was agreed, the evidence should be there."),
("p", "Building those reports by hand took hours every month and still arrived late. So we built two apps that do it for us."),
("h", "What they do"),
("ul", [
"Client is the portal: live dashboards for each engagement, always up to date.",
"Report turns a month of LinkedIn campaign exports into a clean, client-ready one-pager.",
"Social Tracking checks behind the scenes that every agreed action was really done, with evidence.",
]),
("h", "Why it is powerful"),
("p", "Proof changes the relationship. Instead of \"trust us, it is working\", clients see posts, conversations, meetings and pipeline in one place, every week. Problems surface early, and good results are visible to the whole leadership team, not just the person who hired us."),
("p", "Internally, it keeps us honest and fast: what is measured every week gets improved every week."),
("h", "Who it is for"),
("p", "Every Gershon client, and every executive who has ever wondered what an agency actually did last month."),
]},

{
"slug": "talking-points",
"app": "Talking Points", "url": "https://talkingpoints.gershon.ai", "tag": "Meeting prep", "read": 3,
"title": "Talking Points: walk into every meeting prepared",
"dek": "AI-assisted talking points and messaging guidance for sharper client and prospect conversations.",
"body": [
("h", "Why we built it"),
("p", "All the outreach in the world ends in a meeting, and a meeting is won or lost in the first ten minutes. Preparing well, knowing the company, the person, their likely objections and the angle that will resonate, takes time that busy founders rarely have between calls."),
("p", "We saw too many hard-won meetings start with \"so, tell me about your company\". We wanted every one of them to start with something sharper."),
("h", "What it does"),
("ul", [
"Prepares talking points for each meeting from what is known about the company and the person.",
"Suggests the angles, questions and messages most likely to land.",
"Keeps a weekly rhythm so preparation is ready before the calendar fills up.",
]),
("h", "Why it is powerful"),
("p", "Talking Points turns preparation from an afterthought into a habit. You arrive knowing what matters to the buyer, which makes you more credible and the conversation shorter and more useful for both sides."),
("p", "In a new market, where you cannot rely on reputation yet, that preparation is often the deciding factor."),
("h", "Who it is for"),
("p", "Founders, sales leaders and account managers who take many first meetings and want each one to count."),
]},

{
"slug": "welcome",
"app": "Welcome", "url": "https://welcome.gershon.ai", "tag": "Onboarding", "read": 2,
"title": "Welcome: onboarding as a conversation, not a form",
"dek": "Conversational client onboarding that captures context, goals and requirements in one structured flow.",
"body": [
("h", "Why we built it"),
("p", "The first days of an engagement set its pace. Traditional onboarding means long forms, back-and-forth emails and a kickoff call spent collecting information that should already be known. Momentum is lost before any real work starts."),
("h", "What it does"),
("ul", [
"Guides new clients through a conversation instead of a questionnaire.",
"Captures their context, goals, targets and requirements in a structured way.",
"Saves progress, so it can be completed in several short sessions.",
"Hands everything to our team and to the other apps, starting with ICP.",
]),
("h", "Why it is powerful"),
("p", "Welcome makes the kickoff call about decisions, not data collection. Campaigns start faster, with fewer misunderstandings, because what the client said is written down once and used everywhere."),
("h", "Who it is for"),
("p", "Every new Gershon client, from the first day of the engagement."),
]},

{
"slug": "gauge",
"app": "Gauge", "url": "https://gauge.gershon.ai", "tag": "Self-assessment", "read": 2,
"title": "Gauge: how good are you really with Sales Navigator?",
"dek": "Sign in with LinkedIn and get a score that shows how well you use Sales Navigator, and what to improve first.",
"body": [
("h", "Why we built it"),
("p", "Sales Navigator is one of the most powerful prospecting tools a B2B company can buy, and one of the most under-used. We meet teams paying for licences every month while using a fraction of what they include."),
("p", "Telling people they could do better is easy. Showing them, with a score, is far more convincing."),
("h", "What it does"),
("ul", [
"Lets you sign in with LinkedIn in a few seconds.",
"Measures how you actually use Sales Navigator.",
"Gives you a clear score and the levers that would raise it fastest.",
]),
("h", "Why it is powerful"),
("p", "Gauge turns a vague feeling (\"we should use LinkedIn better\") into a number and a short list of actions. It is the quickest way to see whether the money spent on Sales Navigator is producing pipeline, and where the easy wins are."),
("h", "Who it is for"),
("p", "Founders, sales teams and anyone paying for Sales Navigator who wants to know if they are getting their money's worth."),
]},

{
"slug": "tools",
"app": "Tools", "url": "https://tools.gershoncrm.com", "tag": "Stack health", "read": 2,
"title": "Tools: are you getting what you pay for from your growth stack?",
"dek": "One score for every growth tool you pay for: how well each outreach and AI platform is really being used.",
"body": [
("h", "Why we built it"),
("p", "Modern outbound runs on a stack of subscriptions: automation platforms, data providers, email finders, AI models. Each has its own dashboard, its own billing and its own way of quietly failing. We were losing time logging into each one to check that campaigns were really running."),
("h", "What it does"),
("ul", [
"Connects to the outreach and AI platforms you use.",
"Grades how well each one is used, in one dashboard.",
"Shows the raw data behind every grade, plus usage and cost for AI services.",
"Keeps a daily history so trends and breakdowns are easy to spot.",
]),
("h", "Why it is powerful"),
("p", "Tools makes the invisible visible. A stalled automation or an unused subscription shows up the same day, not at the end of the month. Every dollar in the growth stack is accounted for, and every tool is either earning its place or flagged."),
("h", "Who it is for"),
("p", "Teams running several outreach and AI tools who want one honest view of what is working."),
]},

{
"slug": "linalysis",
"app": "Linalysis", "url": "https://linalysis.net", "tag": "LinkedIn analytics", "read": 3,
"title": "Linalysis: LinkedIn analytics that span years, not snapshots",
"dek": "Connections, profile views, Social Selling Index and company pages, tracked over the long term so you can see what really moves.",
"body": [
("h", "Why we built it"),
("p", "LinkedIn shows you how you are doing today. It does not easily show how you are doing compared with last quarter or last year, and that is the only comparison that tells you whether your effort is working."),
("p", "We wanted a long memory: every connection, every profile view and every change in Social Selling Index, kept and charted over time."),
("h", "What it does"),
("ul", [
"Tracks connections, profile views and Social Selling Index (SSI) over time.",
"Follows company pages alongside personal profiles.",
"Turns the history into clear charts that show trends, not just snapshots.",
]),
("h", "Why it is powerful"),
("p", "With a long history, cause and effect become visible. You can see which month your network really started growing, which campaign lifted your profile views and whether your SSI is climbing or flat. Decisions about LinkedIn stop being opinions."),
("p", "Linalysis is also the design reference for every Gershon app: clean, fast and focused on the numbers that matter."),
("h", "Who it is for"),
("p", "Professionals and companies who invest in LinkedIn and want to measure that investment over the long run."),
]},

{
"slug": "nexashare",
"app": "NexaShare", "url": "https://nexashare.com", "tag": "Amplification", "read": 3,
"title": "NexaShare: make sure the right people see what you publish",
"dek": "LinkedIn content amplification: get your team and network to repost and react to what you publish, at the moment it counts.",
"body": [
("h", "Why we built it"),
("p", "A great post that nobody sees is wasted. On LinkedIn, the first reactions and reposts decide how far a post travels. Most companies have employees and partners happy to help, but no simple way to ask them at the right moment."),
("h", "What it does"),
("ul", [
"Detects new posts from the company pages and people you choose to amplify.",
"Helps your team and network repost and react quickly, in the right way.",
"Reports what was shared, by whom, and what it produced.",
]),
("h", "Why it is powerful"),
("p", "NexaShare multiplies the reach of every post by the size of your team, without asking anyone to remember anything. Company content stops depending on a handful of enthusiasts and starts working the way LinkedIn rewards: early, genuine engagement from real people."),
("p", "Paired with Publish and Social, it completes the content cycle: write it, get it seen, measure it."),
("h", "Who it is for"),
("p", "Companies whose teams and partners want to support their content but need it to take seconds, not effort."),
]},

{
"slug": "gershon-mcp",
"app": "Gershon MCP", "url": "https://gershon.ai/mcp", "tag": "AI connector", "read": 2,
"title": "Gershon MCP: your AI assistant, plugged into your U.S. campaign",
"dek": "One connector that lets Claude, ChatGPT or Gemini read Gershon's platforms through safe, read-only actions.",
"body": [
("h", "Why we built it"),
("p", "More and more executives start their day by asking an AI assistant questions. We wanted our clients to be able to ask theirs about their U.S. campaign, and get answers from the real data, not a guess."),
("h", "What it does"),
("ul", [
"Connects AI assistants such as Claude, ChatGPT or Gemini to Gershon's platforms.",
"Exposes safe, read-only actions: campaign status, prospects, reports and more.",
"Lets you ask questions in plain language and get answers grounded in your data.",
]),
("h", "Why it is powerful"),
("p", "The Gershon MCP puts your U.S. pipeline wherever you already work. \"Which prospects replied this week?\" or \"How is the campaign trending?\" becomes a question you can ask in seconds. Read-only by design, it informs without ever acting in your name."),
("h", "Who it is for"),
("p", "Clients and partners who already use an AI assistant and want it to know their U.S. campaign as well as we do."),
]},
]
