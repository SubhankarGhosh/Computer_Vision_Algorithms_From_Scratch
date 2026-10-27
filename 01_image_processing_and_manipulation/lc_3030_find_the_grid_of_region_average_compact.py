"""LeetCode 3030: Find the Grid of Region Average (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/find-the-grid-of-region-average/
Difficulty: Medium
Category: Image Processing & Manipulation

Computer Vision Context:
    Edge-Preserving Smoothing & Adaptive Local Window Filtering:
    Traditional linear blur (such as Gaussian or box filter) blurs across high-contrast edges.
    Bilateral and edge-preserving filters restrict neighborhood averaging only to regions where
    adjacent pixel gradients |I(p1) - I(p2)| do not exceed a given threshold.
    
    In this problem:
    - A 3x3 subgrid is a "valid region" iff every adjacent horizontal and vertical pixel pair
      within the 3x3 patch satisfies |image[r1][c1] - image[r2][c2]| <= threshold (12 edge checks).
    - The average of a valid region is floor(sum(9 pixels) / 9).
    - Each pixel's output is the floored average of all valid region averages containing it.
    - If a pixel belongs to no valid regions, it retains its original value.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 01_image_processing_and_manipulation/lc_3030_find_the_grid_of_region_average_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def result_grid(image: List[List[int]], threshold: int) -> List[List[int]]:
    """Computes the region-averaged grid using edge-preserving 3x3 subgrid checks.

    Algorithmic Requirements:
    - Time Complexity: O(m * n). There are (m - 2) * (n - 2) possible 3x3 patches,
      each requiring constant 12 edge checks and 9 pixel additions (O(1) work per patch).
    - Space Complexity: O(m * n) to track sum of region averages and region counts per pixel.

    Steps to implement:
    1. Initialize `sum_intensities` (m x n) and `count` (m x n) with 0s.
    2. Define helper `is_valid_region(top_r, top_c)`:
       - Check horizontal adjacencies for rows top_r to top_r + 2:
         |image[i][j] - image[i][j+1]| <= threshold for j in [top_c, top_c + 1]
       - Check vertical adjacencies for cols top_c to top_c + 2:
         |image[i][j] - image[i+1][j]| <= threshold for i in [top_r, top_r + 1]
    3. Loop top_r from 0 to m - 3 and top_c from 0 to n - 3:
       - If is_valid_region(top_r, top_c):
         - Compute patch average: avg = sum(9 pixels) // 9
         - For all (i, j) in [top_r, top_r+2] x [top_c, top_c+2]:
           sum_intensities[i][j] += avg
           count[i][j] += 1
    4. Construct `result` matrix:
       - If count[i][j] > 0: result[i][j] = sum_intensities[i][j] // count[i][j]
       - Else: result[i][j] = image[i][j]

    -------------------------------------------------------------------------
    TODO: Complete the region validity and output reconstruction logic.
    -------------------------------------------------------------------------
    """
    m, n = len(image), len(image[0])
    sum_intensities = [[0] * n for _ in range(m)]
    count = [[0] * n for _ in range(m)]

    def is_valid_region(r: int, c: int) -> bool:
        # Check horizontal adjacencies (3 rows, 2 pairs each = 6 checks)
        for i in range(r, r + 3):
            for j in range(c, c + 2):
                if abs(image[i][j] - image[i][j + 1]) > threshold:
                    return False
        # Check vertical adjacencies (2 pairs each across 3 cols = 6 checks)
        for i in range(r, r + 2):
            for j in range(c, c + 3):
                if abs(image[i][j] - image[i + 1][j]) > threshold:
                    return False
        return True

    # Traverse all 3x3 windows
    for r in range(m - 2):
        for c in range(n - 2):
            if is_valid_region(r, c):
                # Calculate the 3x3 patch average
                region_sum = 0
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        region_sum += image[i][j]
                
                avg = region_sum // 9

                # Accumulate for all 9 cells in this region
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        sum_intensities[i][j] += avg
                        count[i][j] += 1

    # Build final result grid
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            # <<< YOUR CODE HERE >>>
            # Hint: if count[i][j] > 0, set result to sum_intensities[i][j] // count[i][j]
            # otherwise keep image[i][j]
            pixel_val = TODO  # Replace with: (sum_intensities[i][j] // count[i][j]) if count[i][j] > 0 else image[i][j]
            if pixel_val is None:
                raise NotImplementedError("TODO: Reconstruct pixel intensity from region averages.")
            result[i][j] = pixel_val

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

    print("Running tests for lc_3030_find_the_grid_of_region_average_compact.py...")
    try:
        for idx, (img, thresh, expected) in enumerate(test_cases, 1):
            res = result_grid(img, thresh)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
