# Max Area of Island

## Problem Statement
You are given a matrix `grid` where `grid[i]` is either a `0` (representing water) or `1` (representing land).

An **island** is defined as a group of `1's` connected **horizontally** or **vertically**. You may assume all four edges of the grid are surrounded by water.

The **area of an island** is defined as the number of cells within the island.

Return the **maximum area of an island** in `grid`. If no island exists, return `0`.

---

## Example 1

### **Input:**
```plaintext
grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]
```

### **Output:**
```plaintext
6
```

### **Explanation:**
`1's` cannot be connected diagonally, so the maximum area of the island is `6`.

---

## **Constraints:**
- `1 <= grid.length, grid[i].length <= 50`

---

## **Recommended Time & Space Complexity**
You should aim for a solution with:
- **O(m * n)** time complexity, where `m` is the number of rows and `n` is the number of columns in the grid.
- **O(m * n)** space complexity.

