# Search in Rotated Sorted Array

## Problem Statement
You are given an array of length `n` which was originally sorted in ascending order. It has now been rotated between `1` and `n` times. For example, the array `nums = [1,2,3,4,5,6]` might become:
- `[3,4,5,6,1,2]` if it was rotated 4 times.
- `[1,2,3,4,5,6]` if it was rotated 6 times.

Given the rotated sorted array `nums` and an integer `target`, return the **index** of `target` within `nums`, or `-1` if it is not present.

You may assume all elements in the rotated sorted array `nums` are unique.

---

## Examples

### Example 1:
**Input:**  
`nums = [3,4,5,6,1,2]`, `target = 1`  

**Output:**  
`4`  

**Explanation:**  
The target `1` is located at index `4`.

---

### Example 2:
**Input:**  
`nums = [3,5,6,0,1,2]`, `target = 4`  

**Output:**  
`-1`  

**Explanation:**  
The target `4` is not present in the array.

---

### Example 3:
**Input:**  
`nums = [4,5,6,7,0,1,2]`, `target = 0`  

**Output:**  
`4`  

**Explanation:**  
The target `0` is located at index `4`.

---

## Constraints
- `1 <= nums.length <= 1000`
- `-1000 <= nums[i] <= 1000`
- `-1000 <= target <= 1000`
- All elements in `nums` are unique.

---

## Recommended Time & Space Complexity
- **Time Complexity:** O(log n), where `n` is the size of the input array.
- **Space Complexity:** O(1)

---

## Solution

### Approach
To solve this problem in O(log n) time, we can use a **modified binary search**:
1. The array is divided into two parts: one part is sorted, and the other contains the rotation point.
2. Use binary search to determine which part of the array to search for the target:
   - Compare the middle element with the leftmost and rightmost elements to identify the sorted part.
   - Check if the target lies within the sorted part. If it does, narrow the search to that part.
   - Otherwise, search in the other part.
3. Continue narrowing down the range until the target is found or the search space is empty.

---

### Algorithm
1. Initialize two pointers: `left = 0` and `right = len(nums) - 1`.
2. While `left <= right`:
   - Calculate the middle index: `mid = left + (right - left) // 2`.
   - If `nums[mid] == target`, return `mid`.
   - Determine which part of the array is sorted:
     - If `nums[left] <= nums[mid]`, the left part is sorted:
       - If `target` lies within the range `[nums[left], nums[mid]]`, narrow the search to the left part by setting `right = mid - 1`.
       - Otherwise, search in the right part by setting `left = mid + 1`.
     - Otherwise, the right part is sorted:
       - If `target` lies within the range `[nums[mid], nums[right]]`, narrow the search to the right part by setting `left = mid + 1`.
       - Otherwise, search in the left part by setting `right = mid - 1`.
3. If the loop ends without finding the target, return `-1`.

---
