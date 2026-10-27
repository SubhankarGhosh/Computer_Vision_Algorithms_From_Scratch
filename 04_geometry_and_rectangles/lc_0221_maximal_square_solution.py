"""LeetCode 221: Maximal Square (Reference Solution)

Problem URL: https://leetcode.com/problems/maximal-square/
Difficulty: Medium
Category: Geometry & Rectangles

Computer Vision Context:
    Morphological Square Structuring Element Fitting via 2D Dynamic Programming:
    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
"""

from __future__ import annotations
from typing import List


def maximal_square(matrix: List[List[str]]) -> int:
    """Finds the largest square containing only 1's and returns its area.

    Complexity Analysis:
    - Time Complexity: O(m * n). Evaluates each matrix cell once.
    - Space Complexity: O(m * n) DP table (can be compressed to O(n)).
    """
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_side = 0

    for r in range(1, m + 1):
        for c in range(1, n + 1):
            if matrix[r - 1][c - 1] == "1":
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
                max_side = max(max_side, dp[r][c])

    return max_side * max_side


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ],
            4,
        ),
        (
            [["0", "1"], ["1", "0"]],
            1,
        ),
        (
            [["0"]],
            0,
        ),
    ]

    print("Running verification for lc_0221_maximal_square_solution.py...")
    for idx, (mat, expected) in enumerate(test_cases, 1):
        res = maximal_square(mat)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
