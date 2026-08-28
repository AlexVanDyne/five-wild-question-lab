# Five Wild Question Lab — Prototype Test Plan

## 1. Research objective

Determine whether a staged system of sourced AI generation, blind human review, factual verification, immutable revision, and player calibration produces a more reliable and reusable trivia database than unreviewed AI generation or undifferentiated popularity voting.

The prototype tests the workflow and data model. It does not assume that any particular model is already a competent trivia editor.

## 2. Primary hypotheses

### H1 — Blind solving detects ambiguity

Reviewers who commit an answer before seeing the intended key will detect ambiguous or underspecified questions more reliably than reviewers who see the key first.

Primary measure: known-ambiguity recall.

### H2 — Fact-grounded generation reduces factual defects

Candidates generated from a verified fact package will produce fewer correctness, source-scope, and temporal-validity failures than free-generation candidates.

Primary measure: blocking factual defects per 100 candidates.

### H3 — Human revision creates measurable uplift

Questions returned for revision will improve in clarity, fairness, and wording on a new independently reviewed revision.

Primary measure: final-revision quality minus initial-revision quality.

### H4 — Quality and difficulty are independent

High-quality questions will exist across difficulty bands, and low player correctness alone will not predict poor editorial quality.

Primary measure: correlation between editorial quality and empirical difficulty, interpreted alongside ambiguity and complaint rates.

### H5 — Question families improve game diversity

Excluding sibling questions derived from the same fact will reduce repeated answers and repeated subject matter within a game without materially reducing pack construction success.

Primary measure: repeated-family incidents per game.

## 3. Pilot content set

Create 120 initial candidates:

| Cohort | Count | Purpose |
|---|---:|---|
| Fact-grounded AI candidates | 60 | Evaluate the proposed generation pipeline |
| Ungrounded AI candidates | 20 | Comparison group for factual and scope failures |
| Strong human-authored controls | 20 | Estimate false-rejection rate |
| Intentionally flawed controls | 20 | Estimate defect-detection recall |

Balance the set across at least six categories and four target-difficulty bands. Avoid allowing one answer, franchise, historical period, country, or celebrity to dominate the sample.

### Flawed-control classes

Use at least four controls from each class:

1. Ambiguous scope or missing qualifier.
2. Factually incorrect or source does not support the claim.
3. Time-sensitive fact without date or expiration.
4. Exact or semantic duplicate.
5. Missing reasonable answer alias or precision rule.

Do not reveal control labels to reviewers.

## 4. Review assignment

Each revision receives three independent reviews:

- two general editorial reviews;
- one verified fact-check review.

Reviewers must not review their own authored or edited questions. Reviewers should not see prior ratings or decisions before submitting.

For revised questions, assign at least two reviewers who did not review the earlier revision. This limits anchoring and allows cleaner measurement of revision uplift.

## 5. Review procedure

### Stage A — Blind solve

Record:

- proposed answer;
- confidence from 1 to 5;
- whether another answer may be defensible;
- initial interpretation notes;
- time to answer.

### Stage B — Evidence reveal

Show:

- canonical answer;
- aliases;
- explanation;
- fact claim;
- sources and evidence summaries;
- temporal classification.

### Stage C — Decision

Record hard gates:

- factual correctness;
- answer uniqueness;
- source quality and scope;
- temporal validity;
- audience appropriateness;
- duplicate status.

Record ratings:

- clarity;
- fairness;
- interestingness;
- wording;
- predicted difficulty.

Record decision:

- approve;
- needs revision;
- reject.

## 6. Approval policy for the pilot

Use the prototype defaults unless deliberately testing threshold sensitivity:

- three independent reviews;
- two correctness passes;
- one fact-checker source and correctness pass;
- no failed hard gate;
- clarity at least 4.0;
- fairness at least 4.0;
- interestingness at least 3.5;
- wording at least 3.5.

Difficulty remains outside the approval-quality calculation.

## 7. Revision study

For every salvageable `needs_revision` item:

1. An editor creates a new immutable revision.
2. The editor records the specific rationale.
3. The revision returns to blind review.
4. Prior reviews remain attached to the old revision.
5. Compare rating dimensions and hard-gate outcomes between revisions.

### Revision-uplift formula

```text
uplift = weighted_quality(final_revision) - weighted_quality(initial_revision)
```

Weighted quality:

