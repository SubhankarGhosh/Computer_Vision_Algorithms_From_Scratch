# Module 03 Clarifications & Pitfalls: Matrix Operations & Distance

This document highlights critical performance traps, memory boundaries, and index transformations across Module 03.

---

### Q1: Multi-Source BFS Initialization
* **The Pitfall**: Running independent BFS passes from each source point separately leads to catastrophic $\mathcal{O}(K \cdot m \cdot n)$ time complexity (e.g. In **LC 542: 01 Matrix**, if there are thousands of 0s, running a separate BFS from each 0 results in TLE).
* **The Solution**: Enqueue **all** source coordinates into the `deque` simultaneously *before* starting the `while queue:` loop. The single joint wavefront guarantees each cell is visited exactly once at its global minimum distance in $\mathcal{O}(mn)$ time.

---

### Q2: 1-Based Padding in 2D Prefix Sums (LC 304)
* **The Pitfall**: Computing $SAT(r - 1, c)$ and $SAT(r, c - 1)$ directly on a 0-indexed matrix requires cumbersome boundary checks (`if r > 0`, `if c > 0`, `if r > 0 and c > 0`).
* **The Solution**: Allocate the prefix sum array with dimensions $(m + 1) \times (n + 1)$ filled with 0s:
  ```python
  pref = [[0] * (n + 1) for _ in range(m + 1)]
  for r in range(m):
      for c in range(n):
          pref[r + 1][c + 1] = matrix[r][c] + pref[r][c + 1] + pref[r + 1][c] - pref[r][c]
  ```
  Query for rectangle $(r_1, c_1)$ to $(r_2, c_2)$ becomes cleanly:
  ```python
  return pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1]
  ```

---

### Q3: 0-1 BFS vs Dijkstra (LC 1368)
* **Why not standard Dijkstra?**
  Dijkstra's algorithm uses a binary min-heap (`heapq`), introducing an $\mathcal{O}(\log(mn))$ overhead per edge traversal.
* **Why 0-1 BFS?**
  Because edge weights are only $0$ and $1$, a double-ended queue maintains the property that elements in the queue never have costs differing by more than 1. By pushing 0-cost transitions to the front (`appendleft`) and 1-cost transitions to the back (`append`), distances remain strictly sorted without sorting overhead, achieving optimal $\mathcal{O}(mn)$ time.

---

### Q4: LC 74 vs LC 240: Flat Binary Search vs Saddleback Search
* **LC 74: Search a 2D Matrix**:
  The first integer of each row is greater than the last integer of the previous row. The matrix is strictly a flattened sorted 1D array. Use binary search over virtual index $[0, mn - 1]$ with $r = \lfloor idx / n \rfloor, c = idx \pmod n$.
* **LC 240: Search a 2D Matrix II**:
  Each row and column is sorted independently, but row $i$ does NOT exceed row $i-1$. Virtual 1D binary search does NOT work!
  Instead, start at the top-right corner $(0, n - 1)$ (or bottom-left):
  * If `val > target`, column must decrease: $c \leftarrow c - 1$.
  * If `val < target`, row must increase: $r \leftarrow r + 1$.
  Runs in $\mathcal{O}(m + n)$ time.
