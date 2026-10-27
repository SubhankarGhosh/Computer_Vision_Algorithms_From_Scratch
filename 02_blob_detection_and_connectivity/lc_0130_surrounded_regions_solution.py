"""LeetCode 130: Surrounded Regions (Reference Solution)

Problem URL: https://leetcode.com/problems/surrounded-regions/
Difficulty: Medium
Category: Blob Detection & Connectivity

Computer Vision Context:
    Geodesic reconstruction from boundary (morphological hole filling):
    Pixels unreachable from the border via 4-connected background paths are interior holes.
"""

from __future__ import annotations
import collections
from typing import List


def solve(board: List[List[str]]) -> None:
    """Modifies the board in-place, flipping all surrounded 'O' regions to 'X'.

    Complexity Analysis:
    - Time Complexity: O(m * n). Every pixel is inspected at most twice.
    - Space Complexity: O(m + n) for boundary seed queue.
    """
    if not board or not board[0]:
        return

    m, n = len(board), len(board[0])
    queue = collections.deque()

    # Seed boundary 'O's
    for r in range(m):
        for c in (0, n - 1):
            if board[r][c] == "O":
                board[r][c] = "S"
                queue.append((r, c))

    for c in range(n):
        for r in (0, m - 1):
            if board[r][c] == "O":
                board[r][c] = "S"
                queue.append((r, c))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Flood fill safe components
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O":
                board[nr][nc] = "S"
                queue.append((nr, nc))

    # Reconstruct: flip internal 'O' to 'X', restore 'S' to 'O'
    for r in range(m):
        for c in range(n):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "S":
                board[r][c] = "O"


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
            ],
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"],
            ],
        ),
        (
            [["X"]],
            [["X"]],
        ),
    ]

    print("Running verification for lc_0130_surrounded_regions_solution.py...")
    for idx, (board, expected) in enumerate(test_cases, 1):
        board_copy = [row[:] for row in board]
        solve(board_copy)
        assert board_copy == expected, f"Case {idx} failed: got {board_copy}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
