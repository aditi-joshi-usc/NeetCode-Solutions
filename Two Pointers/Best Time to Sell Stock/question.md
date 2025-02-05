# Best Time to Buy and Sell Stock

## Problem Statement

You are given an integer array `prices` where `prices[i]` represents the price of **NeetCoin** on the `i`th day.

You may choose **a single day** to **buy** one NeetCoin and **a different future day** to **sell** it.

Return the **maximum profit** you can achieve. If no profitable transaction is possible, return `0`.

## Examples

### Example 1:
**Input:**  
`prices = [10,1,5,6,7,1]`

**Output:**  
`6`

**Explanation:**  
Buy on `prices[1] = 1` and sell on `prices[4] = 7`, yielding a profit of `7 - 1 = 6`.

---

### Example 2:
**Input:**  
`prices = [10,8,7,5,2]`

**Output:**  
`0`

**Explanation:**  
No profitable transactions can be made, so the maximum profit is `0`.

## Constraints
- `1 <= prices.length <= 100`
- `0 <= prices[i] <= 100`
