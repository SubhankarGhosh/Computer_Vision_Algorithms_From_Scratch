"""LeetCode 304: Range Sum Query 2D - Immutable (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/range-sum-query-2d-immutable/
Difficulty: Medium
Category: Matrix Operations & Distance

Computer Vision Context:
    Integral Images (Summed-Area Tables):
    Introduced by Crow (1984) and revolutionized by the Viola-Jones Face Detector (2001),
    an Integral Image precomputes cumulative 2D sums such that the sum of pixel intensities
    over ANY arbitrary rectangular box can be evaluated in exactly O(1) time using 4 array lookups:
        Area(D) = SAT(r2, c2) - SAT(r1-1, c2) - SAT(r2, c1-1) + SAT(r1-1, c1-1)

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 03_matrix_operations_and_distance/lc_0304_range_sum_query_2d_immutable_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


class NumMatrix:
    """Precomputes a 2D Summed-Area Table to answer rectangular sum queries in O(1) time."""

    def __init__(self, matrix: List[List[int]]):
        """Initializes the (m+1) x (n+1) 1-based prefix sum table.

        Algorithmic Requirements:
        - Time Complexity: O(m * n) construction.
        - Space Complexity: O(m * n) to store prefix table.
        """
        if not matrix or not matrix[0]:
            self.pref = [[0]]
            return

        m, n = len(matrix), len(matrix[0])
        # 1-based padding to eliminate boundary checks
        self.pref = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                # pref[r+1][c+1] = matrix[r][c] + top + left - top_left
                self.pref[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.pref[r][c + 1]
                    + self.pref[r + 1][c]
                    - self.pref[r][c]
                )

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """Returns the sum of elements inside the rectangle defined by (row1, col1) to (row2, col2).

        Algorithmic Requirements:
        - Time Complexity: O(1) per query.
        - Space Complexity: O(1).

        Inclusion-Exclusion Formula with 1-based indexing:
            Total = pref[row2 + 1][col2 + 1]
            SubTop = pref[row1][col2 + 1]
            SubLeft = pref[row2 + 1][col1]
            AddTopLeft = pref[row1][col1]
            Result = Total - SubTop - SubLeft + AddTopLeft

        -------------------------------------------------------------------------
        TODO: Implement the O(1) 4-corner inclusion-exclusion calculation.
        -------------------------------------------------------------------------
        """
        # <<< YOUR CODE HERE >>>
        # Hint: Total - top_strip - left_strip + intersection
        total = self.pref[row2 + 1][col2 + 1]
        top_strip = self.pref[row1][col2 + 1]
        left_strip = self.pref[row2 + 1][col1]
        top_left = self.pref[row1][col1]

        ans = TODO  # Replace with: total - top_strip - left_strip + top_left
        if ans is None:
            raise NotImplementedError("TODO: Compute box sum via inclusion-exclusion.")
        return ans


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

    print("Running tests for lc_0304_range_sum_query_2d_immutable_compact.py...")
    try:
        num_mat = NumMatrix(mat)
        assert num_mat.sum_region(2, 1, 4, 3) == 8, "Query 1 failed"
        assert num_mat.sum_region(1, 1, 2, 2) == 11, "Query 2 failed"
        assert num_mat.sum_region(1, 2, 2, 4) == 12, "Query 3 failed"
        print("  [PASS] All box sum queries matched expected values!")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
