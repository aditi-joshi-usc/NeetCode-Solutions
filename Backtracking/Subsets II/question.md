# Subsets II

## Problem Statement

You are given an array `nums` of integers, which may contain duplicates. Return all possible subsets.

The solution must not contain duplicate subsets. You may return the solution in any order.

### Examples

- **Example 1**:
  - **Input**: `nums = [1,2,1]`
  - **Output**: `[[],[1],[1,2],[1,1],[1,2,1],[2]]`

- **Example 2**:
  - **Input**: `nums = [7,7]`
  - **Output**: `[[],[7], [7,7]]`

### Constraints

- `1 <= nums.length <= 11`
- `-20 <= nums[i] <= 20`

## Recommended Time & Space Complexity

You should aim for a solution as good or better than **O(n * (2^n))** time and **O(n)** space, where `n` is the size of the input array.
