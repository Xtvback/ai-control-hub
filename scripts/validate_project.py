#!/usr/bin/env python3
"""Validate the local AI Control Hub structure without external access."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "docs/SECURITY.md",
    "docs/ROADMAP.md",
    "scripts/smoke_test.py",
    "scripts/validate_project.py",
    ".github/workflows/smoke-test.yml",
    ".github/workflows/code-quality.yml",
]

def validate(root=ROOT):
    missing = [path for path in REQUIRED if not (root / path).is_file()]
    if missing:
        raise ValueError("Missing required files: " + ", ".join(missing))
    return len(REQUIRED)

if __name__ == "__main__":
    print(f"Validated {validate()} required project files.")
