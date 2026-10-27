"""LeetCode 286: Walls and Gates (Reference Solution)

Problem URL: https://leetcode.com/problems/walls-and-gates/
Difficulty: Medium
Category: Matrix Operations & Distance

Computer Vision Context:
    Multi-Source Voronoi Distance Transform:
    Enqueues all gates (0) initially; updates empty rooms (INF) with shortest geodesic distance.
"""

from __future__ import annotations
import collections
from typing import List

INF = 2147483647


def walls_and_gates(rooms: List[List[int]]) -> None:
    """Fills each empty room with the distance to its nearest gate in-place.

    Complexity Analysis:
    - Time Complexity: O(m * n). Every room is updated and visited at most once.
    - Space Complexity: O(m * n) queue memory for multi-source BFS.
    """
    if not rooms or not rooms[0]:
        return

    m, n = len(rooms), len(rooms[0])
    queue = collections.deque()

    for r in range(m):
        for c in range(n):
            if rooms[r][c] == 0:
                queue.append((r, c))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == INF:
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [
                [INF, -1, 0, INF],
                [INF, INF, INF, -1],
                [INF, -1, INF, -1],
                [0, -1, INF, INF],
            ],
            [
                [3, -1, 0, 1],
                [2, 2, 1, -1],
                [1, -1, 2, -1],
                [0, -1, 3, 4],
            ],
        ),
        (
            [[-1]],
            [[-1]],
        ),
    ]

    print("Running verification for lc_0286_walls_and_gates_solution.py...")
    for idx, (grid, expected) in enumerate(test_cases, 1):
        grid_copy = [row[:] for row in grid]
        walls_and_gates(grid_copy)
        assert grid_copy == expected, f"Case {idx} failed: got {grid_copy}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
