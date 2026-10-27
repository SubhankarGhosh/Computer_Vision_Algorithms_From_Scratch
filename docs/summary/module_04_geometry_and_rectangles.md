# Module 04 Summary: Geometry & Rectangles

This document outlines the geometric, combinatorial, and data-structure foundations for Axis-Aligned Bounding Boxes (AABBs), Intersection-over-Union (IoU), morphological structuring element fitting, and 2D Sweep-Line algorithms.

---

## 1. Axis-Aligned Bounding Boxes (AABB) & Overlap Detection

In object detection (YOLO, Faster R-CNN, SSD), detections are parameterized as Axis-Aligned Bounding Boxes:
$$B = [x_1, y_1, x_2, y_2] \quad \text{where } x_1 < x_2 \text{ and } y_1 < y_2$$

### Separating Axis Theorem (1D Projection Overlap)
Two 2D axis-aligned rectangles $A$ and $B$ overlap with **non-zero area** if and only if their 1D orthogonal projections onto both the $X$-axis and $Y$-axis overlap simultaneously:
$$\text{Overlap}_X \iff \max(A.x_1, B.x_1) < \min(A.x_2, B.x_2)$$
$$\text{Overlap}_Y \iff \max(A.y_1, B.y_1) < \min(A.y_2, B.y_2)$$
This condition forms the basis of **LC 836: Rectangle Overlap**, running in $\mathcal{O}(1)$ time.

---

## 2. Principle of Inclusion-Exclusion & Intersection-over-Union (IoU)

Evaluating detector accuracy requires computing the Jaccard index (IoU):
$$\text{IoU}(A, B) = \frac{\text{Area}(A \cap B)}{\text{Area}(A \cup B)} = \frac{\text{Area}(A \cap B)}{\text{Area}(A) + \text{Area}(B) - \text{Area}(A \cap B)}$$

In **LC 223: Rectangle Area**, the union area of two rectangles is evaluated via inclusion-exclusion:
$$\text{Area}(A \cup B) = (A.x_2 - A.x_1)(A.y_2 - A.y_1) + (B.x_2 - B.x_1)(B.y_2 - B.y_1) - \Delta x \cdot \Delta y$$
Where $\Delta x = \max(0, \min(A.x_2, B.x_2) - \max(A.x_1, B.x_1))$ and $\Delta y = \max(0, \min(A.y_2, B.y_2) - \max(A.y_1, B.y_1))$.

---

## 3. Morphological Structuring Elements (Maximal Square)

In mathematical morphology, erosion by a flat square structuring element $S_k$ of size $k \times k$ identifies regions capable of enclosing $S_k$:
$$\mathcal{I} \ominus S_k$$

In **LC 221: Maximal Square**, Dynamic Programming computes the largest square structuring element ending at $(r, c)$:
$$DP[r][c] = \begin{cases} \min(DP[r-1][c], DP[r][c-1], DP[r-1][c-1]) + 1 & \text{if } I(r, c) = 1 \\ 0 & \text{otherwise} \end{cases}$$
The optimal side length $k^* = \max_{r, c} DP[r][c]$ yields the maximal square area $(k^*)^2$ in $\mathcal{O}(m \cdot n)$ time.

---

## 4. Monotonic Stack for Arbitrary Rectangle Fitting

In **LC 85: Maximal Rectangle**, arbitrary bounding boxes are fit inside binary masks.
* We convert the 2D matrix into a series of 1D histograms:
  $$h_r[c] = \begin{cases} h_{r-1}[c] + 1 & \text{if } M[r][c] = 1 \\ 0 & \text{if } M[r][c] = 0 \end{cases}$$
* For each row's histogram, a **Monotonic Increasing Stack** determines the left and right boundary limits for each bar in linear $\mathcal{O}(n)$ time.
* Overall matrix runtime is optimal $\mathcal{O}(m \cdot n)$.

---

## 5. 2D Sweep-Line Algorithm (Rectangle Area II)

When computing the total area covered by $N$ overlapping bounding boxes (**LC 850**):
* Rather than naive rasterization (prohibited by $10^9$ coordinates), we use a **1D Sweep-Line** along the $X$-axis:
  1. Decompose each box into an `OPEN` event at $x_1$ and a `CLOSE` event at $x_2$.
  2. Collect all unique $y$-coordinates and sort them to define discrete vertical intervals $[y_j, y_{j+1}]$.
  3. Sweep across sorted $x$-events. For each strip of width $\Delta x = x_{i+1} - x_i$, sum the lengths of all vertical intervals currently covered by at least one active box:
     $$\Delta \text{Area} = \Delta x \times \sum_{j: \text{count}[j] > 0} (y_{j+1} - y_j)$$
* Runs in $\mathcal{O}(N^2)$ (or $\mathcal{O}(N \log N)$ with segment tree), operating gracefully over coordinate spaces up to $10^9$.
