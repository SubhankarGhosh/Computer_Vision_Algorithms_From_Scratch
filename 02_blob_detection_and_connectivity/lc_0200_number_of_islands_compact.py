"""LeetCode 200: Number of Islands (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/number-of-islands/
Difficulty: Medium
Category: Blob Detection & Connectivity

Computer Vision Context:
    Connected Component Labeling (CCL):
    Identifies and counts all mutually disjoint 4-connected binary blobs (foreground '1's)
    surrounded by background ('0's).
    This is the foundational step in object detection pipelines, particle counting,
    and document OCR layout analysis.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 02_blob_detection_and_connectivity/lc_0200_number_of_islands_compact.py
"""

from __future__ import annotations
import collections
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def num_islands(grid: List[List[str]]) -> int:
    """Counts the number of 4-connected islands in a binary grid.

    Algorithmic Requirements:
    - Time Complexity: O(m * n) where m, n are grid dimensions.
    - Space Complexity: O(min(m, n)) queue memory when using iterative BFS.

    Steps to implement (BFS Connected Component Labeling):
    1. Check base case: if not grid, return 0.
    2. Determine dimensions m = len(grid), n = len(grid[0]).
    3. Initialize `island_count = 0`.
    4. Iterate r in 0..m-1 and c in 0..n-1:
       - If grid[r][c] == '1':
         - Increment island_count += 1
         - Flood fill to mark entire island visited:
           - grid[r][c] = '0'
           - queue = collections.deque([(r, c)])
           - While queue has elements:
             - Pop (curr_r, curr_c)
             - For each neighbor (nr, nc) in 4 directions:
               - If 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                 - grid[nr][nc] = '0'
                 - queue.append((nr, nc))
    5. Return `island_count`.

    -------------------------------------------------------------------------
    TODO: Implement BFS Connected Component Labeling.
    -------------------------------------------------------------------------
    """
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    island_count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1":
                # <<< YOUR CODE HERE >>>
                # Hint: Increment island_count and launch BFS queue
                island_count += 1
                grid[r][c] = "0"
                queue = collections.deque([(r, c)])

                while queue:
                    curr_r, curr_c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                            visited_mark = TODO  # Replace with: "0"
                            if visited_mark is None:
                                raise NotImplementedError("TODO: Mark cell as visited to prevent revisiting.")
                            grid[nr][nc] = visited_mark
                            queue.append((nr, nc))

    return island_count


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
    ]

    print("Running tests for lc_0200_number_of_islands_compact.py...")
    try:
        for idx, (g, expected) in enumerate(test_cases, 1):
            g_copy = [row[:] for row in g]
            res = num_islands(g_copy)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
