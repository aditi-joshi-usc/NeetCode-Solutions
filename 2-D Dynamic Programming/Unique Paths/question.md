# Unique Paths

## Difficulty: Medium

## Problem Description
There is an `m x n` grid where you are allowed to move either down or to the right at any point in time.

Given the two integers `m` and `n`, return the number of possible unique paths that can be taken from the top-left corner of the grid (`grid[0][0]`) to the bottom-right corner (`grid[m - 1][n - 1]`).

You may assume the output will fit in a 32-bit integer.

## Examples

### Example 1:
```
Input: m = 3, n = 6
Output: 21
```

### Example 2:
```
Input: m = 3, n = 3
Output: 6
```

## Visual Example
For m = 3, n = 3:
```
[S][ ][ ]
[ ][ ][ ]
[ ][ ][E]
```
Where:
- S: Starting point (top-left)
- E: Ending point (bottom-right)
- You can only move down or right at each step

## Constraints
* `1 <= m, n <= 100`

