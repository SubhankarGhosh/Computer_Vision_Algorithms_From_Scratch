"""LeetCode 850: Rectangle Area II (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/rectangle-area-ii/
Difficulty: Hard
Category: Geometry & Rectangles

Computer Vision Context:
    Multi-Box Union Area & Non-Maximum Suppression (NMS) Coverage:
    In object detection, evaluating the collective spatial coverage of multiple overlapping
    bounding boxes cannot be solved via simple pair-wise IoU due to higher-order overlaps.
    Using a 2D Sweep-Line with 1D Coordinate Compression:
    1. Generate OPEN (x1, +1, y1, y2) and CLOSE (x2, -1, y1, y2) events along the x-axis.
    2. Collect and sort all unique y-coordinates into discrete vertical segments [Y[i], Y[i+1]].
    3. Sweep from left to right: for each horizontal delta (curr_x - prev_x), compute the total
       active vertical length currently covered by at least one rectangle.
    4. Accumulate area modulo 10^9 + 7.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 04_geometry_and_rectangles/lc_0850_rectangle_area_ii_compact.py
"""

from __future__ import annotations
from typing import List, Tuple

# Sentinel placeholder for exercise tasks
TODO = None
MOD = 10**9 + 7


def rectangle_area(rectangles: List[List[int]]) -> int:
    """Calculates the total union area of overlapping rectangles modulo 10^9 + 7 using 2D sweep-line.

    Algorithmic Requirements:
    - Time Complexity: O(N^2) with 1D coordinate compression (where N is number of rectangles <= 200).
    - Space Complexity: O(N) to store events and discrete y-interval coverage counts.

    Steps to implement:
    1. Collect all unique y-coordinates: `y_set = set()` for y1, y2 in rectangles.
       Sort them: `Y = sorted(y_set)`.
       Map each y to its index: `y_idx = {y: i for i, y in enumerate(Y)}`.
    2. Build sweep-line events:
       - for each [x1, y1, x2, y2]:
         - events.append((x1, 1, y1, y2))   # Open rectangle
         - events.append((x2, -1, y1, y2))  # Close rectangle
       - Sort events by x coordinate.
    3. Initialize `count = [0] * (len(Y) - 1)`, `total_area = 0`, `cur_x = events[0][0]`.
    4. For each event (x, typ, y1, y2):
       - If x > cur_x:
         - Calculate active vertical length: `cur_y = sum(Y[i+1] - Y[i] for i, c in enumerate(count) if c > 0)`.
         - total_area = (total_area + (x - cur_x) * cur_y) % MOD
         - cur_x = x
       - Update segment counts:
         - for i from y_idx[y1] to y_idx[y2] - 1:
           - count[i] += typ
    5. Return total_area.

    -------------------------------------------------------------------------
    TODO: Implement sweep-line event processing and vertical strip summation.
    -------------------------------------------------------------------------
    """
    y_set = set()
    events: List[Tuple[int, int, int, int]] = []

    for x1, y1, x2, y2 in rectangles:
        events.append((x1, 1, y1, y2))
        events.append((x2, -1, y1, y2))
        y_set.add(y1)
        y_set.add(y2)

    events.sort(key=lambda e: e[0])
    Y = sorted(y_set)
    y_idx = {y: i for i, y in enumerate(Y)}

    count = [0] * (len(Y) - 1)
    total_area = 0
    cur_x = events[0][0]

    for x, typ, y1, y2 in events:
        if x > cur_x:
            # <<< YOUR CODE HERE >>>
            # Hint: Compute total active vertical length where count[i] > 0
            cur_y = sum(Y[i + 1] - Y[i] for i, c in enumerate(count) if c > 0)
            strip_area = (x - cur_x) * cur_y

            updated_area = TODO  # Replace with: (total_area + strip_area) % MOD
            if updated_area is None:
                raise NotImplementedError("TODO: Accumulate strip area into total_area modulo 10^9 + 7.")
            total_area = updated_area
            cur_x = x

        # Update active intervals for this rectangle
        for i in range(y_idx[y1], y_idx[y2]):
            count[i] += typ

    return total_area


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]], 6),
        ([[0, 0, 1000000000, 1000000000]], 49),  # 10^18 % (10^9 + 7) = 49
        ([[0, 0, 1, 1], [0, 0, 1, 1]], 1),
    ]

    print("Running tests for lc_0850_rectangle_area_ii_compact.py...")
    try:
        for idx, (rects, expected) in enumerate(test_cases, 1):
            res = rectangle_area(rects)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
