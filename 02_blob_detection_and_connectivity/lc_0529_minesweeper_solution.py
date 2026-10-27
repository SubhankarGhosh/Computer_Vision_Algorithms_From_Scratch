"""LeetCode 529: Minesweeper (Reference Solution)

Problem URL: https://leetcode.com/problems/minesweeper/
Difficulty: Medium
Category: Blob Detection & Connectivity

Computer Vision Context:
    8-neighborhood convolution-style counting and wavefront component expansion.
"""

from __future__ import annotations
import collections
from typing import List


def update_board(board: List[List[str]], click: List[int]) -> List[List[str]]:
    """Updates the Minesweeper board according to the clicked position.

    Complexity Analysis:
    - Time Complexity: O(m * n). Each cell is revealed at most once with 8 constant checks.
    - Space Complexity: O(m * n) queue space for BFS.
    """
    m, n = len(board), len(board[0])
    cr, cc = click[0], click[1]

    if board[cr][cc] == "M":
        board[cr][cc] = "X"
        return board

    if board[cr][cc] != "E":
        return board

    directions_8 = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    queue = collections.deque([(cr, cc)])

    while queue:
        r, c = queue.popleft()
        mine_count = 0

        for dr, dc in directions_8:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "M":
                mine_count += 1

        if mine_count > 0:
            board[r][c] = str(mine_count)
        else:
            board[r][c] = "B"
            for dr, dc in directions_8:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "E":
                    board[nr][nc] = "B"
                    queue.append((nr, nc))

    return board


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [
                ["E", "E", "E", "E", "E"],
                ["E", "E", "M", "E", "E"],
                ["E", "E", "E", "E", "E"],
                ["E", "E", "E", "E", "E"],
            ],
            [3, 0],
            [
                ["B", "1", "E", "1", "B"],
                ["B", "1", "M", "1", "B"],
                ["B", "1", "1", "1", "B"],
                ["B", "B", "B", "B", "B"],
            ],
        ),
        (
            [
                ["B", "1", "E", "1", "B"],
                ["B", "1", "M", "1", "B"],
                ["B", "1", "1", "1", "B"],
                ["B", "B", "B", "B", "B"],
            ],
            [1, 2],
            [
                ["B", "1", "E", "1", "B"],
                ["B", "1", "X", "1", "B"],
                ["B", "1", "1", "1", "B"],
                ["B", "B", "B", "B", "B"],
            ],
        ),
    ]

    print("Running verification for lc_0529_minesweeper_solution.py...")
    for idx, (b, clk, expected) in enumerate(test_cases, 1):
        b_copy = [row[:] for row in b]
        res = update_board(b_copy, clk)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
