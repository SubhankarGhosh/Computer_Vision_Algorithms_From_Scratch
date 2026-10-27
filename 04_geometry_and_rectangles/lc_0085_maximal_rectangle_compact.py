"""LeetCode 85: Maximal Rectangle (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/maximal-rectangle/
Difficulty: Hard
Category: Geometry & Rectangles

Computer Vision Context:
    Maximal Bounding Box Fitting in Arbitrary Binary Masks:
    Detects the largest axis-aligned rectangle enclosing contiguous foreground (1s).
    By maintaining a running column height histogram row-by-row and applying
    the Monotonic Increasing Stack algorithm (LC 84: Largest Rectangle in Histogram),
    the search evaluates all potential bounding box geometries in optimal O(m * n) time.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 04_geometry_and_rectangles/lc_0085_maximal_rectangle_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def maximal_rectangle(matrix: List[List[str]]) -> int:
    """Finds the largest rectangle containing only 1's in a binary matrix.

    Algorithmic Requirements:
    - Time Complexity: O(m * n). Single row-wise pass with O(n) monotonic stack per row.
    - Space Complexity: O(n) for the height histogram and stack.

    Steps to implement:
    1. If not matrix or not matrix[0], return 0.
    2. Dimensions m = len(matrix), n = len(matrix[0]).
    3. Initialize `heights = [0] * n` and `max_area = 0`.
    4. For each row:
       - Update heights: `heights[c] = heights[c] + 1 if matrix[r][c] == '1' else 0`.
       - Compute largest rectangle in histogram with sentinel 0 appended:
         - stack = []
         - for i, h in enumerate(heights + [0]):
           - while stack and h < heights[stack[-1]]:
             - height = heights[stack.pop()]
             - width = i if not stack else i - stack[-1] - 1
             - max_area = max(max_area, height * width)
           - stack.append(i)
    5. Return `max_area`.

    -------------------------------------------------------------------------
    TODO: Implement row height accumulation and monotonic stack area calculation.
    -------------------------------------------------------------------------
    """
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    max_area = 0

    for r in range(m):
        # Step 1: Update heights histogram
        for c in range(n):
            if matrix[r][c] == "1":
                heights[c] += 1
            else:
                heights[c] = 0

        # Step 2: Monotonic stack to find largest rectangle in heights histogram
        stack: List[int] = []
        extended_heights = heights + [0]  # Sentinel 0 to flush stack at the end

        for i, h in enumerate(extended_heights):
            while stack and h < extended_heights[stack[-1]]:
                # <<< YOUR CODE HERE >>>
                # Hint: Pop previous height, calculate width, and update max_area
                popped_idx = stack.pop()
                bar_height = extended_heights[popped_idx]
                bar_width = i if not stack else i - stack[-1] - 1

                area = TODO  # Replace with: bar_height * bar_width
                if area is None:
                    raise NotImplementedError("TODO: Compute area = bar_height * bar_width.")
                max_area = max(max_area, area)

            stack.append(i)

    return max_area


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ],
            6,
        ),
        (
            [["0"]],
            0,
        ),
        (
            [["1"]],
            1,
        ),
    ]

    print("Running tests for lc_0085_maximal_rectangle_compact.py...")
    try:
        for idx, (mat, expected) in enumerate(test_cases, 1):
            res = maximal_rectangle(mat)
            assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
