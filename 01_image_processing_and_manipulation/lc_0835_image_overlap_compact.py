"""LeetCode 835: Image Overlap (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/image-overlap/
Difficulty: Medium
Category: Image Processing & Manipulation

Computer Vision Context:
    In template matching and motion estimation, discrete cross-correlation computes
    the degree of alignment between two binary images under rigid spatial translation.
    Given two binary images img1 and img2 of size n x n:
    Translating img1 by an offset vector (dr, dc) aligns pixel (r1, c1) with (r1 + dr, c1 + dc).
    If img1[r1][c1] == 1 and img2[r2][c2] == 1, they coincide under shift:
        (dr, dc) = (r2 - r1, c2 - c1)

    By accumulating a 2D histogram of shift vectors between all active (foreground)
    pixels in img1 and img2, the mode of the histogram directly gives the maximum overlap.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 01_image_processing_and_manipulation/lc_0835_image_overlap_compact.py
"""

from __future__ import annotations
import collections
from typing import List, Tuple

# Sentinel placeholder for exercise tasks
TODO = None


def largest_overlap(img1: List[List[int]], img2: List[List[int]]) -> int:
    """Calculates the maximum possible overlap of 1s between two binary images under 2D translation.

    Algorithmic Requirements:
    - Time Complexity: O(A * B + n^2) where A and B are counts of 1s in img1 and img2 (at most n^4).
      Significantly faster than exhaustive dense window shifting O(n^4) on sparse masks.
    - Space Complexity: O(A + B) to store coordinates of active pixels and shift counts.

    Steps to implement:
    1. Extract coordinates of all active pixels (value == 1) in img1 into list `points1`.
    2. Extract coordinates of all active pixels (value == 1) in img2 into list `points2`.
    3. If either list is empty, return 0 (no possible overlap).
    4. Initialize a frequency counter `shift_counts = collections.defaultdict(int)`.
    5. For each (r1, c1) in points1:
       - For each (r2, c2) in points2:
         - Compute displacement vector: shift = (r2 - r1, c2 - c1)
         - Increment shift_counts[shift] += 1
    6. Return the maximum frequency found in shift_counts (or 0 if empty).

    -------------------------------------------------------------------------
    TODO: Implement coordinate extraction and displacement vector counting.
    -------------------------------------------------------------------------
    """
    n = len(img1)

    # Step 1: Collect coordinates of 1s in img1 and img2
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

    # Step 2: Accumulate shift vectors
    shift_counts: collections.defaultdict[Tuple[int, int], int] = collections.defaultdict(int)

    # <<< YOUR CODE HERE >>>
    # Hint: For each (r1, c1) in points1 and (r2, c2) in points2:
    # compute shift = (r2 - r1, c2 - c1) and increment shift_counts[shift]
    for r1, c1 in points1:
        for r2, c2 in points2:
            shift = TODO  # Replace with: (r2 - r1, c2 - c1)
            if shift is None:
                raise NotImplementedError("TODO: Compute displacement vector (r2 - r1, c2 - c1).")
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

    print("Running tests for lc_0835_image_overlap_compact.py...")
    try:
        for idx, (img1, img2, expected) in enumerate(test_cases, 1):
            res = largest_overlap(img1, img2)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
