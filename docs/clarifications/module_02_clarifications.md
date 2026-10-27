# Module 02 Clarifications & Pitfalls: Blob Detection & Connectivity

This document details critical edge cases, memory models, recursion limits, and topological subtleties across the 10 Module 02 problems.

---

### Q1: Python Recursion Limit vs. Iterative BFS (`RecursionError`)
* **The Pitfall**: In deep DFS recursions (e.g., a spiral or snake grid of size $300 \times 300 = 90,000$ cells), Python's default recursion limit (`sys.getrecursionlimit()` is 1000) causes an immediate `RecursionError: maximum recursion depth exceeded`.
* **Resolution**:
  * In interviews and production, prefer **Iterative BFS using `collections.deque`**. BFS memory is bounded by the wavefront width ($\mathcal{O}(\min(m, n))$) rather than total component size ($\mathcal{O}(mn)$).
  * If DFS is preferred, use an explicit list stack `stack = [(r, c)]` rather than call stack recursion.

---

### Q2: State Modification in Flood Fill (Avoiding Infinite Loops)
* **The Pitfall**: In **LC 733: Flood Fill**, if `image[sr][sc] == color` (target color is already the current color), a standard DFS/BFS without an initial guard will continuously re-enqueue adjacent cells of the same color, creating an infinite loop.
* **Rule**:
  ```python
  if image[sr][sc] == color:
      return image
  ```

---

### Q3: String Matrices vs. Integer Matrices
* Pay close attention to input types:
  * **LC 200: Number of Islands** gives strings: `'1'` (land) and `'0'` (water). Checking `if grid[r][c] == 1` causes silent failure!
  * **LC 695: Max Area of Island** gives integers: `1` and `0`.
  * **LC 1254: Number of Closed Islands** inverts the polarity: `0` is land, `1` is water!

---

### Q4: Boundary Premature Mutation (LC 1034: Coloring A Border)
* **The Pitfall**: When coloring the border of a connected component, mutating a cell's color to `newColor` *during* the traversal changes how its neighbors perceive it. Adjacent component pixels will subsequently believe their neighbor is an outsider, erroneously coloring internal pixels as borders!
* **Resolution**:
  * Traverse the component using a `visited` set without mutating values.
  * Collect border cells into a separate list `border_cells = []`.
  * After the entire component is explored, color only the collected `border_cells`.

---

### Q5: Complete Sub-Island Verification (LC 1905)
* **The Pitfall**: In **LC 1905: Count Sub Islands**, when checking if an island in `grid2` is a sub-island of `grid1`, terminating traversal early as soon as `grid1[r][c] == 0` is found leaves the remainder of that `grid2` island unvisited. Later, a future iteration will pick up the unvisited remainder and count it as a separate valid sub-island!
* **Resolution**:
  * Must traverse the **entire** island in `grid2` to mark all cells visited, maintaining a boolean flag `is_sub = is_sub and (grid1[r][c] == 1)`.
