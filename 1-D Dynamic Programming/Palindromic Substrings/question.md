# Palindromic Substrings

## Problem Statement
Given a string `s`, return the number of substrings within `s` that are palindromes.

A **palindrome** is a string that reads the same forward and backward.

### Examples

**Example 1:**
- **Input:**
  ```
  s = "abc"
  ```
**Output:**
```
3
```
**Explanation:**
The palindromic substrings are "a", "b", and "c".
**Example 2:**

**Input:**
```
s = "aaa"
```
**Output:**
```
6
```
**Explanation:**
The palindromic substrings are "a", "a", "a", "aa", "aa", and "aaa". Note that different substrings are counted as different palindromes even if the string contents are the same.
**Constraints**
```
1 <= s.length <= 1000
```
s consists of lowercase English letters.
Recommended Time & Space Complexity
Time Complexity: O(n²)
Space Complexity: O(1)
