"""LeetCode 661: Image Smoother (Reference Solution)

Problem URL: https://leetcode.com/problems/image-smoother/
Difficulty: Easy
Category: Image Processing & Manipulation

Computer Vision Context:
    Discrete 2D Box Blur / Mean Filter with clamping at image borders:
    I_smooth(r, c) = floor( (1 / |N(r, c)|) * sum_{p in N(r, c)} I(p) )
"""

from __future__ import annotations
from typing import List


def image_smoother(img: List[List[int]]) -> List[List[int]]:
    """Applies a 3x3 box blur filter over an m x n image.

    Complexity Analysis:
    - Time Complexity: O(m * n). Each pixel checks at most 9 neighbors, which is O(1) constant work per cell.
    - Space Complexity: O(m * n) to construct the output matrix.
      (Can be reduced to O(1) auxiliary space using 8-bit integer packing: val |= (avg << 8)).
    """
    m, n = len(img), len(img[0])
    result = [[0] * n for _ in range(m)]

    offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),  (0, 0),  (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    for r in range(m):
        for c in range(n):
            total_sum = 0
            count = 0
            for dr, dc in offsets:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    total_sum += img[nr][nc]
                    count += 1
            result[r][c] = total_sum // count

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

    print("Running verification for lc_0661_image_smoother_solution.py...")
    for idx, (grid, expected) in enumerate(test_cases, 1):
        res = image_smoother(grid)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
