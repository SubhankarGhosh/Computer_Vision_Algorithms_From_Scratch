"""LeetCode 733: Flood Fill (Reference Solution)

Problem URL: https://leetcode.com/problems/flood-fill/
Difficulty: Easy
Category: Blob Detection & Connectivity

Computer Vision Context:
    Seed fill / Connected component painting:
    Expands 4-connected wavefront from (sr, sc) across homogeneous intensity region.
"""

from __future__ import annotations
import collections
from typing import List


def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    """Performs a 4-connected flood fill starting from (sr, sc).

    Complexity Analysis:
    - Time Complexity: O(m * n). Each cell is queued and colored at most once.
    - Space Complexity: O(m * n) worst-case queue memory for broad wavefronts.
    """
    m, n = len(image), len(image[0])
    start_color = image[sr][sc]

    # Guard condition against infinite cycling
    if start_color == color:
        return image

    queue = collections.deque([(sr, sc)])
    image[sr][sc] = color

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == start_color:
                image[nr][nc] = color
                queue.append((nr, nc))

    return image


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2,
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        ),
        (
            [[0, 0, 0], [0, 0, 0]], 0, 0, 0,
            [[0, 0, 0], [0, 0, 0]],
        ),
        (
            [[0, 0, 0], [0, 1, 1]], 1, 1, 1,
            [[0, 0, 0], [0, 1, 1]],
        ),
    ]

    print("Running verification for lc_0733_flood_fill_solution.py...")
    for idx, (img, sr, sc, col, expected) in enumerate(test_cases, 1):
        img_copy = [row[:] for row in img]
        res = flood_fill(img_copy, sr, sc, col)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
