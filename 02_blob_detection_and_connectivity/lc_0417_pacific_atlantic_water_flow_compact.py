"""LeetCode 417: Pacific Atlantic Water Flow (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/pacific-atlantic-water-flow/
Difficulty: Medium
Category: Blob Detection & Connectivity

Computer Vision Context:
    Topographic Watershed Segmentation & Dual Drainage Basin Analysis:
    In digital elevation models (DEMs), drainage divides separate catchments that drain
    into different terminal basins.
    Instead of simulating rainfall draining downhill from every grid cell (O(m^2 * n^2)),
    we invert the flow: launch multi-source BFS from the ocean boundaries uphill
    (heights[neighbor] >= heights[current]).
    The set intersection of Pacific-reachable and Atlantic-reachable cells delineates
    the shared watershed ridgeline.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 02_blob_detection_and_connectivity/lc_0417_pacific_atlantic_water_flow_compact.py
"""

from __future__ import annotations
import collections
from typing import List, Set, Tuple

# Sentinel placeholder for exercise tasks
TODO = None


def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    """Finds all grid coordinates from which water can drain into both oceans.

    Algorithmic Requirements:
    - Time Complexity: O(m * n). Two BFS traversals across the grid.
    - Space Complexity: O(m * n) to maintain ocean reachability sets.

    Steps to implement:
    1. If not heights or not heights[0], return [].
    2. Dimensions m = len(heights), n = len(heights[0]).
    3. Initialize `pacific_reach: Set[Tuple[int, int]] = set()` and `atlantic_reach = set()`.
    4. Multi-source BFS helper `bfs(seeds) -> reach_set`:
       - queue = collections.deque(seeds)
       - reach_set = set(seeds)
       - while queue:
         - pop (r, c)
         - for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           - nr, nc = r + dr, c + dc
           - if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in reach_set:
             - if heights[nr][nc] >= heights[r][c]:  # flows uphill!
               - reach_set.add((nr, nc))
               - queue.append((nr, nc))
    5. Pacific seeds: row 0 (all cols) and col 0 (all rows).
    6. Atlantic seeds: row m - 1 (all cols) and col n - 1 (all rows).
    7. Return sorted list of [r, c] for all (r, c) in pacific_reach & atlantic_reach.

    -------------------------------------------------------------------------
    TODO: Implement uphill reverse BFS reachability.
    -------------------------------------------------------------------------
    """
    if not heights or not heights[0]:
        return []

    m, n = len(heights), len(heights[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(seeds: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
        queue = collections.deque(seeds)
        reach: Set[Tuple[int, int]] = set(seeds)

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in reach:
                    # <<< YOUR CODE HERE >>>
                    # Hint: Water flows downhill, so reverse flow must travel UPHILL
                    # Check if heights[nr][nc] >= heights[r][c]
                    can_flow_uphill = heights[nr][nc] >= heights[r][c]
                    if can_flow_uphill:
                        valid_neighbor = TODO  # Replace with: (nr, nc)
                        if valid_neighbor is None:
                            raise NotImplementedError("TODO: Enqueue valid uphill neighbor coordinate.")
                        reach.add(valid_neighbor)
                        queue.append(valid_neighbor)

        return reach

    # Collect initial ocean boundaries
    pacific_seeds = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
    atlantic_seeds = [(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)]

    pacific_reach = bfs(pacific_seeds)
    atlantic_reach = bfs(atlantic_seeds)

    # Intersection of both drainage basins
    result = [[r, c] for (r, c) in sorted(pacific_reach & atlantic_reach)]
    return result


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ],
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
        ),
        (
            [[1]],
            [[0, 0]],
        ),
    ]

    print("Running tests for lc_0417_pacific_atlantic_water_flow_compact.py...")
    try:
        for idx, (h, expected) in enumerate(test_cases, 1):
            res = pacific_atlantic(h)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
