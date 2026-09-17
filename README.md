# The Unofficial Guide

Zachary Evans - Corpus: campus_life

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size: Max of 500 characters**
**Overlap: 0 characters**

For the campus_life documents, I decided to chunk the documents based on paragraph boundaries, or making it look for (\n\n), I set 500 as the max for characters in a chunk because the longest document had 549 characters, and I figure that every paragraph would be below that threshold. I did no overlap as most documents and paragraphs are self contained, so there was no need to add overlap.

## Sample Chunks

**Chunk 1** — source:admin_add_drop_deadline.txt#0 `` — produced by: chunker.py::split_documents``

```
On the add/drop deadline
```

**Chunk 2** — source: course_cs_210_workload.txt#2 `` — produced by: chunker.py::split_documents ``

```
It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 3** — source: course_phys_130.txt#3  `` — produced by: chunker.py::split_documents ``

```
The one piece of advice: the lab practical is worth 20% and almost nobody prepares for it.
```

**Chunk 4** — source: dining_verrill_street_grill.txt#1 `` — produced by: chunker.py::split_documents ``

```
I'm a junior and I've done this twice now. Wait times: up to 30 minutes on Friday evenings, otherwise under 10. The thing worth going for is the burger, which is the only late-night hot food on campus. The thing to know is that one register, so the queue is a single line no matter how busy.
```

**Chunk 5** — source: housing_morrow_house.txt#2   `` — produced by: chunker.py::split_documents ``

```
The good: cheapest housing tier by about $900 a year, and the singles are real singles.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question: "Do dining dollars transfer from spring to autumn?"**

**Answer:**

```
(best distance 0.269, cutoff 0.6)

No, dining dollars do not transfer from spring to the following autumn; whatever is left in May disappears.

Source: admin_dining_dollars.txt

Sources retrieved: admin_dining_dollars.txt, admin_meal_plan_changes.txt, money_jobs.txt

1 model calls this session, 348 tokens (316 in, 32 out)
```

**My relevance cutoff:**

The in-corpus questions had their best distances ranging from 0.2686 to 0.4056 with an average of 0.3264. The out-of-corpus questions had their best distances ranging from 0.7803 to 0.8502 with an average of 0.8169. There is a clear gap between the two groups, with the closest values being 0.3747 apart. I kept the relevance cut off at 0.6 because of this. It safely falls between the two groups while still giving some wiggle room for less sure answers to come through.

| Question | In corpus? | Best distance |
|---|---|---|
| "Do dining dollars transfer from spring to autumn?" | Yes | 0.2686 |
| "Is the Ridgeway Café open on weekends?" | Yes | 0.3016 |
| "When is it expected to be cold outside?" | Yes | 0.4056 |
| "When are the walk in hours for the health center?" | Yes | 0.3269 |
| "When are applications for studying abroad open?" | Yes | 0.3095 |
| "What is the capital of Mongolia?" | No | 0.7986 |
| "How do I change the oil in a diesel engine?" | No | 0.8502 |
| "Who won the 1994 World Cup?" | No | 0.7803 |
| "What is the recommended dosage of ibuprofen for a headache?" | No | 0.8243 |
| "How do I write a for loop in Rust?" | No | 0.8313 |


## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**

**2.**

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
