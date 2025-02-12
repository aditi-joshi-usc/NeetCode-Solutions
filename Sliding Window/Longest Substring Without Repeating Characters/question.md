# Longest Substring Without Repeating Characters

## Problem Statement

Given a string `s`, find the length of the **longest substring** without duplicate characters.

A **substring** is a contiguous sequence of characters within a string.

## Examples

### Example 1
**Input:**  
`s = "zxyzxyz"`


**Output:**  
`3`

**Explanation:**  
The longest substring without duplicate characters is `"xyz"`, which has a length of `3`.

---

### Example 2
**Input:**  
`s = "xxxx"`

**Output:**  
`1`

**Explanation:**  
The longest substring without repeating characters is `"x"`, which has a length of `1`.

---

## Constraints
- `0 <= s.length <= 1000`
- `s` may consist of **printable ASCII characters**.

---

## Recommended Time & Space Complexity
- **Time Complexity**: O(n), where `n` is the length of the string.
- **Space Complexity**: O(m), where `m` is the number of unique characters in the string.
