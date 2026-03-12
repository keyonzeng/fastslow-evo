#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET_SKILL_DIR="$HOME/.openclaw/workspace/skills/fastslow-evo"
RUNTIME_DIR="$HOME/.openclaw/workspace/fastslow"

mkdir -p "$HOME/.openclaw/workspace/skills"
mkdir -p "$RUNTIME_DIR/evidence/incidents" "$RUNTIME_DIR/evidence/corrections" "$RUNTIME_DIR/evidence/wins"
mkdir -p "$RUNTIME_DIR/proposals" "$RUNTIME_DIR/scorecards"
mkdir -p "$RUNTIME_DIR/specs/behaviors" "$RUNTIME_DIR/specs/capabilities" "$RUNTIME_DIR/specs/evolutions" "$RUNTIME_DIR/specs/materializations" "$RUNTIME_DIR/specs/validations"

if [ "$DIR" != "$TARGET_SKILL_DIR" ]; then
  rm -rf "$TARGET_SKILL_DIR"
  mkdir -p "$(dirname "$TARGET_SKILL_DIR")"
  cp -R "$DIR" "$TARGET_SKILL_DIR"
fi

cp -f "$TARGET_SKILL_DIR/assets/incident-record.template.md" "$RUNTIME_DIR/evidence/incidents/_template.md"
cp -f "$TARGET_SKILL_DIR/assets/correction-record.template.md" "$RUNTIME_DIR/evidence/corrections/_template.md"
cp -f "$TARGET_SKILL_DIR/assets/win-record.template.md" "$RUNTIME_DIR/evidence/wins/_template.md"
cp -f "$TARGET_SKILL_DIR/assets/promotion-candidate.template.md" "$RUNTIME_DIR/proposals/_promotion-candidate.template.md"
cp -f "$TARGET_SKILL_DIR/assets/scorecard.template.md" "$RUNTIME_DIR/scorecards/_scorecard.template.md"

printf 'FastSlow Evo installed (protocol-first, no Python runtime required).\n'
printf 'Skill dir: %s\n' "$TARGET_SKILL_DIR"
printf 'Runtime dir: %s\n' "$RUNTIME_DIR"
printf 'Next read: %s\n' "$TARGET_SKILL_DIR/references/runtime-core/minimal-usable-workflow.md"
