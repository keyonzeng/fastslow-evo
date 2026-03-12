# FastSlow Evo Release Checklist

Use this checklist before packaging, publishing, or reinstalling the skill.
Do not use it on the default runtime path.

## 1. Runtime entry quality

Confirm that `SKILL.md` still does all of the following:
- states the fast/slow dual-loop identity clearly
- keeps routing states limited to `fast`, `slow candidate`, `observe`, `ignore`, `reject`
- gives a 30-second operating path
- points to the smallest useful reference set
- keeps runtime and maintenance references separate

## 2. Reference hygiene

Confirm that references are still separated physically and conceptually:
- `references/runtime-core/`
- `references/runtime-branches/`
- `references/runtime-optional/`
- `references/maintenance/`
- `references/examples/`

Check that:
- runtime files do not depend on maintenance files by default
- example files still illustrate `fast`, `slow candidate`, and `reject`
- outdated example names are either removed or intentionally preserved

## 3. Path integrity

Run a repository-wide reference check.
Confirm that markdown references to `references/...` resolve to real files.
Do not package with broken internal links.

## 4. Installation path

Confirm that `install.sh`:
- installs to `~/.openclaw/workspace/skills/fastslow-evo`
- prepares `~/.openclaw/workspace/fastslow`
- copies current templates into runtime folders
- points users to the current minimal workflow path

## 5. Runtime artifact sanity

Confirm that runtime templates still exist and match the current protocol model:
- incident record
- correction record
- win record
- promotion candidate
- scorecard

## 6. Packaging sanity

Before packaging:
- remove accidental junk files if any were added
- ensure no temporary review artifacts live inside the skill directory
- keep runtime evidence under workspace-level `fastslow/`, not inside the skill
- confirm no symlink-based surprises exist if packaging is planned

## 7. Final judgment

Ask:
- Is the skill still judgment-first rather than automation-first?
- Is the fast loop still easy to use without over-promoting?
- Is the slow loop still reviewable and rollback-aware?
- Would a fresh OpenClaw agent know where to start in under 30 seconds?

If any answer is no, fix that before release.
