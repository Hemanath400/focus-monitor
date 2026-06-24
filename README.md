# 🧠 AI Developer Focus Monitor

A real-time AI-powered productivity tracking system that monitors developer activity from VS Code, analyzes behavior using machine learning, and predicts burnout risk.

---

## 🚀 Features

- 🔌 VS Code Extension for live activity tracking
- ⚙️ Flask backend API for logging events
- 🗄️ SQLite database for activity storage
- 📊 Real-time Streamlit dashboard
- 🤖 ML-based burnout prediction model
- 📈 Focus score analytics
- ⏱️ Idle vs coding behavior tracking

---

## 🏗️ System Architecture

VS Code Extension

↓

Flask API (/log)

↓

SQLite Database

↓

ML Model (Burnout Prediction)

↓

Streamlit Dashboard (Real-time UI)



---
## 🧠 Machine Learning

The system predicts burnout risk based on:
- Coding duration
- Idle time
- Activity frequency

Output:
- 🟢 Low Risk
- 🟠 Medium Risk
- 🔴 High Risk
---
## 📁 Project Structure

focus-monitor/

│

├── app/                 # Flask backend

├── dashboard/          # Streamlit UI

├── ml/                 # ML model + prediction

├── extensions/        # VS Code extension

├── data/              # SQLite DB

├── requirements.txt

└── README.md


---
## ⚙️ Installation

### 1. Clone repo
```bash
git clone https://github.com/your-username/focus-monitor.git
cd focus-monitor
---
### 2. Install Python dependencies

<pre class="overflow-visible! px-0!" data-start="2151" data-end="2194"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>pip install </span><span class="ͼ12">-r</span><span> requirements.txt</span></code></pre></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

### 3. Run backend

<pre class="overflow-visible! px-0!" data-start="2215" data-end="2245"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>python </span><span class="ͼ12">-m</span><span> app.main</span></code></pre></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

### 4. Run dashboard

<pre class="overflow-visible! px-0!" data-start="2268" data-end="2310"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>streamlit run dashboard/app.py</span></code></pre></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

### 5. Run VS Code extension

* Open `extensions/vscode`
* Press `F5`

---

## 📊 Dashboard Preview

* Real-time activity tracking
* Focus score %
* Burnout prediction
* Idle vs coding analysis

---

## 💡 Future Improvements

* Chrome extension tracking
* AI productivity coach alerts
* LLM-based suggestions
* Cloud deployment

---

## 👨‍💻 Author 	

Built as a real-time AI productivity system for developer behavior analysis and burnout prediction.

<pre class="overflow-visible! px-0!" data-start="1501" data-end="1718"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"></pre></div></div></div></div></div></div></div></div></div></div></div></div></div></pre>
