# GitHub README visual design

Read for creation, redesign, or visual polish. Choose a layout for the product,
not a universal template. Preserve existing branding and useful project detail.

## Choose a direction

| Direction | Fits | Above-the-fold composition |
|---|---|---|
| Product showcase | Apps, dashboards, visual tools | Name and value → compact links → real result screenshot → quick start |
| Developer utility | Libraries, CLIs, infrastructure | Name and value → minimal status badges → small input/output example → install |
| Research or report | Papers, datasets, analytical tools | Name and scope → result figure with caption → reproduce or explore → sources |

For an internal or configuration repository, emphasize setup and operational
clarity; do not force a marketing hero. A small CLI can look excellent with a
clear text example and no banner. These compositions are starting points, not
mandatory heading orders.

## Compose a coherent page

- Keep the first screen focused on what the project does, one credible result,
  and where to start. Avoid an oversized logo pushing those below the fold.
- Use one primary preview, consistent heading levels, short paragraphs, and
  blank lines. Put detail in linked docs or a concise `<details>` disclosure.
- Use badges only for useful, verifiable status. Prefer a consistent style and
  a small set; decorative technology walls compete with the product preview.
- Keep the primary action easy to identify. Use real links to quick start, demo,
  or docs; never publish a nonexistent destination to complete a design.
- Use tables for comparisons and settings, not multi-column page layout or
  large feature cards. On narrow widths, long tables are hard to read.
- Make the page work as plain Markdown before using minimal supported HTML.
  Do not depend on CSS, scripts, iframes, custom fonts, or interactive widgets.
  GitHub sanitizes HTML; a standalone web preview cannot prove GitHub behavior.

## Select and produce evidence

| Need | Preferred asset | Check |
|---|---|---|
| Show application output | Real screenshot with sanitized data | Result and meaningful text remain legible at README width |
| Explain an interaction | Short, focused GIF plus static fallback or caption | No distracting endless motion; file size is reasonable |
| Show CLI behavior | Copyable input/output, optionally a terminal capture | Commands match a real run; captured text is readable |
| Explain structure | Small diagram | Labels remain readable in light and dark themes |
| Establish identity | Existing logo or restrained illustration | Decorative image is distinct from product evidence |

Capture an existing runnable product when feasible. Crop irrelevant browser
chrome and private details while retaining enough context to understand the
result. Inspect generated assets after creation. Do not invent performance
charts, customer logos, features, or screenshots of a nonexistent implementation.
If an illustrative mockup is useful, label it visibly as illustrative.

Store assets in the target repository with descriptive filenames and alt text.
Link a screenshot to a verified richer demo when one exists. Avoid screenshots
containing installation instructions that users need to copy.

## Theme and width compatibility

Use an intentional background on screenshots; transparent dark text may disappear
in dark mode. For logos or diagrams that require separate theme variants, use a
`<picture>` with `prefers-color-scheme` sources and an `<img>` fallback, and verify
the referenced assets. Prefer a single theme-safe image when possible.

Inspect a rendered page at desktop and narrow widths (approximately 390 px).
Check clipping, unreadable captions, oversized hero images, badge wrapping,
long command blocks, and tables. Check light and dark backgrounds when the
renderer supports them. Fix issues instead of merely noting them.

Prefer a GitHub rendering surface when available. A local Markdown preview is
useful but may differ from GitHub; disclose that distinction. If no renderer is
available, inspect Markdown and each asset and report visual review as incomplete.

## Acceptance criteria

A visitor can identify the product, see useful evidence, and find the next step
without scrolling through decoration. Assets are readable, links are real,
headings are coherent, and setup is copyable. State the checks performed; avoid
unsupported claims that the README is beautiful, accessible, or conversion-proven.
