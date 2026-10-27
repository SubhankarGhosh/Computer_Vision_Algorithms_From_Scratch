"""LeetCode 836: Rectangle Overlap (Reference Solution)

Problem URL: https://leetcode.com/problems/rectangle-overlap/
Difficulty: Easy
Category: Geometry & Rectangles

Computer Vision Context:
    Axis-Aligned Bounding Box (AABB) 1D Projection Overlap:
    Ensures both x-axis and y-axis intervals intersect with strictly positive width and height.
"""

from __future__ import annotations
from typing import List


def is_rectangle_overlap(rec1: List[int], rec2: List[int]) -> bool:
    """Determines whether two axis-aligned rectangles overlap with positive area.

    Complexity Analysis:
    - Time Complexity: O(1). Constant coordinate comparisons.
    - Space Complexity: O(1) auxiliary space.
    """
    # Guard against 0-area degenerate boxes
    if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:
        return False

    return (
        rec1[0] < rec2[2]
        and rec2[0] < rec1[2]
        and rec1[1] < rec2[3]
        and rec2[1] < rec1[3]
    )


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ([0, 0, 2, 2], [1, 1, 3, 3], True),
        ([0, 0, 1, 1], [1, 0, 2, 1], False),  # Sharing an edge is NOT an overlap
        ([0, 0, 1, 1], [2, 2, 3, 3], False),
        ([0, 0, 1, 1], [0, 0, 1, 1], True),
    ]

    print("Running verification for lc_0836_rectangle_overlap_solution.py...")
    for idx, (r1, r2, expected) in enumerate(test_cases, 1):
        res = is_rectangle_overlap(r1, r2)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
