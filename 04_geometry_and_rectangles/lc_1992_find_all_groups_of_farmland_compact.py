"""LeetCode 1992: Find All Groups of Farmland (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/find-all-groups-of-farmland/
Difficulty: Medium
Category: Geometry & Rectangles

Computer Vision Context:
    Disconnected Axis-Aligned Bounding Box (AABB) Detection:
    In agricultural aerial imagery and remote sensing, fields often form distinct rectangular plots.
    Since each group of farmland is guaranteed to be a solid, non-overlapping rectangle of 1s:
    1. Identify top-left corners (r1, c1): land[r][c] == 1 with no top or left neighbor.
    2. Expand rightwards along the row to determine c2.
    3. Expand downwards along the column to determine r2.
    4. Record the bounding box [r1, c1, r2, c2].
    This solves bounding box regression in strictly O(m * n) time with O(1) auxiliary space!

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 04_geometry_and_rectangles/lc_1992_find_all_groups_of_farmland_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def find_farmland(land: List[List[int]]) -> List[List[int]]:
    """Detects bounding boxes [r1, c1, r2, c2] of all rectangular farmland components.

    Algorithmic Requirements:
    - Time Complexity: O(m * n). Single raster scan.
    - Space Complexity: O(1) auxiliary space (excluding result list).

    Steps to implement:
    1. Dimensions m = len(land), n = len(land[0]).
    2. Initialize `result: List[List[int]] = []`.
    3. Iterate r in 0..m-1 and c in 0..n-1:
       - Check if (r, c) is the top-left corner of a farmland rectangle:
         - land[r][c] == 1
         - (r == 0 or land[r - 1][c] == 0)
         - (c == 0 or land[r][c - 1] == 0)
       - If top-left:
         - Find right boundary c2: while c2 + 1 < n and land[r][c2 + 1] == 1: c2 += 1
         - Find bottom boundary r2: while r2 + 1 < m and land[r2 + 1][c] == 1: r2 += 1
         - Append [r, c, r2, c2] to result.
    4. Return result.

    -------------------------------------------------------------------------
    TODO: Implement top-left corner detection and boundary expansion.
    -------------------------------------------------------------------------
    """
    m, n = len(land), len(land[0])
    result: List[List[int]] = []

    for r in range(m):
        for c in range(n):
            if land[r][c] == 1:
                # Top-left corner conditions
                is_top_left = (r == 0 or land[r - 1][c] == 0) and (c == 0 or land[r][c - 1] == 0)
                if is_top_left:
                    r2, c2 = r, c
                    # <<< YOUR CODE HERE >>>
                    # Hint: Expand c2 rightwards while within bounds and land[r][c2+1] == 1
                    # Expand r2 downwards while within bounds and land[r2+1][c] == 1
                    while c2 + 1 < n and land[r][c2 + 1] == 1:
                        c2 += 1
                    while r2 + 1 < m and land[r2 + 1][c] == 1:
                        r2 += 1

                    bbox = TODO  # Replace with: [r, c, r2, c2]
                    if bbox is None:
                        raise NotImplementedError("TODO: Record bounding box [r1, c1, r2, c2].")
                    result.append(bbox)

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

    print("Running tests for lc_1992_find_all_groups_of_farmland_compact.py...")
    try:
        for idx, (grid, expected) in enumerate(test_cases, 1):
            res = find_farmland(grid)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
