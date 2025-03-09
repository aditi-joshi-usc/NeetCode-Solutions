# Permutations

## Problem Statement

Given an array `nums` of unique integers, return all the possible permutations. You may return the answer in any order.

### Examples

- **Example 1**:
  - **Input**: `nums = [1,2,3]`
  - **Output**: `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

- **Example 2**:
  - **Input**: `nums = [7]`
  - **Output**: `[[7]]`

### Constraints

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`

## Recommended Time & Space Complexity

You should aim for a solution with **O(n * n!)** time and **O(n)** space, where `n` is the size of the input array.
