# Module 02: Blob Detection & Connectivity

This module covers Connected Component Labeling (CCL), binary mask segmentation, contour/perimeter extraction, hole filling, and drainage basin analysis.

---

## 📚 Problem Curriculum

| Problem | LeetCode Link | Difficulty | CV Concept | Compact Practice | Reference Solution | Status |
| :--- | :--- | :---: | :--- | :---: | :---: | :---: |
| **LC 733** | [Flood Fill](https://leetcode.com/problems/flood-fill/) | Easy | Seed Fill & Connected Region Growth | [`lc_0733_flood_fill_compact.py`](lc_0733_flood_fill_compact.py) | [`lc_0733_flood_fill_solution.py`](lc_0733_flood_fill_solution.py) | 🟢 Complete |
| **LC 463** | [Island Perimeter](https://leetcode.com/problems/island-perimeter/) | Easy | Contour & Boundary Perimeter Extraction | [`lc_0463_island_perimeter_compact.py`](lc_0463_island_perimeter_compact.py) | [`lc_0463_island_perimeter_solution.py`](lc_0463_island_perimeter_solution.py) | 🟢 Complete |
| **LC 200** | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | 4-Connected Component Labeling (CCL) | [`lc_0200_number_of_islands_compact.py`](lc_0200_number_of_islands_compact.py) | [`lc_0200_number_of_islands_solution.py`](lc_0200_number_of_islands_solution.py) | 🟢 Complete |
| **LC 695** | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | Medium | Zeroth-Order Spatial Moment ($M_{00}$) | [`lc_0695_max_area_of_island_compact.py`](lc_0695_max_area_of_island_compact.py) | [`lc_0695_max_area_of_island_solution.py`](lc_0695_max_area_of_island_solution.py) | 🟢 Complete |
| **LC 130** | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | Medium | Morphological Hole Filling & Border Reachability | [`lc_0130_surrounded_regions_compact.py`](lc_0130_surrounded_regions_compact.py) | [`lc_0130_surrounded_regions_solution.py`](lc_0130_surrounded_regions_solution.py) | 🟢 Complete |
| **LC 1034** | [Coloring A Border](https://leetcode.com/problems/coloring-a-border/) | Medium | Morphological Boundary Erosion ($A \setminus (A \ominus B)$) | [`lc_1034_coloring_a_border_compact.py`](lc_1034_coloring_a_border_compact.py) | [`lc_1034_coloring_a_border_solution.py`](lc_1034_coloring_a_border_solution.py) | 🟢 Complete |
| **LC 529** | [Minesweeper](https://leetcode.com/problems/minesweeper/) | Medium | 8-Neighborhood Wavefront Expansion | [`lc_0529_minesweeper_compact.py`](lc_0529_minesweeper_compact.py) | [`lc_0529_minesweeper_solution.py`](lc_0529_minesweeper_solution.py) | 🟢 Complete |
| **LC 417** | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Medium | Watershed Segmentation & Drainage Basins | [`lc_0417_pacific_atlantic_water_flow_compact.py`](lc_0417_pacific_atlantic_water_flow_compact.py) | [`lc_0417_pacific_atlantic_water_flow_solution.py`](lc_0417_pacific_atlantic_water_flow_solution.py) | 🟢 Complete |
| **LC 1254** | [Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/) | Medium | Topological Hole Detection | [`lc_1254_number_of_closed_islands_compact.py`](lc_1254_number_of_closed_islands_compact.py) | [`lc_1254_number_of_closed_islands_solution.py`](lc_1254_number_of_closed_islands_solution.py) | 🟢 Complete |
| **LC 1905** | [Count Sub Islands](https://leetcode.com/problems/count-sub-islands/) | Medium | Binary Mask Containment ($Mask_2 \subseteq Mask_1$) | [`lc_1905_count_sub_islands_compact.py`](lc_1905_count_sub_islands_compact.py) | [`lc_1905_count_sub_islands_solution.py`](lc_1905_count_sub_islands_solution.py) | 🟢 Complete |

---

## 🎯 Computer Vision Foundations

1. **Topology & Connectivity**:
   - 4-connectivity vs 8-connectivity rules for foreground and background components.
2. **Component Labeling & Area Moments**:
   - Iterative BFS component discovery avoids Python recursion stack overflows on large masks.
3. **Internal Boundary Extraction**:
   - Distinguishing interior cells from border cells without premature in-place corruption.
4. **Hole Filling via Geodesic Reconstruction**:
   - Inoculating boundary components followed by binary inversion of isolated internal holes.
5. **Drainage Basins & Watershed Transforms**:
   - Inverting topographic fluid flows to trace shared ocean catchment boundaries.
