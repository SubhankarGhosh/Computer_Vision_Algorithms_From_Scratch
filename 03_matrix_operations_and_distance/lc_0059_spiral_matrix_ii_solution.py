"""LeetCode 59: Spiral Matrix II (Reference Solution)

Problem URL: https://leetcode.com/problems/spiral-matrix-ii/
Difficulty: Medium
Category: Matrix Operations & Distance

Computer Vision Context:
    Concentric perimeter boundary generation from 1 to n^2.
"""

from __future__ import annotations
from typing import List


def generate_matrix(n: int) -> List[List[int]]:
    """Generates an n x n matrix filled with 1 to n^2 in spiral order.

    Complexity Analysis:
    - Time Complexity: O(n^2). Populates each cell once.
    - Space Complexity: O(1) auxiliary space (excluding the n x n result matrix).
    """
    mat = [[0] * n for _ in range(n)]
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1

    while top <= bottom and left <= right:
        # 1. Right
        for c in range(left, right + 1):
            mat[top][c] = num
            num += 1
        top += 1

        # 2. Down
        for r in range(top, bottom + 1):
            mat[r][right] = num
            num += 1
        right -= 1

        # 3. Left
        if top <= bottom:
            for c in range(right, left - 1, -1):
                mat[bottom][c] = num
                num += 1
            bottom -= 1

        # 4. Up
        if left <= right:
            for r in range(bottom, top - 1, -1):
                mat[r][left] = num
                num += 1
            left += 1

    return mat


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            3,
            [[1, 2, 3], [8, 9, 4], [7, 6, 5]],
        ),
        (
            1,
            [[1]],
        ),
        (
            2,
            [[1, 2], [4, 3]],
        ),
    ]

    print("Running verification for lc_0059_spiral_matrix_ii_solution.py...")
    for idx, (n_dim, expected) in enumerate(test_cases, 1):
        res = generate_matrix(n_dim)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
