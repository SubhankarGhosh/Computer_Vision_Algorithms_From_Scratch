"""LeetCode 695: Max Area of Island (Reference Solution)

Problem URL: https://leetcode.com/problems/max-area-of-island/
Difficulty: Medium
Category: Blob Detection & Connectivity

Computer Vision Context:
    Zeroth-order moment calculation:
    Evaluates area = sum(1) for each connected component to find the maximum blob size.
"""

from __future__ import annotations
import collections
from typing import List


def max_area_of_island(grid: List[List[int]]) -> int:
    """Finds the maximum area of an island in a binary grid.

    Complexity Analysis:
    - Time Complexity: O(m * n). Every pixel is visited at most once.
    - Space Complexity: O(min(m, n)) queue memory with iterative BFS.
    """
    m, n = len(grid), len(grid[0])
    max_area = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
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
                max_area = max(max_area, area)

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

    print("Running verification for lc_0695_max_area_of_island_solution.py...")
    for idx, (g, expected) in enumerate(test_cases, 1):
        g_copy = [row[:] for row in g]
        res = max_area_of_island(g_copy)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
