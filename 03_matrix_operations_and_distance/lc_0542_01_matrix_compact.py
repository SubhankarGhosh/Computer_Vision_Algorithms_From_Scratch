"""LeetCode 542: 01 Matrix (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/01-matrix/
Difficulty: Medium
Category: Matrix Operations & Distance

Computer Vision Context:
    Distance Transform (Manhattan Distance Map):
    Computes the minimum distance from every pixel to the nearest obstacle (0).
    Multi-source BFS expands from all 0s simultaneously, creating a chamfer distance field
    used for robotic path planning, obstacle avoidance, and shape skeletonization.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 03_matrix_operations_and_distance/lc_0542_01_matrix_compact.py
"""

from __future__ import annotations
import collections
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    """Computes the distance of each cell to the nearest 0.

    Algorithmic Requirements:
    - Time Complexity: O(m * n). Multi-source BFS visits each cell once.
    - Space Complexity: O(m * n) to maintain distance matrix and queue.

    Steps to implement (Multi-Source BFS):
    1. Initialize m = len(mat), n = len(mat[0]).
    2. Create `dist` matrix initialized to -1 for all cells.
    3. Initialize a queue: `queue = collections.deque()`.
    4. Traverse `mat`: for all cells with value 0, set `dist[r][c] = 0` and `queue.append((r, c))`.
    5. While queue:
       - Pop (r, c).
       - For each neighbor (nr, nc) in 4 directions:
         - If 0 <= nr < m and 0 <= nc < n and dist[nr][nc] == -1:
           - dist[nr][nc] = dist[r][c] + 1
           - queue.append((nr, nc))
    6. Return `dist`.

    -------------------------------------------------------------------------
    TODO: Implement multi-source BFS distance propagation below.
    -------------------------------------------------------------------------
    """
    m, n = len(mat), len(mat[0])
    dist = [[-1] * n for _ in range(m)]
    queue = collections.deque()

    # Step 1: Enqueue all 0s as multi-source roots
    for r in range(m):
        for c in range(n):
            if mat[r][c] == 0:
                dist[r][c] = 0
                queue.append((r, c))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Step 2: Propagate distance wavefront
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # <<< YOUR CODE HERE >>>
            # Hint: If neighbor is inside grid and unvisited (dist[nr][nc] == -1),
            # set dist[nr][nc] = dist[r][c] + 1 and enqueue
            if 0 <= nr < m and 0 <= nc < n and dist[nr][nc] == -1:
                next_dist = TODO  # Replace with: dist[r][c] + 1
                if next_dist is None:
                    raise NotImplementedError("TODO: Update neighbor distance and enqueue.")
                dist[nr][nc] = next_dist
                queue.append((nr, nc))

    return dist


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        ),
        (
            [[0, 0, 0], [0, 1, 0], [1, 1, 1]],
            [[0, 0, 0], [0, 1, 0], [1, 2, 1]],
        ),
    ]

    print("Running tests for lc_0542_01_matrix_compact.py...")
    try:
        for idx, (mat, expected) in enumerate(test_cases, 1):
            res = update_matrix(mat)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
