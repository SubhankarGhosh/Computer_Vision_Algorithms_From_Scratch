"""LeetCode 221: Maximal Square (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/maximal-square/
Difficulty: Medium
Category: Geometry & Rectangles

Computer Vision Context:
    Morphological Square Structuring Element Fitting:
    In mathematical morphology, erosion by a square structuring element of size k x k
    identifies all regions that can completely enclose a k x k square.
    Using 2D Dynamic Programming, dp[r][c] represents the side length of the maximal square
    having its bottom-right corner at (r, c):
        dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1  (if matrix[r][c] == '1')
    The maximum square area is max(dp)^2.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 04_geometry_and_rectangles/lc_0221_maximal_square_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def maximal_square(matrix: List[List[str]]) -> int:
    """Finds the largest square containing only 1's and returns its area.

    Algorithmic Requirements:
    - Time Complexity: O(m * n). Single 2D DP pass.
    - Space Complexity: O(m * n) or O(n) auxiliary DP table.

    Steps to implement:
    1. Base case: if not matrix or not matrix[0], return 0.
    2. Dimensions m = len(matrix), n = len(matrix[0]).
    3. Initialize dp matrix of size (m + 1) x (n + 1) with 0s.
    4. max_side = 0.
    5. Iterate r from 1 to m and c from 1 to n:
       - If matrix[r-1][c-1] == '1':
         - dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
         - max_side = max(max_side, dp[r][c])
    6. Return max_side * max_side.

    -------------------------------------------------------------------------
    TODO: Implement the 2D DP square fitting recurrence.
    -------------------------------------------------------------------------
    """
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_side = 0

    for r in range(1, m + 1):
        for c in range(1, n + 1):
            if matrix[r - 1][c - 1] == "1":
                # <<< YOUR CODE HERE >>>
                # Hint: Side length is 1 + min of top, left, and top-left DP neighbors
                top = dp[r - 1][c]
                left = dp[r][c - 1]
                top_left = dp[r - 1][c - 1]

                side_len = TODO  # Replace with: min(top, left, top_left) + 1
                if side_len is None:
                    raise NotImplementedError("TODO: Apply DP transition min(top, left, top_left) + 1.")
                dp[r][c] = side_len
                max_side = max(max_side, side_len)

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

    print("Running tests for lc_0221_maximal_square_compact.py...")
    try:
        for idx, (mat, expected) in enumerate(test_cases, 1):
            res = maximal_square(mat)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
