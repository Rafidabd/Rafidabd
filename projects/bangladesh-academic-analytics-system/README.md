# Bangladesh Academic Analytics System

I started this as a command line program for storing and analyzing student results. It grew into a Flask application as I added ways to look at academic performance over time.

The current code covers student records, exam datasets, subject averages, rankings, trends, recurring weaknesses, risk rules and simple performance estimates. The weights and thresholds are stored in `config/config.json`. The prediction methods are **heuristic calculations, not machine learning**.

## A note on this public copy

This is a **code snapshot** of an earlier version, not the complete code behind my newer [interactive AAS demo](https://aas-admissions-demo-rfd.onrender.com). The demo lets visitors try student, admission preparation and educator tools using fictional data, without creating a real account. The files here have been cleaned for public viewing and do not contain personal records or results submitted for my research.

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

Open `http://127.0.0.1:5000`. To use the older command line interface, run `python main.py`.

The data files start empty. Add fictional records locally to try the app.

**Don't deploy this version publicly with real student data.** The interface doesn't have authentication or the safeguards needed for that.

## How the files fit together

- `app.py`: Flask routes and pages
- `main.py`: CLI entry point
- `config/`: subjects, grading rules and analysis thresholds
- `modules/`: data management, analytics and the academic intelligence modules
- `templates/`, `static/`: the web interface
- `scripts/`: creates empty local data files for testing

## A guide to the public code

If you're looking through the source instead of trying the newer demo, these are the main places to start:

- **[Flask routes](app.py):** student pages, dataset views and the analysis endpoints in this older interface.
- **[Student management](modules/student_manager.py) and [datasets](modules/dataset_manager.py):** reading, editing and organizing locally stored records.
- **[Core analytics](modules/analytics.py):** grading, averages, ranking and subject-level calculations.
- **[Performance history](modules/intelligence/performance.py), [trends](modules/intelligence/trends.py) and [risk](modules/intelligence/risk.py):** bringing together consecutive exams and applying thresholds.
- **[Heuristic prediction](modules/intelligence/prediction.py):** combining the most recent result, historical average and trend-adjusted estimate. The weights live in [config.json](config/config.json); there's no trained model.
- **[Advanced analysis](modules/intelligence/advanced_analysis.py):** comparisons such as stability, consistency, co-movement and exam context.
- **[Admission-prep course definitions](modules/admission_prep/course.py):** storing and validating topics and course units. This file isn't a complete admission-prep planner.
- **[Admission-prep unit tests](tests/test_admission_course.py):** a few checks for course and topic handling.

This is the code that is **actually in this public snapshot**. It isn't a copy of every feature or every later change in the live demo. I've kept the local student data out of this version.

## Why I started researching the problem

My system once estimated at least 80 on an upcoming mathematics quiz. I scored 65, but it was the highest mark in my group. That made me think harder about whether raw marks from different exams can be compared directly.

I've begun a small study with historical NDC HSC 2026 report cards, **When 80 Doesn't Mean the Same**, comparing raw score trends with students' standing in the same quiz groups. The first pilot uses 20 histories traced to report cards. This research is ongoing and **has not been integrated into the software as a validated feature**.

[Research website](https://rafidabd.github.io/Rafidabd/when-80/) · [First results](../../research/when-80/RESULTS.md)
