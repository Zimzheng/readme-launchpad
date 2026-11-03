# GitHub README playbook

Use this reference after the user has supplied or confirmed the README languages and the
repository has been inspected.

## 1. Information architecture

A README is a landing page and an operational starting point. Choose sections
based on evidence in the repository instead of mechanically filling a template.

| Reader question | Suitable README element |
|---|---|
| What is this? | Name and concrete one-sentence description |
| Why would I use it? | Three to five outcome-oriented capabilities |
| What does it look like? | Screenshot, GIF, terminal recording, diagram, or labeled mockup |
| Can I try it now? | Shortest verified install and run commands |
| How does it fit my work? | Brief usage example, architecture note, or linked demo |
| Where do I go next? | Documentation, examples, issue tracker, contribution and license links |

Put the first three answers above the fold. Use a table of contents only when
the document is long enough to make scanning difficult.

## 2. Visual demo patterns

### Static product or report preview

Store a stable asset under `assets/`, `docs/assets/`, or `screenshots/`. Use
descriptive alt text and a relative path:

```md
[![Report preview](assets/report-preview.svg)](https://example.github.io/project/demo.html)
```

The image is clickable; the destination should be a live demo, a verified HTML
preview, or a source-file page clearly labeled as such. GitHub Markdown does
not safely embed arbitrary interactive HTML, so do not promise inline
interactivity inside a README.

### Interaction explanation

Use a secondary diagram or caption to explain a behavior a static screenshot
cannot show: anchors, filtering, responsive layout, print rules, or an
authorization flow. Keep it subordinate to the primary product preview.

### Example safety

Prefer a synthetic scenario. Mark it “示例”, “演示”, or “fictional” wherever a
reader could interpret it as a real customer, metric, source, or deployment.

## 3. Installation and usage

Give the shortest working command first. Show each command in its own runnable
block and include path creation when the destination may not exist:

```bash
mkdir -p ~/.example/skills
git clone https://github.com/owner/project.git ~/.example/skills/project
```

Do not use `<repository-url>`, invented versions, or generic placeholders when
the user wants copyable installation instructions. For several hosts, present a
small table followed by host-specific complete commands. Distinguish “install”
from “clone source to contribute”.

## 4. Language variants

Ask only if the task lacks an explicit choice; reuse confirmed preferences during follow-up edits. Use the requested primary language in `README.md`.
When optional variants are requested, make each a maintained peer document:

```md
[简体中文](README.md) | [English](README.en.md)
```

Do not create an unrequested translation or add a language switcher that points
to nonexistent files.

## 5. Release checklist

- Claims, commands, links, package names, and asset paths match the repository.
- Previews have useful alt text and their links have a verified destination.
- Sample content has no customer data, local paths, account identifiers, tokens,
  private research, or screenshots with sensitive text.
- The README separates facts, examples, and future plans.
- The staging diff contains only intended documentation and asset files.
- Remote publishing, hosted demos, repository creation, and Pages settings have
  direct user authorization.

## Sources informing these conventions

- GitHub Docs, “Basic writing and formatting syntax”: relative links and image
  paths remain portable across repository branches and clones.
- banesullivan/README: use concise demos and simple installation as a landing
  page, with deeper material moved into documentation.
- usman-idris/readme-examples: screenshots, GIFs, clear descriptions, demos and
  short installation paths are recurring characteristics of effective READMEs.


## 6. Language assets and generalization

Treat each requested language version as a complete reading experience: body,
editable preview, caption, alt text and linked example instructions. Use separate
localized illustrations when their embedded text is meaningful. Label mockups as
illustrations. Do not translate an authentic screenshot into a purported real UI.

Audit a reusable project's positioning for inherited client assumptions: named
customers, domain jargon, value claims, fixed steps, default duration, chapter
counts and oddly specific exclusions. Replace accidental assumptions with the
project's actual supported scope. Keep useful examples, marked as examples;
generalization does not require deleting the project's intentional specialty.

## 7. Capability and installation evidence

Separate model-generated work, deterministic scripts, host features and user
judgment. For supported hosts, document native discovery location, invocation,
prerequisites and applicable local/project/cloud scope. For hosts without a native
mechanism, describe manual instruction loading without claiming installation.
Use official documentation for changing conventions and record when checked.

Do not collapse these evidence levels:

| Evidence | What it establishes |
|---|---|
| Files copied to destination | Installer behavior, not host discovery |
| Script tests passed | Tested executable behavior, not model writing quality |
| Host recognized skill | Discovery, not a complete successful invocation |
| End-to-end invocation | The tested host and scenario only |
| Published page inspected | Observed rendering and navigation only |

## 8. Attribution and release acceptance

Reused code or assets require examining their licenses and preserving applicable
notices. Runtime dependencies belong in setup documentation. Inspiration can be
acknowledged optionally with accurate wording, before the license section in each
README. Do not describe a consulted project as a dependency or imply code reuse
without evidence. Optional acknowledgments do not replace required notices.

Reuse explicit authorization for the same publishing destination and scope.
Prepare reviewable files before seeking any new authorization. After publishing,
check the actual default branch, localized images, language switches, demo
landing pages and intended remote contents. Synchronize promised archives and
local copies. Record what could not be tested without claiming success.

The validator accepts multiple README variants and an explicit release file list:

```sh
python3 scripts/validate_readme.py README.md --repo-root . --variants README.en.md
python3 scripts/validate_readme.py README.md --repo-root . --publish-files SKILL.md references/readme-playbook.md
```

Relative links resolve from each document's directory; root-relative links resolve
from the repository root. URL-encoded paths and angle-bracket paths with spaces
are supported. The scanner skips fenced examples and inline code when resolving
links, but scans the complete text for common credential and local-path patterns.
External URL availability, anchor validity, factual claims, locale correctness and
binary privacy require separate review. It does not execute installation commands.

## 9. Whole-page maintenance and editorial compression

For a general README refresh:

1. Establish the current product contract from source and working entry points.
2. Audit the whole existing page: positioning, examples, defaults, installation, usage, capabilities,
   limitations, attribution and language variants. Identify outdated claims and repeated explanations.
3. Rewrite the existing narrative around current use. Remove stale prose rather than layering a
   release announcement over it. Preserve unique operational details and required legal notices.
4. Prefer actual output previews over legacy style samples when they better demonstrate the result.
   Keep contextual labels and links to editable sources; do not invent demos to fill a section.
5. Compress upstream history into accurate attribution plus a notice link. Keep a comparison only
   when it helps readers choose the product, and move detailed provenance to maintained references.
6. Verify that a first-time reader can identify the product, result and next action without knowing
   previous releases. Check translations for equivalent claims, not necessarily identical wording.

Example: replace "v1.2 changes and limits" with current capability and limits descriptions; update
old "always ask for a style" wording when the product now chooses autonomously. This example is an
editorial pattern, not a requirement that every project supports autonomous selection.

Acceptance checks (editorial judgment, not keyword bans):

- No update-only section is the sole explanation of a current capability.
- No old default or upstream description contradicts the new overview.
- Attribution remains accurate without dominating the primary reader journey.
- Installation requirements and material limitations survive compression.
- Version numbers remain where functionally needed; do not strip compatibility instructions.
- A targeted installation fix does not trigger an unsolicited whole-page rewrite.
- Release history remains appropriate when explicitly requested or central to the repository.

Do not add brittle tests that reject version headings or enforce one section order. Mechanical
validation checks links and common publishing risks; it cannot determine editorial clarity.
