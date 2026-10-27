"""LeetCode 74: Search a 2D Matrix (Reference Solution)

Problem URL: https://leetcode.com/problems/search-a-2d-matrix/
Difficulty: Medium
Category: Matrix Operations & Distance

Computer Vision Context:
    Virtual 1D Raster Indexing:
    r = index // n,  c = index % n
    Enables logarithmic search over row-major sorted grids.
"""

from __future__ import annotations
from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """Searches for a target value in an m x n matrix using virtual 1D binary search.

    Complexity Analysis:
    - Time Complexity: O(log(m * n)). Exactly logarithmic in total cell count.
    - Space Complexity: O(1) auxiliary space.
    """
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        r = mid // n
        c = mid % n
        mid_val = matrix[r][c]

        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3,
            True,
        ),
        (
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13,
            False,
        ),
        (
            [[1]], 1,
            True,
        ),
        (
            [[1]], 2,
            False,
        ),
    ]

    print("Running verification for lc_0074_search_a_2d_matrix_solution.py...")
    for idx, (mat, target, expected) in enumerate(test_cases, 1):
        res = search_matrix(mat, target)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
