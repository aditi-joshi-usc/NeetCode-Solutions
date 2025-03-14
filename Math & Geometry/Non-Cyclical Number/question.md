# Non-Cyclical Number

## Problem Statement

A non-cyclical number is defined by the following algorithm:  
Given a positive integer `n`, replace it with the sum of the squares of its digits.  
Repeat the process until the number equals 1, or it loops endlessly in a cycle that does not include 1.  
If the process stops at 1, then `n` is a non-cyclical number; otherwise, it is not.

Given a positive integer `n`, return `true` if it is a non-cyclical number, otherwise return `false`.

## Examples

- **Example 1:**
  - **Input:** `n = 100`
  - **Output:** `true`
  - **Explanation:**  
    `1^2 + 0^2 + 0^2 = 1`. Since we reach 1, the number is non-cyclical.

- **Example 2:**
  - **Input:** `n = 101`
  - **Output:** `false`
  - **Explanation:**  
    The sequence is:
    ```
    101  => 1^2 + 0^2 + 1^2 = 2
     2   => 2^2 = 4
     4   => 4^2 = 16
    16   => 1^2 + 6^2 = 37
    37   => 3^2 + 7^2 = 58
    58   => 5^2 + 8^2 = 89
    89   => 8^2 + 9^2 = 145
    145  => 1^2 + 4^2 + 5^2 = 42
    42   => 4^2 + 2^2 = 20
    20   => 2^2 + 0^2 = 4
    ```
    At this point, the number `4` has already appeared in the sequence, indicating a loop.  
    Thus, 101 is a cyclical number and the function should return `false`.

## Constraints

- `1 <= n <= 1000`
- The recommended time and space complexity is O(log(n)), where the number of digits in `n` is O(log(n)).

## Approach

We can solve this problem using an iterative approach with a set to detect cycles:
  
1. **Cycle Detection:**  
   Use a set to store numbers that have already been seen. If a number repeats, a cycle is detected, and we return `false`.

2. **Iterative Process:**  
   - Compute the sum of the squares of digits of `n`.
   - If the computed sum is `1`, return `true`.
   - Otherwise, add the current number to the set and update `n` to the computed sum.
  
3. **Termination:**  
   The process terminates either when `n` equals `1` or when a cycle (repeated number) is detected.

**Time Complexity Analysis:**
- Calculating the sum of the squares of the digits of `n` takes O(d) time, where `d` is the number of digits. Since `d = O(log(n))`, each iteration is O(log(n)).
- The number of iterations before termination is bounded (in practice, the sequence rapidly converges or cycles), so the overall time complexity is effectively O(log(n)).
- The space complexity is O(log(n)) due to storing the numbers seen in the cycle detection set.

## Python Implementation

```python
class Solution:
    def isNonCyclicalNumber(self, n: int) -> bool:
        def sum_of_squares(num: int) -> int:
            total = 0
            while num:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum_of_squares(n)
        return n == 1

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    n1 = 100
    print(solution.isNonCyclicalNumber(n1))  # Expected output: True
    
    # Example 2
    n2 = 101
    print(solution.isNonCyclicalNumber(n2))  # Expected output: False
