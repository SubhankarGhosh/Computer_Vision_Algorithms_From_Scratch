# Module 02 Summary: Blob Detection & Connectivity

This document provides the theoretical, topological, and morphological foundations of Connected Component Analysis, Blob Detection, and Boundary Extraction in 2D binary and multi-label images.

---

## 1. Pixel Adjacency and Grid Topology

In discrete grid geometry, neighborhood connectivity defines how adjacent pixels group into continuous objects (blobs or components).

### 4-Connectivity vs. 8-Connectivity
For a pixel $p = (r, c)$:
* **4-Neighborhood ($N_4(p)$)**:
  $$N_4(p) = \{(r \pm 1, c), (r, c \pm 1)\}$$
  Shares an entire edge. Used in standard LeetCode problems (LC 200, LC 733, LC 1254, LC 1905).
* **8-Neighborhood ($N_8(p)$)**:
  $$N_8(p) = N_4(p) \cup \{(r \pm 1, c \pm 1)\}$$
  Includes diagonal adjacencies. Used in **LC 529: Minesweeper** and contour smoothing.

> [!IMPORTANT]
> **Topology Paradox**: If both foreground (1s) and background (0s) use 8-connectivity, diagonal lines of 1s allow 0s to leak through while simultaneously forming a continuous barrier. In classical vision, to avoid topological contradictions (Jordan Curve Theorem violations), foreground is typically chosen as 8-connected and background as 4-connected (or vice versa).

---

## 2. Connected Component Labeling (CCL)

Connected Component Labeling is the process of assigning unique region labels to disjoint connected subsets of active pixels:
$$\mathcal{I} = \bigcup_{k=1}^K \mathcal{C}_k \quad \text{where } \mathcal{C}_i \cap \mathcal{C}_j = \emptyset \text{ for } i \neq j$$

### Algorithmic Realizations:
1. **Breadth-First Search (BFS) / Depth-First Search (DFS)**:
   * Scan matrix in raster order.
   * Upon encountering an unvisited foreground pixel, launch BFS/DFS wavefront to discover the entire component.
   * **Time Complexity**: $\mathcal{O}(m \cdot n)$ since each cell and edge is traversed $\mathcal{O}(1)$ times.
   * **Space Complexity**: $\mathcal{O}(\min(m, n))$ for BFS queue auxiliary memory vs $\mathcal{O}(m \cdot n)$ call stack for naive DFS.
2. **Disjoint Set Union (DSU / Union-Find)**:
   * Two-pass algorithm linking adjacent active neighbors via union-by-rank and path compression.
   * Running time is near-linear $\mathcal{O}(m \cdot n \cdot \alpha(m \cdot n))$. Highly effective for streaming image rows.

---

## 3. Boundary & Contour Extraction

A connected blob $\mathcal{C}$ consists of interior pixels and boundary pixels.
* **Morphological Erosion**:
  $$\mathcal{C} \ominus B = \{p \mid B_p \subseteq \mathcal{C}\}$$
  where $B$ is the elementary $3 \times 3$ cross structuring element.
* **Internal Boundary Extraction**:
  $$\partial \mathcal{C} = \mathcal{C} \setminus (\mathcal{C} \ominus B)$$
  A pixel $p \in \mathcal{C}$ is on the boundary iff at least one of its 4-neighbors does not belong to $\mathcal{C}$ or lies outside the image boundary.
  This is the exact mathematical foundation of **LeetCode 1034: Coloring A Border** and **LeetCode 463: Island Perimeter**.

---

## 4. Morphological Hole Filling & Watershed Analysis

### Hole Detection & Border Constraints
A "hole" in binary morphology is a connected component of background pixels entirely enclosed by foreground pixels, having no path to the image border.
* In **LeetCode 130: Surrounded Regions** and **LeetCode 1254: Number of Closed Islands**, holes are identified via **geodesic reconstruction from the image boundary**:
  1. Initialize seed markers at all pixels on the image border ($r \in \{0, m-1\}$ or $c \in \{0, n-1\}$).
  2. Dilate/flood-fill outwards across background cells.
  3. All background components unreachable from the border are closed holes.

### Watersheds and Drainage Basins
In topographic surface analysis, local minima act as catchments. **LeetCode 417: Pacific Atlantic Water Flow** models dual-ocean drainage. Simulating rain flow backwards (from sea level uphill) constructs the reachability basins via multi-source wavefront expansion.