```text
30% clarity
25% fairness
25% interestingness
20% wording
```

Also report each component separately. A composite can hide an important regression.

## 8. Player test

Build a frozen pack of approximately 50 approved revisions with balanced categories and predicted difficulty.

Target at least 20 independent player attempts per item. Larger samples are preferable for cohort-specific difficulty.

Record:

- exact question revision ID;
- raw and normalized response;
- automatic or host adjudication method;
- correctness;
- response time;
- skip;
- host override;
- good-question reaction;
- unclear wording;
- answer-should-count report;
- too-easy or too-hard reaction;
- fact-seems-wrong report.

Do not alter wording during the frozen-pack test. Corrections should create a new revision and a new test cohort.

## 9. Primary metrics

### Approval yield

```text
approved or published revisions / initial candidates
```

### Known-defect recall

```text
seeded blocking defects correctly flagged / seeded blocking defects
```

Calculate separately by defect class and review stage.

### False-rejection rate

```text
strong controls rejected / strong controls
```

### Blind-answer agreement

```text
blind answers matching accepted policy / completed blind reviews
```

Analyze alternative-plausible reports separately from simple knowledge misses.

### Post-publication issue rate

```text
material ambiguity, answer-policy, factual, or temporal reports / player serves
```

### Host-override rate

```text
manual answer adjudications / answered serves
```

A high override rate often indicates missing aliases or overly rigid matching.

### Cost per approved question

```text
(generation cost + reviewer labor + editor labor + verification labor) / approved revisions
```

### Time to publish

Measure median and 90th-percentile duration from candidate creation to publication.

## 10. Secondary metrics

- Review completion time by role.
- Reviewer agreement by category.
- Reviewer calibration against gold controls.
- Average number of revisions per published question.
- Source failures by source type.
- Duplicate rate by generation prompt and model.
- Answer-frequency concentration.
- Category and difficulty coverage.
- Player response-time distribution.
- Family exclusion rate during pack construction.

## 11. Recommended go/no-go criteria

Proceed to a multi-user production MVP when the pilot demonstrates all of the following:

1. At least 80% of known blocking defects are caught before publication.
2. Fewer than 10% of strong controls are falsely rejected.
3. Fact-grounded candidates have a materially lower factual-defect rate than ungrounded candidates.
4. Revised questions show positive median clarity and fairness uplift.
5. Published questions have a materially lower issue rate than unreviewed AI controls.
6. Reviewer and verification cost per approved question is compatible with the intended game economics.
7. The approved pool can construct balanced games without repeated families or severe coverage gaps.

These are provisional thresholds. Pre-register any changes before inspecting final pilot outcomes.

## 12. Failure interpretation

### High rejection rate, low player issue rate

The process may be overly conservative. Inspect strong-control false rejections and whether interestingness thresholds are unnecessarily restrictive.

### Low rejection rate, high player issue rate

The editorial process is not catching ambiguity, missing aliases, or source-scope defects. Strengthen blind review and fact-check rubrics before increasing generation volume.

### High reviewer disagreement

Separate category expertise, rubric ambiguity, and genuinely contested content. Do not average factual disagreement into a popularity score.

### Good editorial scores, unexpected player difficulty

Recalibrate difficulty. Do not rewrite a clear and fair question solely because it was harder or easier than predicted.

### Low approval yield but strong revision uplift

The generator may be a useful ideation system even when first-pass publishing yield is low. Compare editing cost with human-authored alternatives.

## 13. Data integrity requirements

- Store the exact revision served.
- Do not overwrite published revisions.
- Do not allow authors to approve their own work.
- Preserve rejected candidates and reason codes.
- Preserve manual answer overrides.
- Preserve question-family relationships.
- Date-bound unstable facts and expire them automatically in production.
- Keep quality, difficulty, correctness, and popularity as separate fields.

## 14. Prototype walkthrough

A compact demonstration session can be completed in approximately 20–30 minutes:

1. Review the ambiguous desert control blind.
2. Inspect why the alternative answer is plausible.
3. Rewrite it with “by total area.”
4. Switch reviewer roles and approve the new revision.
5. Publish an eligible revision.
6. Capture a Five Wild question and inspect its components.
7. Generate a fact-grounded candidate batch.
8. Add one candidate to review.
9. Play a mini-round.
10. Inspect telemetry and revision history in the database.
11. Export the full dataset.
