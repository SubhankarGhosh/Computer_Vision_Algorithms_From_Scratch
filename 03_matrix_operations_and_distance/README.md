# Module 03: Matrix Operations & Distance

This module covers distance transforms (Manhattan distance maps), cellular automata state transitions, 2D raster search, integral images (Summed-Area Tables for Haar features), multi-source BFS wavefronts, and 0-1 BFS optical vector fields.

---

## 📚 Problem Curriculum

| Problem | LeetCode Link | Difficulty | CV Concept | Compact Practice | Reference Solution | Status |
| :--- | :--- | :---: | :--- | :---: | :---: | :---: |
| **LC 542** | [01 Matrix](https://leetcode.com/problems/01-matrix/) | Medium | Manhattan Distance Transform Map | [`lc_0542_01_matrix_compact.py`](lc_0542_01_matrix_compact.py) | [`lc_0542_01_matrix_solution.py`](lc_0542_01_matrix_solution.py) | 🟢 Complete |
| **LC 289** | [Game of Life](https://leetcode.com/problems/game-of-life/) | Medium | Cellular Automata & In-Place Bit Encoding | [`lc_0289_game_of_life_compact.py`](lc_0289_game_of_life_compact.py) | [`lc_0289_game_of_life_solution.py`](lc_0289_game_of_life_solution.py) | 🟢 Complete |
| **LC 74** | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Medium | 1D-to-2D Raster Coordinate Mapping | [`lc_0074_search_a_2d_matrix_compact.py`](lc_0074_search_a_2d_matrix_compact.py) | [`lc_0074_search_a_2d_matrix_solution.py`](lc_0074_search_a_2d_matrix_solution.py) | 🟢 Complete |
| **LC 240** | [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) | Medium | Saddleback Gradient Search | [`lc_0240_search_a_2d_matrix_ii_compact.py`](lc_0240_search_a_2d_matrix_ii_compact.py) | [`lc_0240_search_a_2d_matrix_ii_solution.py`](lc_0240_search_a_2d_matrix_ii_solution.py) | 🟢 Complete |
| **LC 54** | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | Boundary Peeling & Spiral Scan Traversal | [`lc_0054_spiral_matrix_compact.py`](lc_0054_spiral_matrix_compact.py) | [`lc_0054_spiral_matrix_solution.py`](lc_0054_spiral_matrix_solution.py) | 🟢 Complete |
| **LC 59** | [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/) | Medium | Synthetic Matrix Pattern Generation | [`lc_0059_spiral_matrix_ii_compact.py`](lc_0059_spiral_matrix_ii_compact.py) | [`lc_0059_spiral_matrix_ii_solution.py`](lc_0059_spiral_matrix_ii_solution.py) | 🟢 Complete |
| **LC 304** | [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | Medium | Integral Image (Viola-Jones Summed-Area Table) | [`lc_0304_range_sum_query_2d_immutable_compact.py`](lc_0304_range_sum_query_2d_immutable_compact.py) | [`lc_0304_range_sum_query_2d_immutable_solution.py`](lc_0304_range_sum_query_2d_immutable_solution.py) | 🟢 Complete |
| **LC 286** | [Walls and Gates](https://leetcode.com/problems/walls-and-gates/) | Medium | Multi-Source Voronoi Distance Propagation | [`lc_0286_walls_and_gates_compact.py`](lc_0286_walls_and_gates_compact.py) | [`lc_0286_walls_and_gates_solution.py`](lc_0286_walls_and_gates_solution.py) | 🟢 Complete |
| **LC 317** | [Shortest Distance from All Buildings](https://leetcode.com/problems/shortest-distance-from-all-buildings/) | Hard | Multi-Source Distance Surface & Optimal Centroid | [`lc_0317_shortest_distance_from_all_buildings_compact.py`](lc_0317_shortest_distance_from_all_buildings_compact.py) | [`lc_0317_shortest_distance_from_all_buildings_solution.py`](lc_0317_shortest_distance_from_all_buildings_solution.py) | 🟢 Complete |
| **LC 1368** | [Minimum Cost to Make at Least One Valid Path](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/) | Hard | 0-1 BFS & Dijkstra on Directed Vector Field | [`lc_1368_minimum_cost_to_make_at_least_one_valid_path_in_a_grid_compact.py`](lc_1368_minimum_cost_to_make_at_least_one_valid_path_in_a_grid_compact.py) | [`lc_1368_minimum_cost_to_make_at_least_one_valid_path_in_a_grid_solution.py`](lc_1368_minimum_cost_to_make_at_least_one_valid_path_in_a_grid_solution.py) | 🟢 Complete |
| **LC 2503** | [Maximum Number of Points From Grid Queries](https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/) | Hard | Thresholded Watershed Flooding & Priority Queue | [`lc_2503_maximum_number_of_points_from_grid_queries_compact.py`](lc_2503_maximum_number_of_points_from_grid_queries_compact.py) | [`lc_2503_maximum_number_of_points_from_grid_queries_solution.py`](lc_2503_maximum_number_of_points_from_grid_queries_solution.py) | 🟢 Complete |

---

## 🎯 Computer Vision Foundations

1. **Chamfer & Manhattan Distance Transforms**:
   - Simultaneous multi-source wavefront expansion for obstacle distance fields.
2. **Cellular Automata Memory Optimization**:
   - In-place bit packing ($0 \le \text{state} \le 3$) to simulate synchronous state transitions in $\mathcal{O}(1)$ space.
3. **Integral Images (Summed-Area Tables)**:
   - Viola-Jones rectangular feature extraction in constant $\mathcal{O}(1)$ query time.
4. **0-1 BFS on Optical Flow Fields**:
   - Linear $\mathcal{O}(mn)$ shortest path search across directed vector fields.
5. **Priority-Queue Monotonic Watershed Flooding**:
   - Offline threshold query processing over elevation surfaces.
