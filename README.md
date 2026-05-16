# Raah — Your Personal AI Roadmap

**Live:** [emaan.pythonanywhere.com](https://emaan.pythonanywhere.com)

Raah is an AI-powered roadmap generator that builds a personalized, week-by-week learning plan based on who you actually are — your goals, your fears, how you learn, and how much time you have. Not a generic curriculum. A roadmap made for you.

---

## Meet Riruru

Riruru is Raah's mascot and mentor. The name came from Raah itself — one night while lying in bed, the idea struck to give Raah a face. Riruru is named after a character from a childhood cartoon — a robot who was kind, strong, and always believed in the people around her. That's exactly who Riruru is inside Raah. The actual mascot illustration is me.

Riruru doesn't just generate a roadmap. She talks to you. She celebrates every task you complete. She knows your biggest fear and addresses it every single week. She's the mentor most people never had.

---

## What Raah Does

You answer 11 questions during onboarding:
- Your name and learning track
- How many hours per week you have
- Your timeline (1 month, 3 months, 6 months)
- Your current skill level
- Your 3-month goal
- How you learn best
- What keeps you consistent
- Your guidance tone preference
- Your biggest fear

Raah takes all of that and generates a full personalized roadmap — week by week, task by task, with a real project every single week. No theory-only weeks. No generic advice.

---

## Tracks Available

- Web Development
- Artificial Intelligence
- Software Engineering
- Cybersecurity
- Data Science
- Internship Preparation

---

## Features

**Personalized Roadmap Generation**
Every roadmap is generated fresh using Groq's LLaMA 3.3 70B model based on your exact answers. No two roadmaps are the same.

**Riruru Reactions**
Every time you complete a task, Riruru responds personally — addressing you by name, connecting the task to your fear and your goal. Powered by AI, feels human.

**XP System**
Earn 10 XP for every completed task. Watch your progress bar fill up as you move through your roadmap.

**Week Locking**
Weeks unlock progressively. You can't skip ahead — you earn each week by completing the one before it.

**Save and Restore Progress**
No account needed. Generate a save code that encodes your entire progress. Share your device, come back later, give it to a friend — paste the code and pick up exactly where you left off.

**Mobile Responsive**
Fully usable on phone. Built for students on the go.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| AI | Groq API — LLaMA 3.3 70B |
| Session Management | Flask-Session (filesystem) |
| Frontend | HTML, CSS, JavaScript |
| Templating | Jinja2 |
| Fonts | Google Fonts — Quicksand, Fredoka |
| Deployment | PythonAnywhere |
| Version Control | Git, GitHub |

---

## How It Works

1. User goes through 11-step onboarding
2. Answers are stored in session
3. A detailed prompt is sent to Groq API with the full user profile
4. LLaMA 3.3 70B generates a personalized roadmap in structured markdown
5. A custom parser extracts weeks, tasks, notes, proof of work, and fallback plans
6. Roadmap is displayed week by week with interactive task completion
7. Each task completion triggers another AI call for a personal Riruru reaction

---

## Running Locally

```bash
git clone https://github.com/EmaanInk/raah.git
cd raah
pip install flask flask-session groq python-dotenv
```

Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```

Run:
```bash
python app.py
```

Open `http://127.0.0.1:5000`

---

## Project Structure

```
raah/
├── app.py              # Flask backend, all routes, AI integration
├── templates/          # Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   ├── onboarding_step_1.html ... onboarding_step_11.html
│   ├── summary.html
│   ├── roadmap.html
│   ├── week_focus.html
│   ├── save_code.html
│   └── restore.html
├── static/
│   ├── css/style.css
│   ├── js/main.js
│   └── images/         # Riruru illustrations
├── flask_sessions/     # Server-side session storage
├── requirements.txt
└── .env                # Not committed — add your own
```

---

## What's Coming in V2

- User accounts and persistent database storage
- Streak tracking and consistency rewards
- Community roadmaps — share your roadmap with others
- Progress certificates
- More tracks including UI/UX and Mobile Development
- Riruru voice messages

---

## Built By

**Emaan** — CS student, 4th semester, building in public.

Raah started as an idea that struck at night while lying in bed. It became the project I'm most proud of. V1 is everything I wanted it to be.

Follow the journey: [LinkedIn](www.linkedin.com/in/emaan-khan-476698407) | [GitHub](https://github.com/EmaanInk)
