# Coin Change Problem

## Problem Statement

You are given an integer array `coins` representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc.) and an integer `amount` representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return `-1`.

**Examples:**

1. **Example 1:**
    - **Input:** `coins = [1, 5, 10]`, `amount = 12`
    - **Output:** `3`
    - **Explanation:** `12 = 10 + 1 + 1`

2. **Example 2:**
    - **Input:** `coins = [2]`, `amount = 3`
    - **Output:** `-1`
    - **Explanation:** The amount of `3` cannot be made up with coins of `2`.

3. **Example 3:**
    - **Input:** `coins = [1]`, `amount = 0`
    - **Output:** `0`
    - **Explanation:** Choosing `0` coins is a valid way to make up `0`.


**Time Complexity:** O(n * t) where `n` is the number of coins and `t` is the target amount.  
**Space Complexity:** O(t)
