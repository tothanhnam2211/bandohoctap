# YOURDREAM H07 — Jules engineering handoff (candidate)

## Read this first
- **Game:** `games/H07/index.html` (self-contained candidate)
- **Data contract:** `games/H07/h07_argon_to_jules_handoff.contract.json`
- **Source:** User pasted Argon's v2.1 HTML and JSON in ChatGPT; this branch contains a *new adapted implementation*, not a byte-exact mirror of Argon's source. Preserve links to V02 and verify final v2.1 source/art with Argon before claiming faithful import.
- **Status:** preview candidate, NOT QA-passed, NOT approved, NOT deployed.

## Jules brief
Create a premium mobile-first educational game based on H07, preserve three acts and both 33/38m² grade-8 presets. Grade 9 must use **S_G09_B21**. No teacher QA data on public UI. No paid APIs. Build real direct manipulation, Socratic mistakes and beautiful responsive presentation. Use existing repository deployment and ensure main is unaffected.

## Must fix before a learner release
1. Add tests for all grid counts (128,32,8), game state invalidation, both G08 areas and double counts, G09 x=4,5,9 edge cases.
2. Validate all user state on load, game accessibility, responsive canvas text/collisions and print A4 on mobile + desktop.
3. Integrate actual Argon clean-plate artwork only with verified alignment; current page uses code-drawn vector 2D.
4. Playtest with actual children/teachers before pedagogical acceptance; robot tests alone insufficient.
5. Verify Cloudflare build/preview configuration and only share a verified deployed preview URL, never infer one from file path.
6. Avoid overclaiming world physics, no dynamic rain weather simulation currently; this is a meaningful *candidate* for Jules to elevate.

## Next
Review then create a PR from `handoff/h07-v21-jules-ready-20261026` only after test/preview. Product Owner controls merge and release.
