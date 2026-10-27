"""LeetCode 2503: Maximum Number of Points From Grid Queries (Reference Solution)

Problem URL: https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/
Difficulty: Hard
Category: Matrix Operations & Distance

Computer Vision Context:
    Priority-Queue Watershed Flooding with Offline Elevation Queries:
    Discovers terrain valleys in monotonic elevation order via a single Min-Heap pass.
"""

from __future__ import annotations
import heapq
from typing import List, Set, Tuple


def max_points(grid: List[List[int]], queries: List[int]) -> List[int]:
    """Answers all elevation threshold queries using offline sorting and min-heap wavefront expansion.

    Complexity Analysis:
    - Time Complexity: O(mn log(mn) + k log k) where k is len(queries).
      Each cell enters and exits the heap at most once.
    - Space Complexity: O(mn + k) for heap, visited set, and result list.
    """
    m, n = len(grid), len(grid[0])
    k = len(queries)
    sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
    ans = [0] * k

    heap = [(grid[0][0], 0, 0)]
    visited: Set[Tuple[int, int]] = {(0, 0)}
    points = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for orig_idx, q in sorted_queries:
        while heap and heap[0][0] < q:
            val, r, c = heapq.heappop(heap)
            points += 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))

        ans[orig_idx] = points

    return ans


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [[1, 2, 3], [2, 5, 7], [3, 5, 1]],
            [5, 6, 2],
            [5, 8, 1],
        ),
        (
            [[5, 2, 1], [1, 1, 2]],
            [3],
            [0],
        ),
    ]

    print("Running verification for lc_2503_maximum_number_of_points_from_grid_queries_solution.py...")
    for idx, (grid, q_list, expected) in enumerate(test_cases, 1):
        res = max_points(grid, q_list)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
