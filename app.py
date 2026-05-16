from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session
from groq import Groq
from dotenv import load_dotenv
import os
import re
import json
import base64
import zlib

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

app = Flask(__name__)
app.jinja_env.globals.update(enumerate=enumerate)
app.secret_key = "EMAAN_SECRET_KEY_2026"

# Server-side session config
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = os.path.join(os.path.dirname(__file__), 'flask_sessions')
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = 86400
os.makedirs(app.config['SESSION_FILE_DIR'], exist_ok=True)
Session(app)

def parse_roadmap(text):
    weeks = []
    sections = re.split(r'##\s*Week\s*\d+', text, flags=re.IGNORECASE)
    titles = re.findall(r'##\s*Week\s*\d+\s*[:—\-]*\s*(.+)', text, flags=re.IGNORECASE)
    
    for i, section in enumerate(sections[1:]):
        if not section.strip():
            continue
        
        week = {}
        week['number'] = i + 1
        week['title'] = titles[i].strip() if i < len(titles) else f"Week {i+1}"
        
        tasks = re.findall(r'-\s*(.+)', section)
        clean_tasks = []
        for t in tasks:
            if "**Your proof" in t or "**If you fall" in t:
                break
            clean_tasks.append(t.strip())
        week['tasks'] = clean_tasks
        
        def extract(pattern, default=""):
            match = re.search(pattern, section, re.DOTALL | re.IGNORECASE)
            return match.group(1).strip() if match else default

        week['note'] = extract(r'\*\*A personal note.*?\*\*\s*(.+?)(?=\*\*|$)', "Stay focused!")
        week['proof'] = extract(r'\*\*Your proof.*?\*\*\s*(.+?)(?=\*\*|$)', "Complete the tasks.")
        week['fallback'] = extract(r'\*\*If you fall behind.*?\*\*\s*(.+?)(?=\-\-\-|$)', "Take a breath and restart.")
        
        weeks.append(week)
    
    return weeks


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/onboarding")
def onboarding():
    return redirect(url_for("onboarding_step_1"))


@app.route("/onboarding/step-1", methods=["GET", "POST"])
def onboarding_step_1():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if not name:
            return render_template("onboarding_step_1.html",
                error="Please tell Raah your name. Riruru would love to get to know you.")
        onboarding_data = session.get("onboarding", {})
        onboarding_data["name"] = name
        session["onboarding"] = onboarding_data
        return redirect(url_for("onboarding_step_2"))
    return render_template("onboarding_step_1.html")


@app.route("/onboarding/step-2", methods=["GET", "POST"])
def onboarding_step_2():
    if request.method == "POST":
        track = request.form.get("track", "").strip()
        if not track:
            return render_template("onboarding_step_2.html", error="Please choose a track.")
        onboarding_data = session.get("onboarding", {})
        onboarding_data["track"] = track
        session["onboarding"] = onboarding_data
        return redirect(url_for("onboarding_step_3"))
    return render_template("onboarding_step_2.html")


@app.route("/onboarding/step-3", methods=["GET", "POST"])
def onboarding_step_3():
    if request.method == "POST":
        hrs_per_week = request.form.get("hrs_per_week", "").strip()
        if not hrs_per_week:
            return render_template("onboarding_step_3.html", error="Please enter hours.")
        onboarding_data = session.get("onboarding", {})
        onboarding_data["hrs_per_week"] = hrs_per_week
        session["onboarding"] = onboarding_data
        return redirect(url_for("onboarding_step_4"))
    return render_template("onboarding_step_3.html")


@app.route("/onboarding/step-4", methods=["GET", "POST"])
def onboarding_step_4():
    if request.method == "POST":
        time_horizon = request.form.get("time_horizon", "").strip()
        if not time_horizon:
            return render_template("onboarding_step_4.html", error="Please choose your time horizon.")
        onboarding_data = session.get("onboarding", {})
        onboarding_data["time_horizon"] = time_horizon
        session["onboarding"] = onboarding_data
        return redirect(url_for("onboarding_step_5"))
    return render_template("onboarding_step_4.html")


@app.route("/onboarding/step-5", methods=["GET", "POST"])
def onboarding_step_5():
    if request.method == "POST":
        study_year = request.form.get("study_year", "").strip()
        if not study_year:
            return render_template("onboarding_step_5.html", error="Please select your current year.")
        onboarding_data = session.get("onboarding", {})
        onboarding_data["study_year"] = study_year
        session["onboarding"] = onboarding_data
        return redirect(url_for("onboarding_step_6"))
    return render_template("onboarding_step_5.html")


@app.route("/onboarding/step-6", methods=["GET", "POST"])
def onboarding_step_6():
    if request.method == "POST":
        skill_lvl = request.form.get("skill_lvl", "").strip()
        if not skill_lvl:
            return render_template("onboarding_step_6.html", error="Please select your current skill level.")
        onboarding_data = session.get("onboarding", {})
        onboarding_data["skill_lvl"] = skill_lvl
        session["onboarding"] = onboarding_data
        return redirect(url_for("onboarding_step_7"))
    return render_template("onboarding_step_6.html")


