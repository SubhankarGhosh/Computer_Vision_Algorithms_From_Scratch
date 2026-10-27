"""LeetCode 286: Walls and Gates (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/walls-and-gates/
Difficulty: Medium
Category: Matrix Operations & Distance

Computer Vision Context:
    Multi-Source Voronoi Distance Transform:
    Given a grid with obstacles (-1), gates (0), and empty space (INF = 2147483647),
    a simultaneous multi-source BFS from all gates partitions space into Voronoi cells,
    labeling each empty room with its exact geodesic distance to the nearest gate.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 03_matrix_operations_and_distance/lc_0286_walls_and_gates_compact.py
"""

from __future__ import annotations
import collections
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None
INF = 2147483647


def walls_and_gates(rooms: List[List[int]]) -> None:
    """Fills each empty room with the distance to its nearest gate in-place.

    Algorithmic Requirements:
    - Time Complexity: O(m * n).
    - Space Complexity: O(m * n) queue memory for multi-source BFS.

    Steps to implement:
    1. If not rooms or not rooms[0], return.
    2. Dimensions m = len(rooms), n = len(rooms[0]).
    3. Initialize `queue = collections.deque()`.
    4. Enqueue all gates (rooms[r][c] == 0) as simultaneous roots: `queue.append((r, c))`.
    5. Directions = [(-1, 0), (1, 0), (0, -1), (0, 1)].
    6. While queue:
       - Pop (r, c).
       - For each (dr, dc) in directions:
         - nr, nc = r + dr, c + dc
         - If 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == INF:
           - rooms[nr][nc] = rooms[r][c] + 1
           - queue.append((nr, nc))

    -------------------------------------------------------------------------
    TODO: Implement multi-source BFS gate propagation logic.
    -------------------------------------------------------------------------
    """
    if not rooms or not rooms[0]:
        return

    m, n = len(rooms), len(rooms[0])
    queue = collections.deque()

    # Step 1: Enqueue all gates simultaneously
    for r in range(m):
        for c in range(n):
            if rooms[r][c] == 0:
                queue.append((r, c))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Step 2: Multi-source wavefront expansion
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # <<< YOUR CODE HERE >>>
            # Hint: If neighbor is an empty room (INF), assign distance rooms[r][c] + 1 and enqueue
            if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == INF:
                gate_dist = TODO  # Replace with: rooms[r][c] + 1
                if gate_dist is None:
                    raise NotImplementedError("TODO: Update room distance to nearest gate.")
                rooms[nr][nc] = gate_dist
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

    print("Running tests for lc_0286_walls_and_gates_compact.py...")
    try:
        for idx, (grid, expected) in enumerate(test_cases, 1):
            grid_copy = [row[:] for row in grid]
            walls_and_gates(grid_copy)
            assert grid_copy == expected, f"Case {idx} failed: got {grid_copy}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
