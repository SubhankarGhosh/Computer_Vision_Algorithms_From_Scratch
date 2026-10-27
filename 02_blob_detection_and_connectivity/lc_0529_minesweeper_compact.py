"""LeetCode 529: Minesweeper (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/minesweeper/
Difficulty: Medium
Category: Blob Detection & Connectivity

Computer Vision Context:
    8-Neighborhood Wavefront Expansion & Feature Counting:
    Applies an 8-connected structuring element to compute local mine counts.
    If a cell has 0 neighboring mines, a recursive/iterative wavefront reveals
    all unrevealed 8-neighbors (topological connected region unmasking).

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 02_blob_detection_and_connectivity/lc_0529_minesweeper_compact.py
"""

from __future__ import annotations
import collections
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def update_board(board: List[List[str]], click: List[int]) -> List[List[str]]:
    """Updates the Minesweeper board according to the clicked position.

    Algorithmic Requirements:
    - Time Complexity: O(m * n). Evaluates each revealed cell at most once.
    - Space Complexity: O(m * n) queue memory for blank region expansion.

    Steps to implement:
    1. Unpack click: click_r, click_c = click[0], click[1].
    2. If board[click_r][click_c] == 'M':
       - Hit mine! board[click_r][click_c] = 'X'
       - Return board immediately.
    3. If board[click_r][click_c] == 'E':
       - Launch iterative BFS with queue = collections.deque([(click_r, click_c)])
       - Define 8-directional neighbor offsets.
       - While queue:
         - Pop (r, c).
         - Count adjacent mines ('M') in all 8 directions.
         - If mine_count > 0:
           - board[r][c] = str(mine_count)
         - Else (mine_count == 0):
           - board[r][c] = 'B'
           - For each 8-neighbor (nr, nc):
             - If within bounds and board[nr][nc] == 'E':
               - Mark board[nr][nc] = 'B' (to avoid duplicate queuing!)
               - queue.append((nr, nc))
    4. Return board.

    -------------------------------------------------------------------------
    TODO: Implement 8-neighbor mine count and blank wavefront expansion.
    -------------------------------------------------------------------------
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

        # Count 8-neighborhood mines
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
                    # <<< YOUR CODE HERE >>>
                    # Hint: Pre-mark cell as 'B' and append to queue
                    mark_blank = TODO  # Replace with: "B"
                    if mark_blank is None:
                        raise NotImplementedError("TODO: Mark blank cell and enqueue.")
                    board[nr][nc] = mark_blank
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

    print("Running tests for lc_0529_minesweeper_compact.py...")
    try:
        for idx, (b, clk, expected) in enumerate(test_cases, 1):
            b_copy = [row[:] for row in b]
            res = update_board(b_copy, clk)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
