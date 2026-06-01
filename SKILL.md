---
name: deep-hedging-broadening
description: >
  Use this skill when the user wants to broaden Deep Hedging research directions,
  find adjacent or emerging literature, identify future paper extensions, search
  survey/review papers, or explore cross-domain applications related to financial
  mathematics, reinforcement learning hedging, stochastic control, generative AI,
  multi-asset derivatives, ESG/climate risk, crypto derivatives, quantum finance,
  graph neural networks in finance, or physics-inspired finance.
---

# Deep Hedging Broadening Literature Assistant

This skill helps broaden Jessica Zhang's Deep Hedging research beyond highly
overlapping literature. The goal is to discover adjacent fields, emerging methods,
survey papers, future directions, new applications, datasets, optimization
frameworks, and theoretical extensions.

## When To Use

Use this skill when the user asks to:

- broaden a Deep Hedging research direction
- find papers outside the immediate Deep Hedging literature
- identify adjacent research fields
- search for survey/review/future-direction papers
- propose new paper topics or extensions
- connect Deep Hedging with reinforcement learning, stochastic control,
  generative AI, multi-asset derivatives, ESG/climate risk, crypto derivatives,
  graph neural networks, quantum finance, or physics-inspired finance

## Context To Load

Before doing the task, read:

- `references/research_profile.md` for the researcher's profile and broadening goals
- `references/system_prompt.md` for output expectations and behavior rules

Do not load extra files unless needed.

## Workflow

1. Clarify the target broadening direction if the user has not specified one.
2. Search for literature in adjacent, emerging, survey, review, or extension areas.
3. Prefer papers that create new research possibilities over papers that merely
   overlap with existing Deep Hedging work.
4. For each result, return structured information:
   - title
   - authors
   - year
   - short abstract or summary
   - broadening value score
   - why it broadens the user's current work
   - link, preferably Google Scholar, arXiv, SSRN, publisher page, or DOI
5. Only download PDFs when the user explicitly asks to download.

## Output Format

Use a concise structured format:

| Title | Year | Area | Broadening Value | Why It Helps |
|---|---:|---|---:|---|

After the table, include 2-4 suggested research directions that could follow
from the papers.
