"""LeetCode 463: Island Perimeter (Reference Solution)

Problem URL: https://leetcode.com/problems/island-perimeter/
Difficulty: Easy
Category: Blob Detection & Connectivity

Computer Vision Context:
    Discrete boundary edge summation:
    Perimeter = 4 * LandCells - 2 * SharedEdges
"""

from __future__ import annotations
from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """Calculates the perimeter of a single connected island.

    Complexity Analysis:
    - Time Complexity: O(m * n). Evaluates each cell once in raster order.
    - Space Complexity: O(1) auxiliary space.
    """
    m, n = len(grid), len(grid[0])
    perimeter = 0

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]],
            16,
        ),
        (
            [[1]],
            4,
        ),
        (
            [[1, 0]],
            4,
        ),
    ]

    print("Running verification for lc_0463_island_perimeter_solution.py...")
    for idx, (g, expected) in enumerate(test_cases, 1):
        res = island_perimeter(g)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
