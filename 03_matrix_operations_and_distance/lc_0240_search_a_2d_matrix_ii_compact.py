"""LeetCode 240: Search a 2D Matrix II (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/search-a-2d-matrix-ii/
Difficulty: Medium
Category: Matrix Operations & Distance

Computer Vision Context:
    Saddleback Search / Monotonic 2D Gradient Descent:
    Given a matrix where each row and each column is sorted independently,
    we can prune an entire row or column at each step.
    By starting at the top-right saddle point (0, n - 1):
        - If matrix[r][c] > target: the entire column c must be > target -> c -= 1
        - If matrix[r][c] < target: the entire row r must be < target -> r += 1
    This achieves optimal O(m + n) time complexity without flattened binary search.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 03_matrix_operations_and_distance/lc_0240_search_a_2d_matrix_ii_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """Searches for target in a row-sorted and column-sorted matrix in O(m + n) time.

    Algorithmic Requirements:
    - Time Complexity: O(m + n) where m is row count and n is column count.
    - Space Complexity: O(1) auxiliary space.

    Steps to implement:
    1. Check base case: if not matrix or not matrix[0], return False.
    2. Start at top-right corner: r = 0, c = len(matrix[0]) - 1.
    3. While r < len(matrix) and c >= 0:
       - If matrix[r][c] == target: return True
       - If matrix[r][c] > target: decrement c -= 1 (eliminate column)
       - If matrix[r][c] < target: increment r += 1 (eliminate row)
    4. Return False if out of bounds.

    -------------------------------------------------------------------------
    TODO: Implement saddleback pointer advancement logic.
    -------------------------------------------------------------------------
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
            # <<< YOUR CODE HERE >>>
            # Hint: Value too large; eliminate current column by moving left (c -= 1)
            next_col = TODO  # Replace with: c - 1
            if next_col is None:
                raise NotImplementedError("TODO: Move left to eliminate column.")
            c = next_col
        else:
            # Value too small; eliminate current row by moving down (r += 1)
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

    print("Running tests for lc_0240_search_a_2d_matrix_ii_compact.py...")
    try:
        for idx, (mat, target, expected) in enumerate(test_cases, 1):
            res = search_matrix(mat, target)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
