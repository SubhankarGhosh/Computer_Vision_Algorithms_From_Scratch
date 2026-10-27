"""LeetCode 59: Spiral Matrix II (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/spiral-matrix-ii/
Difficulty: Medium
Category: Matrix Operations & Distance

Computer Vision Context:
    Synthetic Matrix Generation & Spiral Scanning:
    Constructs an n x n matrix populated sequentially from 1 to n^2 in clockwise spiral order.
    Demonstrates synthetic spatial coordinate generation used in image interpolation filters
    and procedural texture generation.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 03_matrix_operations_and_distance/lc_0059_spiral_matrix_ii_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def generate_matrix(n: int) -> List[List[int]]:
    """Generates an n x n matrix filled with 1 to n^2 in spiral order.

    Algorithmic Requirements:
    - Time Complexity: O(n^2). Populates each cell exactly once.
    - Space Complexity: O(1) auxiliary space (excluding the n x n output matrix).

    Steps to implement:
    1. Initialize `mat = [[0] * n for _ in range(n)]`.
    2. Boundaries: top = 0, bottom = n - 1, left = 0, right = n - 1.
    3. Counter: num = 1.
    4. While top <= bottom and left <= right:
       - Right: for c from left to right: mat[top][c] = num; num += 1; top += 1
       - Down: for r from top to bottom: mat[r][right] = num; num += 1; right -= 1
       - Left: for c from right down to left: mat[bottom][c] = num; num += 1; bottom -= 1
       - Up: for r from bottom down to top: mat[r][left] = num; num += 1; left += 1
    5. Return `mat`.

    -------------------------------------------------------------------------
    TODO: Implement spiral matrix generation logic.
    -------------------------------------------------------------------------
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
                # <<< YOUR CODE HERE >>>
                # Hint: Assign current num to mat[bottom][c] and increment num
                fill_val = TODO  # Replace with: num
                if fill_val is None:
                    raise NotImplementedError("TODO: Populate bottom row from right to left.")
                mat[bottom][c] = fill_val
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

    print("Running tests for lc_0059_spiral_matrix_ii_compact.py...")
    try:
        for idx, (n_dim, expected) in enumerate(test_cases, 1):
            res = generate_matrix(n_dim)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
