"""LeetCode 850: Rectangle Area II (Reference Solution)

Problem URL: https://leetcode.com/problems/rectangle-area-ii/
Difficulty: Hard
Category: Geometry & Rectangles

Computer Vision Context:
    Multi-Box Union Area Coverage via 2D Sweep-Line & 1D Coordinate Compression:
    Computes total continuous pixel area covered by N overlapping bounding boxes modulo 10^9 + 7.
"""

from __future__ import annotations
from typing import List, Tuple

MOD = 10**9 + 7


def rectangle_area(rectangles: List[List[int]]) -> int:
    """Calculates the total union area of overlapping rectangles modulo 10^9 + 7 using 2D sweep-line.

    Complexity Analysis:
    - Time Complexity: O(N^2) where N is the number of rectangles (N <= 200).
      Sorting 2N events takes O(N log N).
      Each event updates at most 2N intervals in O(N).
      Overall 2N * O(N) = O(N^2) operations.
    - Space Complexity: O(N) to store events and discrete y-interval coverage counts.
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
            cur_y = sum(Y[i + 1] - Y[i] for i, c in enumerate(count) if c > 0)
            total_area = (total_area + (x - cur_x) * cur_y) % MOD
            cur_x = x

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

    print("Running verification for lc_0850_rectangle_area_ii_solution.py...")
    for idx, (rects, expected) in enumerate(test_cases, 1):
        res = rectangle_area(rects)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
