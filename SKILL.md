---
name: smartcv-application-kit
description: Creates honest job-application materials from a job posting and candidate-provided CV, including fit analysis, a tailored CV, and a cover letter. Use when the user asks to assess application fit, tailor a CV/resume, write a cover or motivation letter, or prepare a complete job-application kit. The repository also provides portable prompts for ChatGPT, Claude, and Gemini.
---

# SmartCV Application Kit

Use the same factual and privacy rules that power the portable prompts in `prompts/`.

## Collect inputs

Ask for the job posting and the current CV/resume. If the user requests visual CV preservation, collect a PDF, image, or template showing the original design. Default all outputs to the posting's language unless the user specifies another.

## Produce a factual application kit

1. Analyse the role's level, must-haves, nice-to-haves, location, and constraints.
2. Give an honest match score and requirement-by-requirement fit table.
3. Tailor the CV by reordering and clarifying existing evidence; preserve the original visual system when a reference is supplied.
4. Write a targeted cover or motivation letter.
5. List every missing fact as `[to confirm]` or `[add metric]`.

## Non-negotiable rules

- Never invent experience, tools, achievements, metrics, qualifications, dates, or eligibility.
- Do not infer work authorisation, languages, credentials, or protected personal information.
- Make gaps visible rather than hiding them.
- Keep claims specific and interview-defensible.
- Use candidate materials only for the current application.

## Portable prompts

For a prompt users can paste into ChatGPT, Claude, or Gemini, use the relevant file in `prompts/`:

- `01-job-fit-analysis.md`
- `02-tailor-cv.md`
- `03-cover-letter.md`
- `04-full-application-kit.md`
