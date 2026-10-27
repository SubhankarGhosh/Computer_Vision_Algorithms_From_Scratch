"""LeetCode 48: Rotate Image (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/rotate-image/
Difficulty: Medium
Category: Image Processing & Manipulation

Computer Vision Context:
    An affine 90-degree clockwise image rotation transforms spatial coordinates
    from (r, c) to (c, n - 1 - r).
    In linear algebra and spatial transformations, this orthogonal transformation
    can be decomposed into two elementary operations:
        1. Matrix Transpose: M[r][c] <-> M[c][r]
        2. Horizontal Row Reversal: row.reverse() (reflection along the vertical midline)

    This decomposition allows the operation to run strictly IN-PLACE with O(1) auxiliary space,
    avoiding memory allocation for large image buffers.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 01_image_processing_and_manipulation/lc_0048_rotate_image_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def rotate(matrix: List[List[int]]) -> None:
    """Rotates an n x n 2D matrix by 90 degrees clockwise in-place.

    Algorithmic Requirements:
    - Time Complexity: O(n^2) where n is the dimension of the square matrix.
    - Space Complexity: O(1) auxiliary memory (do NOT allocate another 2D matrix).

    Steps to implement:
    1. Transpose the matrix in-place:
       - Iterate i from 0 to n - 1.
       - Iterate j from i + 1 to n - 1 (only upper triangle to avoid double-swapping!).
       - Swap matrix[i][j] with matrix[j][i].
    2. Reverse each row:
       - For each row in matrix:
         - Reverse the row in-place (e.g. using two pointers or row.reverse()).

    -------------------------------------------------------------------------
    TODO: Implement the in-place transpose and row reflection logic below.
    -------------------------------------------------------------------------
    """
    n = len(matrix)

    # Step 1: Transpose matrix (swap along the main diagonal)
    for i in range(n):
        for j in range(i + 1, n):
            # <<< YOUR CODE HERE >>>
            # Hint: swap matrix[i][j] and matrix[j][i]
            # Set target = (matrix[j][i], matrix[i][j])
            swapped = TODO  # Replace with: (matrix[j][i], matrix[i][j])
            if swapped is None:
                raise NotImplementedError("TODO: Implement matrix transposition.")
            matrix[i][j], matrix[j][i] = swapped

    # Step 2: Reverse each row horizontally
    for i in range(n):
        left, right = 0, n - 1
        while left < right:
            # <<< YOUR CODE HERE >>>
            # Hint: swap matrix[i][left] and matrix[i][right]
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

    print("Running tests for lc_0048_rotate_image_compact.py...")
    try:
        for idx, (mat, expected) in enumerate(test_cases, 1):
            mat_copy = [row[:] for row in mat]
            rotate(mat_copy)
            assert mat_copy == expected, f"Case {idx} failed: got {mat_copy}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