@app.route("/onboarding/step-7", methods=["GET", "POST"])
def onboarding_step_7():
    if request.method == "POST":
        goal_3_months = request.form.get("goal_3_months", "").strip()
        if not goal_3_months:
            return render_template("onboarding_step_7.html", error="Please tell me about your goal.")
        onboarding_data = session.get("onboarding", {})
        onboarding_data["goal_3_months"] = goal_3_months
        session["onboarding"] = onboarding_data
        return redirect(url_for("onboarding_step_8"))
    return render_template("onboarding_step_7.html")


@app.route("/onboarding/step-8", methods=["GET", "POST"])
def onboarding_step_8():
    if request.method == "POST":
        learning_style = request.form.get("learning_style", "").strip()
        if not learning_style:
            return render_template("onboarding_step_8.html", error="Please select your learning style.")
        onboarding_data = session.get("onboarding", {})
        onboarding_data["learning_style"] = learning_style
        session["onboarding"] = onboarding_data
        return redirect(url_for("onboarding_step_9"))
    return render_template("onboarding_step_8.html")


@app.route("/onboarding/step-9", methods=["GET", "POST"])
def onboarding_step_9():
    if request.method == "POST":
        biggest_fear = request.form.get("biggest_fear", "").strip()
        if not biggest_fear:
            return render_template("onboarding_step_9.html", error="Tell me what you fear the most.")
        onboarding_data = session.get("onboarding", {})
        onboarding_data["biggest_fear"] = biggest_fear
        session["onboarding"] = onboarding_data
        return redirect(url_for("onboarding_step_10"))
    return render_template("onboarding_step_9.html")


@app.route("/onboarding/step-10", methods=["GET", "POST"])
def onboarding_step_10():
    if request.method == "POST":
        consistency_style = request.form.get("consistency_style", "").strip()
        if not consistency_style:
            return render_template("onboarding_step_10.html", error="Please select your consistency style.")
        onboarding_data = session.get("onboarding", {})
        onboarding_data["consistency_style"] = consistency_style
        session["onboarding"] = onboarding_data
        return redirect(url_for("onboarding_step_11"))
    return render_template("onboarding_step_10.html")


@app.route("/onboarding/step-11", methods=["GET", "POST"])
def onboarding_step_11():
    if request.method == "POST":
        guidance_tone = request.form.get("guidance_tone", "").strip()
        if not guidance_tone:
            return render_template("onboarding_step_11.html", error="Please select your guidance tone.")
        onboarding_data = session.get("onboarding", {})
        onboarding_data["guidance_tone"] = guidance_tone
        session["onboarding"] = onboarding_data
        return redirect(url_for("summary"))
    return render_template("onboarding_step_11.html")


@app.route("/summary")
def summary():
    data = session.get("onboarding", {})
    return render_template("summary.html", data=data)


