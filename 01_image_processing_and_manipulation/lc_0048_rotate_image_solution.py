"""LeetCode 48: Rotate Image (Reference Solution)

Problem URL: https://leetcode.com/problems/rotate-image/
Difficulty: Medium
Category: Image Processing & Manipulation

Computer Vision Context:
    Orthogonal 90-degree clockwise image rotation:
        (r, c) -> (c, n - 1 - r)
    Decomposition into linear transformations:
        1. Transpose: (r, c) -> (c, r)
        2. Horizontal Reflection: (c, r) -> (c, n - 1 - r)
"""

from __future__ import annotations
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """Rotates an n x n 2D matrix by 90 degrees clockwise in-place.

    Complexity Analysis:
    - Time Complexity: O(n^2).
      Transposing accesses n*(n-1)/2 elements.
      Reversing rows accesses n*(n/2) elements.
      Total operations ~ n^2.
    - Space Complexity: O(1) auxiliary space, modifying matrix directly in-place.
    """
    n = len(matrix)

    # 1. Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 2. Reflect horizontally (reverse each row)
    for i in range(n):
        left, right = 0, n - 1
        while left < right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
        ),
        (
            [
                [5, 1, 9, 11],
                [2, 4, 8, 10],
                [13, 3, 6, 7],
                [15, 14, 12, 16],
            ],
            [
                [15, 13, 2, 5],
                [14, 3, 4, 1],
                [12, 6, 8, 9],
                [16, 7, 10, 11],
            ],
        ),
        (
            [[1]],
            [[1]],
        ),
        (
            [[1, 2], [3, 4]],
            [[3, 1], [4, 2]],
        ),
    ]

    print("Running verification for lc_0048_rotate_image_solution.py...")
    for idx, (mat, expected) in enumerate(test_cases, 1):
        mat_copy = [row[:] for row in mat]
        rotate(mat_copy)
        assert mat_copy == expected, f"Case {idx} failed: got {mat_copy}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
