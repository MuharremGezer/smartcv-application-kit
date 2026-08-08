# SmartCV Application Kit

A Codex skill for producing truthful, downloadable job-application materials from a job posting and a candidate's supplied CV.
Instead, I created a clear prompt/skill file that job seekers can use while keeping their own information under control (It's not my job, but I took into consideration the needs and demands of my close circle - Turkish friends :)).

## What it creates

- Recruiter-style screening report with an honest match score out of 100
- Tailored CV/resume that preserves the source CV's design
- Cover or motivation letter in the posting's language

The skill never invents experience, metrics, qualifications, or eligibility details.

## Install

From Codex, ask to install this GitHub repository as a skill, or run the skill installer with this repository URL:

```text
https://github.com/muharremgezer/smartcv-application-kit
```

## Structure

- `SKILL.md` — core workflow and rules
- `references/` — scoring, CV tailoring, and letter specifications
- `scripts/render_html_to_pdf.py` — optional HTML-to-PDF CV renderer

## Requirements

The PDF renderer needs `weasyprint`; page-count reporting additionally uses `pypdf` when available.
