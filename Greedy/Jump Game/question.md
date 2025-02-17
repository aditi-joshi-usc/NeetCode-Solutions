# Jump Game

## Difficulty: Medium

## Problem Description
You are given an integer array `nums` where each element `nums[i]` indicates your maximum jump length at that position.

Return `true` if you can reach the last index starting from index `0`, or `false` otherwise.

## Examples

### Example 1:
```
Input: nums = [1,2,0,1,0]
Output: true
```
**Explanation:** First jump from index 0 to 1, then from index 1 to 3, and lastly from index 3 to 4.

### Example 2:
```
Input: nums = [1,2,1,0,1]
Output: false
```

## Visual Example
For nums = [1,2,0,1,0]:
```
[1]-→[2]→[0]→[1]→[0]
 0   1  2   3   4
```
Where:
- At index 0: Can jump max 1 step
- At index 1: Can jump max 2 steps
- At index 2: Can't jump (0 steps)
- At index 3: Can jump max 1 step
- At index 4: Reached destination

## Constraints
* `1 <= nums.length <= 1000`
* `0 <= nums[i] <= 1000`
