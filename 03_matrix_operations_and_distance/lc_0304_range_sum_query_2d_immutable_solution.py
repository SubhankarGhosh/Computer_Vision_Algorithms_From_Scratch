"""LeetCode 304: Range Sum Query 2D - Immutable (Reference Solution)

Problem URL: https://leetcode.com/problems/range-sum-query-2d-immutable/
Difficulty: Medium
Category: Matrix Operations & Distance

Computer Vision Context:
    Integral Images (Summed-Area Tables for Viola-Jones Haar-like Features):
    Evaluates arbitrary rectangular box integrals in O(1) time.
"""

from __future__ import annotations
from typing import List


class NumMatrix:
    """Precomputes a 2D Summed-Area Table to answer rectangular sum queries in O(1) time."""

    def __init__(self, matrix: List[List[int]]):
        """Initializes the (m+1) x (n+1) 1-based prefix sum table.

        Complexity Analysis:
        - Time Complexity: O(m * n) construction.
        - Space Complexity: O(m * n) to store the prefix sum matrix.
        """
        if not matrix or not matrix[0]:
            self.pref = [[0]]
            return

        m, n = len(matrix), len(matrix[0])
        self.pref = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                self.pref[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.pref[r][c + 1]
                    + self.pref[r + 1][c]
                    - self.pref[r][c]
                )

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """Returns the sum of elements inside the rectangle in O(1) time.

        Complexity Analysis:
        - Time Complexity: O(1) per query.
        - Space Complexity: O(1).
        """
        return (
            self.pref[row2 + 1][col2 + 1]
            - self.pref[row1][col2 + 1]
            - self.pref[row2 + 1][col1]
            + self.pref[row1][col1]
        )


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    mat = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]

    print("Running verification for lc_0304_range_sum_query_2d_immutable_solution.py...")
    num_mat = NumMatrix(mat)
    assert num_mat.sum_region(2, 1, 4, 3) == 8, "Query 1 failed"
    assert num_mat.sum_region(1, 1, 2, 2) == 11, "Query 2 failed"
    assert num_mat.sum_region(1, 2, 2, 4) == 12, "Query 3 failed"
    print("  [PASS] Query (2,1)->(4,3) == 8")
    print("  [PASS] Query (1,1)->(2,2) == 11")
    print("  [PASS] Query (1,2)->(2,4) == 12")
    print("All tests passed with 100% success rate!")
