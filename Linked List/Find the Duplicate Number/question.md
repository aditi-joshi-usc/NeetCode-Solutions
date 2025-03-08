# Find the Duplicate Number

## Problem Statement
You are given an array of integers `nums` containing `n + 1` integers. Each integer in `nums` is in the range `[1, n]` inclusive. Every integer appears exactly once, except for one integer which appears two or more times. Your task is to return the integer that appears more than once.

### Example 1
- **Input:** `nums = [1,2,3,2,2]`
- **Output:** `2`

### Example 2
- **Input:** `nums = [1,2,3,4,4]`
- **Output:** `4`

## Constraints
- `1 <= n <= 10000`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`

## Follow-up
Can you solve the problem without modifying the array `nums` and using **O(1)** extra space?

## Recommended Time & Space Complexity
Aim for a solution with **O(n)** time and **O(1)** space, where `n` is the size of the input array.

## Solution Approach
To solve this problem efficiently, you can use the **Floyd's Tortoise and Hare (Cycle Detection)** algorithm. This approach leverages the fact that the numbers in the array can be treated as pointers to the next index, creating a cycle due to the duplicate number.

### Steps:
1. **Initialization**: Start with two pointers, `tortoise` and `hare`. The `tortoise` moves one step at a time, while the `hare` moves two steps at a time.
2. **Finding the Intersection**: Move both pointers until they meet. This meeting point indicates that a cycle exists.
3. **Finding the Entrance to the Cycle**: Reset one pointer to the start of the array and move both pointers one step at a time until they meet again. The meeting point will be the duplicate number.

## Example Code
Here is a sample implementation in Python:

```python
def findDuplicate(nums):
    # Step 1: Finding the intersection point
    tortoise = nums[0]
    hare = nums[0]
    
    while True:
        tortoise = nums[tortoise]  # Move tortoise by 1 step
        hare = nums[nums[hare]]    # Move hare by 2 steps
        if tortoise == hare:
            break

    # Step 2: Finding the entrance to the cycle
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare
