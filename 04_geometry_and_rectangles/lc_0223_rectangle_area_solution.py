"""LeetCode 223: Rectangle Area (Reference Solution)

Problem URL: https://leetcode.com/problems/rectangle-area/
Difficulty: Medium
Category: Geometry & Rectangles

Computer Vision Context:
    Intersection-over-Union (IoU) Union Area Calculation:
    Area(A cup B) = Area(A) + Area(B) - Area(A cap B)
"""

from __future__ import annotations


def compute_area(
    ax1: int, ay1: int, ax2: int, ay2: int,
    bx1: int, by1: int, bx2: int, by2: int
) -> int:
    """Calculates the total area covered by two 2D axis-aligned rectangles.

    Complexity Analysis:
    - Time Complexity: O(1).
    - Space Complexity: O(1).
    """
    area_a = (ax2 - ax1) * (ay2 - ay1)
    area_b = (bx2 - bx1) * (by2 - by1)

    overlap_w = max(0, min(ax2, bx2) - max(ax1, bx1))
    overlap_h = max(0, min(ay2, by2) - max(ay1, by1))
    overlap_area = overlap_w * overlap_h

    return area_a + area_b - overlap_area


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (-3, 0, 3, 4, 0, -1, 9, 2, 45),
        (-2, -2, 2, 2, -2, -2, 2, 2, 16),
        (0, 0, 2, 2, 2, 2, 4, 4, 8),
    ]

    print("Running verification for lc_0223_rectangle_area_solution.py...")
    for idx, (ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, expected) in enumerate(test_cases, 1):
        res = compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
