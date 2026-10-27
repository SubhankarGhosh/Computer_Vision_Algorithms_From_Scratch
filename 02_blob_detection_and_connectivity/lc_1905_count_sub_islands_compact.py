"""LeetCode 1905: Count Sub Islands (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/count-sub-islands/
Difficulty: Medium
Category: Blob Detection & Connectivity

Computer Vision Context:
    Binary Mask Containment / Subset Verification:
    Given two segmentation masks M1 and M2, determine whether a connected component C in M2
    is strictly a subset of M1:
        C subseteq M1  <==>  forall p in C, M1(p) == 1
    
    Critical Implementation Trap:
    Do NOT break early when finding an invalid cell (where grid1[r][c] == 0)!
    If you stop traversing early, unvisited cells of the same island in grid2 will remain,
    and a later iteration will incorrectly count that detached fragment as a valid sub-island.
    Always complete the BFS traversal of the full island, tracking validity via a boolean flag.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 02_blob_detection_and_connectivity/lc_1905_count_sub_islands_compact.py
"""

from __future__ import annotations
import collections
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def count_sub_islands(grid1: List[List[int]], grid2: List[List[int]]) -> int:
    """Counts how many islands in grid2 are completely contained within islands of grid1.

    Algorithmic Requirements:
    - Time Complexity: O(m * n).
    - Space Complexity: O(min(m, n)) queue memory with iterative BFS.

    Steps to implement:
    1. Dimensions m = len(grid1), n = len(grid1[0]).
    2. Initialize `sub_island_count = 0`.
    3. Directions = [(-1, 0), (1, 0), (0, -1), (0, 1)].
    4. Iterate r in 0..m-1 and c in 0..n-1:
       - If grid2[r][c] == 1:
         - is_sub = True
         - grid2[r][c] = 0 (mark visited in grid2)
         - queue = collections.deque([(r, c)])
         - while queue:
           - pop (curr_r, curr_c)
           - if grid1[curr_r][curr_c] == 0:
             is_sub = False (cell not supported by grid1!)
           - for (dr, dc) in directions:
             - nr, nc = curr_r + dr, curr_c + dc
             - if 0 <= nr < m and 0 <= nc < n and grid2[nr][nc] == 1:
               - grid2[nr][nc] = 0
               - queue.append((nr, nc))
         - If is_sub is True, increment sub_island_count += 1
    5. Return `sub_island_count`.

    -------------------------------------------------------------------------
    TODO: Implement full island exploration and containment checking.
    -------------------------------------------------------------------------
    """
    m, n = len(grid1), len(grid1[0])
    sub_island_count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(m):
        for c in range(n):
            if grid2[r][c] == 1:
                is_sub = True
                grid2[r][c] = 0
                queue = collections.deque([(r, c)])

                while queue:
                    curr_r, curr_c = queue.popleft()
                    # Check if cell in grid2 has corresponding land in grid1
                    if grid1[curr_r][curr_c] == 0:
                        is_sub = False

                    for dr, dc in directions:
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < m and 0 <= nc < n and grid2[nr][nc] == 1:
                            grid2[nr][nc] = 0
                            queue.append((nr, nc))

                # <<< YOUR CODE HERE >>>
                # Hint: If the entire island was supported by grid1, increment sub_island_count
                if is_sub:
                    increment = TODO  # Replace with: 1
                    if increment is None:
                        raise NotImplementedError("TODO: Increment sub_island_count for valid sub-island.")
                    sub_island_count += increment

    return sub_island_count


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [
                [1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 1, 1],
            ],
            [
                [1, 1, 1, 0, 0],
                [0, 0, 1, 1, 1],
                [0, 1, 0, 0, 0],
                [1, 0, 1, 1, 0],
                [0, 1, 0, 1, 0],
            ],
            3,
        ),
        (
            [
                [1, 0, 1, 0, 1],
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [1, 0, 1, 0, 1],
            ],
            [
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [1, 0, 0, 0, 1],
            ],
            2,
        ),
    ]

    print("Running tests for lc_1905_count_sub_islands_compact.py...")
    try:
        for idx, (g1, g2, expected) in enumerate(test_cases, 1):
            g1_copy = [row[:] for row in g1]
            g2_copy = [row[:] for row in g2]
            res = count_sub_islands(g1_copy, g2_copy)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
