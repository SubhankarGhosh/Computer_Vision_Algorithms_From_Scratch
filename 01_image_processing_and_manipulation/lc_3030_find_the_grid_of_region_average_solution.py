"""LeetCode 3030: Find the Grid of Region Average (Reference Solution)

Problem URL: https://leetcode.com/problems/find-the-grid-of-region-average/
Difficulty: Medium
Category: Image Processing & Manipulation

Computer Vision Context:
    Edge-Preserving Smoothing & Adaptive Local Window Filtering:
    Applies local mean filtering only over 3x3 patches where intra-patch gradient
    discontinuities |I(p1) - I(p2)| across all adjacent horizontal and vertical pairs
    do not exceed a given threshold.
"""

from __future__ import annotations
from typing import List


def result_grid(image: List[List[int]], threshold: int) -> List[List[int]]:
    """Computes the region-averaged grid using edge-preserving 3x3 subgrid checks.

    Complexity Analysis:
    - Time Complexity: O(m * n).
      There are (m - 2) * (n - 2) subgrids of size 3x3.
      Each subgrid requires exactly 12 edge difference checks and 9 pixel additions (O(1)).
      Building the result takes O(m * n) iterations.
      Overall time is linear in the number of pixels.
    - Space Complexity: O(m * n) auxiliary space for `sum_intensities` and `count` matrices.
    """
    m, n = len(image), len(image[0])
    sum_intensities = [[0] * n for _ in range(m)]
    count = [[0] * n for _ in range(m)]

    def is_valid_region(r: int, c: int) -> bool:
        # Check horizontal adjacencies (3 rows * 2 pairs = 6 checks)
        for i in range(r, r + 3):
            for j in range(c, c + 2):
                if abs(image[i][j] - image[i][j + 1]) > threshold:
                    return False
        # Check vertical adjacencies (2 pairs * 3 cols = 6 checks)
        for i in range(r, r + 2):
            for j in range(c, c + 3):
                if abs(image[i][j] - image[i + 1][j]) > threshold:
                    return False
        return True

    # Check each possible 3x3 top-left corner
    for r in range(m - 2):
        for c in range(n - 2):
            if is_valid_region(r, c):
                region_sum = 0
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        region_sum += image[i][j]
                avg = region_sum // 9

                # Accumulate for all 9 cells
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        sum_intensities[i][j] += avg
                        count[i][j] += 1

    # Formulate output grid
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if count[i][j] > 0:
                result[i][j] = sum_intensities[i][j] // count[i][j]
            else:
                result[i][j] = image[i][j]

    return result


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [[5, 6, 7, 10], [8, 9, 10, 10], [11, 12, 13, 10]],
            3,
            [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]],
        ),
        (
            [[10, 20, 30], [200, 50, 200], [10, 20, 30]],
            5,
            [[10, 20, 30], [200, 50, 200], [10, 20, 30]],
        ),
    ]

    print("Running verification for lc_3030_find_the_grid_of_region_average_solution.py...")
    for idx, (img, thresh, expected) in enumerate(test_cases, 1):
        res = result_grid(img, thresh)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
