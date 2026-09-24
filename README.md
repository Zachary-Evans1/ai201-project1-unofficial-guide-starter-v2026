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

This repo uses the campus_life corpus, which contains of a bunch of short posts about information and student life at an unnamed university. The system lets a user ask questions about information covered by the corpus and retrieves relevant documents to help answer them. This is a Retrieval-Augmented Generation (RAG) AI system, which uses retrieved information from the corpus to answer a question. It also is grounded so the Gemini answers only use the provided documents without relying on outside information.

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

I only used Claude code once, to generate my chunking function. It followed my instructions well so I did not have to change anything about. I told it I wanted the documents split by paragraphs, a maximum chunk size of 500 characters and no overlap. When I tested it myself, I found that splitting at paragraphs could create chunks out of heading, such as "On the add/drop deadline," but it met my 4th criteria with 4/5 chunks being complete thoughts, and the system worked, so I left it as is for now.

**2.**

I used ChatGPT to help brainstorm a lot and also to make sure I wasn't overlooking steps. I specifically used it to help calculate the average/mean and the gap for the retrieval results. The ranges were both decently below and above the cutoff of 0.6, so I didn't change the cutoff at all. It was working and there was a clear gap between the in-corpus and out-of-corpus scores.

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
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 0/5 | 3/5 | 2/5 | MISS |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks are complete and self-contained thoughts, not sentence fragments or headings.| 4/5 | 4/5 | 4/5 | 4/5 | MET |
| 5. There should not be more than 200 chunks generated by the system.| numofchunks <= 200 | 271 | 271 | 271 | MISS |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

### Criterion 1

Produced by `run_eval.py::main`, using `generate.py::answer_from_chunks`.

### Do dining dollars transfer from spring to autumn? — run 1

- Best distance: 0.2686 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, admin_meal_plan_changes.txt, money_jobs.txt

```
No, dining dollars do not roll over from the spring semester to the following autumn; whatever is left in May disappears. (Source: admin_dining_dollars.txt)
```

### Is the Ridgeway Café open on weekends? — run 1

- Best distance: 0.2994 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_the_ridgeway_cafe.txt, dining_the_ridgeway_cafe_followup.txt, study_library_hours.txt

```
I don't have enough information in the provided documents to answer whether The Ridgeway Café is open on weekends.
```

### When is it expected to be cold outside? — run 1

- Best distance: 0.4056 (passed the gate)
- Sources retrieved: housing_innisfree_hall.txt, housing_old_brewhouse.txt, transit_walking.txt, winter_gear.txt

```
It is expected to be cold from mid-November to early March. This information comes from the document `winter_gear.txt`.
```

### When are the walk in hours for the health center? — run 1

- Best distance: 0.3269 (passed the gate)
- Sources retrieved: dining_kestrel_commons.txt, dining_the_ridgeway_cafe.txt, health_center.txt, transit_walking.txt

```
Walk-in hours for the health center are from 8am to 11am (health_center.txt).
```

### When are applications for studying abroad open? — run 1

- Best distance: 0.3095 (passed the gate)
- Sources retrieved: admin_graduation_requirements.txt, admin_study_abroad.txt, advising_registration.txt, study_library_hours.txt

```
Applications for studying abroad open in October for the following academic year (admin_study_abroad.txt).
```

### Criterion 2

Produced by `run_eval.py::main`, using `generate.py::answer_from_chunks`.

### Do dining dollars transfer from spring to autumn? — run 1

- Best distance: 0.2686 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, admin_meal_plan_changes.txt, money_jobs.txt

```
No, dining dollars do not roll over from the spring semester to the following autumn; whatever is left in May disappears. (Source: admin_dining_dollars.txt)
```

### Do dining dollars transfer from spring to autumn? — run 2

- Best distance: 0.2686 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, admin_meal_plan_changes.txt, money_jobs.txt

```
No, dining dollars do not roll over from the spring semester to the following autumn; whatever is left in May disappears. (Source: admin_dining_dollars.txt)
```

### Do dining dollars transfer from spring to autumn? — run 3

- Best distance: 0.2686 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, admin_meal_plan_changes.txt, money_jobs.txt

```
No, dining dollars do not transfer from spring to the following autumn; whatever is left in May disappears. 

Source: admin_dining_dollars.txt
```

### Criterion 3

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.6. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.799 | refused |
| How do I change the oil in a diesel engine? | 0.850 | refused |
| Who won the 1994 World Cup? | 0.780 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.824 | refused |
| How do I write a for loop in Rust? | 0.831 | refused |

### Criterion 4

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

### Criterion 5

produced by 'python app.py index' 

Corpus: campus_life                                                                            
  loaded   88 documents, 27,908 characters, ~317 characters per document
  chunked  271 chunks, 101 characters on average (shortest 10, longest 373), produced by chunker.py::split_documents
  embedding 271 chunks (first run downloads the model)...
  stored   271 chunks in 3.0s

Ready. Try: python app.py ask "your question here"

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | In all three runs 4/5 chunks contained the answer, which met the criteria |
| 2 | Every answer names a source | MISS | The number of times the Source was listed was inconsistent, it happened 0, 3, and 2 out of five times in the run, the Criterion wanted 5/5 so it is a miss |
| 3 | Gate stops out-of-corpus questions | MET | The one pass it did refused every out-of-corpus question, so it passed. |
| 4 | Chunks are complete and self-contained thoughts, not sentence fragments or headings. | MET | 4/5 chunks from the sample chunks from Unit 1 of the project contained complete thoughts. |
| 5 | There should not be more than 200 chunks generated by the system. | MISS | 271 chunks are generated every time, I set the number too low and my chunker has a design flaw. |
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
