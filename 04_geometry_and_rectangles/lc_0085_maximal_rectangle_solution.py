"""LeetCode 85: Maximal Rectangle (Reference Solution)

Problem URL: https://leetcode.com/problems/maximal-rectangle/
Difficulty: Hard
Category: Geometry & Rectangles

Computer Vision Context:
    Maximal Bounding Box Fitting in Arbitrary Binary Masks:
    Evaluates largest rectangular submask using row-wise histograms and monotonic stacks.
"""

from __future__ import annotations
from typing import List


def maximal_rectangle(matrix: List[List[str]]) -> int:
    """Finds the largest rectangle containing only 1's in a binary matrix.

    Complexity Analysis:
    - Time Complexity: O(m * n). Each row computes heights in O(n) and runs a monotonic stack in O(n).
    - Space Complexity: O(n) for height buffer and index stack.
    """
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    max_area = 0

    for r in range(m):
        for c in range(n):
            if matrix[r][c] == "1":
                heights[c] += 1
            else:
                heights[c] = 0

        # Monotonic stack for largest rectangle in histogram
        stack: List[int] = []
        extended_heights = heights + [0]

        for i, h in enumerate(extended_heights):
            while stack and h < extended_heights[stack[-1]]:
                popped_idx = stack.pop()
                bar_height = extended_heights[popped_idx]
                bar_width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, bar_height * bar_width)
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

    print("Running verification for lc_0085_maximal_rectangle_solution.py...")
    for idx, (mat, expected) in enumerate(test_cases, 1):
        res = maximal_rectangle(mat)
        assert res == expected, f"Case {idx} failed: got {res}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
