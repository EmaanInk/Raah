0) Document purpose
This spec defines Raah as a professional product: a calm mentor-style web app that generates weekly roadmaps with deliverables (proof-based learning), starting with Tech tracks first, then expanding to other life/career domains using the same engine.

1) One-line summary
Raah helps motivated people who feel lost build a realistic weekly path with convincing guidance—starting with Tech, later expanding beyond tech—using onboarding, constraints-aware planning, and weekly “proof tasks” instead of generic roadmaps.

2) Problem statement
People don’t fail because they lack ambition. They fail because:

advice is generic (“learn X, then Y”)
plans ignore real life constraints (time, exams, energy)
steps don’t feel justified, so skeptical users don’t follow through
progress isn’t structured as weekly deliverables, so weeks blur together
Raah fixes this with:

mentor tone + explanations (“why this week matters”)
personalization (hours, pace, format, constraints, tone)
weekly proof (small builds, reps, artifacts)
3) Vision vs v1 scope (important)
Vision (long-term)
Raah becomes a domain-flexible roadmap mentor (tech, design, business, academics, habits, languages, etc.) using one core planning engine.

v1 scope (ship first, professionally)
Tech-only tracks (high quality, not shallow):

Software engineering / Web / Backend basics
AI / ML / Data fundamentals track
Interview readiness track (projects + practice + communication)
“Clarity + fundamentals” track for overwhelmed beginners
v2+ expansion (after v1 is stable)
Add new domains as new task libraries + prompts, not new apps:

UI/UX, cybersecurity, devops, digital skills, etc.
Rule: never promise perfect roadmaps for every domain in v1. Label non-tech as Coming soon until libraries exist.

4) Target users
Primary
students and early-career learners in tech who feel paralyzed and need direction
Secondary
self-learners switching into tech
busy learners needing realistic pacing
User traits Raah optimizes for
hard to convince without reasoning
scared of choosing the wrong path
wants accountability without shame
5) Product principles (non-negotiable)
Calm onboarding: short steps, friendly micro-copy, progress indicator
Low-pressure inputs: multiple choice + optional text + “I’m not sure yet”
Explainability: user can see why the roadmap matches their answers
Weekly deliverables: each week ends with a concrete proof artifact
Constraint-aware planning: time + energy + external pressures matter
Tone control: gentle vs balanced vs strict (user chooses)
Professional UX: responsive UI, validation, saved progress, clean architecture
6) Core user journey (end-to-end)
Landing: Raah introduces itself (trust + clarity)
Onboarding wizard (questions below)
Confirmation summary (user verifies understanding)
Roadmap generation
Dashboard: current week, tasks, notes, checkoffs
Weekly reflection + replanning hook (“I fell behind”)
Optional export/print-friendly roadmap
7) Onboarding questionnaire (full flow)
Global rules

Prefer one question per screen
Always show Step X of Y
Include “I’m not sure yet” wherever it reduces fear
Add 1-line “why we ask” micro-copy on each screen
Screen 0 — Welcome + name
Title: “Hi, I’m Raah.”
Input: preferred name
Why: “So I can speak to you like a mentor, not a form.”
Screen 1 — Tech track selection (v1 gate)
Question: “Which tech direction do you want Raah to guide you in?”

Software / Web / Apps
AI / ML / Data
Interview readiness (projects + prep)
I’m exploring tech broadly / not sure yet
Screen 2 — 3-month direction
Question: “What are you trying to achieve in the next 3 months?”

Internship/job readiness
Strong fundamentals
Portfolio projects
Semester survival + steady skill growth
I’m not sure yet
Screen 3 — Interest / excitement
Question: “What kind of work excites you most (in tech)?”

Building products people use
ML/experimentation
Data + insights
Automation/tooling
Teaching/explaining
I’m not sure yet
Screen 4 — Passion vs profession (gentle)
Question: “Do you want this interest to become your profession?”

Yes
Maybe
Not necessarily (skills first)
I don’t know yet
Screen 5 — Honest skill level (tech)
Question: “What’s your current level?”

Complete beginner
Small scripts / basics
Small projects/apps
Intermediate+
Screen 6 — Weekly time budget
Question: “How many hours per week can you realistically give?”

3–5
6–10
11–15
16+
Screen 7 — Constraints (multi-select OK)
Question: “What limits your learning most right now?”

