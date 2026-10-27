"""LeetCode 130: Surrounded Regions (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/surrounded-regions/
Difficulty: Medium
Category: Blob Detection & Connectivity

Computer Vision Context:
    Morphological Hole Filling & Border Reachability:
    In binary morphology, a "hole" is a connected component of background pixels ('O')
    that cannot reach the image boundary without crossing foreground pixels ('X').
    To fill holes in-place:
    1. Mark all 'O' pixels connected to the boundary as "immune" (e.g. temporary label 'S').
    2. Convert all remaining 'O' pixels to 'X' (these are surrounded internal holes).
    3. Revert the immune 'S' pixels back to 'O'.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 02_blob_detection_and_connectivity/lc_0130_surrounded_regions_compact.py
"""

from __future__ import annotations
import collections
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def solve(board: List[List[str]]) -> None:
    """Modifies the board in-place, flipping all surrounded 'O' regions to 'X'.

    Algorithmic Requirements:
    - Time Complexity: O(m * n).
    - Space Complexity: O(m + n) queue space for boundary seeds.

    Steps to implement:
    1. If not board or not board[0], return.
    2. Identify all boundary cells having 'O':
       - Rows 0 and m - 1 for all columns.
       - Columns 0 and n - 1 for all rows.
    3. Enqueue all boundary 'O's and repaint them to 'S' (Safe/Immune).
    4. Run BFS from boundary seeds:
       - For each (r, c) in queue, check 4 neighbors.
       - If neighbor (nr, nc) is within bounds and board[nr][nc] == 'O':
         - board[nr][nc] = 'S'
         - queue.append((nr, nc))
    5. Final pass over entire board:
       - If board[r][c] == 'O': flip to 'X' (surrounded hole filled)
       - If board[r][c] == 'S': restore to 'O' (boundary-connected region)

    -------------------------------------------------------------------------
    TODO: Implement boundary-connected flood fill and hole filling pass.
    -------------------------------------------------------------------------
    """
    if not board or not board[0]:
        return

    m, n = len(board), len(board[0])
    queue = collections.deque()

    # Step 1: Collect boundary 'O' cells
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

    # Step 2: Flood fill boundary-reachable components
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O":
                board[nr][nc] = "S"
                queue.append((nr, nc))

    # Step 3: Reconstruct grid (flip internal 'O' -> 'X', restore 'S' -> 'O')
    for r in range(m):
        for c in range(n):
            if board[r][c] == "O":
                # <<< YOUR CODE HERE >>>
                # Hint: Internal unreached 'O' is surrounded and must become 'X'
                filled_val = TODO  # Replace with: "X"
                if filled_val is None:
                    raise NotImplementedError("TODO: Fill surrounded hole with 'X'.")
                board[r][c] = filled_val
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

    print("Running tests for lc_0130_surrounded_regions_compact.py...")
    try:
        for idx, (board, expected) in enumerate(test_cases, 1):
            board_copy = [row[:] for row in board]
            solve(board_copy)
            assert board_copy == expected, f"Case {idx} failed: got {board_copy}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
