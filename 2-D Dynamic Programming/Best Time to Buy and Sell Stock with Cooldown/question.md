# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement

You are given an integer array `prices` where `prices[i]` is the price of NeetCoin on the ith day.

You may buy and sell one NeetCoin multiple times with the following restrictions:
- **Cooldown:** After you sell your NeetCoin, you cannot buy another one on the next day.
- **Single Holding:** You may only own at most one NeetCoin at a time.
- **Multiple Transactions:** You may complete as many transactions as you like.

Return the maximum profit you can achieve.

## Examples

### Example 1

- **Input:**  
  `prices = [1, 3, 4, 0, 4]`
- **Output:**  
  `6`
- **Explanation:**  
  - Buy on day 0 (price = 1) and sell on day 1 (price = 3) for a profit of `3 - 1 = 2`.  
  - Then buy on day 3 (price = 0) and sell on day 4 (price = 4) for a profit of `4 - 0 = 4`.  
  - Total profit = `2 + 4 = 6`.

### Example 2

- **Input:**  
  `prices = [1]`
- **Output:**  
  `0`

## Constraints

- `1 <= prices.length <= 5000`
- `0 <= prices[i] <= 1000`

## Recommended Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)  
  where `n` is the size of the input array.

## Approach

This problem can be solved using a dynamic programming approach with a state-machine model to capture the allowed transitions:

1. **States:**
   - **Hold:** Maximum profit on day `i` when you are holding a NeetCoin.
   - **Not Hold:** Maximum profit on day `i` when you are not holding a NeetCoin (this includes a cooldown if you sold on day `i-1`).

2. **Transitions:**
   - **Transition to `not_hold`:**  
     On day `i`, if you are not holding a coin, you can either:
     - Continue not holding from day `i-1`, or
     - Sell the coin you held on day `i-1`, earning a profit of `prices[i]`:
       ```
       not_hold[i] = max(not_hold[i - 1], hold[i - 1] + prices[i])
       ```
   - **Transition to `hold`:**  
     On day `i`, if you want to hold a coin, you can either:
     - Continue holding from day `i-1`, or
     - Buy today. If you buy today, you must have been in a state where you were not holding a coin two days ago (to respect the cooldown after selling):
       ```
       hold[i] = max(hold[i - 1], not_hold[i - 2] - prices[i])
       ```
       For the special case when `i == 1`, buying today compares directly with the first day's buy:
       ```
       hold = max(hold[0], -prices)
       ```

3. **Initialization:**
   - On day 0:
     - If you buy, `hold[0] = -prices[0]`.
     - You can't sell on day 0, so `not_hold[0] = 0`.

4. **Result:**
   - The answer is `not_hold[n - 1]`, because by the end of the period, the maximum profit is realized when you are not holding a coin.

## Python Code

```python
def maxProfit(prices):
    if not prices:
        return 0

    n = len(prices)
    # Initialize DP arrays with n elements:
    # hold[i]: Maximum profit on day i when holding a coin.
    # not_hold[i]: Maximum profit on day i when not holding a coin.
    hold = [0] * n
    not_hold = [0] * n
    
    # Day 0 initialization
    hold[0] = -prices[0]
    not_hold[0] = 0

    for i in range(1, n):
        # Compute not_hold[i]: either do nothing or sell the coin today.
        not_hold[i] = max(not_hold[i - 1], hold[i - 1] + prices[i])
        
        # Compute hold[i]:
        if i == 1:
            hold[i] = max(hold[i - 1], -prices[i])
        else:
            hold[i] = max(hold[i - 1], not_hold[i - 2] - prices[i])
    
    # Final profit is in not_hold[n - 1] as we should not be holding any coin at the end.
    return not_hold[-1]

# Sample Test Cases
if __name__ == "__main__":
    # Example 1:
    prices = [1, 3, 4, 0, 4]
    print("Maximum Profit:", maxProfit(prices))  # Expected Output: 6

    # Example 2:
    prices =
    print("Maximum Profit:", maxProfit(prices))  # Expected Output: 0
