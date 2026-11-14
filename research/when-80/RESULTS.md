# When 80 Doesn't Mean the Same
## First results, October 31, 2026

I started this after my academic analytics program predicted at least 80 for my next mathematics quiz. I scored 65, the highest mark in my group. It made me wonder how often a change in marks tells a different story from a change in relative standing.

I've now compared report card histories from 20 students in Notre Dame College's HSC 2026 batch. It's a small, preliminary analysis, but I finally have a number for the question I started with.

**In 148 of 814 comparisons (18.2%), the raw mark and relative standing moved in opposite directions.**

Of those 148 cases, 36 involved a lower raw mark but higher relative standing. The other 112 involved a higher raw mark but lower standing.

These are *repeated comparisons for individual students across quizzes*, not different students. The same student appears across several subjects and rounds.

### What I compared

I used consecutive quiz rounds within the same subject and report period: Term, Sent Up I or Sent Up II. Each comparison uses only students who had numerical marks for **both** quizzes. I calculated their percentile standing within that same group for each quiz, assigning tied scores a midpoint rank.

I kept the individual quiz marks separate from NDC's weighted report card totals. I didn't use official across the whole college places as quiz ranks, and I didn't mix first year and second year papers into the same comparison.

| Measure | Count |
| --- | ---: |
| Students with report cards available | 20 |
| Comparable consecutive quiz pairs | 57 |
| Students in each matched group | 14 to 18 |
| Matched comparisons of individual students' quiz marks | 936 |
| Cases where both measures changed | 814 |
| Opposite direction changes | 148 (18.2%) |

The other 122 comparisons had no change in at least one measure, so I left them out of the 18.2% denominator.

### A Mathematics example

In one first year Mathematics pair, a student went from **44 in Quiz 2 to 40 in Quiz 3**. Within the 17 students whose marks were available for both quizzes, that student's percentile standing moved from **29.4% to 64.7%**.

The matched group's average fell from **56.9 to 33.6** between those quizzes. The student's mark fell, but their position within the same group improved.

That doesn't prove Quiz 3 was harder. I can't separate paper difficulty from preparation, marking or other changes using these marks alone.

### Results by subject

| Subject | Opposite direction cases | Cases where both measures changed | Share |
| --- | ---: | ---: | ---: |
| Bangla | 30 | 122 | 24.6% |
| English | 28 | 139 | 20.1% |
| ICT | 11 | 37 | 29.7% |
| Mathematics | 27 | 133 | 20.3% |
| Physics | 11 | 130 | 8.5% |
| Chemistry | 24 | 126 | 19.0% |
| Biology | 17 | 127 | 13.4% |

ICT has fewer usable quiz comparisons because several quiz columns weren't used. These percentages describe the available comparisons; they don't show that one subject is inherently harder than another.

### Checking the result another way

I repeated the count after requiring a raw score change of at least **5 marks** and a percentile change of at least **10 percentage points**. There were still **79 cases with changes in opposite directions among 628 qualifying comparisons (12.6%)**.

Using standardized scores instead of percentiles gave **142 cases with changes in opposite directions among 850 comparisons where both measures changed (16.7%)**. The two standing measures can treat ties and score distributions differently, which is why their counts aren't identical.

### What I take from this

For these students and quizzes, a raw score trend sometimes leaves out what happened in the rest of the participating group. That's enough for me to question a dashboard that shows only a rising or falling mark.

It isn't enough to say relative standing is fairer, or that a falling mark means the exam was harder. A volunteer group's standing isn't an official NDC rank. This pilot uses only 20 histories, some incomplete; its results may change when I review the extraction and rerun the analysis using the expanded observed dataset. Also, repeated comparisons from the same people aren't independent observations, so I'm not using this percentage as a population estimate or claiming statistical significance.

**Record status, November 14, 2026:** I have 31 observed student histories: **20 transcribed from supplied report cards** and **11 entered from handwritten notes and subsequently checked against their source records**. The working file also contains **4 synthetic test histories**, which are not student observations. The 35 total working-file entries must not be described as 35 participants. This October 31 pilot calculation uses only the **original 20 report-card histories**; the 11 additional verified histories and four synthetic examples were not included in these results.

This is a first descriptive result, not a finished paper. My next step is to rerun the comparisons with the 31 observed student histories, check the extraction with a second pass, look more carefully at missing marks and ties, and see whether showing both measures actually makes my analytics software easier to understand.

*The underlying report cards and individual student marks are private.*

[Research overview](README.md) · [Method notes](METHODS.md) · [About the data](DATA.md)
