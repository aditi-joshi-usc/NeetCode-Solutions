# Single Number Problem

## Problem Statement
You are given a non-empty array of integers `nums`. Every integer appears twice except for one.

Return the integer that appears only once.

You must implement a solution with **O(n)** runtime complexity and use only **O(1)** extra space.

## Example 1:
**Input:**
```python
nums = [3,2,3]
```
**Output:**
```python
2
```

## Example 2:
**Input:**
```python
nums = [7,6,6,7,8]
```
**Output:**
```python
8
```

## Constraints:
- `1 <= nums.length <= 10000`
- `-10000 <= nums[i] <= 10000`

---

# Climbing Stairs Problem

## Problem Statement
You are given an integer `n` representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

## Example 1:
**Input:**
```python
n = 2
```
**Output:**
```python
2
```
**Explanation:**
```
1 + 1 = 2
2 = 2
```

## Example 2:
**Input:**
```python
n = 3
```
**Output:**
```python
3
```
**Explanation:**
```
1 + 1 + 1 = 3
1 + 2 = 3
2 + 1 = 3
```

## Constraints:
- `1 <= n <= 30`

## Recommended Time & Space Complexity
You should aim for a solution as good or better than **O(n)** time and **O(n)** space, where `n` is the number of steps.