@app.route("/roadmap")
def roadmap():
    data = session.get("onboarding", {})
    if not data:
        return redirect(url_for("onboarding"))

    if 'xp' not in session:
        session['xp'] = 0
    if 'current_active_week' not in session:
        session['current_active_week'] = 1
    if 'completed_tasks' not in session:
        session['completed_tasks'] = {}

    # If roadmap already exists don't regenerate
    if session.get('weeks') and len(session.get('weeks', [])) > 0:
        return render_template(
            "roadmap.html",
            weeks=session['weeks'],
            data=data,
            xp=session['xp'],
            completed_tasks=session['completed_tasks'],
            current_active_week=session['current_active_week']
        )

    prompt = f"""
You are Riruru — a warm, genuine mentor inside Raah. You are not a robot. You are like that one person in someone's life who actually believed in them when nobody else did.

You are speaking directly to {data.get('name')}. You have studied everything about them. You know their fears. You know their goal. You know how much time they have. And you have built this roadmap specifically for them — not from a template, but from genuinely thinking about their situation.

Here is who {data.get('name')} is:
- Track they want to master: {data.get('track')}
- Current skill level: {data.get('skill_lvl')}
- Hours available per week: {data.get('hrs_per_week')}
- Goal in 3 months: {data.get('goal_3_months')}
- How they learn best: {data.get('learning_style')}
- What helps them stay consistent: {data.get('consistency_style')}
- Guidance tone they want: {data.get('guidance_tone')}
- Their biggest fear: {data.get('biggest_fear')}
- Timeline: {data.get('time_horizon')}
- University year: {data.get('study_year')}

Now generate {data.get('name')}'s personal roadmap.

RULES:
- Use {data.get('name')}'s name throughout
- Their biggest fear is "{data.get('biggest_fear')}" — address it every week
- Fit within {data.get('hrs_per_week')} hours per week
- Tone: {data.get('guidance_tone')}
- Learning style: {data.get('learning_style')}
- Include a real project every week
- Go from current level to mastery

For EACH week use EXACTLY this format:

## Week [N] — [motivating theme]

**A personal note to {data.get('name')}:**
[2-3 warm sentences explaining why this week specifically]

**This week, {data.get('name')}, you will:**
- [specific task]
- [specific task]
- [specific task]
- [mini project]

**Your proof this week:**
[one concrete deliverable]

**If you fall behind, {data.get('name')}:**
[one kind sentence]

---

Generate weeks based on {data.get('time_horizon')} timeline.
End with a personal closing message from Riruru to {data.get('name')}.
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content
    except Exception as e:
        result = f"Error: {str(e)}"

    weeks = parse_roadmap(result)
    print(f"=== PARSED {len(weeks)} WEEKS ===")

    session['weeks'] = weeks
    session['roadmap'] = result
    session.modified = True

    print(f"=== SAVED TO SESSION: {len(session.get('weeks', []))} weeks ===")

    return render_template(
        "roadmap.html",
        weeks=weeks,
        data=data,
        xp=session['xp'],
        completed_tasks=session['completed_tasks'],
        current_active_week=session['current_active_week']
    )


@app.route("/complete-task", methods=["POST"])
def complete_task():
    data = request.get_json()
    week_num = str(data.get("week"))
    task_index = str(data.get("task_index"))

    completed = session.get("completed_tasks", {})
    if week_num not in completed:
        completed[week_num] = []

    if task_index not in completed[week_num]:
        completed[week_num].append(task_index)
        session["xp"] = session.get("xp", 0) + 10

    session["completed_tasks"] = completed
    session.modified = True

    return {"xp": session["xp"], "completed": completed}


@app.route("/riruru-reaction", methods=["POST"])
def riruru_reaction():
    data_json = request.get_json()
    task = data_json.get("task")
    week_title = data_json.get("week_title")
    user_data = session.get("onboarding", {})

    prompt = f"""
You are Riruru — a warm personal mentor inside Raah.

{user_data.get('name')} just completed this task: "{task}"
This was part of their week called: "{week_title}"
Their biggest fear is: "{user_data.get('biggest_fear')}"
Their guidance tone preference: "{user_data.get('guidance_tone')}"

Respond in exactly 2-3 sentences as Riruru.
- Address {user_data.get('name')} by name
- Celebrate this specific task
- Connect it to their fear or goal
- Sound warm and real, not robotic
- No emojis, no bullet points
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        reaction = response.choices[0].message.content
    except Exception as e:
        reaction = "Great work! Keep going."

    return {"reaction": reaction}


@app.route("/reset")
def reset():
    session.clear()
    session.modified = True
    return redirect(url_for('index'))


@app.route("/week/<int:num>")
def week_focus(num):
    weeks = session.get('weeks', [])
    print(f"DEBUG: Week {num} requested. Session has {len(weeks)} weeks.")

    this_week = None
    for w in weeks:
        if str(w.get('number')) == str(num):
            this_week = w
            break

    if not this_week:
        return f"Week {num} not found. Session has {len(weeks)} weeks.", 404

    data = session.get("onboarding", {})
    completed_tasks = session.get('completed_tasks', {})

    return render_template(
        "week_focus.html",
        week=this_week,
        data=data,
        completed_tasks=completed_tasks
    )


@app.route("/unlock-next-week", methods=["POST"])
def unlock_next_week():
    current = session.get('current_active_week', 1)
    session['current_active_week'] = current + 1
    session.modified = True
    return {"status": "success", "new_week": session['current_active_week']}

@app.route("/save-progress")
def save_progress():
    data = {
        "onboarding": session.get("onboarding", {}),
        "weeks": session.get("weeks", []),
        "xp": session.get("xp", 0),
        "completed_tasks": session.get("completed_tasks", {}),
        "current_active_week": session.get("current_active_week", 1)
    }
    json_str = json.dumps(data)
    compressed = zlib.compress(json_str.encode())
    code = base64.urlsafe_b64encode(compressed).decode()
    return render_template("save_code.html", code=code)


@app.route("/restore", methods=["GET", "POST"])
def restore():
    if request.method == "POST":
        code = request.form.get("code", "").strip()
        try:
            compressed = base64.urlsafe_b64decode(code.encode())
            json_str = zlib.decompress(compressed).decode()
            data = json.loads(json_str)
            session["onboarding"] = data.get("onboarding", {})
            session["weeks"] = data.get("weeks", [])
            session["xp"] = data.get("xp", 0)
            session["completed_tasks"] = data.get("completed_tasks", {})
            session["current_active_week"] = data.get("current_active_week", 1)
            session.modified = True
            return redirect(url_for("roadmap"))
        except Exception:
            return render_template("restore.html", error="Invalid code. Please check and try again.")
    return render_template("restore.html")


if __name__ == "__main__":
    app.run(debug=True)