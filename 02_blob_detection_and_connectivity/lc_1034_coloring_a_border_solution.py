"""LeetCode 1034: Coloring A Border (Reference Solution)

Problem URL: https://leetcode.com/problems/coloring-a-border/
Difficulty: Medium
Category: Blob Detection & Connectivity

Computer Vision Context:
    Contour & Internal Boundary Extraction:
    Identifies and repaints only the outer interface pixels of a connected blob,
    leaving interior pixels unchanged.
"""

from __future__ import annotations
import collections
from typing import List, Set, Tuple


def color_border(grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
    """Colors the border of the connected component containing (row, col).

    Complexity Analysis:
    - Time Complexity: O(m * n). Evaluates connected component in single BFS pass.
    - Space Complexity: O(m * n) for visited set and border list.
    """
    m, n = len(grid), len(grid[0])
    orig_color = grid[row][col]

    if orig_color == color:
        return grid

    visited: Set[Tuple[int, int]] = {(row, col)}
    borders: List[Tuple[int, int]] = []
    queue = collections.deque([(row, col)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c = queue.popleft()
        is_border = False

        if r == 0 or r == m - 1 or c == 0 or c == n - 1:
            is_border = True

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                if grid[nr][nc] == orig_color:
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                else:
                    is_border = True
            else:
                is_border = True

        if is_border:
            borders.append((r, c))

    for br, bc in borders:
        grid[br][bc] = color

    return grid


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [[1, 1], [1, 2]], 0, 0, 3,
            [[3, 3], [3, 2]],
        ),
        (
            [[1, 2, 2], [2, 3, 2]], 0, 1, 3,
            [[1, 3, 3], [2, 3, 3]],
        ),
        (
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 2,
            [[2, 2, 2], [2, 1, 2], [2, 2, 2]],
        ),
    ]

    print("Running verification for lc_1034_coloring_a_border_solution.py...")
    for idx, (g, r, c, col, expected) in enumerate(test_cases, 1):
        g_copy = [row[:] for row in g]
        res = color_border(g_copy, r, c, col)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
