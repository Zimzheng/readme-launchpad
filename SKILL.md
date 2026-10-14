---
name: github-readme-craft
description: Create or revise a high-quality GitHub README with language selection, verified installation steps, clickable visual demos, and privacy-aware publishing checks. Use for repository landing pages, README rewrites, and GitHub documentation polish.
---

# GitHub README Craft

Create a README that lets a new visitor understand the project, see a credible
example, install it, and take the next useful action without reading the code.

## Preserve the task context

Use the user's explicitly selected primary and optional languages. Ask only when
that choice is missing; preserve it across follow-up edits in the same task.
Do not infer language from account locale or folder names. Put the primary
language in `README.md` and link only requested, existing variants.

Read [readme-playbook.md](references/readme-playbook.md) when drafting or reviewing
language assets, host installation, attribution, or release evidence.

## Discover the product before writing

- Inspect the repository structure, package manifests, executable entry points,
  existing docs, demos, and deployment configuration.
- Identify the audience, the one-sentence value proposition, the shortest
  successful install/run path, and what evidence can demonstrate the result.
- Verify installation commands against the repository's actual files and tools.
  Do not publish placeholder commands, untested package names, or guessed URLs.
- Preserve useful project-specific information. Keep the README as a landing
  page; move exhaustive API or implementation reference to linked documents.

- Identify what the model, executable scripts, host environment and user each do.
  Describe dependencies and prerequisites without assigning one layer's capability
  to another.
- When generalizing a project, inspect claims, terms, examples, defaults and
  exclusions for assumptions inherited from the original client or use case.
  Retain intentional domain scope; do not broaden the product beyond evidence.

## Build the README

- Put the project name, a concrete one-sentence description, and the most
  useful action near the top. Use badges only when they convey maintained facts.
- Include a visual demonstration when it helps readers judge the product:
  screenshots, a short GIF, a terminal capture, a diagram, or an explicitly
  labeled illustrative mockup. Never present a mockup as a live result.
- Make preview images clickable when a richer destination exists. Use repository
  relative paths for image assets and internal documentation links.
- When a full HTML report, app, or interactive sample cannot render inside
  GitHub Markdown, link the preview image to a verified public demo page or
  clearly label the source-file destination.
- Localize editable illustrations, captions and alt text alongside each README.
  Authentic screenshots may retain the real UI language; explain any mismatch.
  Preserve equivalent capabilities and limitations across language versions.
- For genuinely supported hosts, state install locations, invocation, prerequisites
  and verification status. Distinguish native skill discovery from manual reading,
  and local installation from cloud availability. Verify changing host conventions
  against official documentation; do not add hosts solely to fill a table.
- Give complete, copyable commands. Include prerequisites only when required.
  Separate ordinary user installation from contributor/development setup.
- Use concise sections chosen for the project: overview, demo, features, quick
  start, usage, architecture, configuration, examples, documentation,
  contributing, security, and license. Omit sections that add no value.

## Privacy and publishing

- Use fictional or sanitized examples for public demonstrations unless the user
  explicitly approves real project material. Explain that sample data is
  fictional when readers could mistake it for a finding or customer deployment.
- Before a public commit or push, scan staged content for local paths, tokens,
  credentials, personally identifying material, private research artifacts, and
  accidental output files. Remove only the findings relevant to public release.
- Do not create a repository, enable GitHub Pages, push, or alter a remote until
  the user authorizes that external action. If hosting is needed for a clickable
  HTML demo, prepare the files and configuration first; request authorization
  immediately before enabling or publishing the public site if not already authorized.
- Preserve specific publishing authorization across follow-up edits to the same
  repository. Ask again only when destination, visibility or scope changes.
- Distinguish reused code/assets, runtime dependencies and methodological
  inspiration. Preserve required third-party notices. Optional acknowledgments
  belong before the license section in README variants, not in task instructions;
  use accurate wording and follow the user's preference.

## Verify before handoff

Run `scripts/validate_readme.py README.md --repo-root . --variants README.en.md`
(adapt the variant list to the task) when Python is
available. Resolve its errors and review warnings. Also render or inspect visual
assets when possible, test the shortest documented install path, and verify that
each clickable demo destination is reachable in the intended public context.

- Use `--publish-files` for the actual text files being released, including assets
  and examples when applicable; inspect binary assets visually. Pattern scanning
  is a limited aid, not proof that private content is absent.
- Report evidence precisely: copy/install tests, executable tests, host discovery,
  full invocation, external links and visual review are separate checks. Mark
  untested claims explicitly; mechanical validation does not prove usability.
- After authorized publishing, inspect the real default-branch README, images,
  language links and demo destinations. Compare intended files with remote content
  and keep local deliverables/archives consistent. Do not enable hosting merely
  to satisfy a demo preference. Stop after the requested result is verified;
  explain a concrete blocker if verification is unavailable.
