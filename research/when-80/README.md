# When 80 Doesn't Mean the Same

*An ongoing study of examination marks and student progress at Notre Dame College, Dhaka.*

**Independent research · HSC 2026 cohort · October 2026**

## Why I started

An early version of my academic analytics system predicted that I'd score at least 80 on my next mathematics quiz. I got 65. It was the highest score in my group.

The prediction made me wonder what I'd missed. I couldn't tell from the mark alone whether I was doing worse, or whether that particular quiz had been different. That question stayed with me as I kept building the program.

## What I'm trying to find out

**For the same students taking comparable quizzes, how often do changes in raw marks and changes in their relative standing point in opposite directions?**

I'm comparing raw percentage scores with standing among the *participating students* who have marks for both quizzes. I'm not assuming either measure is automatically fairer or more accurate. I want to see where they agree, where they disagree and whether the answer changes when I use percentiles instead of standardized scores.

I also want to understand what the findings might mean for my software. That is a question for a later interface experiment, not something the report card data alone can answer.

## The records

The study uses historical records from NDC's **HSC 2026 cohort**. I'm collecting the three report cards issued during a student's time at the college: **Term, Sent Up 1 and Sent Up 2**. Together, these include monthly quiz rounds and major examinations.

NDC has three departments: Science, Humanities and Business Studies, with different subject combinations. I'll make comparisons within suitable departments, subjects and papers rather than mixing unrelated exams.

## Why this setting matters

At NDC, monthly quizzes and larger internal examinations are part of the same academic history. Students get three major report cards, but the combined scores on those cards may reuse earlier marks. These are college assessments, not the national HSC board exams. Comparing the totals as if they were new examinations would tell the wrong story.

It's a useful place for me to begin because the same students have repeated assessments across time. That gives me a chance to ask a narrower question than whether the marks are "fair": does a change in the raw mark always match a change in the student's position in the participating group?

The study is based on one college, not a sample of all Bangladesh. It can't establish how often the same issue occurs elsewhere.

## Who might find the question useful?

**Students** may want to know whether a drop in marks also meant a drop in standing on that assessment. **Teachers** may find a second comparison useful when discussing a change in results, alongside their knowledge of the class and paper. **Families** could have a better starting point for talking about progress without reducing it to a single number.

For me, as someone building education software, the question is also about what a dashboard should say when the available measures disagree. These are possible uses to investigate, not benefits the study has shown.

A rise in relative standing isn't proof that a student learned more. It might reflect how everyone else performed. That's why I don't want the answer to be "replace marks with ranks." I want to know when the two views disagree and what each one can actually tell us.

**First results, October 31, 2026:** The published pilot used **20 histories transcribed from supplied report cards**. In **148 of 814 comparisons (18.2%)** where both measures changed, raw marks and relative standing moved in opposite directions. This is preliminary; [the full breakdown is here](RESULTS.md).

**Record update, November 14, 2026:** I have since checked **11 additional histories** originally entered from handwritten notes against their source records. This brings the observed research set to **31 student histories**. The working file also has **4 synthetic software-test histories**, which are not student observations. The published pilot results above still use only the original 20 histories and have not been recalculated with all 31.

## The first calculation

I compared consecutive quizzes within the same subject, using students with a mark in both rounds to calculate their relative standing. The matched groups had between 14 and 18 students. The result is an early descriptive count, not a claim about everyone at NDC. I also checked the pattern with a minimum change threshold and standardized scores; details are in the [results note](RESULTS.md).

Although I have checked the additional handwritten histories against their sources, I still need to rerun the comparisons using the full observed set and review the transcriptions carefully before drawing stronger conclusions. I haven't tested the dashboard interface with students yet.

## Limits

A lower average in the participating sample does **not** prove that a question paper was harder. Preparation, marking, syllabus coverage and sample composition can all matter. Standing in a volunteer sample is not an official NDC rank, and neither raw nor relative scores measure a student's true ability. A relative measure can be misleading too, especially when only a small or changing group of students is available.

This is a study at one college. I won't use it to make claims about all Bangladeshi students.

## The related software

This question came out of building my **Bangladesh Academic Analytics System**, a Python/Flask project for storing academic histories and analyzing performance over time. It has modules for history, trends, risk, heuristic prediction and more. The research is a way to question an assumption behind parts of that work: that scores from different assessments can be compared directly.

I've published a [source snapshot](../../projects/bangladesh-academic-analytics-system/README.md) without the local student data. The newest local changes aren't all in that copy.

**Read:** [First results](RESULTS.md) · [Research website](https://rafidabd.github.io/Rafidabd/when-80/) · [Short abstract](BRIEF.md) · [Method and limitations](METHODS.md) · [About the records](DATA.md) · [Progress log](PROGRESS.md)

*This is an early descriptive analysis, not a finished paper.*
