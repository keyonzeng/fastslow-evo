#!/usr/bin/env python3
from pathlib import Path
import shutil
import sys

HOME = Path.home()
SKILL_NAME = "fastslow-evo"
SRC = Path(__file__).resolve().parents[1]
DEST = HOME / ".openclaw" / "workspace" / "skills" / SKILL_NAME
RUNTIME = HOME / ".openclaw" / "workspace" / "fastslow"

TEMPLATE_FILES = {
    "assets/incident-record.template.md": RUNTIME / "evidence" / "incidents" / "_template.md",
    "assets/correction-record.template.md": RUNTIME / "evidence" / "corrections" / "_template.md",
    "assets/win-record.template.md": RUNTIME / "evidence" / "wins" / "_template.md",
    "assets/promotion-candidate.template.md": RUNTIME / "proposals" / "_promotion-candidate.template.md",
    "assets/scorecard.template.md": RUNTIME / "scorecards" / "_scorecard.template.md",
}

README = """# FastSlow Runtime

This directory stores FastSlow Evo runtime artifacts.

## Structure
- evidence/incidents/
- evidence/corrections/
- evidence/wins/
- proposals/
- scorecards/
- specs/capabilities/
- specs/behaviors/
- specs/validations/
- specs/evolutions/
- specs/materializations/
"""


def safe_copy_skill(src: Path, dest: Path):
    src_r = src.resolve()
    if dest.exists() and dest.resolve() == src_r:
        return "in-place"
    if dest.exists():
        shutil.rmtree(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dest)
    return "copied"


def init_runtime():
    dirs = [
        RUNTIME / "evidence" / "incidents",
        RUNTIME / "evidence" / "corrections",
        RUNTIME / "evidence" / "wins",
        RUNTIME / "proposals",
        RUNTIME / "scorecards",
        RUNTIME / "specs" / "capabilities",
        RUNTIME / "specs" / "behaviors",
        RUNTIME / "specs" / "validations",
        RUNTIME / "specs" / "evolutions",
        RUNTIME / "specs" / "materializations",
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
    (RUNTIME / "README.md").write_text(README, encoding="utf-8")
    for rel, target in TEMPLATE_FILES.items():
        src = SRC / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if src.exists() and not target.exists():
            shutil.copy2(src, target)


def main():
    mode = safe_copy_skill(SRC, DEST)
    init_runtime()
    ok = (DEST / "SKILL.md").exists() or (SRC / "SKILL.md").exists()
    print(f"install_mode={mode}")
    print(f"skill_path={DEST}")
    print(f"runtime_path={RUNTIME}")
    print(f"skill_ready={ok}")
    if not ok:
        sys.exit(1)
    print("FastSlow Evo installed for OpenClaw.")

if __name__ == "__main__":
    main()
