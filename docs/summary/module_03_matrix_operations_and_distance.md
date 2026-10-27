# Module 03 Summary: Matrix Operations & Distance

This document details the mathematical, topological, and computational geometry foundations of 2D matrix algorithms, Distance Transforms, Integral Images (Summed-Area Tables), Cellular Automata, and Shortest Paths on Grid Graphs.

---

## 1. Distance Transforms & Wavefront Propagation

A **Distance Transform (DT)** converts a binary image $\mathcal{I}$ into a grayscale distance map where every pixel contains its minimum distance to the nearest foreground (or background) feature:
$$D(p) = \min_{q \in \mathcal{S}} d(p, q)$$

### Manhattan ($L_1$) Metric
For points $p = (r_1, c_1)$ and $q = (r_2, c_2)$, the Manhattan distance is:
$$d_{L_1}(p, q) = |r_1 - r_2| + |c_1 - c_2|$$
* **Multi-Source BFS**:
  By enqueuing all source points $\mathcal{S}$ simultaneously at $t = 0$, a uniform BFS wavefront expands at rate $1 \text{ pixel/step}$.
  Every unvisited cell reached receives its exact geodesic $L_1$ distance in $\mathcal{O}(m \cdot n)$ time.
  This directly solves **LC 542: 01 Matrix** and **LC 286: Walls and Gates**.
* **Centroid Optimization (Geometric Median)**:
  In **LC 317: Shortest Distance from All Buildings**, we aggregate multi-source distance surfaces:
  $$\mathcal{D}_{\text{total}}(p) = \sum_{k=1}^K d_{L_1}(p, B_k)$$
  Finding $p^* = \arg\min_p \mathcal{D}_{\text{total}}(p)$ optimizes facility location under Manhattan travel geometry.

---

## 2. Cellular Automata & In-Place State Encoding

John Conway's Game of Life (**LC 289**) is a 2D discrete dynamical system governed by local transition rules based on the 8-neighborhood sum:
$$S(r, c) = \sum_{(dr, dc) \in N_8} I(r + dr, c + dc)$$

### State Encoding via Bit Manipulation
To update an $m \times n$ matrix synchronously in-place without auxiliary memory:
* Bit 0: Current State ($0$ = dead, $1$ = alive).
* Bit 1: Next State ($0$ = will die, $1$ = will live).
$$\text{cell} \leftarrow \text{cell} \mid (\text{next\_state} \ll 1)$$
During neighbor counting, extract the current state using bitwise AND: `neighbor & 1`.
After inspecting all cells, shift states globally: `cell >>= 1`. This achieves $\mathcal{O}(mn)$ time with $\mathcal{O}(1)$ auxiliary space.

---

## 3. Integral Images (Summed-Area Tables)

Introduced by Frank Crow (1984) and made famous by Paul Viola and Michael Jones (2001) for real-time face detection, an **Integral Image** $SAT$ allows computing the sum of pixel values over any arbitrary axis-aligned rectangular window in $\mathcal{O}(1)$ time.

### Mathematical Formulation
$$SAT(r, c) = \sum_{i=0}^r \sum_{j=0}^c I(i, j)$$

Computed recursively in a single 2D pass:
$$SAT(r, c) = I(r, c) + SAT(r - 1, c) + SAT(r, c - 1) - SAT(r - 1, c - 1)$$

### $\mathcal{O}(1)$ Box Sum Query
For any rectangle with top-left $(r_1, c_1)$ and bottom-right $(r_2, c_2)$:
$$\text{Sum}(R) = SAT(r_2, c_2) - SAT(r_1 - 1, c_2) - SAT(r_2, c_1 - 1) + SAT(r_1 - 1, c_1 - 1)$$
This is the core engine of **LC 304: Range Sum Query 2D - Immutable**.

```text
       c1-1    c2
r1-1    +-------+
        |   A   |   B
        +-------+-------+
        |       |       |
        |   C   |   D   |  <-- Area D = (A+B+C+D) - (A+B) - (A+C) + A
r2      +-------+-------+
```

---

## 4. Shortest Path on Directed Vector Fields (0-1 BFS)

In **LC 1368: Minimum Cost to Make at Least One Valid Path in a Grid**, the grid represents a directed velocity / flow field. Following the sign costs $0$; altering the direction costs $1$.
* While Dijkstra's algorithm solves general shortest paths in $\mathcal{O}(V \log V + E) = \mathcal{O}(mn \log(mn))$, edge weights in this grid are strictly binary $w \in \{0, 1\}$.
* **0-1 BFS**:
  Using a double-ended queue (`collections.deque`):
  * Traversing a 0-weight edge: `deque.appendleft((nr, nc, cost))`
  * Traversing a 1-weight edge: `deque.append((nr, nc, cost + 1))`
  This maintains queue monotonicity, guaranteeing optimal paths in strictly linear $\mathcal{O}(m \cdot n)$ time.

---

## 5. Offline Watershed Flooding & Min-Heap Queues

In **LC 2503: Maximum Number of Points From Grid Queries**, queries seek the maximum connected region reachable from $(0, 0)$ where all cells have elevation $< q$.
* By sorting queries offline ($q_1 \le q_2 \le \dots \le q_k$) and using a Min-Heap (priority queue) at the wavefront boundary, cells are discovered in monotonically increasing order of elevation.
* Once a cell is absorbed into the connected component, it never needs to be visited again, executing all $k$ queries in $\mathcal{O}(mn \log(mn) + k \log k)$ time.
