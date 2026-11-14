# Hi, I'm Rafid 👋

I'm a student at Notre Dame College, Dhaka. I started learning Python by making small programs, but I've become more interested in building things that help me understand a problem properly.

Most of my coding time goes into student performance and education. Outside of that, I play chess and have spent a big part of college organizing events with the Notre Dame Chess Club.

## Main work

| Software | Research |
| :--- | :--- |
| **[Bangladesh Academic Analytics System (AAS)](projects/bangladesh-academic-analytics-system/README.md)** | **[When 80 Doesn't Mean the Same](research/when-80/README.md)** |
| A Python and Flask project for looking at academic records over time: subject analysis, trends, risk rules, and predictions based on configurable weights. | An ongoing NDC study asking when a student's raw mark and their standing among the same participating students tell different stories. |
| [Try the interactive demo](https://aas-admissions-demo-rfd.onrender.com) · [Browse the public code snapshot](projects/bangladesh-academic-analytics-system/) | [Research website](https://rafidabd.github.io/Rafidabd/when-80/) · [First results](research/when-80/RESULTS.md) · [Methods](research/when-80/METHODS.md) |
| *The demo uses fictional records. The public source is an earlier version, not all the code behind the newer demo.* | *Ongoing research. The published pilot uses 20 report-card histories, not every entry in my working file.* |

### How one led to the other

My analytics program once estimated that I'd score at least 80 on a mathematics quiz. I scored 65, which turned out to be the highest mark in my group.

It was a pretty good reminder that a prediction can be wrong for reasons the code doesn't understand. I had been comparing marks across exams without paying enough attention to how different the exams themselves could be.

That's what led me to start *When 80 Doesn't Mean the Same*. I've been collecting report cards and older marks from NDC's HSC 2026 batch. My first public analysis uses 20 histories I could trace to supplied report cards: in 148 of 814 matched quiz comparisons where both measures changed, raw marks and relative standing moved in opposite directions (18.2%). I have since checked 11 additional histories entered from handwritten notes against their source records, bringing the observed research records to 31 students. Four synthetic histories remain separate software tests. The published pilot still uses only the original 20 report-card histories; its figures have not yet been recalculated with the additional 11. It's an early result, not a finding about the entire college.

[Research website](https://rafidabd.github.io/Rafidabd/when-80/) · [First results](research/when-80/RESULTS.md) · [Read the method](research/when-80/METHODS.md) · [See the progress notes](research/when-80/PROGRESS.md)

### More about the software

The Academic Analytics System began as a command line project. I gradually added student histories, subject analysis, trend and risk rules, and heuristic predictions before building a Flask interface around it.

I also have an [interactive demo](https://aas-admissions-demo-rfd.onrender.com) where visitors can explore the student, admission preparation and educator tools with fictional sample data, without signing up. It's a preview, not a place for real student records. The public source linked above is a cleaned snapshot of an earlier version, not the complete code behind the newer demo. I haven't called the prediction system machine learning because it isn't.

## Other things I've been building

| NIRAPOD | unwind. |
| :--- | :--- |
| **[Digital trust prototype](projects/nirapod/README.md)** | **[Browser playground](https://github.com/Rafidabd/unwind-playground)** |
| A Bangla-first, English-supported tool I'm working on for examining scam messages, suspicious posts, and online claims. It shows warning signs and possible sources to check, not automatic truth verdicts. | I got bored waiting for my actual projects to load, made a tiny universe, and kept adding things. Now there's a rage room, marble machines, chess pieces, painting, and planets to mess with. |
| [Read what it does](projects/nirapod/README.md) | [Play it](https://rafidabd.github.io/unwind-playground/) · [Browse the code](https://github.com/Rafidabd/unwind-playground) |
| *Prototype · source private · no public demo yet* | *Live website · source public* |

## Earlier code

- [Student Performance Tracker](https://github.com/Rafidabd/student-performance-tracker) — one of my earlier Python projects for student records, rankings, charts and CSV reports.
- [Expense Tracker CLI](https://github.com/Rafidabd/expense-tracker-cli) — a command line expense tracker that saves records and summarizes spending.

I mostly work in **Python**, with **Flask, HTML, CSS, JavaScript, Jinja2, JSON and CSV** for the web and data parts of my projects. I've also used **Matplotlib, Git and testing tools** while learning how to organize larger programs.

## Away from the keyboard

Chess has been a big part of my life outside coding. I joined the Notre Dame Chess Club as a volunteer and eventually became its president, which meant a lot of time organizing tournaments, coaching chess teams, working with volunteers and handling unexpected changes. I've also competed in debates and coached debate teams, taken part in math and English olympiads, played football as a goalkeeper and helped with student publications.

I'm still learning a lot, and I like having the earlier projects here alongside the newer ones. They show how I got from small Python exercises to problems I now want to spend much more time on.
