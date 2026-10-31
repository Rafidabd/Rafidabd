# When 80 Doesn't Mean the Same

*An ongoing study of examination marks and student progress at Notre Dame College, Dhaka.*

**Independent research · HSC 2026 cohort · October 2026**

## Why I started

An early version of my academic analytics system predicted that I'd score at least 80 on my next mathematics quiz. I got 55. It was the highest score in my group.

The prediction missed something important: a mark doesn't tell the whole story when the examination itself changes. That made me question the way I'd been comparing results across different exams.

## What I'm trying to find out

**When a student's marks rise or fall between examinations, does their standing among students taking those same examinations always move in the same direction?**

I'm comparing raw percentage scores with performance relative to the *participating students* who took each assessment. I'm not assuming one measure is automatically fairer or more accurate. I want to see where they agree, where they disagree, and what that means for my software.

## The records

The study uses historical records from NDC's **HSC 2026 cohort**. I'm collecting the three report cards issued during a student's time at the college: **Term, Sent-Up 1 and Sent-Up 2**. Together, these include monthly quiz rounds and major examinations.

NDC has three departments—Science, Humanities and Business Studies—with different subject combinations. I'll make comparisons within suitable departments, subjects and papers rather than mixing unrelated exams.

**Progress on October 31, 2026:** I have reported receiving records from **30 students**. I haven't completed the checks for duplicates, legibility, missing marks and usable comparisons, so I'm not publishing an analyzed sample size or findings yet.

## Planned analysis

1. Separate the **actual quiz and exam marks** from the **weighted totals** on the report cards. The totals reuse earlier assessment components and cannot be treated as separate independent exams.
2. Reconstruct subject-by-subject histories and compare like with like wherever possible.
3. For each shared assessment with enough readable records, compare scores with the distribution **in the participating sample**. Standardized scores and percentiles are candidates.
4. Count cases where raw marks and relative standing change in different directions. Then check whether those cases depend on missing data or the comparison method.

These are planned steps, not completed results. Details and open decisions are in the [methods note](METHODS.md).

## Limits

A lower average in the participating sample does **not** prove that a question paper was harder. Preparation, marking, syllabus coverage and sample composition can all matter. Standing in a volunteer sample is not an official NDC rank, and neither raw nor relative scores measure a student's true ability.

This is a single-institution study. I won't use it to make claims about all Bangladeshi students.

## The related software

This question came out of building my **Bangladesh Academic Analytics System**, a Python/Flask project for storing academic histories and analyzing performance over time. It has modules for history, trends, risk, heuristic prediction and more. The research is a way to question an assumption behind parts of that work: that scores from different assessments can be compared directly.

The latest software source isn't fully public yet. I'm preparing a separate, privacy-reviewed code release.

**Read:** [One-page brief](BRIEF.md) · [Method and limitations](METHODS.md) · [Progress log](PROGRESS.md) · [Visual explanation (HTML file)](../../docs/when-80/index.html)

*Status: data collection and study design in progress. No findings, publication, peer review or validated prediction results are claimed.*
