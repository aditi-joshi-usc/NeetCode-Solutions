# Kth Largest Element in an Array

## Problem Statement

Given an unsorted array of integers `nums` and an integer `k`, return the **kth largest element** in the array. By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

### Examples

- **Example 1**:
  - **Input**: `nums = [2, 3, 1, 5, 4], k = 2`
  - **Output**: `4`

- **Example 2**:
  - **Input**: `nums = [2, 3, 1, 1, 5, 5, 4], k = 3`
  - **Output**: `4`

### Constraints

- `1 <= k <= nums.length <= 10000`
- `-1000 <= nums[i] <= 1000`

## Recommended Time & Space Complexity

You should aim for a solution as good or better than **O(n log k)** time and **O(k)** space, where `n` is the size of the input array, and `k` represents the rank of the largest number to be returned (i.e., the k-th largest element).

## Follow-up

Can you solve it without sorting? 

### Possible Approaches

1. **Sorting**: Sort the array and return the element at the index `len(nums) - k`.
2. **Min-Heap**: Use a min-heap of size `k` to keep track of the k largest elements.
3. **Quickselect Algorithm**: Use the Quickselect algorithm to find the kth largest element in average O(n) time.

Feel free to choose the approach that best fits your needs!
