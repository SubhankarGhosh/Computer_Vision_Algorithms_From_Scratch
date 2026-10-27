"""LeetCode 1368: Minimum Cost to Make at Least One Valid Path in a Grid (Reference Solution)

Problem URL: https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
Difficulty: Hard
Category: Matrix Operations & Distance

Computer Vision Context:
    Shortest Path on Directed Vector Fields (0-1 BFS):
    Operates in O(m * n) time using double-ended queue ordering.
"""

from __future__ import annotations
import collections
from typing import List


def min_cost(grid: List[List[int]]) -> int:
    """Computes the minimum cost to reach (m-1, n-1) using 0-1 BFS.

    Complexity Analysis:
    - Time Complexity: O(m * n). Every cell is expanded at most once at its minimal cost.
    - Space Complexity: O(m * n) for dist matrix and deque.
    """
    m, n = len(grid), len(grid[0])
    dist = [[float("inf")] * n for _ in range(m)]
    dist[0][0] = 0

    deque = collections.deque([(0, 0)])
    # 1: right, 2: left, 3: down, 4: up
    dir_map = {
        1: (0, 1),
        2: (0, -1),
        3: (1, 0),
        4: (-1, 0),
    }

    while deque:
        r, c = deque.popleft()

        if r == m - 1 and c == n - 1:
            return int(dist[r][c])

        for dir_idx, (dr, dc) in dir_map.items():
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                weight = 0 if grid[r][c] == dir_idx else 1
                if dist[r][c] + weight < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + weight
                    if weight == 0:
                        deque.appendleft((nr, nc))
                    else:
                        deque.append((nr, nc))

    return int(dist[m - 1][n - 1])


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]],
            3,
        ),
        (
            [[1, 1, 3], [3, 2, 2], [1, 1, 4]],
            0,
        ),
        (
            [[1, 2], [4, 3]],
            1,
        ),
    ]

    print("Running verification for lc_1368_minimum_cost_to_make_at_least_one_valid_path_in_a_grid_solution.py...")
    for idx, (grid, expected) in enumerate(test_cases, 1):
        res = min_cost(grid)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
