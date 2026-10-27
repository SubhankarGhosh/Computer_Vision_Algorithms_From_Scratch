"""LeetCode 542: 01 Matrix (Reference Solution)

Problem URL: https://leetcode.com/problems/01-matrix/
Difficulty: Medium
Category: Matrix Operations & Distance

Computer Vision Context:
    Distance Transform (Manhattan Chamfer Map):
    Simultaneous multi-source BFS computes shortest L1 distances from boundary features.
"""

from __future__ import annotations
import collections
from typing import List


def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    """Computes the distance of each cell to the nearest 0.

    Complexity Analysis:
    - Time Complexity: O(m * n). Every cell is processed at most once.
    - Space Complexity: O(m * n) to maintain the distance matrix and queue.
    """
    m, n = len(mat), len(mat[0])
    dist = [[-1] * n for _ in range(m)]
    queue = collections.deque()

    for r in range(m):
        for c in range(n):
            if mat[r][c] == 0:
                dist[r][c] = 0
                queue.append((r, c))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
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

    print("Running verification for lc_0542_01_matrix_solution.py...")
    for idx, (mat, expected) in enumerate(test_cases, 1):
        res = update_matrix(mat)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
