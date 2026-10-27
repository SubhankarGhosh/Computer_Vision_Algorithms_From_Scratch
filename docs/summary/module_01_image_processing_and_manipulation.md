# Module 01 Summary: Image Processing & Manipulation

This document outlines the theoretical and mathematical foundations behind discrete spatial domain image processing, mapping directly to LeetCode problems 832, 661, 48, 835, and 3030.

---

## 1. Mathematical Model of a Discrete Image

In digital image processing, an image $I$ is represented as a 2D discrete function sampled over a bounded spatial grid:
$$I: \{0, 1, \dots, H - 1\} \times \{0, 1, \dots, W - 1\} \to \mathcal{V}$$

Where:
* $H$ is the height (total rows), indexed by $r \in [0, H-1]$ pointing vertically downward.
* $W$ is the width (total columns), indexed by $c \in [0, W-1]$ pointing horizontally rightward.
* $\mathcal{V}$ is the pixel value range (e.g. $\{0, 1\}$ for binary images, $[0, 255]$ for 8-bit grayscale).

---

## 2. Geometric Transformations & Linear Algebra

### Horizontal Reflection (Flipping)
A horizontal reflection maps each pixel coordinate $(r, c)$ across the vertical centerline:
$$(r, c) \mapsto (r, W - 1 - c)$$
When paired with binary inversion ($I'(r, c) = 1 - I(r, c)$), this corresponds to **LeetCode 832: Flipping an Image**. Using XOR:
$$I'(r, c) = I(r, W - 1 - c) \oplus 1$$

### In-Place $90^\circ$ Clockwise Rotation
An orthogonal affine rotation of $90^\circ$ clockwise transforms coordinate $(r, c)$ to $(c, H - 1 - r)$.
In linear algebra, this transformation can be factored into two elementary operations:
1. **Matrix Transpose**: Reflect across the main diagonal:
   $$M_{r, c} \leftrightarrow M_{c, r} \quad (\forall r < c)$$
2. **Horizontal Row Reversal**: Reflect each row horizontally:
   $$M_{r, c} \leftrightarrow M_{r, W - 1 - c} \quad (\forall c < \lfloor W / 2 \rfloor)$$
This eliminates auxiliary memory, solving **LeetCode 48: Rotate Image** in $\mathcal{O}(N^2)$ time with strictly $\mathcal{O}(1)$ space.

---

## 3. Neighborhood Operations & Discrete 2D Convolution

A neighborhood filter computes an output pixel as a function of the pixels in a $(2k+1) \times (2k+1)$ spatial window centered at $(r, c)$.

### The Box Blur / Mean Filter
The continuous 2D smoothing filter with a uniform box kernel $K$ is given by:
$$I_{\text{smooth}}(r, c) = \frac{1}{|N(r, c)|} \sum_{(dr, dc) \in N(r, c)} I(r + dr, c + dc)$$
Where $N(r, c) = \{(dr, dc) \in \{-1, 0, 1\}^2 \mid 0 \le r + dr < H \text{ and } 0 \le c + dc < W\}$.
For interior pixels, $|N(r, c)| = 9$. For edge pixels, $|N(r, c)| = 6$. For corner pixels, $|N(r, c)| = 4$.
This models **LeetCode 661: Image Smoother**.

### Cross-Correlation and Template Matching
To measure the alignment between two binary images $A$ and $B$, we compute the 2D cross-correlation surface over all possible integer translation shifts $(dr, dc)$:
$$\mathcal{C}(dr, dc) = \sum_{r} \sum_{c} A(r, c) \cdot B(r + dr, c + dc)$$
In **LeetCode 835: Image Overlap**, rather than evaluating all $(2N-1)^2$ possible shifts exhaustively over dense matrices, we represent the images as sparse sets of active coordinates:
$$\mathcal{S}_A = \{(r, c) \mid A(r, c) = 1\}, \quad \mathcal{S}_B = \{(r, c) \mid B(r, c) = 1\}$$
For every pair $(p_A, p_B) \in \mathcal{S}_A \times \mathcal{S}_B$, the displacement vector is $\vec{\Delta} = p_A - p_B$. The translation yielding the maximum frequency count in the histogram of displacement vectors gives the optimal overlap in $\mathcal{O}(|\mathcal{S}_A| \cdot |\mathcal{S}_B|)$ time.

---

## 4. Edge-Preserving & Bilateral-Style Filtering

Standard linear blurring blurs structural edges. Modern edge-preserving filters (e.g., Bilateral Filter, Guided Filter) condition neighborhood averaging on pixel similarity:
$$w(p, q) = w_{\text{spatial}}(\|p - q\|) \cdot w_{\text{range}}(|I(p) - I(q)|)$$

In **LeetCode 3030: Find the Grid of Region Average**, a $3 \times 3$ patch is considered a valid homogeneous region if and only if:
$$\forall (u, v) \text{ adjacent in patch}, \quad |I(u) - I(v)| \le \text{threshold}$$
Overlapping valid patches accumulate their floored mean intensities onto constituent pixels, which are then averaged to produce the final edge-aware smoothed image.
