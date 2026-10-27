"""LeetCode 695: Max Area of Island (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/max-area-of-island/
Difficulty: Medium
Category: Blob Detection & Connectivity

Computer Vision Context:
    Zeroth-Order Spatial Moment / Component Area:
    In object analysis, the area of a binary blob C is its zeroth-order moment:
        M_00 = sum_{(r, c) in C} 1
    This metric is used to filter out noise particles (small dust) or isolate
    the dominant foreground region.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 02_blob_detection_and_connectivity/lc_0695_max_area_of_island_compact.py
"""

from __future__ import annotations
import collections
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def max_area_of_island(grid: List[List[int]]) -> int:
    """Finds the maximum area (number of 4-connected cells) of an island in a binary grid.

    Algorithmic Requirements:
    - Time Complexity: O(m * n).
    - Space Complexity: O(min(m, n)) queue space with iterative BFS.

    Steps to implement:
    1. Dimensions m = len(grid), n = len(grid[0]).
    2. Initialize `max_area = 0`.
    3. Iterate each cell (r, c):
       - If grid[r][c] == 1:
         - Initialize `area = 0`
         - Set grid[r][c] = 0 (mark visited)
         - queue = collections.deque([(r, c)])
         - While queue:
           - pop (curr_r, curr_c), increment area += 1
           - for each neighbor (nr, nc) in 4 directions:
             - if 0 <= nr < m, 0 <= nc < n and grid[nr][nc] == 1:
               - mark grid[nr][nc] = 0
               - append (nr, nc)
         - max_area = max(max_area, area)
    4. Return `max_area`.

    -------------------------------------------------------------------------
    TODO: Implement component area calculation using iterative BFS.
    -------------------------------------------------------------------------
    """
    m, n = len(grid), len(grid[0])
    max_area = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                # <<< YOUR CODE HERE >>>
                # Hint: launch BFS, accumulate area, update max_area
                area = 0
                grid[r][c] = 0
                queue = collections.deque([(r, c)])

                while queue:
                    curr_r, curr_c = queue.popleft()
                    area += 1
                    for dr, dc in directions:
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            queue.append((nr, nc))

                updated_max = TODO  # Replace with: max(max_area, area)
                if updated_max is None:
                    raise NotImplementedError("TODO: Update max_area with the current component area.")
                max_area = updated_max

    return max_area


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            ],
            6,
        ),
        (
            [[0, 0, 0, 0, 0, 0, 0, 0]],
            0,
        ),
        (
            [[1]],
            1,
        ),
    ]

    print("Running tests for lc_0695_max_area_of_island_compact.py...")
    try:
        for idx, (g, expected) in enumerate(test_cases, 1):
            g_copy = [row[:] for row in g]
            res = max_area_of_island(g_copy)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
