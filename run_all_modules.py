"""Master Test Runner for Computer Vision Algorithms From Scratch.

Discovers and executes all 32 reference solutions sequentially across all 4 modules,
reporting individual module metrics and total curriculum pass rate.
"""

from __future__ import annotations
import os
import sys
import subprocess
from pathlib import Path

# Ensure UTF-8 output encoding on Windows consoles
if sys.platform == "win32":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    os.environ["PYTHONIOENCODING"] = "utf-8"

REPO_ROOT = Path(__file__).resolve().parent

MODULE_DIRS = [
    ("Module 01: Image Processing & Manipulation", REPO_ROOT / "01_image_processing_and_manipulation"),
    ("Module 02: Blob Detection & Connectivity", REPO_ROOT / "02_blob_detection_and_connectivity"),
    ("Module 03: Matrix Operations & Distance", REPO_ROOT / "03_matrix_operations_and_distance"),
    ("Module 04: Geometry & Rectangles", REPO_ROOT / "04_geometry_and_rectangles"),
]


def run_all() -> int:
    print("=" * 80)
    print("  COMPUTER VISION ALGORITHMS FROM SCRATCH: CURRICULUM VERIFICATION SUITE")
    print("=" * 80)

    total_passed = 0
    total_failed = 0
    failures = []

    for mod_title, mod_dir in MODULE_DIRS:
        print(f"\n[+] {mod_title}")
        print("-" * 80)

        solution_files = sorted(mod_dir.glob("*_solution.py"))
        if not solution_files:
            print("    (No solution files found)")
            continue

        for sol_path in solution_files:
            rel_path = sol_path.relative_to(REPO_ROOT)
            cmd = [sys.executable, str(sol_path)]
            result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

            if result.returncode == 0:
                print(f"    [PASS] {sol_path.name}")
                total_passed += 1
            else:
                print(f"    [FAIL] {sol_path.name}")
                total_failed += 1
                failures.append((str(rel_path), result.stderr))

    print("\n" + "=" * 80)
    print("  SUMMARY REPORT")
    print("=" * 80)
    print(f"  Total Solutions Executed: {total_passed + total_failed}")
    print(f"  Passed:                   {total_passed}")
    print(f"  Failed:                   {total_failed}")
    print(f"  Success Rate:             {(total_passed / (total_passed + total_failed) * 100):.1f}%")

    if failures:
        print("\n[!] Failures:")
        for file, err in failures:
            print(f"  - {file}:\n{err}")
        return 1

    print("\n[SUCCESS] All 32 Computer Vision Algorithm reference solutions passed deterministically!")
    return 0


if __name__ == "__main__":
    sys.exit(run_all())
