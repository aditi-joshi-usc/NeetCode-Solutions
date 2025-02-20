# Set Matrix Zeroes

## Problem Statement

**Difficulty**: Medium

Given an `m x n` matrix of integers `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must update the matrix **in-place**.

**Follow up**: Could you solve it using `O(1)` space?

### Examples

**Example 1:**
```
Input: matrix = [
  [0,1],
  [1,0]
]

Output: [
  [0,0],
  [0,0]
]
```

**Example 2:**
```
Input: matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]

Output: [
  [1,0,3],
  [0,0,0],
  [6,0,8]
]
```

### Constraints:
- `1 <= matrix.length, matrix[0].length <= 100`
- `-2^31 <= matrix[i][j] <= (2^31) - 1`



## Key Insights

1. The challenge is to update the matrix in-place without using extra space.
2. Using the first row and column as markers is the key insight for the constant space solution.
3. We need to handle the first row and column separately to avoid losing information.
4. The time complexity remains O(m×n) because we need to visit each cell at least once.
