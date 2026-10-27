"""LeetCode 2503: Maximum Number of Points From Grid Queries (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/
Difficulty: Hard
Category: Matrix Operations & Distance

Computer Vision Context:
    Monotonic Watershed Flooding & Priority-Queue Wavefront:
    In topographic digital elevation models, water rising to elevation level q fills
    all contiguous valleys connected to the source basin (0, 0) having height < q.
    Rather than re-running BFS for every query (O(k * m * n)), we process queries offline
    in sorted order. A Min-Heap (priority queue) holds the expanding wavefront boundary,
    ensuring each pixel is visited at most once across all queries in O(mn log(mn) + k log k) time.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 03_matrix_operations_and_distance/lc_2503_maximum_number_of_points_from_grid_queries_compact.py
"""

from __future__ import annotations
import heapq
from typing import List, Set, Tuple

# Sentinel placeholder for exercise tasks
TODO = None


def max_points(grid: List[List[int]], queries: List[int]) -> List[int]:
    """Answers all elevation threshold queries using offline sorting and min-heap wavefront expansion.

    Algorithmic Requirements:
    - Time Complexity: O(mn log(mn) + k log k) where k is len(queries).
    - Space Complexity: O(mn + k) for heap, visited set, and result list.

    Steps to implement:
    1. Dimensions m = len(grid), n = len(grid[0]).
    2. Sort queries with their original indices:
       sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
    3. Initialize `ans = [0] * len(queries)`.
    4. Min-Heap: `heap = [(grid[0][0], 0, 0)]`.
    5. Track `visited: Set[Tuple[int, int]] = {(0, 0)}`.
    6. Accumulator: `points = 0`.
    7. Directions = [(-1, 0), (1, 0), (0, -1), (0, 1)].
    8. For (orig_idx, q) in sorted_queries:
       - While heap and heap[0][0] < q:
         - pop (val, r, c) from heap
         - points += 1
         - for (dr, dc) in directions:
           - nr, nc = r + dr, c + dc
           - if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
             - visited.add((nr, nc))
             - heapq.heappush(heap, (grid[nr][nc], nr, nc))
       - ans[orig_idx] = points
    9. Return ans.

    -------------------------------------------------------------------------
    TODO: Implement priority-queue watershed flooding logic.
    -------------------------------------------------------------------------
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
        # <<< YOUR CODE HERE >>>
        # Hint: While min-heap has cells with height < q, pop, increment points,
        # and push valid unvisited neighbors into heap
        while heap and heap[0][0] < q:
            val, r, c = heapq.heappop(heap)
            points += 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))

        recorded_points = TODO  # Replace with: points
        if recorded_points is None:
            raise NotImplementedError("TODO: Record points reached for the current query elevation.")
        ans[orig_idx] = recorded_points

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

    print("Running tests for lc_2503_maximum_number_of_points_from_grid_queries_compact.py...")
    try:
        for idx, (grid, q_list, expected) in enumerate(test_cases, 1):
            res = max_points(grid, q_list)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
