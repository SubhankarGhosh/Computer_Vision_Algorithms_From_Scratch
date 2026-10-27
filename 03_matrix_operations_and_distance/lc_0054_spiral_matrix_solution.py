"""LeetCode 54: Spiral Matrix (Reference Solution)

Problem URL: https://leetcode.com/problems/spiral-matrix/
Difficulty: Medium
Category: Matrix Operations & Distance

Computer Vision Context:
    Concentric perimeter peeling and space-filling spiral scanning.
"""

from __future__ import annotations
from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """Returns all elements of the matrix in spiral order.

    Complexity Analysis:
    - Time Complexity: O(m * n). Exactly one visit per element.
    - Space Complexity: O(1) auxiliary space (excluding result array).
    """
    if not matrix or not matrix[0]:
        return []

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    result: List[int] = []

    while top <= bottom and left <= right:
        # 1. Right
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1

        # 2. Down
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1

        # 3. Left
        if top <= bottom:
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1

        # 4. Up
        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1

    return result


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        ),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
        (
            [[7]],
            [7],
        ),
    ]

    print("Running verification for lc_0054_spiral_matrix_solution.py...")
    for idx, (mat, expected) in enumerate(test_cases, 1):
        res = spiral_order(mat)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
