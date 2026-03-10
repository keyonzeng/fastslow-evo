# Validation Model

A capability upgrade is not complete until validation is explicit.

## Validation Questions

- What exactly is being improved?
- What concrete inputs demonstrate success?
- What failure signals would invalidate the claim?
- What is the fallback if validation fails?
- What regression could this introduce elsewhere?

## Validation Levels

### V0 — Plausibility
Reasoned but untested. Not enough for durable upgrade.

### V1 — Single-case pass
Works on one known example. Good for local note, not broad claim.

### V2 — Multi-case pass
Works on multiple representative examples. Good for checklist/script/skill promotion.

### V3 — Repeated operational pass
Continues to work in real usage over time. Good for strong capability claim.

## Regression Checks

At minimum ask:
- Did complexity increase?
- Did runtime or cost get worse meaningfully?
- Did safety posture degrade?
- Did false confidence increase?

## Example

Claim:
Agent can handle SVG->PNG Chinese rendering.

Weak validation:
- file was created

Strong validation:
- multiple Chinese SVG samples rendered
- expected font available or embedded
- final raster output checked for readable Chinese
- fallback path documented if fonts missing
