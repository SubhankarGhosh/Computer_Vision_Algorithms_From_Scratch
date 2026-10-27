# Module 01: Image Processing & Manipulation

This module focuses on fundamental spatial domain operations on 2D images, including geometric transformations, neighborhood filtering (discrete convolution), and spatial template matching.

---

## 📚 Problem Curriculum

| Problem | LeetCode Link | Difficulty | CV Concept | Compact Practice | Reference Solution |
| :--- | :--- | :---: | :--- | :---: | :---: |
| **LC 832** | [Flipping an Image](https://leetcode.com/problems/flipping-an-image/) | Easy | Horizontal Mirroring & Binary Inversion | [`lc_0832_flipping_an_image_compact.py`](lc_0832_flipping_an_image_compact.py) | [`lc_0832_flipping_an_image_solution.py`](lc_0832_flipping_an_image_solution.py) |
| **LC 661** | [Image Smoother](https://leetcode.com/problems/image-smoother/) | Easy | $3 \times 3$ Box Blur / Mean Filter Convolution | [`lc_0661_image_smoother_compact.py`](lc_0661_image_smoother_compact.py) | [`lc_0661_image_smoother_solution.py`](lc_0661_image_smoother_solution.py) |
| **LC 48** | [Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | In-Place 90° Clockwise Rotation | `lc_0048_rotate_image_compact.py` | `lc_0048_rotate_image_solution.py` |
| **LC 835** | [Image Overlap](https://leetcode.com/problems/image-overlap/) | Medium | 2D Cross-Correlation & Template Matching | `lc_0835_image_overlap_compact.py` | `lc_0835_image_overlap_solution.py` |
| **LC 3030** | [Find the Grid of Region Average](https://leetcode.com/problems/find-the-grid-of-region-average/) | Medium | Edge-Preserving Smoothing & Bilateral Filtering | `lc_3030_find_the_grid_of_region_average_compact.py` | `lc_3030_find_the_grid_of_region_average_solution.py` |

---

## 🎯 Computer Vision Foundations

1. **Spatial Representation**:
   Images are 2D discrete matrices $I(r, c)$ where $r \in [0, H-1]$ represents row index (y-axis pointing downward) and $c \in [0, W-1]$ represents column index (x-axis pointing rightward).
2. **Discrete 2D Convolution**:
   A linear filter applies a kernel $K$ of size $(2k+1) \times (2k+1)$ centered at $(r, c)$:
   $$I_{\text{smooth}}(r, c) = \frac{1}{|N(r, c)|} \sum_{(dr, dc) \in N(r, c)} I(r + dr, c + dc)$$
3. **Cross-Correlation & Shift Vectors**:
   Finding optimal image alignment via discrete translation vectors $\vec{\Delta} = (\Delta r, \Delta c)$ maximizing $\sum_{(r, c)} A(r, c) \cdot B(r + \Delta r, c + \Delta c)$.
