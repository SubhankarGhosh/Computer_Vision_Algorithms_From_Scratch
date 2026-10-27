"""LeetCode 1254: Number of Closed Islands (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/number-of-closed-islands/
Difficulty: Medium
Category: Blob Detection & Connectivity

Computer Vision Context:
    Topological Hole Detection & Border Geodesic Pruning:
    In this problem, polarity is INVERTED compared to standard LeetCode conventions:
        0 = LAND (foreground)
        1 = WATER (background)
    A "closed island" is a connected component of 0s totally enclosed by 1s (i.e. a topological hole).
    Any 0 connected to the boundary of the image cannot be a closed island.
    Two-Stage Algorithm:
    1. Geodesic Pruning: Flood fill from all boundary 0s, flipping them to 1.
    2. Component Counting: Count remaining 0-components.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 02_blob_detection_and_connectivity/lc_1254_number_of_closed_islands_compact.py
"""

from __future__ import annotations
import collections
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def closed_island(grid: List[List[int]]) -> int:
    """Counts the number of closed islands (0s surrounded completely by 1s).

    Algorithmic Requirements:
    - Time Complexity: O(m * n).
    - Space Complexity: O(min(m, n)) queue memory for BFS.

    Steps to implement:
    1. Dimensions m = len(grid), n = len(grid[0]).
    2. Helper `sink(r, c)`:
       - grid[r][c] = 1
       - queue = collections.deque([(r, c)])
       - while queue:
         - pop (curr_r, curr_c)
         - for (dr, dc) in directions:
           - nr, nc = curr_r + dr, curr_c + dc
           - if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
             - grid[nr][nc] = 1
             - queue.append((nr, nc))
    3. Stage 1: Sink boundary-connected 0s:
       - For r in 0..m-1: sink(r, 0) if grid[r][0] == 0; sink(r, n-1) if grid[r][n-1] == 0
       - For c in 0..n-1: sink(0, c) if grid[0][c] == 0; sink(m-1, c) if grid[m-1][c] == 0
    4. Stage 2: Count internal closed islands:
       - closed_count = 0
       - For r in 1..m-2 and c in 1..n-2:
         - If grid[r][c] == 0:
           - closed_count += 1
           - sink(r, c)
    5. Return `closed_count`.

    -------------------------------------------------------------------------
    TODO: Implement boundary pruning and internal closed island counting.
    -------------------------------------------------------------------------
    """
    m, n = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def sink(start_r: int, start_c: int) -> None:
        grid[start_r][start_c] = 1
        queue = collections.deque([(start_r, start_c)])
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc))

    # Stage 1: Eliminate boundary-connected land
    for r in range(m):
        for c in (0, n - 1):
            if grid[r][c] == 0:
                sink(r, c)

    for c in range(n):
        for r in (0, m - 1):
            if grid[r][c] == 0:
                sink(r, c)

    # Stage 2: Count surviving closed islands
    closed_count = 0
    for r in range(1, m - 1):
        for c in range(1, n - 1):
            if grid[r][c] == 0:
                # <<< YOUR CODE HERE >>>
                # Hint: increment closed_count and sink the entire closed island
                sink_called = False
                sink(r, c)
                sink_called = True

                increment_val = TODO  # Replace with: 1
                if increment_val is None:
                    raise NotImplementedError("TODO: Increment closed island count.")
                closed_count += increment_val

    return closed_count


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [
                [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0],
            ],
            2,
        ),
        (
            [
                [0, 0, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0],
            ],
            1,
        ),
        (
            [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            1,
        ),
    ]

    print("Running tests for lc_1254_number_of_closed_islands_compact.py...")
    try:
        for idx, (g, expected) in enumerate(test_cases, 1):
            g_copy = [row[:] for row in g]
            res = closed_island(g_copy)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
