# Number of Connected Components in an Undirected Graph

## Problem Statement
You are given an undirected graph with `n` nodes, where the nodes are numbered from `0` to `n - 1`. The edges of the graph are represented as an array, where `edges[i] = [a, b]` indicates that there is an edge between node `a` and node `b`. Your task is to return the total number of connected components in the graph.

### Examples
**Example 1:**
- **Input:**
  ```python
  n = 3
  edges = [[0, 1], [0, 2]]
**Output:**
```
1
```
**Example 2:**
Input:
```
n = 6
edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
```
**Output:**
```
2
```
## Constraints
```
1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
```
