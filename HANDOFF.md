# Legacy Content Export Handoff

This document outlines the process for exporting the legacy 30-Day Math Content from the `bandohoctap` repository and provides mapping instructions for future integration with the YOURDREAM Webapp.

## Reproducing the Export

1. Make sure you are in the root directory of the repository.
2. Run the export script:
   ```bash
   python export_legacy_content.py
   ```
3. The script will parse `data/curriculum.json` and read each associated lesson file.
4. It will extract the JSON data while preserving UTF-8 formatting (important for Vietnamese text) and extract any referenced assets (like `.png`, `.mp4`, `.pdf`, `.html`).
5. All valid data and assets will be copied to the `legacy_export/` directory.

### Output Files

*   `legacy_export/data/`: Contains `curriculum.json` and each day's JSON lesson data.
*   `legacy_export/assets/`: Contains the preserved assets organized by day or module (like `stem_labs`).
*   `legacy_export/inventory.json`: Contains three properties:
    *   `available_days`: Lessons that were successfully found and exported.
    *   `missing_days`: Lessons that were listed in `curriculum.json` but where the actual JSON file is missing.
    *   `unresolved_references`: Assets referenced in a lesson's JSON but not found on the filesystem.
*   `legacy_export/manifest.json`: Contains SHA-256 hashes for all exported files to verify their integrity.

## YOURDREAM Mapping Instructions

To integrate the exported data into the YOURDREAM Webapp adapter, map the legacy schema as follows:

*   **Lesson Metadata:** `id`, `day`, `title`, and `status` remain the same and can be mapped directly from `curriculum.json` or the individual day JSON files.
*   **Downloads/Documents:** `download_links` mapped to YOURDREAM document/attachment features. Note the path changes (e.g. `assets/day-01/Phieu_Hoc_Tap_Ngay_1.pdf`).
*   **Video Content (Shorts):** The `shorts.clips` array contains objects with `id`, `title`, `video_url`, and descriptions. Map the `video_url` directly to YOURDREAM's video player module.
*   **Theory/Infographic:** Map `infographic_tab.image_url` to image display blocks, and `infographic_tab.theory_sections` to text/markdown blocks.
*   **Quizzes:** Map the `quiz_tab.questions` array. Map `question` to the prompt, `options` to choices, and use `correct_index` to identify the right answer. `explanation` can be mapped to feedback or hint fields.
*   **Interactive Elements:** The `stem3d_tab.src` points to a local HTML page (e.g., `assets/stem_labs/songuyen.html`). Consider using an `iframe` component within YOURDREAM to render these legacy interactives until they are ported.

## Known Blockers & Limitations

*   **Missing Content:** Many days (Day 03 through Day 30) are defined in `curriculum.json` but their underlying data JSON files are completely missing from the repository. Only days 1 and 2 actually exist. The export correctly excludes the non-existent files and lists them in `inventory.json`.
*   **Unresolved Assets:** Some days reference video clips that do not exist in the `assets/` directory (e.g., `clip2.mp4` and `clip3.mp4` for Day 01). These are logged in `inventory.json` under `unresolved_references`.
*   **Hardcoded Paths:** The `stem_labs` HTML files and some JSON properties use hardcoded path structures. Ensure the static file hosting mechanism in the new adapter preserves this nested structure or uses a URL resolver mapping.