"""LeetCode 200: Number of Islands (Reference Solution)

Problem URL: https://leetcode.com/problems/number-of-islands/
Difficulty: Medium
Category: Blob Detection & Connectivity

Computer Vision Context:
    Connected Component Labeling (CCL) with 4-connectivity:
    Discovers discrete objects by marking all connected pixels with a component ID
    or zeroing them out during a single raster scan.
"""

from __future__ import annotations
import collections
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """Counts the number of 4-connected islands in a binary grid.

    Complexity Analysis:
    - Time Complexity: O(m * n). Every pixel is inspected at most a constant number of times.
    - Space Complexity: O(min(m, n)) queue memory when using iterative BFS.
    """
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    island_count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1":
                island_count += 1
                grid[r][c] = "0"
                queue = collections.deque([(r, c)])
                while queue:
                    curr_r, curr_c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            queue.append((nr, nc))

    return island_count


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
    ]

    print("Running verification for lc_0200_number_of_islands_solution.py...")
    for idx, (g, expected) in enumerate(test_cases, 1):
        g_copy = [row[:] for row in g]
        res = num_islands(g_copy)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
