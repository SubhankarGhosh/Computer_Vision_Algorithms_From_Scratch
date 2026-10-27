# Module 01 Clarifications & Pitfalls: Image Processing & Manipulation

This document highlights critical algorithmic nuances, memory boundaries, and coordinate system conventions frequently tested in interviews for Module 01.

---

### Q1: Matrix $(r, c)$ vs. Image $(x, y)$ Coordinates
* **The Pitfall**: In Cartesian coordinate geometry and computer graphics APIs (e.g. OpenCV image sizing), points are specified as $(x, y)$ where $x$ is horizontal (width) and $y$ is vertical (height). However, in nested matrix arrays (`image[r][c]`), $r$ indexes the row (vertical position) and $c$ indexes the column (horizontal position).
* **Rule of Thumb**:
  * $r \leftrightarrow y$ (height / rows: $0 \le r < H$)
  * $c \leftrightarrow x$ (width / cols: $0 \le c < W$)
  * Always use `m = len(image)` (rows) and `n = len(image[0])` (columns).

---

### Q2: In-Place Modification vs. Out-of-Place Contamination (LC 661 vs LC 48)
* **The Pitfall**: In convolution or neighborhood filtering (like **LC 661: Image Smoother**), modifying `image[r][c]` directly during traversal corrupts subsequent neighborhood calculations for adjacent pixels $(r, c+1)$ or $(r+1, c)$.
* **Resolution**:
  * **Approach A (Standard)**: Allocate an auxiliary output matrix `result = [[0] * n for _ in range(m)]` ($\mathcal{O}(mn)$ space).
  * **Approach B (Bit-Packing / State Encoding)**: If pixel intensities are bounded (e.g. 8-bit $0 \le \text{val} \le 255$), use bit shifting to encode the new value in the upper 8 bits: `image[r][c] |= (new_val << 8)`. After the pass, extract with `image[r][c] >>= 8` to achieve $\mathcal{O}(1)$ auxiliary space.

---

### Q3: Why Transpose + Reverse yields $90^\circ$ Clockwise Rotation (LC 48)
* Let coordinate be $(r, c)$.
* **Transpose** swaps coordinates: $(r, c) \to (c, r)$.
* **Horizontal Reflection** flips column: $(c, r) \to (c, N - 1 - r)$.
* This precisely matches the clockwise transformation equation $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$.
* *Note*: If you want $90^\circ$ **counter-clockwise** rotation, reverse each row first, then transpose!

---

### Q4: LC 835 Sparse Displacement Hash vs. Dense 2D Shift
* Evaluating every possible $(2N - 1)^2$ shift across two $N \times N$ matrices naively takes $\mathcal{O}(N^4)$ time.
* If the image has few 1s (sparse active pixels), collecting coordinates $\mathcal{S}_A$ and $\mathcal{S}_B$ and aggregating vector differences $\vec{d} = (r_a - r_b, c_a - c_b)$ in a hash map (`collections.defaultdict(int)`) runs in $\mathcal{O}(|\mathcal{S}_A| \cdot |\mathcal{S}_B|)$.
* In the worst case where $|\mathcal{S}_A| \approx N^2$, this is $\mathcal{O}(N^4)$, but in typical sparse binary masks, it is orders of magnitude faster.
