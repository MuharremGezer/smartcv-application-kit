---
name: smartcv-application-kit
description: >
  Creates an honest, downloadable job-application kit from candidate-provided materials: a recruiter-style screening report with a score out of 100, a tailored CV/resume that preserves the original supplied CV design, and a cover or motivation letter. Use whenever a user shares a job posting and asks to assess fit, score their candidacy, tailor or regenerate a CV/resume, write a cover/motivation letter (including ön yazı, niyet mektubu, candidature, or lettre de motivation), or produce downloadable application files. Ask the user for their CV/resume and, when relevant, its original visual reference, photo, or brand assets; no candidate data or visual assets are bundled with this skill. Prefer this skill over inline help when the user wants files or a scored screening.
---

# SmartCV Application Kit

Create a complete, honest application kit as downloadable files. Default deliverables are editable `.docx` files:

1. **Screening report** — recruiter first-pass assessment: match score /100, fit table, missing keywords, red flags, and fixes.
2. **Tailored CV / resume** — optimized for the posting while preserving the candidate's facts and original supplied visual format.
3. **Cover / motivation letter** — written in the posting's language and tone.

## Required inputs

Collect the job posting and the candidate's current CV/resume before producing the kit. Accept pasted text, uploaded files, or links. If the posting is a link, fetch it; if it is inaccessible, ask the user to paste it.

Ask only for inputs that affect the requested deliverables:

- **CV design reference:** treat the candidate's existing CV as the required design reference. If the CV was pasted as text or the supplied file does not show its layout, ask for a PDF, image, or template before creating the tailored CV. Rebuild the CV in that original visual format; do not substitute a generic template unless the candidate explicitly asks for one.
- **Photo, logo, fonts, or brand assets:** use only when supplied and when the candidate explicitly wants them included. Do not request a photo by default.
- **Missing material facts:** ask one concise question only when a decisive requirement, metric, employment detail, work authorization, or letter recipient cannot be inferred. Otherwise proceed with clearly stated assumptions.

## Core rules

- **Never fabricate.** Use only candidate-provided facts. Mark unknown metrics or claims with a visible placeholder such as `[add metric]` or `[to confirm]` and list them in the handoff.
- **Respect privacy.** Treat candidate materials as private. Do not carry facts, contact details, photos, or assets from one candidate into another application.
- **Language default and check.** Treat the posting language as the default language for every deliverable. Before creating files, always ask whether the user wants any deliverable in a different language, unless they have already specified the output language. If the posting language is ambiguous, ask which language to use as the default.
- **Honesty over flattery.** Score realistically, name material gaps directly, and suggest better-fit alternatives when appropriate.
- **Match the role's level.** Judge requirements against the role's stated seniority and contract/eligibility constraints.
- **Avoid protected or unnecessary personal data.** Do not add a photo, date of birth, nationality, marital status, or similar detail unless the candidate supplied it and explicitly requests its inclusion or it is genuinely required.

## Workflow

### 1. Analyze the posting

Extract the role title, organization, location, contract type, seniority, must-have and nice-to-have requirements, tools, values/tone, posting language, and eligibility constraints.

### 2. Build the screening report

Follow `references/screening_report_spec.md`. Include the score, a concise recruiter read, a requirement-by-requirement table, missing keywords, red flags, practical improvements, and better-fit alternatives for a low score.

### 3. Build the tailored CV / resume

Follow `references/cv_tailoring_spec.md`. Reorder and rephrase existing experience using the posting's vocabulary, never invent tools or results, and always preserve the layout, hierarchy, colors, typography, and overall format of the supplied original CV. If the visual source is unavailable, ask the candidate for it before producing the CV.

### 4. Build the cover / motivation letter

Follow `references/cover_letter_spec.md`. Map real experience to the core requirements, match the posting language and tone, and mention work authorization only when the candidate has confirmed the relevant facts.

### 5. Deliver and validate

Save requested documents in the active task's `outputs/` directory. Validate `.docx` files with the available document workflow. Present the CV first, then letter, then screening report. Summarize the score, high-leverage improvements, assumptions, and any placeholders without pasting the full documents into chat.

## Optional designed PDF

Create the editable `.docx` by closely reproducing the supplied original design. Offer a pixel-faithful designed PDF when the source format cannot be faithfully represented in Word or when the candidate requests one. Use supplied fonts, photos, and visual assets only; otherwise use system-safe typography. Use `scripts/render_html_to_pdf.py` to render an HTML CV and verify it fits the requested page count.

## References

- `references/screening_report_spec.md` — report structure, scoring rubric, and styling.
- `references/cv_tailoring_spec.md` — tailoring rules and editable/DOCX/PDF production guidance.
- `references/cover_letter_spec.md` — cover and motivation letter principles and structure.
