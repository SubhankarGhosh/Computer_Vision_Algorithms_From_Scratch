"""LeetCode 835: Image Overlap (Reference Solution)

Problem URL: https://leetcode.com/problems/image-overlap/
Difficulty: Medium
Category: Image Processing & Manipulation

Computer Vision Context:
    2D Discrete Cross-Correlation via Active Coordinate Mapping:
    Instead of sliding a window across all (2n - 1)^2 translations (dense approach),
    we map active foreground pixels A and B:
        shift_vector = (r_b - r_a, c_b - c_a)
    The translation vector that occurs with the highest frequency maximizes the overlap.
"""

from __future__ import annotations
import collections
from typing import List, Tuple


def largest_overlap(img1: List[List[int]], img2: List[List[int]]) -> int:
    """Calculates the maximum possible overlap of 1s between two binary images under 2D translation.

    Complexity Analysis:
    - Time Complexity: O(A * B + n^2) where A is count of 1s in img1, B is count of 1s in img2.
      In the worst case (all 1s), A = B = n^2, giving O(n^4).
      In typical image processing with sparse masks (A, B << n^2), this runs in O(sparse) time.
    - Space Complexity: O(A + B) to store coordinates of active pixels and displacement histogram.
    """
    n = len(img1)

    points1: List[Tuple[int, int]] = []
    points2: List[Tuple[int, int]] = []

    for r in range(n):
        for c in range(n):
            if img1[r][c] == 1:
                points1.append((r, c))
            if img2[r][c] == 1:
                points2.append((r, c))

    if not points1 or not points2:
        return 0

    shift_counts: collections.defaultdict[Tuple[int, int], int] = collections.defaultdict(int)

    for r1, c1 in points1:
        for r2, c2 in points2:
            shift = (r2 - r1, c2 - c1)
            shift_counts[shift] += 1

    return max(shift_counts.values()) if shift_counts else 0


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [[1, 1, 0], [0, 1, 0], [0, 1, 0]],
            [[0, 0, 0], [0, 1, 1], [0, 0, 1]],
            3,
        ),
        (
            [[1]],
            [[1]],
            1,
        ),
        (
            [[0]],
            [[0]],
            0,
        ),
        (
            [[1, 0], [0, 0]],
            [[0, 0], [0, 1]],
            1,
        ),
    ]

    print("Running verification for lc_0835_image_overlap_solution.py...")
    for idx, (img1, img2, expected) in enumerate(test_cases, 1):
        res = largest_overlap(img1, img2)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
