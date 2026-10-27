"""LeetCode 417: Pacific Atlantic Water Flow (Reference Solution)

Problem URL: https://leetcode.com/problems/pacific-atlantic-water-flow/
Difficulty: Medium
Category: Blob Detection & Connectivity

Computer Vision Context:
    Watershed Segmentation & Catchment Basin Ridge Line:
    Reverses downhill fluid drainage via dual multi-source uphill BFS wavefronts.
"""

from __future__ import annotations
import collections
from typing import List, Set, Tuple


def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    """Finds all grid coordinates from which water can drain into both oceans.

    Complexity Analysis:
    - Time Complexity: O(m * n). Both Pacific and Atlantic BFS explore each cell at most once.
    - Space Complexity: O(m * n) to maintain reachability sets and queues.
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
                    if heights[nr][nc] >= heights[r][c]:
                        reach.add((nr, nc))
                        queue.append((nr, nc))

        return reach

    pacific_seeds = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
    atlantic_seeds = [(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)]

    pacific_reach = bfs(pacific_seeds)
    atlantic_reach = bfs(atlantic_seeds)

    return [[r, c] for (r, c) in sorted(pacific_reach & atlantic_reach)]


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

    print("Running verification for lc_0417_pacific_atlantic_water_flow_solution.py...")
    for idx, (h, expected) in enumerate(test_cases, 1):
        res = pacific_atlantic(h)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