Exams / workload
Laptop/internet limits
English technical reading
Motivation/focus swings
No mentor/community
Other (short text)
Screen 8 — Timeline preference
Question: “What timeline should the roadmap optimize for?”

4 weeks
3 months
6 months
No fixed date
Screen 9 — Learning format preference
Question: “How do you learn best?”

Written (docs/articles/guides)
Video then practice
Mixed
Build-first (minimal theory)
I’m not sure yet
Optional: English technical reading comfort (Comfortable / Sometimes / Not comfortable)

Screen 10 — Learning pace
Question: “What pace feels sustainable?”

Steady
Balanced
Accelerated (must remain realistic)
Not sure—recommend from my hours
If Accelerated: “On a hard week, what breaks first?”
(Time / Motivation / Focus / Confusion)

Screen 11 — End goal (explicit)
Question: “What does success look like at the end?”

Portfolio (2–3 strong proofs)
Fundamentals mastery
Interview readiness
Role clarity + direction
Not sure yet
Optional text: dream role/company

Screen 12 — Consistency style
Question: “What helps you stay consistent?”

Weekly checklist
Project milestones
Short daily tasks
Watch then do
Not sure yet
Screen 13 — Guidance tone
Question: “How should Raah guide you?”

Gentle (no guilt)
Balanced
Direct deadlines
Screen 14 — Confirmation summary + generate
Show summarized answers + buttons:

“Generate my roadmap”
“Edit answers”
8) Roadmap output format (standard for all tech tracks)
Raah outputs Week 1…Week N based on timeline + weekly hours + pace + level.

Each week includes:

Week theme (one line)
Why this week matters (mentor explanation, 2–4 sentences)
Tasks (3–6 bullets, actionable)
Weekly deliverable (proof artifact: repo milestone, mini app, write-up, quiz set, etc.)
Optional resources (clearly labeled; matched to learning format)
If you fall behind (1 practical sentence, kind tone)
9) “Why this roadmap” explainability panel (professor-friendly)
A dedicated panel that maps:

user constraints → pacing decisions
user level → starting difficulty
user track → task library selection
user end goal → final weeks emphasis
This is what separates “toy chatbot” from “designed system.”

10) MVP feature set (single shipped product)
Landing + onboarding wizard
Tech track selection + roadmap generation
Roadmap view + weekly detail pages/sections
Progress tracking (checkboxes, notes, week completion)
“Why this roadmap” explainability
“I fell behind” replanning (minimum: regenerate next 2 weeks with lower load)
User persistence (auth recommended; session-only is weaker for “real product”)
Export/print-friendly roadmap page (PDF optional later)
11) Non-goals (v1)
not a hiring guarantee
not a full course hosting LMS
not a social network
not promising perfect roadmaps for non-tech domains in v1
Allowed: curated optional links (articles/docs/videos) attached to tasks.

12) Success metrics
onboarding completion rate
Week 1 completion rate
return rate (user logs progress at least once)
“Week 1 realism” rating (1–5)
qualitative: felt supported / not pressured (1–5)
13) Engineering standards (“not beginner project”)
modular architecture: routes + services + data layer
validated inputs + user-friendly errors
database models for users, onboarding answers, roadmap, progress events
logging + basic tests for planning rules
responsive UI + accessibility basics (contrast, keyboard nav where possible)
README + architecture diagram + environment setup
14) Recommended tech stack
Frontend: HTML/CSS/JS (upgrade later if needed)
Backend: Flask
DB: SQLite early → PostgreSQL for production
AI layer: optional enhancement for wording + personalization after deterministic roadmap skeleton works
Deployment: choose one stable host after MVP stabilizes
15) Roadmap engine design (how “tech now, everything later” works)
Core engine (shared forever)
inputs: hours, pace, constraints, tone, timeline, level
output: weekly structure + deliverables + difficulty curve
Domain plugins (expand later)
tech_task_library.json (v1)
future: design_task_library, business_task_library, etc.
selection based on “domain/track” screen
Rule: don’t hardcode everything into one giant function. Keep libraries swappable.

16) Positioning statement (for professor / LinkedIn)
Raah is a mentor-style roadmap system for tech learners—turning goals and constraints into weekly proof-based plans with explainable reasoning, starting with high-quality tech tracks and designed to expand beyond tech without rewriting the core product.

If you want the next mentor step: tell me your exact v1 tech tracks (keep 3–4 max). I’ll help you define the task library categories per track so generation feels expert, not generic.