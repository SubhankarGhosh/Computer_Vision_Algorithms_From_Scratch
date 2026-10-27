"""LeetCode 832: Flipping an Image (Reference Solution)

Problem URL: https://leetcode.com/problems/flipping-an-image/
Difficulty: Easy
Category: Image Processing & Manipulation

Computer Vision Context:
    Horizontal reflection and photometric binary inversion:
    I'(r, c) = 1 - I(r, W - 1 - c)
    In binary images {0, 1}, 1 - x is equivalent to x ^ 1.
"""

from __future__ import annotations
from typing import List


def flip_and_invert_image(image: List[List[int]]) -> List[List[int]]:
    """Flips an image horizontally, then inverts all pixel values in-place.

    Complexity Analysis:
    - Time Complexity: O(n^2) where n is the dimension of the square image.
      Each pixel is inspected at most once in a single linear pass per row.
    - Space Complexity: O(1) auxiliary space as modifications occur directly in-place.
    """
    for row in image:
        left = 0
        right = len(row) - 1
        while left <= right:
            if row[left] == row[right]:
                # Both elements are identical; flipping and inverting changes both
                inverted = row[left] ^ 1
                row[left] = inverted
                row[right] = inverted
            # Note: if row[left] != row[right], reversing and inverting leaves them identical!
            left += 1
            right -= 1

    return image


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        (
            [[1, 1, 0], [1, 0, 1], [0, 0, 0]],
            [[1, 0, 0], [0, 1, 0], [1, 1, 1]],
        ),
        (
            [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]],
            [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]],
        ),
        (
            [[0]],
            [[1]],
        ),
        (
            [[1]],
            [[0]],
        ),
    ]

    print("Running verification for lc_0832_flipping_an_image_solution.py...")
    for idx, (grid, expected) in enumerate(test_cases, 1):
        input_copy = [row[:] for row in grid]
        result = flip_and_invert_image(input_copy)
        assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
        print(f"  [PASS] Test Case {idx}")
    print("All tests passed with 100% success rate!")
