# Kth Largest Element in a Stream

## Problem Statement

Design a class to find the kth largest integer in a stream of values, including duplicates. For example, the 2nd largest from `[1, 2, 3, 3]` is `3`. The stream is not necessarily sorted.

### Implement the following methods:

- `constructor(int k, int[] nums)`: Initializes the object given an integer `k` and the stream of integers `nums`.
- `int add(int val)`: Adds the integer `val` to the stream and returns the kth largest integer in the stream.

### Example:

#### Input:
```python
["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]
```

#### Output:
```python
[null, 3, 3, 3, 5, 6]
```

#### Explanation:
```python
KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);
kthLargest.add(3);   # return 3
kthLargest.add(5);   # return 3
kthLargest.add(6);   # return 3
kthLargest.add(7);   # return 5
kthLargest.add(8);   # return 6
```

### Constraints:

- `1 <= k <= 1000`
- `0 <= nums.length <= 1000`
- `-1000 <= nums[i] <= 1000`
- `-1000 <= val <= 1000`
- There will always be at least `k` integers in the stream when you search for the `k`th integer.

### Recommended Time & Space Complexity

You should aim for a solution with `O(mlogk)` time and `O(k)` space, where `m` is the number of times `add()` is called, and `k` represents the rank of the largest number to be tracked (i.e., the `k`-th largest element).
