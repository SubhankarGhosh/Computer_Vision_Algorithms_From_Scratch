"""LeetCode 289: Game of Life (Reference Solution)

Problem URL: https://leetcode.com/problems/game-of-life/
Difficulty: Medium
Category: Matrix Operations & Distance

Computer Vision Context:
    Synchronous Cellular Automata:
    Uses bit packing to update cell states simultaneously with strictly O(1) auxiliary space.
"""

from __future__ import annotations
from typing import List


def game_of_life(board: List[List[int]]) -> None:
    """Updates the board to its next state in-place.

    Complexity Analysis:
    - Time Complexity: O(m * n). 8 constant neighbor checks per cell.
    - Space Complexity: O(1) auxiliary memory via bit manipulation.
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

            # Rule evaluation
            if board[r][c] & 1 == 1:
                if live_neighbors in (2, 3):
                    board[r][c] |= 2  # Set 2nd bit (next state alive)
            else:
                if live_neighbors == 3:
                    board[r][c] |= 2  # Set 2nd bit (reproduction)

    # Shift states globally
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

    print("Running verification for lc_0289_game_of_life_solution.py...")
    for idx, (b, expected) in enumerate(test_cases, 1):
        b_copy = [row[:] for row in b]
        game_of_life(b_copy)
        assert b_copy == expected, f"Case {idx} failed: got {b_copy}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
