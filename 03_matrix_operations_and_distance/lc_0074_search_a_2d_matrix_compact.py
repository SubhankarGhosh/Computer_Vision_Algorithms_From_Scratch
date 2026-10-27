"""LeetCode 74: Search a 2D Matrix (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/search-a-2d-matrix/
Difficulty: Medium
Category: Matrix Operations & Distance

Computer Vision Context:
    Raster-Scan 1D Coordinate Mapping:
    In graphics hardware and framebuffers, a 2D raster image of size m x n is stored
    contiguously in linear memory:
        index = r * n + c  <===>  r = index // n,  c = index % n
    Since the matrix elements are monotonically increasing row-to-row, the entire matrix
    behaves as a sorted 1D array, enabling O(log(m * n)) binary search.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 03_matrix_operations_and_distance/lc_0074_search_a_2d_matrix_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """Searches for a target value in an m x n matrix using virtual 1D binary search.

    Algorithmic Requirements:
    - Time Complexity: O(log(m * n)).
    - Space Complexity: O(1) auxiliary memory.

    Steps to implement:
    1. If not matrix or not matrix[0], return False.
    2. m = len(matrix), n = len(matrix[0]).
    3. Initialize two pointers: left = 0, right = m * n - 1.
    4. While left <= right:
       - mid = (left + right) // 2
       - Map mid to 2D coordinate: r = mid // n, c = mid % n
       - mid_val = matrix[r][c]
       - If mid_val == target: return True
       - If mid_val < target: left = mid + 1
       - Else: right = mid - 1
    5. Return False if not found.

    -------------------------------------------------------------------------
    TODO: Implement virtual 1D binary search coordinate mapping.
    -------------------------------------------------------------------------
    """
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        # <<< YOUR CODE HERE >>>
        # Hint: Map 1D index mid to 2D coordinates (mid // n, mid % n)
        r = mid // n
        c = mid % n

        mid_val = matrix[r][c]
        if mid_val == target:
            found_flag = TODO  # Replace with: True
            if found_flag is None:
                raise NotImplementedError("TODO: Return True when target is found.")
            return found_flag
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

    print("Running tests for lc_0074_search_a_2d_matrix_compact.py...")
    try:
        for idx, (mat, target, expected) in enumerate(test_cases, 1):
            res = search_matrix(mat, target)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
