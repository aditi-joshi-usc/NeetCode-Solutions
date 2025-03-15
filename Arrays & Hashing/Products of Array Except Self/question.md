# Products of Array Except Self

## Problem Statement

Given an integer array `nums`, return an array `output` where `output[i]` is the product of all the elements of `nums` except `nums[i]`. **Note:** You cannot use the division operation, and each product is guaranteed to fit in a 32-bit integer.

### Example 1

- **Input:** `nums = [1, 2, 4, 6]`
- **Output:** `[48, 24, 12, 8]`

### Example 2

- **Input:** `nums = [-1, 0, 1, 2, 3]`
- **Output:** `[0, -6, 0, 0, 0]`

### Constraints

- `2 <= nums.length <= 1000`
- `-20 <= nums[i] <= 20`

---

## Explanation

The idea is to compute the product of all numbers to the **left** and **right** of each index:

1. **Left Products:**  
   For each index `i`, compute the product of all the elements to the left of `i`.  
   - For index `0`, there are no elements to the left, so the left product is `1`.
   - For index `1`, the left product equals `nums[0]`.
   - For index `2`, the left product equals `nums[0] * nums[1]`.
   - And so on.

2. **Right Products:**  
   Similarly, compute the product of all the elements to the right of each index `i`.
   - For the last index, there are no elements to the right, so the right product is `1`.
   - For the second-last index, the right product equals `nums[last]`.
   - Continue backward accordingly.

By multiplying the left and right products for each index, you get the product of all elements except `nums[i]`.

This approach has:
- **Time Complexity:** O(n) (two passes through the array)
- **Space Complexity:** O(n) (for the output array)

---

## Python Code Implementation

```python
def product_except_self(nums):
    n = len(nums)
    output = * n

    # Compute the left products for each index.
    left = 1
    for i in range(n):
        output[i] = left
        left *= nums[i]
    
    # Compute right products while updating the output.
    right = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right
        right *= nums[i]
    
    return output

# Testing the function with provided examples
print(product_except_self([1, 2, 4, 6]))     # Expected output: [48, 24, 12, 8]
print(product_except_self([-1, 0, 1, 2, 3]))   # Expected output: [0, -6, 0, 0, 0]
