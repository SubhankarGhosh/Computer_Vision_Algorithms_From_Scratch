"""LeetCode 1254: Number of Closed Islands (Reference Solution)

Problem URL: https://leetcode.com/problems/number-of-closed-islands/
Difficulty: Medium
Category: Blob Detection & Connectivity

Computer Vision Context:
    Topological hole detection via border geodesic sinking:
    Prunes non-closed boundary components, then counts closed interior cavities.
"""

from __future__ import annotations
import collections
from typing import List


def closed_island(grid: List[List[int]]) -> int:
    """Counts the number of closed islands (0s surrounded completely by 1s).

    Complexity Analysis:
    - Time Complexity: O(m * n). Each cell is traversed and converted at most once.
    - Space Complexity: O(min(m, n)) queue memory with iterative BFS.
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

    # Stage 1: Sink boundary-connected 0s
    for r in range(m):
        for c in (0, n - 1):
            if grid[r][c] == 0:
                sink(r, c)

    for c in range(n):
        for r in (0, m - 1):
            if grid[r][c] == 0:
                sink(r, c)

    # Stage 2: Count internal closed islands
    closed_count = 0
    for r in range(1, m - 1):
        for c in range(1, n - 1):
            if grid[r][c] == 0:
                closed_count += 1
                sink(r, c)

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

    print("Running verification for lc_1254_number_of_closed_islands_solution.py...")
    for idx, (g, expected) in enumerate(test_cases, 1):
        g_copy = [row[:] for row in g]
        res = closed_island(g_copy)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
