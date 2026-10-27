"""LeetCode 836: Rectangle Overlap (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/rectangle-overlap/
Difficulty: Easy
Category: Geometry & Rectangles

Computer Vision Context:
    Axis-Aligned Bounding Box (AABB) Intersection:
    In object detection and Non-Maximum Suppression (NMS), verifying whether two candidate
    bounding boxes intersect with positive area is the foundational step before calculating IoU.
    Given rec1 = [x1, y1, x2, y2] and rec2 = [x1, y1, x2, y2]:
    Two boxes overlap iff their 1D intervals overlap along BOTH x and y axes:
        x_overlap: max(rec1[0], rec2[0]) < min(rec1[2], rec2[2])
        y_overlap: max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 04_geometry_and_rectangles/lc_0836_rectangle_overlap_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def is_rectangle_overlap(rec1: List[int], rec2: List[int]) -> bool:
    """Determines whether two axis-aligned rectangles overlap with positive area.

    Algorithmic Requirements:
    - Time Complexity: O(1).
    - Space Complexity: O(1).

    Steps to implement:
    1. Check if either rectangle is degenerate (area == 0):
       if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]: return False
    2. Overlap occurs iff:
       rec1[0] < rec2[2] and rec2[0] < rec1[2] and
       rec1[1] < rec2[3] and rec2[1] < rec1[3]

    -------------------------------------------------------------------------
    TODO: Implement the 2D Separating Axis overlap check below.
    -------------------------------------------------------------------------
    """
    # Degenerate rectangle check
    if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:
        return False

    # <<< YOUR CODE HERE >>>
    # Hint: Ensure max(x1_a, x1_b) < min(x2_a, x2_b) and max(y1_a, y1_b) < min(y2_a, y2_b)
    x_overlap = rec1[0] < rec2[2] and rec2[0] < rec1[2]
    y_overlap = rec1[1] < rec2[3] and rec2[1] < rec1[3]

    overlap_result = TODO  # Replace with: x_overlap and y_overlap
    if overlap_result is None:
        raise NotImplementedError("TODO: Verify both x and y intervals overlap.")
    return overlap_result


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ([0, 0, 2, 2], [1, 1, 3, 3], True),
        ([0, 0, 1, 1], [1, 0, 2, 1], False),  # Sharing an edge is NOT positive area overlap
        ([0, 0, 1, 1], [2, 2, 3, 3], False),
        ([0, 0, 1, 1], [0, 0, 1, 1], True),
    ]

    print("Running tests for lc_0836_rectangle_overlap_compact.py...")
    try:
        for idx, (r1, r2, expected) in enumerate(test_cases, 1):
            res = is_rectangle_overlap(r1, r2)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
