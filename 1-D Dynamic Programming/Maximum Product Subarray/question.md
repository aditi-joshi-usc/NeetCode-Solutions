# Maximum Product Subarray

## Problem Statement

Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product, and return that product.

- A subarray is a contiguous sequence of elements within the array.
- The output is guaranteed to fit into a 32-bit integer.

**Examples:**

1. **Example 1:**
   - **Input:** `nums = [1, 2, -3, 4]`
   - **Output:** `4`  
     **Explanation:** The subarray with the largest product is `[4]`.

2. **Example 2:**
   - **Input:** `nums = [-2, -1]`
   - **Output:** `2`  
     **Explanation:** The subarray with the largest product is `[-2, -1]` because `-2 * -1 = 2`.

## Constraints

- `1 <= nums.length <= 1000`
- `-10 <= nums[i] <= 10`

## Approach: Dynamic Programming

### Key Concept

The challenge with this problem is handling negative numbers. A negative number can flip the maximum product to a minimum and vice versa. Thus, we keep track of:

- **`curMax`**: The maximum product ending at the current index.
- **`curMin`**: The minimum product ending at the current index.

At each step and for each number, we calculate the new `curMax` and `curMin` by considering three cases:
- Taking the current number alone.
- Multiplying the current number with the previous `curMax`.
- Multiplying the current number with the previous `curMin`.

### Algorithm Steps

1. **Initialization:**
   - Initialize `res`, `curMax`, and `curMin` with the first element of the array.
  
2. **Iteration:**
   - Loop through the array starting from the second element.
   - If the current number is negative, swap `curMax` and `curMin` (since multiplying by a negative inverts the values).
   - Update `curMax` as the maximum between:
     - The current number.
     - The product of the current number and `curMax`.
   - Update `curMin` as the minimum between:
     - The current number.
     - The product of the current number and `curMin`.
   - Update the global result `res` with the maximum of itself and `curMax`.

3. **Return the Result:**
   - After iterating through all elements, return `res` as the answer.

## Python Implementation

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize the result as well as current max and min with the first element.
        res = nums[0]
        curMax, curMin = nums[0], nums[0]
        
        # Iterate over the array starting from the second element.
        for num in nums[1:]:
            # If the current number is negative, swapping curMax and curMin is needed.
            if num < 0:
                curMax, curMin = curMin, curMax
            
            # Calculate the maximum and minimum product ending at this index.
            curMax = max(num, curMax * num)
            curMin = min(num, curMin * num)
            
            # Update the global maximum product.
            res = max(res, curMax)
            
        return res

# Example test cases
if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([1, 2, -3, 4]))  # Expected output: 4
    print(s.maxProduct([-2, -1]))       # Expected output: 2
