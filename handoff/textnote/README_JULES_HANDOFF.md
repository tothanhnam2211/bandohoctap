# YOURDREAM TextNote -> Jules source handoff (2026-10-27)

**Status:** SOURCES_TRANSFERRED_FOR_DEVELOPMENT_ONLY; not pedagogically approved. This branch is isolated from main and H07 PR #2.

## Source files now available to Jules

- `ALL_16_STUDENT_LESSONS.json` contains 16 authentic, student-facing lesson JSON objects across Grades 6-9. No fabricated replacements.
- `ALL_16_SVG_DIAGRAMS.json` maps the original 16 SVG filenames to their SVG markup.
- `student_payloads/S_G06_B07_student_lesson.json` is a standalone Grade 6 pilot lesson.
- `svg_assets/S_G06_B07_diagram.svg` is the original matching SVG.
- `jules_textnote_contract.schema.json` is the original, INCOMPLETE draft schema: validate and extend rather than treating as an approval gate.

## Original A4 PDF files

The original 16 student PDFs are on private Google Drive:
https://drive.google.com/drive/folders/1_zVL6GS_sA8_rAXucqWPNz4JwQHEVmPg

Pilot `S_G06_B07` PDF:
https://drive.google.com/file/d/1EEwtyh3jsAvxcvh15DySOcWj1v_FIzSD/view

PDF files are not copied into this Git branch (originals are ~7 MB each and private). If Jules cannot access Drive URLs, **do not claim that the PDFs are locally available**. Implement the interactive pilot from the actual lesson JSON and SVG, and report `ORIGINAL_PDF_ACCESS_PENDING` for PDF parity/print checks. Ask the Product Owner to attach the PDF to the Jules session, or request an approved binary handoff route. Do not generate a fake PDF and call it the source.

## Pilot implementation expectations

Inspect current repository and existing Jules session branch before cherry-picking/merging content. Read these files from `handoff/textnote-20261027-jules-source` without overriding Jules's existing work.

Avoid teacher-only answers in client bundles. Some worked examples contain solutions intended for teaching; that is different from exposing private teacher-only exercises.

Keep Vietnamese learner-facing strings. Test the grade-6 S_G06_B07 example plus cross-grade/cross-strand generalization.

Never modify PR #2, merge to main, or deploy production without explicit approval.

## Data fidelity

Input content and SVGs were copied from Antigravity's private Drive handoff. No changes to mathematics or pedagogical language have been made in this source branch. Source transfer does **not** certify mathematical accuracy, live app behavior, or release readiness.
