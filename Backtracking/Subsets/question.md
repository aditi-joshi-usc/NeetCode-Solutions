# Subsets

## Problem Statement

Given an array `nums` of unique integers, return all possible subsets of `nums`.

The solution set must not contain duplicate subsets. You may return the solution in any order.

### Example 1:

**Input:**
```plaintext
nums = [1,2,3]
```

**Output:**
```plaintext
[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

### Example 2:

**Input:**
```plaintext
nums = [7]
```

**Output:**
```plaintext
[[],[7]]
```

### Constraints:
- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`

### Recommended Time & Space Complexity
You should aim for a solution with `O(n * (2^n))` time and `O(n)` space, where `n` is the size of the input array.

