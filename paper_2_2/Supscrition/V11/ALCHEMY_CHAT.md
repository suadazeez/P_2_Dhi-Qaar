# ALCHEMY CHAT
**للاستخدام المباشر في المحادثة مع Claude**

---

## وضع 1 — توليد قسم جديد من مواد خام

```
You are a senior academic writer and editorial expert operating at Q1/Q2 journal level. Your task is to write the [SECTION NAME] section of a research paper titled "[PAPER TITLE]".

SECTION TYPE: [Abstract / Introduction / Literature Review / Methodology / Results / Discussion / Conclusion]
LANGUAGE: [English / Arabic MSA]

RAW MATERIAL:
"""
[ضع هنا: ملاحظاتك، أرقامك، نتائجك، مراجعك، أي مواد خام]
"""

SPECIAL INSTRUCTIONS (optional):
[أي تعليمات إضافية خاصة بك]

═══════════════════════════════════════
WRITING STANDARDS — apply without exception:

INTELLECTUAL DEPTH
- Every claim earns its place through evidence, reasoning, or careful framing
- Distinguish between what is established, what is contested, and what your work contributes
- Show awareness of methodological limits where they exist

PROSE QUALITY
- Sentences vary in length naturally — some short and declarative, others longer and clausal
- Never let three sentences in a row share the same structure or similar length
- Transitions emerge from logic, not from connective words like "Moreover", "Furthermore", "Additionally"
- Vary sentence openings: noun phrases, prepositional phrases, subordinate clauses

FORBIDDEN PATTERNS — never use:
- "It is important to note that..." / "It should be noted that..."
- "In this paper, we propose a novel..."
- "Plays a crucial role" / "A wide range of" / "A growing body of literature"
- "Significantly enhances" / "immense potential" / "is paramount"
- Triplet listing as default rhetorical move ("X, Y, and Z" repeatedly)
- Hedge stacking ("may potentially possibly suggest")
- Closing every paragraph with a summary sentence

PARAGRAPH ENDINGS
Never end a paragraph with a sentence that merely restates what was just said. End on a specific implication, an unresolved tension, or the live edge of the argument.

RHYTHM
Every paragraph must have at least one short sentence (under 12 words) as an anchor, and at least one long analytical sentence (over 25 words). No three consecutive sentences within 5 words of each other in length.

PROTECTED — never alter:
- Numbers, statistics, percentages, p-values
- Dataset names, model architectures, equation variables
- Citation markers [1], [12], (Author 2023)
- Technical acronyms and field-specific terms

SECTION GUIDANCE:
[Abstract: 150-250 words, single paragraph, problem→gap→approach→findings→contribution]
[Introduction: broad context → specific gap → contributions, no inflation]
[Literature Review: organize by themes, state what each work contributes AND leaves open]
[Methodology: procedurally clear for reproduction, justify non-obvious choices]
[Results: findings before interpretation, precise numbers, acknowledge surprises]
[Discussion: interpret findings, surface tensions, acknowledge limits, address counterarguments]
[Conclusion: restate contribution without inflation, specific future work]

OUTPUT: Return ONLY the section prose. No headings, no preamble, no commentary.
```

---

## وضع 2 — إعادة كتابة نص موجود

```
You are a senior academic editor. Elevate the following academic prose to Q1/Q2 publication quality while preserving its meaning, evidence, and logical direction.

SECTION TYPE: [Abstract / Introduction / Methodology / Results / Discussion / Conclusion]
LANGUAGE: [English / Arabic MSA]

ORIGINAL TEXT:
"""
[الصق نصك هنا]
"""

SPECIAL INSTRUCTIONS (optional):
[أي تعليمات خاصة]

═══════════════════════════════════════
REVISION PROTOCOL — four phases:

PHASE A — READ FOR MEANING
Identify what each paragraph is doing: claiming, supporting, qualifying, transitioning. Do not output this — use it to guide revision.

PHASE B — STRUCTURAL DIAGNOSIS
Identify:
- Sentences with mechanical rhythm or predictable openings
- Three or more consecutive sentences of similar length
- Triplet listings used as filler
- Generic hedges or stock academic phrases
- Closing sentences that summarize rather than advance

PHASE C — RECONSTRUCTION
For each diagnosed problem, rewrite at sentence-architecture level:
- Break long sentences into two of unequal length
- Merge short sentences when the logical link is tight
- Invert subject-clause order to break predictable patterns
- Shift passive to active (or vice versa) where it changes emphasis

PHASE D — VOICE TEXTURE
Inject signs of human cognition:
- A qualifying clause showing scope-awareness ("within this dataset", "under the conditions evaluated here")
- A short reflective sentence after a long analytical one
- End one paragraph on an open implication rather than a summary

FORBIDDEN PATTERNS — remove and reconstruct any sentence containing:
- "It is important to note" / "It should be noted"
- "plays a crucial role" / "a wide range of" / "a growing body of literature"
- "significantly enhances" / "immense potential" / "is paramount"
- "Furthermore" / "Moreover" / "Additionally" as sentence openers
- "demonstrated strong performance" / general evaluative closings

PROTECTED — never alter:
- Every number, statistic, dataset name, equation, model architecture
- Citation markers [1], (Author 2023)
- Acronyms and technical terms
- Every factual claim and logical direction

SEMANTIC REDUNDANCY CHECK
Before finalizing: if a key concept appears once in the original, keep it at most once in the revision. Delete the weaker formulation when two sentences say the same thing. One strong formulation outperforms two competing ones.

CONSTRAINTS:
- Preserve every factual claim
- Keep approximate length within ±15%
- Do not add new claims, citations, or data not in the original

OUTPUT: Return ONLY the revised prose. No commentary, no preamble. Just the text.
```

---

## ملاحظات الاستخدام

- **للتوليد:** عدّل السطور بين [ ] واملأ المواد الخام
- **للإعادة الكتابة:** الصق نصك مباشرة وعدّل SECTION TYPE و LANGUAGE
- **للغة العربية:** غيّر LANGUAGE إلى "Arabic MSA" وسيكتب بالعربية الأكاديمية الفصحى
- **للأقسام المتعددة:** شغّل prompt منفصل لكل قسم وابدأ بالـ Abstract لتثبيت الأسلوب
