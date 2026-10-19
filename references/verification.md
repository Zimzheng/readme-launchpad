# Verification and handoff

Verification should follow the user's scope and the actual claims in the README.
Do not run publishing, billing, destructive, or production-changing commands
merely because they appear in a quick start. Use a safe local environment and
respect existing authorization.

## Check the first-use path

Resolve the quick start against package manifests, entry points, example files,
lockfiles, and deployment settings. Check whether the distribution actually
exists. When practical, execute the documented install and smallest useful
example in an isolated directory, including prerequisites and directory changes.
Record the command, environment, and observable outcome. An existing development
checkout can hide missing steps; disclose when a clean environment was not used.

If execution needs unavailable credentials, tooling, or network access, preserve
the distinction: source-checked is not execution-tested. Do not invent a successful
run or quietly remove a required prerequisite to simplify the page.

## Check links and visuals

Run the bundled mechanical validator using the target README and repo root.
Its checks are partial: review anchors, unusual link syntax, and example snippets
manually where relevant. Use its variant and publish-file options when applicable. A warning does not require
adding an image or shell block to a project that does not need one.

Verify demo destinations in the intended public context. A 200 response alone
does not prove a working demo: inspect whether it opens the actual result rather
than a login, error, or source page. Review asset readability and final rendering
as described in visual-design.md; disclose renderer limitations.

For requested language variants, keep commands, feature claims, asset destinations,
and section meaning consistent. Do not create unrequested translations.

Before a public commit or push, inspect the intended diff and staged files for
sensitive material, unintended outputs, and unsanitized screenshots. The validator
recognizes only some patterns; it is not a complete secret scanner.

## Handoff

Use a short report in the conversation; save it only when requested or useful:

| Check | Status | Evidence or limitation |
|---|---|---|
| Quick start | Executed / source-checked / blocked / not applicable | Exact commands and result, or missing requirement |
| Local links and assets | Passed / issues / not checked | Validator plus any manual checks |
| Public demo | Verified / blocked / not applicable | Destination and inspected result |
| Visual rendering | Rendered / assets-only / not checked | Renderer, widths, themes, and any limitations |
| Language parity | Checked / not applicable / not checked | Requested variants |
| Publishing review | Checked / not requested / blocked | Relevant diff and findings; never secret values |

Only include relevant rows and completed evidence. Do not put tool diagnostics
or verification bookkeeping into the public README unless the user requests it.
A completed source edit can be handed off with explicit unverified checks.
Never equate mechanical validation with verified installation or rendered review.

## Evaluate this skill when changing its workflow

Use representative fixtures: a published library, a source-only CLI, a visual
application, and a targeted fix to an existing README. Compare an ordinary agent
prompt with this skill using the same repository snapshot and constraints.
Assess factual claims, successful first use, link correctness, visual readability,
and preservation of unrelated content. Keep generated artifacts outside fixtures.
Record failures and limitations; one model or one successful example does not
establish general improvement. Do not claim benchmark gains without outcomes.
