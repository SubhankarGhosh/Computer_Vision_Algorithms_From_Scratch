# Agent Operating Manual & Background Context

> **Repository**: `Computer_Vision_Algorithms_From_Scratch`  
> **Root Directory**: `D:\GIT\Computer_Vision_Algorithms_From_Scratch`  
> **Target Scope**: Classical Computer Vision Algorithms & Mathematical Primitives grounded in LeetCode Grid / Matrix / Geometry problems  
> **Python Version**: Python 3.11+ / 3.12+ / 3.13  

---

## 1. Project Mission & Pedagogical Framework

The mission of this repository is to bridge the gap between **Abstract Data Structures & Algorithms (LeetCode)** and **Practical Computer Vision Engineering**. By exploring 2D grid algorithms, connected components, integral images, distance transforms, and computational geometry, we build an intuitive, mathematically rigorous understanding of spatial perception from first principles.

### The Compact Practice Framework
Each topic follows the active-learning pattern established across the `From_Scratch` curriculum:
1. **Dual-Script Per-Problem Structure**:
   - `lc_XXXX_<slug>_compact.py`: Guided active-learning script with granular `TODO = None` placeholders, algorithmic step-by-step hints, CV context, complexity requirements, and a self-contained offline test harness.
   - `lc_XXXX_<slug>_solution.py`: Verified, production-grade reference solution with 100% test pass rate for self-checking.
2. **Comprehensive Theory & Architectural Summaries**:
   - `docs/summary/module_XX_<topic>.md`: Deep dive into mathematical foundations (e.g., discrete convolution kernels, morphological operators, connected component labeling, distance transforms, integral images, and AABB intersection geometry).
3. **Clarifications & Pitfalls Documentation**:
   - `docs/clarifications/module_XX_clarifications.md`: Detailed breakdown of common interview traps, off-by-one boundary conditions, in-place vs. out-of-place memory trade-offs, and coordinate system conventions ($(r, c)$ row-major vs. $(x, y)$ Cartesian).
4. **Offline Test Verification**:
   - Zero external dependencies beyond standard library (`math`, `collections`, `heapq`, `typing`).
   - Every script is directly executable via `python <path_to_script>.py`.

---

## 2. Curriculum & Module Map

| Module | Category | Problems Covered | Core CV Concepts |
| :---: | :--- | :--- | :--- |
| **01** | `01_image_processing_and_manipulation` | LC 832, 661, 48, 835, 3030 | Horizontal flip, box blur, 90° rotation, cross-correlation/template matching, bilateral/region smoothing |
| **02** | `02_blob_detection_and_connectivity` | LC 733, 463, 200, 695, 130, 1034, 529, 417, 1254, 1905 | Connected component labeling (CCL), contour perimeter, hole filling, morphological boundary erosion, watershed drainage, mask containment |
| **03** | `03_matrix_operations_and_distance` | LC 542, 289, 74, 240, 54, 59, 304, 286, 317, 1368, 2503 | Distance transforms (Manhattan map), cellular automata, raster search, saddleback search, integral images (summed-area tables), multi-source BFS wavefronts, 0-1 BFS optical flow |
| **04** | `04_geometry_and_rectangles` | LC 836, 223, 221, 1992, 85, 850 | Axis-Aligned Bounding Box (AABB) overlap, IoU area calculation, maximal square structuring element, farmland detection boxes, maximal rectangle histogram stack, sweep-line segment tree |

---

## 3. Directory Layout

```text
Computer_Vision_Algorithms_From_Scratch/
├── .gitignore
├── README.md                                          # Curriculum overview and execution instructions
├── gemini.md                                          # Agent operating manual (Gemini mirror)
├── agents.md                                          # Mirror operating manual for agent pairs
├── docs/
│   ├── summary/                                       # Mathematical and theoretical foundations
│   │   ├── module_01_image_processing_and_manipulation.md
│   │   ├── module_02_blob_detection_and_connectivity.md
│   │   ├── module_03_matrix_operations_and_distance.md
│   │   └── module_04_geometry_and_rectangles.md
│   └── clarifications/                                # Common pitfalls, edge cases, coordinate conventions
│       ├── module_01_clarifications.md
│       ├── module_02_clarifications.md
│       ├── module_03_clarifications.md
│       └── module_04_clarifications.md
├── 01_image_processing_and_manipulation/              # Module 01
│   ├── README.md
│   ├── lc_0832_flipping_an_image_compact.py
│   ├── lc_0832_flipping_an_image_solution.py
│   ├── lc_0661_image_smoother_compact.py
│   ├── lc_0661_image_smoother_solution.py
│   └── ...
├── 02_blob_detection_and_connectivity/                # Module 02
│   ├── README.md
│   └── ...
├── 03_matrix_operations_and_distance/                 # Module 03
│   ├── README.md
│   └── ...
└── 04_geometry_and_rectangles/                        # Module 04
    ├── README.md
    └── ...
```

---

## 4. Coding Conventions & Standards

- **Coordinate System**: Always explicitly clarify in docstrings whether coordinates are $(r, c)$ where $r \in [0, m-1]$ (row / vertical downward) and $c \in [0, n-1]$ (column / horizontal rightward), or $(x, y)$ where $x$ is horizontal and $y$ is vertical.
- **Complexity Documentation**: Every function docstring must explicitly state **Time Complexity** and **Space Complexity** using Big-O notation.
- **Typing**: Use standard Python typing annotations (`List[List[int]]`, `Tuple[int, int]`, `Optional[...]`).
- **Encoding**: Set UTF-8 encoding in PowerShell before running scripts: `$env:PYTHONIOENCODING = "utf-8"`.
