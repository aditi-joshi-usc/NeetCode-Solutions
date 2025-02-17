# Spiral Matrix

## Difficulty: Medium

## Problem Description
Given an `m x n` matrix of integers `matrix`, return a list of all elements within the matrix in *spiral order*.

## Examples

### Example 1:
```
Input: matrix = [[1,2],
                 [3,4]]
Output: [1,2,4,3]
```

### Example 2:
```
Input: matrix = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

### Example 3:
```
Input: matrix = [[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## Visual Example
For a 3×3 matrix, the spiral order looks like:
```
→ → →
    ↓
← ← ↓
↓   
→ →  
```

## Constraints
* `1 <= matrix.length, matrix[i].length <= 10`
* `-100 <= matrix[i][j] <= 100`
