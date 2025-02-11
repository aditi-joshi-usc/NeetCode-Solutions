# Maximum Subarray (Kadane's Algorithm)

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return *its sum*.

---

## Problem Statement

- **Input**: An array of integers `nums`.
- **Output**: The maximum sum of a contiguous subarray in `nums`.
- **Constraints**:
  - \( 1 \le \text{nums.length} \le 1000 \)
  - \(-1000 \le \text{nums}[i] \le 1000\)

---

## Examples

### Example 1

- **Input**: `nums = [2, -3, 4, -2, 2, 1, -1, 4]`
- **Output**: `8`
- **Explanation**: The subarray `[4, -2, 2, 1, -1, 4]` has the largest sum of `8`.

### Example 2

- **Input**: `nums = [-1]`
- **Output**: `-1`
- **Explanation**: The array has only one element, so the subarray is `[-1]` with sum `-1`.

---

## DP Code for reference

```python
class Solution:
    def maxSubArray(self, nums):
        dp = [*nums]  # Copy the original list into dp
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        return max(dp)
