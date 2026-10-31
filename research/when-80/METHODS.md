# Method notes

*Method for the first exploratory comparison, with further checks still underway. Updated October 31, 2026.*

## Records and measures

NDC's HSC 2026 students received three printed academic reports: Term, Sent Up 1 and Sent Up 2. They include major exam results and corresponding monthly quizzes. Science, Humanities and Business Studies have different subjects; first year and second year papers also need to be distinguished.

Each report contains weighted combined results, which reuse quiz marks and sometimes earlier major exam performance. I keep **component marks** and **combined totals** separately. Counting both as distinct assessments would artificially duplicate information.

## Data handling

Each extracted row identifies an anonymous participant code, department, subject/paper, assessment, quiz/major exam type, mark and maximum mark. Missing or illegible values will be recorded rather than guessed.

As of October 31, 2026, the working file contains 20 histories transcribed from report cards, 11 additional histories entered from handwritten notes, and four synthetic examples created for software testing. The first analysis uses only the 20 histories traced to report cards. I haven't included the histories entered from offline notes while their individual sources still need checking, and synthetic entries are never treated as observations. Matched groups for eligible quiz pairs contained 14 to 18 students.

Report card photos and original Google Form responses will stay in restricted storage. Google Forms login for uploads doesn't make the collection process fully anonymous. No report cards, names, IDs, participant level marks or response screenshots are being published here.

## How I'll compare scores

The first analysis compares consecutive pairs of quizzes in the **same subject and report period**. For each pair, I used students who had valid marks for **both** quizzes. That matters: if one quiz has a different set of students, a change in the sample average might reflect who is included rather than a change in the assessment.

1. **Raw marks:** convert scores to percentages where the maximum marks are known; note whether each student's mark rose or fell.
2. **Relative standing:** compare each mark with the distribution of scores for those *same participating students* on each quiz. I checked both standardized scores and midpoint percentiles, using scores only where the matched group had usable variation.
3. **Different directions:** count occasions when raw marks rise while relative standing falls, or the reverse. I assigned tied marks a midpoint percentile rank. Comparisons with no change in either measure did not enter the directional denominator.

If too few students have matching marks for a subject or quiz pair, I'll leave it out rather than report a shaky comparison. Comparing quizzes with major exams, or first year papers with second year papers, needs separate treatment.

## Deciding what counts as a disagreement

For each comparable pair of quizzes, I'll record whether the raw percentage and the chosen relative standing measure went up, down or stayed the same for each student.

A **directional disagreement** is when one rises while the other falls. Ties and very small changes will be reported separately instead of being forced into an increase or decrease. I calculated the main result using nonzero changes in both measures, then checked sensitivity with a minimum of five marks and ten percentile points.

For standardized scores, I need a usable spread of marks; if everyone in the matched group has the same score, the standard deviation is zero and a z score cannot be calculated. Percentiles may also be coarse or tied in a small group. The report will say when those comparisons aren't informative.

The [first results](RESULTS.md) report the number of **students**, the number of eligible **quiz pairs**, and the number of **paired changes for individual students**. Several observations from one student are not the same as several independent participants. The pilot describes patterns rather than treating every change as independent evidence for a statistical test.

## Checks before conclusions

- Confirm unique participant count, complete/legible reports and permission to use records.
- Verify quiz labels, chronology, subject identity and score maxima.
- Report how many students can be matched in **each pair** of assessments. Thirty submissions do not mean thirty usable scores in every subject.
- See whether the overall picture changes with percentiles instead of standardized scores, and after leaving out incomplete histories.
- Report the number of students as well as the number of paired changes. Repeated observations from one student are not independent participants.
- Ask a statistics/education mentor to check the method before external submission.

Retrospective prediction benchmarking may be considered later, but it has **not** been carried out. It would require preventing future information from entering earlier predictions.

## Limits of the comparison

A lower average doesn't necessarily mean an exam was harder. It could also reflect preparation, marking, the material tested or who submitted records. Relative standing in this sample is not an official college rank.

The study can show where two descriptions of performance disagree. It cannot tell me a student's underlying ability or which description is automatically more useful. A relative measure can also hide things: someone's standing may change because of who is in the comparison group, not only because of the student's own work. The participants are from one college, so I won't treat the findings as representative of Bangladesh.

## What the findings might be used for

One practical question is whether a dashboard ought to show raw and relative trends together, or whether that would make things more confusing. The report card analysis alone can't answer whether students, teachers or parents would understand or benefit from such a display. That would need a separate interface study or feedback from actual users.

I'll keep that distinction clear when discussing how this work relates to the Bangladesh Academic Analytics System.
