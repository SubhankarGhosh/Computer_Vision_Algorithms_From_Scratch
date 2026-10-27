"""LeetCode 1034: Coloring A Border (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/coloring-a-border/
Difficulty: Medium
Category: Blob Detection & Connectivity

Computer Vision Context:
    Morphological Boundary Extraction (A \ (A (-) B)):
    Given a connected component of homogeneous intensity, its internal boundary
    consists of all component pixels that interface with an external label or the image frame.
    Interior pixels (those surrounded strictly by fellow component pixels) are preserved.

    Critical Implementation Trap:
    Do NOT mutate pixel colors to `color` during the traversal! Mutating a cell mid-traversal
    will cause its adjacent component neighbors to see an external color and erroneously
    classify themselves as border cells. Collect border coordinates first, then repaint.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 02_blob_detection_and_connectivity/lc_1034_coloring_a_border_compact.py
"""

from __future__ import annotations
import collections
from typing import List, Set, Tuple

# Sentinel placeholder for exercise tasks
TODO = None


def color_border(grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
    """Colors the border of the connected component containing (row, col).

    Algorithmic Requirements:
    - Time Complexity: O(m * n).
    - Space Complexity: O(m * n) to track visited coordinates and border cells.

    Steps to implement:
    1. Identify `orig_color = grid[row][col]`.
    2. If orig_color == color, return grid directly.
    3. Initialize `visited = set([(row, col)])`, `borders = []`, and `queue = collections.deque([(row, col)])`.
    4. While queue:
       - Pop (r, c).
       - Initialize `is_border = False`.
       - If r == 0 or r == m - 1 or c == 0 or c == n - 1:
         is_border = True (touching image frame)
       - For each neighbor (nr, nc) in 4 directions:
         - If 0 <= nr < m and 0 <= nc < n:
           - If grid[nr][nc] == orig_color:
             - If (nr, nc) not in visited:
               - visited.add((nr, nc))
               - queue.append((nr, nc))
           - Else (different color):
             - is_border = True
         - Else (out of bounds):
           - is_border = True
       - If is_border:
         borders.append((r, c))
    5. After traversal finishes, repaint every (r, c) in borders: `grid[r][c] = color`.
    6. Return grid.

    -------------------------------------------------------------------------
    TODO: Implement border classification without premature mutation.
    -------------------------------------------------------------------------
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

        # <<< YOUR CODE HERE >>>
        # Hint: If cell interfaces with an outside label or image frame, record it
        if is_border:
            border_cell = TODO  # Replace with: (r, c)
            if border_cell is None:
                raise NotImplementedError("TODO: Record border coordinate.")
            borders.append(border_cell)

    # Repaint only the border pixels
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

    print("Running tests for lc_1034_coloring_a_border_compact.py...")
    try:
        for idx, (g, r, c, col, expected) in enumerate(test_cases, 1):
            g_copy = [row[:] for row in g]
            res = color_border(g_copy, r, c, col)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
