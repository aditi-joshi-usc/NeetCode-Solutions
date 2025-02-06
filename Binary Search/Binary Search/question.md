# Binary Search Solution

## Problem Statement
You are given an array of distinct integers `nums`, sorted in ascending order, and an integer `target`.

Implement a function to search for `target` within `nums`. If it exists, then return its index; otherwise, return `-1`.

Your solution must run in **O(log n)** time.

### Example 1:
**Input:**
```python
nums = [-1, 0, 2, 4, 6, 8]
target = 4
```
**Output:**
```python
3
```

### Example 2:
**Input:**
```python
nums = [-1, 0, 2, 4, 6, 8]
target = 3
```
**Output:**
```python
-1
```

### Constraints:
- `1 <= nums.length <= 10000`
- `-10000 < nums[i], target < 10000`

---

## Solution
We can use **Binary Search** since the array is already sorted. Binary Search works by repeatedly dividing the search space in half until the target value is found or the space is empty. The time complexity is **O(log n)**.

### Implementation:
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example Usage
nums = [-1, 0, 2, 4, 6, 8]
target = 4
print(binary_search(nums, target))  # Output: 3

target = 3
print(binary_search(nums, target))  # Output: -1
```

---

## Explanation:
1. **Initialize Pointers:** Set `left` at index `0` and `right` at the last index.
2. **Loop Until Search Space is Empty:** While `left <= right`:
   - Calculate `mid = left + (right - left) // 2` to avoid integer overflow.
   - If `nums[mid] == target`, return `mid` (found target).
   - If `nums[mid] < target`, shift `left` to `mid + 1` (search right half).
   - If `nums[mid] > target`, shift `right` to `mid - 1` (search left half).
3. **Return -1:** If the target is not found, return `-1`.

---

### Time Complexity:
- **Best Case:** `O(1)` (Target is at the middle index)
- **Worst/Average Case:** `O(log n)` (Halving the search space in each step)

### Space Complexity:
- **O(1)** (Uses constant extra space)

---

## Edge Cases Considered:
- Single-element arrays.
- Target is smaller or larger than all elements.
- Target is the first, middle, or last element.
- Large input sizes up to `10000` elements.

This implementation ensures an efficient search in logarithmic time complexity.
