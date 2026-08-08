#!/usr/bin/env python3
"""Verify the bounded public cooling scenario contract and emit a receipt."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from cooling_scenario import default_demo  # noqa: E402

ARTIFACT_DIR = ROOT / "artifacts" / "portfolio-core"
SCENARIO_PATH = ARTIFACT_DIR / "cooling-scenario.json"
RECEIPT_PATH = ARTIFACT_DIR / "verification-receipt.json"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def run_tests() -> dict[str, Any]:
    command = [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        sys.stderr.write(completed.stdout)
        sys.stderr.write(completed.stderr)
        raise SystemExit(completed.returncode)
    return {
        "command": " ".join(command),
        "returncode": completed.returncode,
        "stdout_sha256": sha256_bytes(completed.stdout.encode()),
        "stderr_sha256": sha256_bytes(completed.stderr.encode()),
    }


def main() -> int:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    test_result = run_tests()
    scenario = default_demo()
    rendered_scenario = json.dumps(scenario, indent=2, sort_keys=True) + "\n"
    SCENARIO_PATH.write_text(rendered_scenario, encoding="utf-8")

    receipt = {
        "schema": "glaciereq.colossal-cooling-model-receipt.v1",
        "evidence_state": "TEST",
        "scenario_state": "MODELED_SCENARIO_NOT_TELEMETRY",
        "external_queries": 0,
        "external_actions": 0,
        "hardware_control": False,
        "deployment_claim": False,
        "scenario_sha256": sha256_bytes(rendered_scenario.encode()),
        "tests": test_result,
        "canonical_paths": [
            "README.md",
            "HISTORICAL_SURFACES.md",
            "cooling_scenario.py",
            "tests/test_cooling_scenario.py",
        ],
    }
    rendered_receipt = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    RECEIPT_PATH.write_text(rendered_receipt, encoding="utf-8")
    print(rendered_scenario, end="")
    print(rendered_receipt, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
