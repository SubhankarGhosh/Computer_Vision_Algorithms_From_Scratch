"""LeetCode 463: Island Perimeter (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/island-perimeter/
Difficulty: Easy
Category: Blob Detection & Connectivity

Computer Vision Context:
    Boundary & Contour Extraction:
    In discrete binary morphology, the perimeter of a connected component is the total count
    of outer boundary edges interfacing with background (water) or image borders.
    Each 1x1 land cell has 4 potential edges; sharing an edge with an adjacent land cell
    removes 2 boundary edges (1 from each cell).

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 02_blob_detection_and_connectivity/lc_0463_island_perimeter_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def island_perimeter(grid: List[List[int]]) -> int:
    """Calculates the perimeter of a single connected island.

    Algorithmic Requirements:
    - Time Complexity: O(m * n). Single raster scan over grid.
    - Space Complexity: O(1) auxiliary space.

    Steps to implement:
    1. Initialize `perimeter = 0`.
    2. Traverse each cell (r, c) in the grid:
       - If grid[r][c] == 1:
         - Start with 4 sides for this cell: perimeter += 4
         - Check top neighbor (r - 1, c): if r > 0 and grid[r - 1][c] == 1, perimeter -= 2
         - Check left neighbor (r, c - 1): if c > 0 and grid[r][c - 1] == 1, perimeter -= 2
           (Checking only top and left avoids double-counting shared internal edges!)
    3. Return `perimeter`.

    -------------------------------------------------------------------------
    TODO: Implement the perimeter counting and shared edge subtraction logic.
    -------------------------------------------------------------------------
    """
    m, n = len(grid), len(grid[0])
    perimeter = 0

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                perimeter += 4
                # <<< YOUR CODE HERE >>>
                # Hint: If top neighbor is land (grid[r-1][c] == 1), subtract 2
                # If left neighbor is land (grid[r][c-1] == 1), subtract 2
                shared_reduction = 0
                if r > 0 and grid[r - 1][c] == 1:
                    shared_reduction += 2
                if c > 0 and grid[r][c - 1] == 1:
                    shared_reduction += 2

                sub_val = TODO  # Replace with: shared_reduction
                if sub_val is None:
                    raise NotImplementedError("TODO: Subtract shared internal edges.")
                perimeter -= sub_val

    return perimeter


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]],
            16,
        ),
        (
            [[1]],
            4,
        ),
        (
            [[1, 0]],
            4,
        ),
    ]

    print("Running tests for lc_0463_island_perimeter_compact.py...")
    try:
        for idx, (g, expected) in enumerate(test_cases, 1):
            res = island_perimeter(g)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
