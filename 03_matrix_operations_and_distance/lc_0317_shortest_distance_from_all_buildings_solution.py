"""LeetCode 317: Shortest Distance from All Buildings (Reference Solution)

Problem URL: https://leetcode.com/problems/shortest-distance-from-all-buildings/
Difficulty: Hard
Category: Matrix Operations & Distance

Computer Vision Context:
    Geometric Median & Multi-Source Distance Surface Optimization:
    Aggregates L1 distance fields across all buildings to find the global minimum centroid.
"""

from __future__ import annotations
import collections
from typing import List, Set, Tuple


def shortest_distance(grid: List[List[int]]) -> int:
    """Finds the empty land that has the minimum total travel distance to all buildings.

    Complexity Analysis:
    - Time Complexity: O(B * m * n) where B is the number of buildings.
      In the worst case where B ~ m*n, this is O((mn)^2).
    - Space Complexity: O(m * n) to accumulate total distances and reachability counts.
    """
    m, n = len(grid), len(grid[0])
    buildings = [(r, c) for r in range(m) for c in range(n) if grid[r][c] == 1]
    num_buildings = len(buildings)

    if num_buildings == 0:
        return -1

    total_dist = [[0] * n for _ in range(m)]
    reach_count = [[0] * n for _ in range(m)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for br, bc in buildings:
        queue = collections.deque([(br, bc, 0)])
        visited: Set[Tuple[int, int]] = {(br, bc)}

        while queue:
            r, c, d = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    if grid[nr][nc] == 0:
                        visited.add((nr, nc))
                        total_dist[nr][nc] += d + 1
                        reach_count[nr][nc] += 1
                        queue.append((nr, nc, d + 1))

    min_dist = float("inf")
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 0 and reach_count[r][c] == num_buildings:
                min_dist = min(min_dist, total_dist[r][c])

    return min_dist if min_dist != float("inf") else -1


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]],
            7,
        ),
        (
            [[1, 0]],
            1,
        ),
        (
            [[1]],
            -1,
        ),
    ]

    print("Running verification for lc_0317_shortest_distance_from_all_buildings_solution.py...")
    for idx, (grid, expected) in enumerate(test_cases, 1):
        res = shortest_distance(grid)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
