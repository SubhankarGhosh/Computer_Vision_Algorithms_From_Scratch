"""LeetCode 1905: Count Sub Islands (Reference Solution)

Problem URL: https://leetcode.com/problems/count-sub-islands/
Difficulty: Medium
Category: Blob Detection & Connectivity

Computer Vision Context:
    Binary Mask Containment / Structural Subset Testing:
    Evaluates whether each connected component in candidate mask M2 is fully
    enclosed within target mask M1.
"""

from __future__ import annotations
import collections
from typing import List


def count_sub_islands(grid1: List[List[int]], grid2: List[List[int]]) -> int:
    """Counts how many islands in grid2 are completely contained within islands of grid1.

    Complexity Analysis:
    - Time Complexity: O(m * n). Every cell in grid2 is visited once in the BFS exploration.
    - Space Complexity: O(min(m, n)) queue memory with iterative BFS.
    """
    m, n = len(grid1), len(grid1[0])
    sub_island_count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(m):
        for c in range(n):
            if grid2[r][c] == 1:
                is_sub = True
                grid2[r][c] = 0
                queue = collections.deque([(r, c)])

                while queue:
                    curr_r, curr_c = queue.popleft()
                    if grid1[curr_r][curr_c] == 0:
                        is_sub = False

                    for dr, dc in directions:
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < m and 0 <= nc < n and grid2[nr][nc] == 1:
                            grid2[nr][nc] = 0
                            queue.append((nr, nc))

                if is_sub:
                    sub_island_count += 1

    return sub_island_count


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [
                [1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 1, 1],
            ],
            [
                [1, 1, 1, 0, 0],
                [0, 0, 1, 1, 1],
                [0, 1, 0, 0, 0],
                [1, 0, 1, 1, 0],
                [0, 1, 0, 1, 0],
            ],
            3,
        ),
        (
            [
                [1, 0, 1, 0, 1],
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [1, 0, 1, 0, 1],
            ],
            [
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [1, 0, 0, 0, 1],
            ],
            2,
        ),
    ]

    print("Running verification for lc_1905_count_sub_islands_solution.py...")
    for idx, (g1, g2, expected) in enumerate(test_cases, 1):
        g1_copy = [row[:] for row in g1]
        g2_copy = [row[:] for row in g2]
        res = count_sub_islands(g1_copy, g2_copy)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
