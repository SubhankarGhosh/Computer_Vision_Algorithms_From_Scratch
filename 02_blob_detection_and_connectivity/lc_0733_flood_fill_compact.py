"""LeetCode 733: Flood Fill (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/flood-fill/
Difficulty: Easy
Category: Blob Detection & Connectivity

Computer Vision Context:
    Seed fill / Connected region painting:
    Starting from a seed point (sr, sc), find all 4-connected pixels having the same
    initial color and repaint them with the target color.
    This is the fundamental operation used in interactive segmentation tools (e.g., Magic Wand).

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 02_blob_detection_and_connectivity/lc_0733_flood_fill_compact.py
"""

from __future__ import annotations
import collections
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    """Performs a 4-connected flood fill starting from (sr, sc).

    Algorithmic Requirements:
    - Time Complexity: O(m * n) where m, n are grid dimensions.
    - Space Complexity: O(m * n) queue/visited space in worst case.

    Steps to implement (Iterative BFS):
    1. Check guard condition: if image[sr][sc] == color, return image immediately!
    2. Store initial seed color: `start_color = image[sr][sc]`.
    3. Initialize a queue: `queue = collections.deque([(sr, sc)])`.
    4. Repaint the starting pixel: `image[sr][sc] = color`.
    5. While queue is not empty:
       - Pop (r, c) from left of queue.
       - For each neighbor (nr, nc) in 4 directions:
         - If 0 <= nr < m, 0 <= nc < n and image[nr][nc] == start_color:
           - Update color: image[nr][nc] = color
           - Enqueue (nr, nc)
    6. Return image.

    -------------------------------------------------------------------------
    TODO: Implement iterative BFS flood fill logic below.
    -------------------------------------------------------------------------
    """
    m, n = len(image), len(image[0])
    start_color = image[sr][sc]

    # Guard against infinite loop when target color equals start color
    if start_color == color:
        return image

    queue = collections.deque([(sr, sc)])
    image[sr][sc] = color

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # <<< YOUR CODE HERE >>>
            # Hint: Check bounds and whether image[nr][nc] == start_color
            if 0 <= nr < m and 0 <= nc < n:
                if image[nr][nc] == start_color:
                    new_val = TODO  # Replace with: color
                    if new_val is None:
                        raise NotImplementedError("TODO: Repaint pixel with target color.")
                    image[nr][nc] = new_val
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

    print("Running tests for lc_0733_flood_fill_compact.py...")
    try:
        for idx, (img, sr, sc, col, expected) in enumerate(test_cases, 1):
            img_copy = [row[:] for row in img]
            res = flood_fill(img_copy, sr, sc, col)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
