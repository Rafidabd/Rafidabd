# When 80 Doesn't Mean the Same

*An ongoing study of examination marks and student progress at Notre Dame College, Dhaka.*

**Independent research · HSC 2026 cohort · October 2026**

## Why I started

An early version of my academic analytics system predicted that I'd score at least 80 on my next mathematics quiz. I got 55. It was the highest score in my group.

The prediction made me wonder what I'd missed. I couldn't tell from the mark alone whether I was doing worse, or whether that particular quiz had been different. That question stayed with me as I kept building the program.

## What I'm trying to find out

**For the same students taking comparable quizzes, how often do changes in raw marks and changes in their relative standing point in opposite directions?**

I'm comparing raw percentage scores with standing among the *participating students* who have marks for both quizzes. I'm not assuming either measure is automatically fairer or more accurate. I want to see where they agree, where they disagree and whether the answer changes when I use percentiles instead of standardized scores.

I also want to understand what the findings might mean for my software. That is a question for a later interface experiment, not something the report-card data alone can answer.

## The records

The study uses historical records from NDC's **HSC 2026 cohort**. I'm collecting the three report cards issued during a student's time at the college: **Term, Sent-Up 1 and Sent-Up 2**. Together, these include monthly quiz rounds and major examinations.

NDC has three departments: Science, Humanities and Business Studies, with different subject combinations. I'll make comparisons within suitable departments, subjects and papers rather than mixing unrelated exams.

## Why this setting matters

At NDC, monthly quizzes and larger internal examinations are part of the same academic history. Students get three major report cards, but the combined scores on those cards may reuse earlier marks. These are college assessments, not the national HSC board exams. Comparing the totals as if they were new examinations would tell the wrong story.

It's a useful place for me to begin because the same students have repeated assessments across time. That gives me a chance to ask a narrower question than whether the marks are "fair": does a change in the raw mark always match a change in the student's position in the participating group?

The study is based on one college, not a sample of all Bangladesh. It can't establish how often the same issue occurs elsewhere.

## Who might find the question useful?

**Students** may want to know whether a drop in marks also meant a drop in standing on that assessment. **Teachers** may find a second comparison useful when discussing a change in results, alongside their knowledge of the class and paper. **Families** could have a better starting point for talking about progress without reducing it to a single number.

For me, as someone building education software, the question is also about what a dashboard should say when the available measures disagree. These are possible uses to investigate, not benefits the study has shown.

A rise in relative standing isn't proof that a student learned more. It might reflect how everyone else performed. That's why I don't want the answer to be "replace marks with ranks." I want to know when the two views disagree and what each one can actually tell us.

**Progress on October 31, 2026:** I've received records from **35 students**. I'm still checking the submissions for readable marks, missing entries and overlap between assessments. I haven't calculated the study's results yet.

## Planned analysis

1. Separate the **actual quiz and exam marks** from the **weighted totals** on the report cards. The totals reuse earlier assessment components and cannot be treated as separate independent exams.
2. Reconstruct subject-by-subject histories and compare like with like wherever possible.
3. For each pair of comparable quizzes, use the **same participating students** to calculate relative standing in each assessment. Standardized scores and percentiles are two measures I plan to compare.
4. Count cases where raw marks and relative standing change in different directions. Then check whether those cases depend on missing data or the comparison method.

A result showing **frequent disagreement** could make a case for testing richer ways of displaying score history. A result showing **little disagreement** would be useful too: it might mean the extra measure adds little for the quizzes studied. I don't want to decide that in advance.

These are planned steps, not completed results. Details and open decisions are in the [methods note](METHODS.md).

## Limits

A lower average in the participating sample does **not** prove that a question paper was harder. Preparation, marking, syllabus coverage and sample composition can all matter. Standing in a volunteer sample is not an official NDC rank, and neither raw nor relative scores measure a student's true ability. A relative measure can be misleading too, especially when only a small or changing group of students is available.

This is a single-institution study. I won't use it to make claims about all Bangladeshi students.

## The related software

This question came out of building my **Bangladesh Academic Analytics System**, a Python/Flask project for storing academic histories and analyzing performance over time. It has modules for history, trends, risk, heuristic prediction and more. The research is a way to question an assumption behind parts of that work: that scores from different assessments can be compared directly.

I've published a [source snapshot](../../projects/bangladesh-academic-analytics-system/README.md) without the local student data. The newest local changes aren't all in that copy.

**Read:** [Research website](https://rafidabd.github.io/Rafidabd/when-80/) · [Short abstract](BRIEF.md) · [Method and limitations](METHODS.md) · [Progress log](PROGRESS.md)

*Data collection is ongoing. The analysis is not finished.*
