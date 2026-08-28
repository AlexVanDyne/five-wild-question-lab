# Five Wild Question Lab

A local-first prototype for testing a specific trivia-content thesis:

> AI proposes sourced question candidates. Humans approve, revise, or reject them. Player data calibrates difficulty. Strong, versioned questions become a reusable trivia database.

The prototype is intentionally designed around the **editorial loop**, not around a single AI provider.

## Quick start

### Fastest option

Open `Five_Wild_Question_Lab.html` in a modern desktop browser. It is a standalone build with no installation step.

### Recommended option

Serve the project folder locally so browser storage and downloads behave consistently:

```bash
cd five-wild-question-lab
python3 -m http.server 8080
```

Then open `http://localhost:8080`.

No backend, API key, account, or internet connection is required for the seeded prototype.

## What is implemented

### Generation Lab

- Select a verified fact package before generating wording.
- Generate three demo variants at different clue distances.
- Paste structured candidates from a real AI model.
- Run deterministic preflight checks for answer leakage, scope, temporal validity, source presence, and possible duplication.
- Edit a candidate before placing it in the review queue.
- Preserve model name and prompt-version metadata for imported candidates.

The built-in generator is deterministic demo data. It exists to exercise the workflow without exposing an API key in browser code. Use **Paste AI batch** to test real model output.

### Human review

- Three-stage review: blind solve, answer/evidence reveal, assessment and decision.
- Separate hard gates for correctness, uniqueness, source quality, temporal validity, appropriateness, and duplication.
- Independent 1–5 ratings for clarity, fairness, interestingness, wording, and predicted difficulty.
- Difficulty is excluded from the editorial quality score.
- Reviewer-role simulation for general reviewers, fact checkers, and editors.
- Approval eligibility is recalculated from configurable thresholds.
- A reviewer can replace their own review, but cannot count twice on one revision.

### Immutable revisions

- Human rewrites create a new revision instead of overwriting the old one.
- Reviews remain attached to the exact revision they evaluated.
- The new revision returns to blind review.
- Historical player records retain the exact revision ID served.

### Trivia database

- Search and filter by prompt, answer, category, status, origin, and difficulty.
- Inspect the fact package, sources, answer policy, reviews, telemetry, revision history, and Five Wild provenance.
- Publish approved revisions, retire published questions, or open disputes.
- Export the full dataset or a filtered subset as JSON.

### Playable mini-round

- Builds a round from published questions and optional approved previews.
- Excludes sibling variants from the same question family.
- Records exact revision IDs, submitted answers, adjudication method, response time, skips, feedback, and host overrides.
- Uses deterministic alias matching; close responses are surfaced for host review.
- Updates smoothed empirical difficulty after sufficient attempts.

### Five Wild capture

- Captures Who, What, When, Where, Wild, and helper components.
- Preserves session, player, original wording, adjustment state, and table resolution.
- Stores the result as `origin = five_wild_capture`, `status = draft`.
- Routes it through the same fact-checking and editorial process as AI-generated candidates.

### Method and settings

- Experiment hypotheses and falsification conditions.
- A recommended pilot protocol.
- Configurable approval thresholds and Bayesian ranking prior.
- Reviewer calibration display.
- Full local-data export, import, and seeded-data reset.

## Suggested first test

1. Open **Review Queue** and review the ambiguous “largest desert” control before looking at its answer.
2. Create a new revision that adds “by total area.”
3. Review the revised version as three different reviewer roles.
4. Publish it once the approval rules pass.
5. Run a mini-round and record player feedback.
6. Compare the old and new revision histories in the database.
7. Generate or paste a batch from another fact and measure approval yield.

The seeded weak controls are:

- “What is the largest desert in the world?” — intended to test scope ambiguity.
- “Which country invented pizza?” — intended to test factual overreach and source mismatch.

## Data persistence

The prototype stores its state in browser `localStorage` under:

```text
five-wild-question-lab.v1
```

Use **Export** regularly during extended testing. The full export contains facts, sources, question families, revisions, reviews, settings, activity records, and the active or completed play session.

## Imported AI candidate format

Known fact IDs inherit their answer policy, explanation, source package, tags, and temporal classification:

```json
[
  {
    "factId": "f-shortest-war",
    "prompt": "Which war between Britain and the Zanzibar Sultanate lasted less than an hour?",
    "canonicalAnswer": "The Anglo-Zanzibar War",
    "aliases": ["Anglo Zanzibar War"],
    "category": "History",
    "targetDifficulty": 3,
    "generatedStyle": "Contextual clue",
    "model": "Model name",
    "promptVersion": "pilot-v1"
  }
]
```

An unlinked candidate must additionally include:

```text
factClaim
sourcePublisher
sourceEvidence
```

This prevents an unsupported question from appearing to be grounded merely because it was imported.

## Prototype limitations

- It is single-user and local-first; it does not implement authentication, row-level security, or concurrent review assignment.
- The built-in candidate generator is simulated. Real model output is supported by JSON import rather than a browser-side API key.
- Duplicate detection uses exact fact-family linkage and lexical similarity, not production embeddings.
- Seeded source records are representative evidence metadata. A production system should store live URLs, access dates, excerpts or evidence summaries, source snapshots where legally appropriate, and re-verification schedules.
- Reviewer trust and calibration values are illustrative.
- The game-test matcher is intentionally conservative and is not a complete natural-language adjudication engine.

## Project files

```text
Five_Wild_Question_Lab.html    Standalone bundled build
PROTOTYPE_TEST_PLAN.md         Recommended validation study
schema.sql                     Production-oriented PostgreSQL starting schema
sample-ai-batch.json           Example external model import
VALIDATION.md                  Automated prototype validation record
preview.png                    Interface preview
```

## Production transition

The recommended production path remains:

- Next.js frontend
- Supabase/PostgreSQL source of truth
- Supabase Auth and row-level security
- pgvector for semantic duplicate retrieval
- background workers for generation, embeddings, expiration, and score recalculation
- provider-independent AI gateway

The manual database and editorial workflow should be productionized before automatic generation volume is increased.
