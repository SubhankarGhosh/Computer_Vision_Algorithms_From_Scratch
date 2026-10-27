# Computer Vision Algorithms From Scratch: Mastery Laboratory

An active-learning, test-driven curriculum designed to master **Classical Computer Vision Algorithms, 2D Grid Primitives, and Spatial Geometry** from first principles—grounded in 32 high-yield LeetCode problems.

---

## 🗺️ Curriculum Structure & Problem Map

| Module | Category | Problems Covered | Key Computer Vision Concepts | Status |
| :---: | :--- | :--- | :--- | :---: |
| **01** | [Image Processing & Manipulation](01_image_processing_and_manipulation/) | • [832. Flipping an Image](https://leetcode.com/problems/flipping-an-image/) (Easy)<br>• [661. Image Smoother](https://leetcode.com/problems/image-smoother/) (Easy)<br>• [48. Rotate Image](https://leetcode.com/problems/rotate-image/) (Medium)<br>• [835. Image Overlap](https://leetcode.com/problems/image-overlap/) (Medium)<br>• [3030. Find the Grid of Region Average](https://leetcode.com/problems/find-the-grid-of-region-average/) (Medium) | Mirroring, binary inversion, 2D box blur/mean filter convolution, in-place 90° affine rotation, 2D cross-correlation/template matching, edge-preserving smoothing. | 🟢 Ready |
| **02** | [Blob Detection & Connectivity](02_blob_detection_and_connectivity/) | • [733. Flood Fill](https://leetcode.com/problems/flood-fill/) (Easy)<br>• [463. Island Perimeter](https://leetcode.com/problems/island-perimeter/) (Easy)<br>• [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) (Medium)<br>• [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/) (Medium)<br>• [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) (Medium)<br>• [1034. Coloring A Border](https://leetcode.com/problems/coloring-a-border/) (Medium)<br>• [529. Minesweeper](https://leetcode.com/problems/minesweeper/) (Medium)<br>• [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) (Medium)<br>• [1254. Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/) (Medium)<br>• [1905. Count Sub Islands](https://leetcode.com/problems/count-sub-islands/) (Medium) | Connected Component Labeling (CCL 4/8-conn), perimeter/contour extraction, hole filling, morphological boundary erosion, drainage basins/watersheds, binary mask containment. | 🟢 Ready |
| **03** | [Matrix Operations & Distance](03_matrix_operations_and_distance/) | • [542. 01 Matrix](https://leetcode.com/problems/01-matrix/) (Medium)<br>• [289. Game of Life](https://leetcode.com/problems/game-of-life/) (Medium)<br>• [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) (Medium)<br>• [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) (Medium)<br>• [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) (Medium)<br>• [59. Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/) (Medium)<br>• [304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) (Medium)<br>• [286. Walls and Gates](https://leetcode.com/problems/walls-and-gates/) (Medium)<br>• [317. Shortest Distance from All Buildings](https://leetcode.com/problems/shortest-distance-from-all-buildings/) (Hard)<br>• [1368. Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/) (Hard)<br>• [2503. Maximum Number of Points From Grid Queries](https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/) (Hard) | Distance transforms (Manhattan distance map), cellular automata state transitions, raster binary search, saddleback search, integral images (summed-area tables for Viola-Jones), multi-source BFS wavefronts, 0-1 BFS optical vector fields. | 🟢 Ready |
| **04** | [Geometry & Rectangles](04_geometry_and_rectangles/) | • [836. Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/) (Easy)<br>• [223. Rectangle Area](https://leetcode.com/problems/rectangle-area/) (Medium)<br>• [221. Maximal Square](https://leetcode.com/problems/maximal-square/) (Medium)<br>• [1992. Find All Groups of Farmland](https://leetcode.com/problems/find-all-groups-of-farmland/) (Medium)<br>• [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) (Hard)<br>• [850. Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/) (Hard) | Axis-Aligned Bounding Box (AABB) intersection, IoU area calculation, maximal square morphological structuring elements, object detection bounding boxes, monotonic stack histograms, 2D sweep-line segment tree. | 🟢 Ready |

---

## 🛠️ How the Practice Works

Following the **Compact Practice Framework**:
* **Per-Problem Guided Scripts (`lc_XXXX_<slug>_compact.py`)**:
  Contains the problem statement, LeetCode link, Computer Vision intuition, time/space constraints, granular `TODO = None` placeholders, and an offline test suite.
* **Reference Solutions (`lc_XXXX_<slug>_solution.py`)**:
  Complete, verified solution passing 100% of the test cases with interview-ready commentary.
* **Theory & Concept Summaries (`docs/summary/`)**:
  Mathematical background (discrete convolutions, kernels, structuring elements, distance metrics).
* **Clarifications & Traps (`docs/clarifications/`)**:
  Edge cases, row-major vs. Cartesian coordinate traps, and algorithmic nuances.

### Running Exercises Standalone
Every script runs independently with zero external packages:
```powershell
# Set UTF-8 output encoding in PowerShell
$env:PYTHONIOENCODING = "utf-8"

# Run a compact practice script
python 01_image_processing_and_manipulation/lc_0832_flipping_an_image_compact.py

# Run a solution verification script
python 01_image_processing_and_manipulation/lc_0832_flipping_an_image_solution.py

# Run all 32 curriculum reference solutions end-to-end
python run_all_modules.py
```
