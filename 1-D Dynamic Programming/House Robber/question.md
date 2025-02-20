# House Robber

## Difficulty: Medium

You are given an integer array `nums` where `nums[i]` represents the amount of money the `i`th house has. The houses are arranged in a straight line, i.e. the `i`th house is the neighbor of the `(i-1)`th and `(i+1)`th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were **both** broken into.

Return the **maximum** amount of money you can rob without alerting the police.

## Example 1:

```
Input: nums = [1,1,3,3]
Output: 4
Explanation: nums[0] + nums[2] = 1 + 3 = 4.
```

## Example 2:

```
Input: nums = [2,9,8,3,6]
Output: 16
Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.
```

## Constraints:
* `1 <= nums.length <= 100`
* `0 <= nums[i] <= 100`

## Recommended Time & Space Complexity
You should aim for a solution as good or better than `O(n)` time and `O(n)` space, where `n` is the number of houses.

## Hints:
1. Think about using dynamic programming to solve this problem
2. Define a state that represents the maximum amount you can rob up to the current house
3. Consider the two options at each house: rob it or skip it
4. Your recurrence relation should consider the maximum between robbing the current house (plus the maximum amount from two houses ago) and skipping the current house (taking the maximum amount from the previous house)
