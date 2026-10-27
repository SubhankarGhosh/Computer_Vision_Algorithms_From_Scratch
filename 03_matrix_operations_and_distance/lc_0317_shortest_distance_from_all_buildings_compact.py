"""LeetCode 317: Shortest Distance from All Buildings (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/shortest-distance-from-all-buildings/
Difficulty: Hard
Category: Matrix Operations & Distance

Computer Vision Context:
    Geometric Median & Multi-Source Distance Surface Optimization:
    Given an m x n grid with buildings (1), obstacles (2), and empty land (0),
    we seek an empty land cell that minimizes the sum of Manhattan travel distances
    to all buildings:
        p* = argmin_{p in Empty} sum_{k=1}^B d_{L1}(p, Building_k)
    This solves optimal facility location under discrete grid constraints.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 03_matrix_operations_and_distance/lc_0317_shortest_distance_from_all_buildings_compact.py
"""

from __future__ import annotations
import collections
from typing import List, Set, Tuple

# Sentinel placeholder for exercise tasks
TODO = None


def shortest_distance(grid: List[List[int]]) -> int:
    """Finds the empty land that has the minimum total travel distance to all buildings.

    Algorithmic Requirements:
    - Time Complexity: O(B * m * n) where B is the number of buildings.
    - Space Complexity: O(m * n) to accumulate total distances and reachability counts.

    Steps to implement:
    1. Dimensions m = len(grid), n = len(grid[0]).
    2. Identify all buildings: `buildings = [(r, c) for r in range(m) for c in range(n) if grid[r][c] == 1]`.
    3. If no buildings exist, return -1.
    4. Initialize `total_dist = [[0] * n for _ in range(m)]` and `reach_count = [[0] * n for _ in range(m)]`.
    5. Directions = [(-1, 0), (1, 0), (0, -1), (0, 1)].
    6. For each building (br, bc):
       - BFS queue: `queue = collections.deque([(br, bc, 0)])`
       - `visited: Set[Tuple[int, int]] = {(br, bc)}`
       - While queue:
         - pop (r, c, d)
         - for (dr, dc) in directions:
           - nr, nc = r + dr, c + dc
           - if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
             - if grid[nr][nc] == 0:  # Can only walk on empty land
               - visited.add((nr, nc))
               - total_dist[nr][nc] += d + 1
               - reach_count[nr][nc] += 1
               - queue.append((nr, nc, d + 1))
    7. Find minimum total_dist across all empty cells where reach_count == len(buildings).
    8. Return min_dist or -1 if unreachable.

    -------------------------------------------------------------------------
    TODO: Implement multi-source distance aggregation logic.
    -------------------------------------------------------------------------
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
                        # <<< YOUR CODE HERE >>>
                        # Hint: Increment total_dist by d + 1, reach_count by 1, and append to queue
                        add_step = TODO  # Replace with: d + 1
                        if add_step is None:
                            raise NotImplementedError("TODO: Accumulate travel distance for empty land cell.")
                        total_dist[nr][nc] += add_step
                        reach_count[nr][nc] += 1
                        queue.append((nr, nc, add_step))

    # Identify optimal empty cell reachable by all buildings
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

    print("Running tests for lc_0317_shortest_distance_from_all_buildings_compact.py...")
    try:
        for idx, (grid, expected) in enumerate(test_cases, 1):
            res = shortest_distance(grid)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
