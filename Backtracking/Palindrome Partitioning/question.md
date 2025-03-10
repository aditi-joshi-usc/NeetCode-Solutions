# Palindrome Partitioning

## Problem Statement

Given a string `s`, split `s` into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

You may return the solution in any order.

### Examples

- **Example 1**:
  - **Input**: `s = "aab"`
  - **Output**: `[["a","a","b"],["aa","b"]]`

- **Example 2**:
  - **Input**: `s = "a"`
  - **Output**: `[["a"]]`

### Constraints

- `1 <= s.length <= 20`
- `s` contains only lowercase English letters.

## Recommended Time & Space Complexity

You should aim for a solution with **O(n * (2^n))** time and **O(n)** space, where `n` is the length of the input string.
