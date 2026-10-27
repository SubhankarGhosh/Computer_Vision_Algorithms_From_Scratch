"""LeetCode 661: Image Smoother (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/image-smoother/
Difficulty: Easy
Category: Image Processing & Manipulation

Computer Vision Context:
    An image smoother applies a 3x3 uniform box blur filter (mean convolution filter).
    For each pixel (r, c), the smoothed intensity is the integer floor of the average
    of all valid neighboring pixels within its 3x3 window (including itself).
    Pixels on boundaries/corners average over fewer neighbors (6 or 4).

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 01_image_processing_and_manipulation/lc_0661_image_smoother_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def image_smoother(img: List[List[int]]) -> List[List[int]]:
    """Applies a 3x3 box blur filter over an m x n image.

    Algorithmic Requirements:
    - Time Complexity: O(m * n) since each pixel evaluates at most 9 neighbors.
    - Space Complexity: O(m * n) to store the smoothed result matrix.

    Steps to implement:
    1. Determine dimensions: m = len(img), n = len(img[0]).
    2. Initialize an output matrix `result` of size m x n filled with 0s.
    3. For every cell (r, c):
       - Initialize `total_sum = 0` and `count = 0`.
       - Iterate over neighbor offsets dr in [-1, 0, 1] and dc in [-1, 0, 1]:
         - nr, nc = r + dr, c + dc
         - If 0 <= nr < m and 0 <= nc < n:
           total_sum += img[nr][nc]
           count += 1
       - Set `result[r][c] = total_sum // count`.
    4. Return `result`.

    -------------------------------------------------------------------------
    TODO: Implement the 3x3 neighborhood convolution loop below.
    -------------------------------------------------------------------------
    """
    m, n = len(img), len(img[0])
    result = [[0] * n for _ in range(m)]

    for r in range(m):
        for c in range(n):
            total_sum = 0
            count = 0
            # <<< YOUR CODE HERE >>>
            # Hint: Iterate dr in (-1, 0, 1) and dc in (-1, 0, 1)
            # Accumulate img[r + dr][c + dc] when within grid bounds
            offsets = [(-1, -1), (-1, 0), (-1, 1),
                       (0, -1),  (0, 0),  (0, 1),
                       (1, -1),  (1, 0),  (1, 1)]
            
            for dr, dc in offsets:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    total_sum += img[nr][nc]
                    count += 1

            smoothed_val = TODO  # Replace with: total_sum // count
            if smoothed_val is None:
                raise NotImplementedError("TODO: Compute integer floored mean: total_sum // count")
            result[r][c] = smoothed_val

    return result


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        ),
        (
            [[100, 200, 100], [200, 50, 200], [100, 200, 100]],
            [[137, 141, 137], [141, 138, 141], [137, 141, 137]],
        ),
        (
            [[5]],
            [[5]],
        ),
    ]

    print("Running tests for lc_0661_image_smoother_compact.py...")
    try:
        for idx, (grid, expected) in enumerate(test_cases, 1):
            res = image_smoother(grid)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
