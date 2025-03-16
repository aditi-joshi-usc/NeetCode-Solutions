# Coin Change II

## Problem Statement

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a target amount of money.

Return the number of distinct combinations that sum up to `amount`. If it is impossible to form the target amount using the coins, return `0`.

Assume that:
- You have an unlimited number of each coin.
- Each coin value in `coins` is unique.

## Examples

### Example 1
- **Input:**  
  `amount = 4`, `coins = [1, 2, 3]`
- **Output:**  
  `4`
- **Explanation:**  
  The combinations that sum up to 4 are:
  - `1 + 1 + 1 + 1 = 4`
  - `1 + 1 + 2 = 4`
  - `1 + 3 = 4`
  - `2 + 2 = 4`

### Example 2
- **Input:**  
  `amount = 7`, `coins = [2, 4]`
- **Output:**  
  `0`
- **Explanation:**  
  No combination of the given coins can sum up to 7.

## Constraints

- `1 <= coins.length <= 100`
- `1 <= coins[i] <= 1000`
- `0 <= amount <= 1000`

## Recommended Time & Space Complexity

- **Time Complexity:** O(n * amount) where n is the number of coins.
- **Space Complexity:** O(amount)

