# Search a 2D Matrix

## Problem Statement

You are given an `m x n` **2-D integer array** `matrix` and an **integer** `target`.

- Each **row** in `matrix` is **sorted in non-decreasing order**.
- The **first integer** of every row is **greater** than the **last integer** of the previous row.

Return `true` if `target` **exists** within `matrix`, otherwise return `false`.

### Expected Time Complexity:
- **O(log(m * n))**

### Expected Space Complexity:
- **O(1)**

---

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10000 <= matrix[i][j], target <= 10000`

---

## Example 1

**Input:**
```
matrix = [
  [1, 2, 4, 8],
  [10, 11, 12, 13],
  [14, 20, 30, 40]
]
target = 10
Output:


true
```
`Explanation:

10 exists in the matrix.`
Example 2
Input:

```
matrix = [
  [1, 2, 4, 8],
  [10, 11, 12, 13],
  [14, 20, 30, 40]
]

target = 15
```
Output:
```
false
```
`Explanation:

15 does not exist in the matrix.`
