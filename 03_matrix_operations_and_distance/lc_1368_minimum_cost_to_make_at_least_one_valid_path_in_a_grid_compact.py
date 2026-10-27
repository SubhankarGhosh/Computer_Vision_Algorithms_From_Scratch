"""LeetCode 1368: Minimum Cost to Make at Least One Valid Path in a Grid (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
Difficulty: Hard
Category: Matrix Operations & Distance

Computer Vision Context:
    Shortest Path on Directed Vector Fields (0-1 BFS):
    Given a grid where each cell points in one of 4 directions (1: right, 2: left, 3: down, 4: up),
    we seek the minimum cost to reach (m - 1, n - 1) from (0, 0).
    Following the directed sign has cost 0; modifying the vector direction costs 1.
    Because edge weights are strictly {0, 1}, we use 0-1 BFS (double-ended queue):
        - 0-weight edges: deque.appendleft()
        - 1-weight edges: deque.append()
    This guarantees strictly linear O(m * n) shortest path traversal without heap sorting!

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 03_matrix_operations_and_distance/lc_1368_minimum_cost_to_make_at_least_one_valid_path_in_a_grid_compact.py
"""

from __future__ import annotations
import collections
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def min_cost(grid: List[List[int]]) -> int:
    """Computes the minimum cost to reach (m-1, n-1) using 0-1 BFS.

    Algorithmic Requirements:
    - Time Complexity: O(m * n). Exactly linear in number of cells.
    - Space Complexity: O(m * n) to maintain distance matrix and deque.

    Directions mapping (1-indexed matching problem rules):
        1 -> Right (0, 1)
        2 -> Left  (0, -1)
        3 -> Down  (1, 0)
        4 -> Up    (-1, 0)

    Steps to implement:
    1. Dimensions m = len(grid), n = len(grid[0]).
    2. Initialize `dist = [[float('inf')] * n for _ in range(m)]`.
    3. `dist[0][0] = 0`.
    4. `deque = collections.deque([(0, 0)])`.
    5. While deque:
       - Pop (r, c) from left.
       - If r == m - 1 and c == n - 1: return dist[r][c].
       - For direction index (1: Right, 2: Left, 3: Down, 4: Up):
         - nr, nc = r + dr, c + dc
         - weight = 0 if grid[r][c] == dir_idx else 1
         - if 0 <= nr < m and 0 <= nc < n and dist[r][c] + weight < dist[nr][nc]:
           - dist[nr][nc] = dist[r][c] + weight
           - if weight == 0: deque.appendleft((nr, nc))
           - else: deque.append((nr, nc))
    6. Return dist[m - 1][n - 1].

    -------------------------------------------------------------------------
    TODO: Implement 0-1 BFS queue ordering.
    -------------------------------------------------------------------------
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
                    # <<< YOUR CODE HERE >>>
                    # Hint: If weight == 0, appendleft; else append
                    if weight == 0:
                        pushed = TODO  # Replace with: deque.appendleft((nr, nc))
                        if pushed is None:
                            raise NotImplementedError("TODO: Push 0-cost transitions to front of deque.")
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

    print("Running tests for lc_1368_minimum_cost_to_make_at_least_one_valid_path_in_a_grid_compact.py...")
    try:
        for idx, (grid, expected) in enumerate(test_cases, 1):
            res = min_cost(grid)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
