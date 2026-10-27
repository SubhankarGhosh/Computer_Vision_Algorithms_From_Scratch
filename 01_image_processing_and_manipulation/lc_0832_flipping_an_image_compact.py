"""LeetCode 832: Flipping an Image (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/flipping-an-image/
Difficulty: Easy
Category: Image Processing & Manipulation

Computer Vision Context:
    In digital image processing, horizontal reflection (mirroring) and binary inversion
    (photometric negative) are elementary pixel-level spatial transforms.
    Given an n x n binary matrix image:
    1. Flip the image horizontally (reverse each row).
    2. Invert the image (replace 0 with 1, and 1 with 0).

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 01_image_processing_and_manipulation/lc_0832_flipping_an_image_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


def flip_and_invert_image(image: List[List[int]]) -> List[List[int]]:
    """Flips an image horizontally, then inverts all pixel values.

    Algorithmic Requirements:
    - Time Complexity: O(n^2) where n is the dimension of the square image.
    - Space Complexity: O(1) auxiliary space if modified in-place, or O(n^2) for output.

    Steps to implement (In-Place Two-Pointer Approach):
    1. Iterate over each row in `image`.
    2. Use two pointers: `left = 0` and `right = len(row) - 1`.
    3. While `left <= right`:
       - If `row[left] == row[right]`, both values must flip when inverted:
         `row[left] = row[left] ^ 1`
         `row[right] = row[left]`
       - If `row[left] != row[right]`, reversing and inverting leaves them unchanged!
         (e.g., [0, 1] reversed is [1, 0], inverted is [0, 1]).
       - Increment `left += 1`, decrement `right -= 1`.
    4. Return the transformed `image`.

    -------------------------------------------------------------------------
    TODO: Implement the two-pointer in-place flip and invert logic below.
    -------------------------------------------------------------------------
    """
    n = len(image)
    for row in image:
        left = 0
        right = len(row) - 1
        while left <= right:
            # <<< YOUR CODE HERE >>>
            # Hint: If row[left] == row[right], flip row[left] using XOR (^ 1)
            # and copy to row[right].
            if row[left] == row[right]:
                val = TODO  # Replace with: row[left] ^ 1
                if val is None:
                    raise NotImplementedError("TODO: Implement pixel inversion logic.")
                row[left] = val
                row[right] = val
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

    print("Running tests for lc_0832_flipping_an_image_compact.py...")
    try:
        for idx, (grid, expected) in enumerate(test_cases, 1):
            input_copy = [row[:] for row in grid]
            result = flip_and_invert_image(input_copy)
            assert result == expected, f"Case {idx} failed: got {result}, expected {expected}"
            print(f"  [PASS] Test Case {idx}")
        print("All tests passed successfully!")
    except NotImplementedError as e:
        print(f"  [PENDING] {e}")
