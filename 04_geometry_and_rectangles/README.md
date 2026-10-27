# Module 04: Geometry & Rectangles

This module covers Axis-Aligned Bounding Box (AABB) intersection tests, Intersection-over-Union (IoU) calculation, maximal square structuring element fitting, agricultural bounding box regression, monotonic stack histograms, and the 2D sweep-line segment tree.

---

## 📚 Problem Curriculum

| Problem | LeetCode Link | Difficulty | CV Concept | Compact Practice | Reference Solution | Status |
| :--- | :--- | :---: | :--- | :---: | :---: | :---: |
| **LC 836** | [Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/) | Easy | AABB Intersection Verification | [`lc_0836_rectangle_overlap_compact.py`](lc_0836_rectangle_overlap_compact.py) | [`lc_0836_rectangle_overlap_solution.py`](lc_0836_rectangle_overlap_solution.py) | 🟢 Complete |
| **LC 223** | [Rectangle Area](https://leetcode.com/problems/rectangle-area/) | Medium | Inclusion-Exclusion & IoU Area | [`lc_0223_rectangle_area_compact.py`](lc_0223_rectangle_area_compact.py) | [`lc_0223_rectangle_area_solution.py`](lc_0223_rectangle_area_solution.py) | 🟢 Complete |
| **LC 221** | [Maximal Square](https://leetcode.com/problems/maximal-square/) | Medium | Structuring Element Fitting (DP) | [`lc_0221_maximal_square_compact.py`](lc_0221_maximal_square_compact.py) | [`lc_0221_maximal_square_solution.py`](lc_0221_maximal_square_solution.py) | 🟢 Complete |
| **LC 1992** | [Find All Groups of Farmland](https://leetcode.com/problems/find-all-groups-of-farmland/) | Medium | Rectangular Bounding Box Regression | [`lc_1992_find_all_groups_of_farmland_compact.py`](lc_1992_find_all_groups_of_farmland_compact.py) | [`lc_1992_find_all_groups_of_farmland_solution.py`](lc_1992_find_all_groups_of_farmland_solution.py) | 🟢 Complete |
| **LC 85** | [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) | Hard | Monotonic Stack Histogram Fitting | [`lc_0085_maximal_rectangle_compact.py`](lc_0085_maximal_rectangle_compact.py) | [`lc_0085_maximal_rectangle_solution.py`](lc_0085_maximal_rectangle_solution.py) | 🟢 Complete |
| **LC 850** | [Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/) | Hard | 2D Sweep-Line + Coordinate Compression | [`lc_0850_rectangle_area_ii_compact.py`](lc_0850_rectangle_area_ii_compact.py) | [`lc_0850_rectangle_area_ii_solution.py`](lc_0850_rectangle_area_ii_solution.py) | 🟢 Complete |

---

## 🎯 Computer Vision Foundations

1. **Separating Axis Theorem & AABB Overlap**:
   - 1D projection overlap verification along $X$ and $Y$ axes.
2. **IoU & Bounding Box Overlap Evaluation**:
   - Applying the Principle of Inclusion-Exclusion to measure union area.
3. **Structuring Element Fitting (DP)**:
   - Dynamic Programming recurrence for maximal square structuring element morphology.
4. **Bounding Box Regression without Pixel Flooding**:
   - Top-left anchor identification and greedy perimeter expansion in $\mathcal{O}(mn)$ time.
5. **Monotonic Stack Histogram Analysis**:
   - Fitting arbitrary rectangular submasks within binary segmentation frames in $\mathcal{O}(mn)$.
6. **2D Sweep-Line & Coordinate Compression**:
   - Multi-box union area calculation across large coordinate domains up to $10^9$.
