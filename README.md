# Hi, I'm Rafid 👋

I'm a student at Notre Dame College, Dhaka. I started learning Python by making small programs, but I've become more interested in building things that help me understand a problem properly.

Most of my coding time goes into student performance and education. Outside of that, I play chess and have spent a big part of college organizing events with the Notre Dame Chess Club.

## What I'm building

**[Bangladesh Academic Analytics System (AAS)](projects/bangladesh-academic-analytics-system/README.md)** — A Python and Flask project for tracking academic records over time, with subject analysis, trends, risk rules and heuristic predictions. [Try the newer interactive demo](https://aas-admissions-demo-rfd.onrender.com) · [Browse the earlier public code snapshot](projects/bangladesh-academic-analytics-system/). The demo uses fictional sample records; the snapshot does not include all of the demo's newer features.

**[When 80 Doesn't Mean the Same](research/when-80/README.md)** — My ongoing study of raw exam marks and relative standing among students who took the same assessments. [Research website](https://rafidabd.github.io/Rafidabd/when-80/) · [First pilot results](research/when-80/RESULTS.md) · [Method and limitations](research/when-80/METHODS.md).

**[NIRAPOD](projects/nirapod/README.md)** — A Bangla-first, English-supported prototype for examining suspicious messages, online claims and scam warning signs. [Read the project overview](projects/nirapod/README.md). The source is still private, and I haven't released a public demo.

**[unwind.](https://github.com/Rafidabd/unwind-playground)** — A browser playground I started while waiting for other projects to load. Break things, build marble runs, paint a wall, mess with chess pieces, or go destroy Saturn. [Play it](https://rafidabd.github.io/unwind-playground/) · [Browse the code](https://github.com/Rafidabd/unwind-playground).

### How one led to the other

My analytics program once estimated that I'd score at least 80 on a mathematics quiz. I scored 65, which turned out to be the highest mark in my group.

It was a pretty good reminder that a prediction can be wrong for reasons the code doesn't understand. I had been comparing marks across exams without paying enough attention to how different the exams themselves could be.

That's what led me to start *When 80 Doesn't Mean the Same*. I've been collecting report cards and older marks from NDC's HSC 2026 batch. My first public analysis uses 20 histories I could trace to supplied report cards: in 148 of 814 matched quiz comparisons where both measures changed, raw marks and relative standing moved in opposite directions (18.2%). Another 11 histories entered from handwritten notes still need source checks, and four synthetic histories are reserved for software tests. None of those 15 entries went into the pilot result. It's an early result, not a finding about the entire college.

[Research website](https://rafidabd.github.io/Rafidabd/when-80/) · [First results](research/when-80/RESULTS.md) · [Read the method](research/when-80/METHODS.md) · [See the progress notes](research/when-80/PROGRESS.md)

### More about the software

The Academic Analytics System began as a command line project. I gradually added student histories, subject analysis, trend and risk rules, and heuristic predictions before building a Flask interface around it.

I also have an [interactive demo](https://aas-admissions-demo-rfd.onrender.com) where visitors can explore the student, admission preparation and educator tools with fictional sample data, without signing up. It's a preview, not a place for real student records. The public source linked above is a cleaned snapshot of an earlier version, not the complete code behind the newer demo. I haven't called the prediction system machine learning because it isn't.

## Earlier code

- [Student Performance Tracker](https://github.com/Rafidabd/student-performance-tracker) — one of my earlier Python projects for student records, rankings, charts and CSV reports.
- [Expense Tracker CLI](https://github.com/Rafidabd/expense-tracker-cli) — a command line expense tracker that saves records and summarizes spending.

I mostly work in **Python**, with **Flask, HTML, CSS, JavaScript, Jinja2, JSON and CSV** for the web and data parts of my projects. I've also used **Matplotlib, Git and testing tools** while learning how to organize larger programs.

## Away from the keyboard

Chess has been a big part of my life outside coding. I joined the Notre Dame Chess Club as a volunteer and eventually became its president, which meant a lot of time organizing tournaments, coaching chess teams, working with volunteers and handling unexpected changes. I've also competed in debates and coached debate teams, taken part in math and English olympiads, played football as a goalkeeper and helped with student publications.

I'm still learning a lot, and I like having the earlier projects here alongside the newer ones. They show how I got from small Python exercises to problems I now want to spend much more time on.
