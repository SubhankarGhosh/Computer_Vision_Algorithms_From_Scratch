"""LeetCode 240: Search a 2D Matrix II (Reference Solution)

Problem URL: https://leetcode.com/problems/search-a-2d-matrix-ii/
Difficulty: Medium
Category: Matrix Operations & Distance

Computer Vision Context:
    Saddleback Search:
    Prunes an entire row or column at each step starting from top-right corner.
"""

from __future__ import annotations
from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """Searches for target in a row-sorted and column-sorted matrix in O(m + n) time.

    Complexity Analysis:
    - Time Complexity: O(m + n). At each step, either r increases or c decreases.
    - Space Complexity: O(1) auxiliary space.
    """
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    r = 0
    c = n - 1

    while r < m and c >= 0:
        val = matrix[r][c]
        if val == target:
            return True
        elif val > target:
            c -= 1
        else:
            r += 1

    return False


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ], 5,
            True,
        ),
        (
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ], 20,
            False,
        ),
        (
            [[-5]], -5,
            True,
        ),
    ]

    print("Running verification for lc_0240_search_a_2d_matrix_ii_solution.py...")
    for idx, (mat, target, expected) in enumerate(test_cases, 1):
        res = search_matrix(mat, target)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
