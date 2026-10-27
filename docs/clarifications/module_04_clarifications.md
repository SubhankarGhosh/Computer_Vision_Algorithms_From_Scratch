# Module 04 Clarifications & Pitfalls: Geometry & Rectangles

This document highlights critical coordinate system transformations, boundary conditions, and overflow handling for Module 04.

---

### Q1: Point / Line Contact vs. True Overlap (LC 836)
* **The Pitfall**: Two rectangles sharing an edge (e.g. $[0, 0, 1, 1]$ and $[1, 0, 2, 1]$) or a corner touch geometrically, but their intersection area is **zero**.
* **The Rule**: In computer vision bounding box evaluation (IoU), touching borders do NOT constitute an overlap! Use strict inequality:
  ```python
  return (
      rec1[0] < rec2[2] and rec2[0] < rec1[2] and
      rec1[1] < rec2[3] and rec2[1] < rec1[3]
  )
  ```

---

### Q2: Row-Major Grid vs Cartesian Bounding Boxes
* **Cartesian Coordinates ($x, y$)**:
  * Used in **LC 836**, **LC 223**, and **LC 850**: $[x_1, y_1, x_2, y_2]$ where $(x_1, y_1)$ is bottom-left and $(x_2, y_2)$ is top-right ($y$ increases upwards).
* **Matrix Grid Coordinates ($r, c$)**:
  * Used in **LC 221**, **LC 1992**, and **LC 85**: $[r_1, c_1, r_2, c_2]$ where $(r_1, c_1)$ is top-left and $(r_2, c_2)$ is bottom-right ($r$ increases downwards).
* Keep these representations strictly isolated to avoid inverted coordinate bugs.

---

### Q3: Disconnected Solid Rectangles (LC 1992 Farmland)
* Because the problem guarantees that farmland components form solid, non-overlapping rectangles:
  * You do **not** need expensive flood fills!
  * Simply look for top-left corners: $(r, c)$ is a top-left corner iff $land[r][c] == 1$ and neither its top neighbor ($r-1, c$) nor its left neighbor ($r, c-1$) is 1.
  * Once the top-left corner is found, expand rightwards along row $r$ until 0 or edge, then expand downwards along column $c$ until 0 or edge to locate the bottom-right corner $(r_2, c_2)$ in $\mathcal{O}(1)$ local steps.

---

### Q4: Modulo Arithmetic in Area Accumulation (LC 850)
* Coordinates in LC 850 range up to $10^9$, which means intermediate areas can reach $10^{18}$ (fitting comfortably in Python's arbitrary-precision integers, but requiring modulo $10^9 + 7$ at the end).
* Apply modulo at each accumulation step: `total_area = (total_area + delta_x * active_height) % (10**9 + 7)`.
