# Find Minimum in Rotated Sorted Array

## Problem Statement
You are given an array of length `n` which was originally sorted in ascending order. It has now been rotated between `1` and `n` times. For example, the array `nums = [1,2,3,4,5,6]` might become:
- `[3,4,5,6,1,2]` if it was rotated 4 times.
- `[1,2,3,4,5,6]` if it was rotated 6 times.

Notice that rotating the array `k` times moves the last `k` elements of the array to the beginning. Rotating the array `n` times produces the original array.

Assuming all elements in the rotated sorted array `nums` are unique, return the **minimum element** of this array.

---

## Examples

### Example 1:
**Input:**  
`nums = [3,4,5,6,1,2]`  

**Output:**  
`1`  

**Explanation:**  
The array is rotated 4 times, and the minimum element is `1`.

---

### Example 2:
**Input:**  
`nums = [4,5,0,1,2,3]`  

**Output:**  
`0`  

**Explanation:**  
The array is rotated 2 times, and the minimum element is `0`.

---

### Example 3:
**Input:**  
`nums = [4,5,6,7]`  

**Output:**  
`4`  

**Explanation:**  
The array is not rotated, so the minimum element is the first element, `4`.

---

## Constraints
- `1 <= nums.length <= 1000`
- `-1000 <= nums[i] <= 1000`
- All elements in `nums` are unique.

---

## Recommended Time & Space Complexity
- **Time Complexity:** O(log n), where `n` is the size of the input array.
- **Space Complexity:** O(1)

---
