"""LeetCode 54: Spiral Matrix (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/spiral-matrix/
Difficulty: Medium
Category: Matrix Operations & Distance

Computer Vision Context:
    Boundary Peeling & Space-Filling Curves:
    Traverses a 2D matrix in outward-in concentric rectangular perimeters (spiral scanning).
    In vision, perimeter scanning order is used in contour encoding, chained perimeter tracking,
    and progressive raster generation.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 03_matrix_operations_and_distance/lc_0054_spiral_matrix_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """Returns all elements of the matrix in spiral order.

    Algorithmic Requirements:
    - Time Complexity: O(m * n). Visits every cell exactly once.
    - Space Complexity: O(1) auxiliary space (excluding output list).

    Steps to implement:
    1. If not matrix or not matrix[0], return [].
    2. Initialize boundaries:
       top = 0, bottom = len(matrix) - 1
       left = 0, right = len(matrix[0]) - 1
    3. Loop while top <= bottom and left <= right:
       - Move Right: for c from left to right: append matrix[top][c]; top += 1
       - Move Down: for r from top to bottom: append matrix[r][right]; right -= 1
       - Move Left (if top <= bottom): for c from right down to left: append matrix[bottom][c]; bottom -= 1
       - Move Up (if left <= right): for r from bottom down to top: append matrix[r][left]; left += 1
    4. Return result list.

    -------------------------------------------------------------------------
    TODO: Implement boundary-peeling spiral traversal logic.
    -------------------------------------------------------------------------
    """
    if not matrix or not matrix[0]:
        return []

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    result: List[int] = []

    while top <= bottom and left <= right:
        # 1. Traverse Right along top boundary
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1

        # 2. Traverse Down along right boundary
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1

        # 3. Traverse Left along bottom boundary (guard top <= bottom)
        if top <= bottom:
            for c in range(right, left - 1, -1):
                # <<< YOUR CODE HERE >>>
                # Hint: Append matrix[bottom][c]
                val = TODO  # Replace with: matrix[bottom][c]
                if val is None:
                    raise NotImplementedError("TODO: Traverse bottom boundary from right to left.")
                result.append(val)
            bottom -= 1

        # 4. Traverse Up along left boundary (guard left <= right)
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

    print("Running tests for lc_0054_spiral_matrix_compact.py...")
    try:
        for idx, (mat, expected) in enumerate(test_cases, 1):
            res = spiral_order(mat)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
