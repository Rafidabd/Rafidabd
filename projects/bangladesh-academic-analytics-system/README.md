# Bangladesh Academic Analytics System

I started this as a command-line program for storing and analyzing student results. It grew into a Flask application as I added ways to look at academic performance over time.

The current code covers student records, exam datasets, subject averages, rankings, trends, recurring weaknesses, risk rules and simple performance estimates. The weights and thresholds are stored in `config/config.json`. The prediction methods are **heuristic calculations, not machine learning**.

## A note on this public copy

This is a **code snapshot**, not the latest local version or a finished deployment. The files are being copied from my earlier project archive and cleaned for public viewing. It does not contain the personal records or results submitted for my research.

## Running locally

Use Python 3.10 or later:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/setup_local_data.py
python app.py
```

Open `http://127.0.0.1:5000`. To use the older command-line interface, run `python main.py`.

The data files start empty. Add fictional records locally to try the app.

**Don't deploy this version publicly with real student data.** The interface doesn't have authentication or the safeguards needed for that.

## How the files fit together

- `app.py` — Flask routes and pages
- `main.py` — CLI entry point
- `config/` — subjects, grading rules and analysis thresholds
- `modules/` — data management, analytics and the academic intelligence modules
- `templates/`, `static/` — the web interface
- `examples/`, `scripts/` — empty data templates and first-run setup

## Why I started researching the problem

My system once estimated at least 80 on an upcoming mathematics quiz. I scored 55, but it was the highest mark in my group. That made me think harder about whether raw marks from different exams can be compared directly.

I'm now collecting historical NDC HSC 2026 report cards for **When 80 Doesn't Mean the Same**, a study comparing raw-score trends with students' relative standing in shared assessments. The analysis is still in progress and **is not a validated feature in this code**.

[Research page](https://github.com/Rafidabd/Rafidabd/tree/main/research/when-80)
