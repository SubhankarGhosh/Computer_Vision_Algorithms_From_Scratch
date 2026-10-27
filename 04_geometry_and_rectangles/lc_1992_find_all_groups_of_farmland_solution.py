"""LeetCode 1992: Find All Groups of Farmland (Reference Solution)

Problem URL: https://leetcode.com/problems/find-all-groups-of-farmland/
Difficulty: Medium
Category: Geometry & Rectangles

Computer Vision Context:
    Disconnected Axis-Aligned Bounding Box (AABB) Detection:
    Greedy top-left anchor detection and perimeter expansion in O(m * n) time.
"""

from __future__ import annotations
from typing import List


def find_farmland(land: List[List[int]]) -> List[List[int]]:
    """Detects bounding boxes [r1, c1, r2, c2] of all rectangular farmland components.

    Complexity Analysis:
    - Time Complexity: O(m * n). Every cell is inspected at most a constant number of times.
    - Space Complexity: O(1) auxiliary space (excluding result list).
    """
    m, n = len(land), len(land[0])
    result: List[List[int]] = []

    for r in range(m):
        for c in range(n):
            if land[r][c] == 1:
                # Check if this is the unique top-left corner of a farmland rectangle
                if (r == 0 or land[r - 1][c] == 0) and (c == 0 or land[r][c - 1] == 0):
                    r2, c2 = r, c
                    while c2 + 1 < n and land[r][c2 + 1] == 1:
                        c2 += 1
                    while r2 + 1 < m and land[r2 + 1][c] == 1:
                        r2 += 1
                    result.append([r, c, r2, c2])

    return result


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [[1, 0, 0], [0, 1, 1], [0, 1, 1]],
            [[0, 0, 0, 0], [1, 1, 2, 2]],
        ),
        (
            [[1, 1], [1, 1]],
            [[0, 0, 1, 1]],
        ),
        (
            [[0]],
            [],
        ),
    ]

    print("Running verification for lc_1992_find_all_groups_of_farmland_solution.py...")
    for idx, (grid, expected) in enumerate(test_cases, 1):
        res = find_farmland(grid)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
