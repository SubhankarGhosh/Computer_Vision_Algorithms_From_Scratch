"""LeetCode 223: Rectangle Area (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/rectangle-area/
Difficulty: Medium
Category: Geometry & Rectangles

Computer Vision Context:
    Intersection-over-Union (IoU) Numerator & Inclusion-Exclusion:
    Computes the total 2D area covered by two rectilinear bounding boxes:
        Area(A cup B) = Area(A) + Area(B) - Area(A cap B)
    Used in object detection benchmarks (mAP calculation) and Non-Maximum Suppression (NMS).

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 04_geometry_and_rectangles/lc_0223_rectangle_area_compact.py
"""

from __future__ import annotations

# Sentinel placeholder for exercise tasks
TODO = None


def compute_area(
    ax1: int, ay1: int, ax2: int, ay2: int,
    bx1: int, by1: int, bx2: int, by2: int
) -> int:
    """Calculates the total area covered by two 2D axis-aligned rectangles.

    Algorithmic Requirements:
    - Time Complexity: O(1).
    - Space Complexity: O(1).

    Steps to implement:
    1. Area(A) = (ax2 - ax1) * (ay2 - ay1)
    2. Area(B) = (bx2 - bx1) * (by2 - by1)
    3. Overlap width:  w = max(0, min(ax2, bx2) - max(ax1, bx1))
    4. Overlap height: h = max(0, min(ay2, by2) - max(ay1, by1))
    5. Overlap Area = w * h
    6. Return Area(A) + Area(B) - Overlap Area

    -------------------------------------------------------------------------
    TODO: Implement inclusion-exclusion area computation.
    -------------------------------------------------------------------------
    """
    area_a = (ax2 - ax1) * (ay2 - ay1)
    area_b = (bx2 - bx1) * (by2 - by1)

    # <<< YOUR CODE HERE >>>
    # Hint: compute overlap width and height clamped to at least 0
    overlap_w = max(0, min(ax2, bx2) - max(ax1, bx1))
    overlap_h = max(0, min(ay2, by2) - max(ay1, by1))
    overlap_area = overlap_w * overlap_h

    total_union_area = TODO  # Replace with: area_a + area_b - overlap_area
    if total_union_area is None:
        raise NotImplementedError("TODO: Apply Principle of Inclusion-Exclusion.")
    return total_union_area


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (-3, 0, 3, 4, 0, -1, 9, 2, 45),
        (-2, -2, 2, 2, -2, -2, 2, 2, 16),
        (0, 0, 2, 2, 2, 2, 4, 4, 8),
    ]

    print("Running tests for lc_0223_rectangle_area_compact.py...")
    try:
        for idx, (ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, expected) in enumerate(test_cases, 1):
            res = compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
