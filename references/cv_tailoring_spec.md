# CV / Resume Tailoring Spec

Rebuild a candidate-provided CV or resume for a specific posting. Optimize truthfully and always preserve the original supplied CV's visual format. Treat its layout, hierarchy, color system, typography, spacing, columns, and section order as the design authority unless the candidate explicitly asks for a redesign.

## Tailoring rules

1. **Do not fabricate.** Use only candidate-provided content. Use visible placeholders such as `[add metric]` when a result is unknown.
2. **Reposition the headline.** Create a role-oriented, truthful positioning line aligned to the posting.
3. **Rewrite the profile.** Reflect the posting's priorities and vocabulary while retaining the candidate's actual background.
4. **Reorder by relevance.** Lead with the experiences closest to the role; retain less-relevant experience selectively.
5. **Use exact job-language where accurate.** Translate existing responsibilities into the posting's vocabulary without overstating scope.
6. **Verify tools and credentials.** Add a named tool, certification, clearance, language level, or qualification only when the candidate supplied it or confirms it.
7. **Preserve the original format.** Retain the source CV's page size, page count where practical, layout, header, section hierarchy, visual rhythm, colors, and typography. Make only changes necessary for the tailored content or technical editability; do not replace it with a generic template.
8. **Keep the requested length.** Default to the source CV's page count. Expand or condense only when tailored content makes it necessary, and retain the original's overall visual density.
9. **Keep sensitive information optional.** Preserve a source photo or personal details only when the candidate explicitly requests their inclusion in the tailored version.

## Default deliverable — editable `.docx`

Use the available document workflow. Recreate the supplied CV's hierarchy, colors, spacing, typography, columns, header, and section structure as closely as editable Word permits. If the candidate supplies a PDF or image, inspect it visually before building. If its format cannot be replicated faithfully in `.docx`, state the limitation and provide a pixel-faithful PDF alongside the editable `.docx`; do not silently swap in a generic design. Validate the final file before delivery.

## Optional designed PDF

Create a pixel-faithful designed PDF when the original format cannot be faithfully reproduced in editable Word or when the candidate requests it.

1. Derive the layout and visual tokens from the supplied reference.
2. Use only fonts, photos, logos, and other assets supplied by the candidate or system-safe replacements.
3. Write an HTML file with CSS and render it with `scripts/render_html_to_pdf.py input.html output.pdf [base_dir]`.
4. Inspect page count and layout; tighten spacing or simplify only as necessary to meet the requested page count.

## ATS and content checks

- Use a conventional section order appropriate to the market: summary, experience, education, skills, and optional projects/certifications.
- Use the posting's terminology for demonstrated experience, skills, and tools.
- Do not keyword-stuff or list skills without evidence.
- Do not add grades, coursework, dates of birth, passport/nationality, marital status, references, or a photo unless the candidate asks and the information is appropriate for the target context.
