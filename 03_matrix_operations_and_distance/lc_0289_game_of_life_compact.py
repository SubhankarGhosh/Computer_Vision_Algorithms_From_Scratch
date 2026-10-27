"""LeetCode 289: Game of Life (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/game-of-life/
Difficulty: Medium
Category: Matrix Operations & Distance

Computer Vision Context:
    Cellular Automata & In-Place State Bit-Packing:
    Simulates Conway's Game of Life on an m x n board using an 8-neighborhood kernel.
    To avoid allocating an O(m * n) auxiliary buffer, we encode two states into each cell:
        - Bit 0: Current State (0 = dead, 1 = alive)
        - Bit 1: Next State (0 = dead, 1 = alive)
    Neighbor sums inspect `cell & 1`. Next state is written via `cell |= (next_state << 1)`.
    A final pass shifts all cells right (`cell >>= 1`), achieving O(1) auxiliary memory.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 03_matrix_operations_and_distance/lc_0289_game_of_life_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def game_of_life(board: List[List[int]]) -> None:
    """Updates the board to its next state in-place.

    Algorithmic Requirements:
    - Time Complexity: O(m * n). Evaluates 8 neighbors per cell.
    - Space Complexity: O(1) auxiliary space (strict in-place bit manipulation).

    Rules:
    1. Any live cell with < 2 live neighbors dies (underpopulation).
    2. Any live cell with 2 or 3 live neighbors lives.
    3. Any live cell with > 3 live neighbors dies (overpopulation).
    4. Any dead cell with exactly 3 live neighbors becomes alive (reproduction).

    Steps to implement:
    1. Iterate each cell (r, c) in board:
       - Count live neighbors using 8 offsets: `sum(board[nr][nc] & 1)`.
       - Determine if next state is alive (1):
         - If currently alive (board[r][c] & 1 == 1): lives if neighbors in (2, 3).
         - If currently dead (board[r][c] & 1 == 0): lives if neighbors == 3.
       - If next state is 1, set bit 1: `board[r][c] |= 2`.
    2. Iterate each cell and shift state right: `board[r][c] >>= 1`.

    -------------------------------------------------------------------------
    TODO: Implement neighbor counting and in-place bit-packing transitions.
    -------------------------------------------------------------------------
    """
    m, n = len(board), len(board[0])
    offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    for r in range(m):
        for c in range(n):
            live_neighbors = 0
            for dr, dc in offsets:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    live_neighbors += board[nr][nc] & 1

            # <<< YOUR CODE HERE >>>
            # Hint: determine next_state (1 or 0) based on rules.
            # If next_state is 1, set the second bit: board[r][c] |= 2
            next_alive = False
            if board[r][c] & 1 == 1:
                if live_neighbors in (2, 3):
                    next_alive = True
            else:
                if live_neighbors == 3:
                    next_alive = True

            if next_alive:
                bit_mask = TODO  # Replace with: 2
                if bit_mask is None:
                    raise NotImplementedError("TODO: Set bit 1 for next state alive.")
                board[r][c] |= bit_mask

    # Final pass: update current state to next state
    for r in range(m):
        for c in range(n):
            board[r][c] >>= 1


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
            [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
        ),
        (
            [[1, 1], [1, 0]],
            [[1, 1], [1, 1]],
        ),
    ]

    print("Running tests for lc_0289_game_of_life_compact.py...")
    try:
        for idx, (b, expected) in enumerate(test_cases, 1):
            b_copy = [row[:] for row in b]
            game_of_life(b_copy)
            assert b_copy == expected, f"Case {idx} failed: got {b_copy}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
