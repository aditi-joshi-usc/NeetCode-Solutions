# Min Cost to Connect All Points

## Problem Description

You are given a 2D integer array `points`, where `points[i] = [xi, yi]` represents the coordinates of the `i-th` point on a 2D plane. Each point is distinct.

The **cost** of connecting two points `[xi, yi]` and `[xj, yj]` is the **Manhattan distance** between them, calculated as:
|xi - xj| + |yi - yj|
javascript


(where `|val|` denotes the absolute value of `val`).

Your task is to return the **minimum cost** to connect all points such that there exists exactly one path between each pair of points.

---

## Examples

### Example 1

**Input:**
```
points = [[0,0],[2,2],[3,3],[2,44,2]]
```



**Output:**
```
10
```

**Explanation:**
The minimum cost to connect all points is 10. The connections can be visualized as:
```
(0,0) -- (2,2) -- (3,3) -- (2,4) -- (4,2)
```

---

## Constraints

- `1 <= points.length <= 1000`
- `-1000 <= xi, yi <= 1000`

---

## Recommended Complexity

- **Time Complexity:** O((n^2) log n), where `n` is the number of points.
- **Space Complexity:** O(n^2)

---

## Approach

To solve this problem, we can use **Minimum Spanning Tree (MST)** algorithms such as **Prim's Algorithm** or **Kruskal's Algorithm**. These algorithms are well-suited for finding the minimum cost to connect all points in a graph.

### Key Steps:

1. **Graph Representation:**
   - Treat each point as a node in a graph.
   - The edge weight between two nodes is the Manhattan distance between the corresponding points.

2. **Prim's Algorithm:**
   - Start with an arbitrary point and add it to the MST.
   - Use a priority queue to repeatedly add the smallest edge that connects a new point to the MST.
   - Continue until all points are connected.

3. **Kruskal's Algorithm (Alternative):**
   - Compute all possible edges and sort them by weight.
   - Use a union-find data structure to add edges to the MST while ensuring no cycles are formed.
   - Stop when the MST contains exactly `n-1` edges.

---


This problem can be efficiently solved using MST algorithms like Prim's or Kruskal's. Both approaches ensure that the minimum cost to connect all points is computed in O((n^2) log n) time.
