# Plus One

## Problem Description

You are given an integer array `digits`, where each `digits[i]` is the `i-th` digit of a large integer. The digits are ordered from most significant to least significant, and the number does not contain any leading zeroes.

Your task is to increment this large integer by one and return the resulting array of digits.

---

## Examples

### Example 1

**Input:**
```
digits = [1, 2, 3, 4]
```



**Output:**
```
[1, 2, 3, 5]
```



**Explanation:**
The number represented by the array is 1234. After adding one, the new number is 1235, which is represented by `[1, 2, 3, 5]`.

---

### Example 2

**Input:**
```
digits = [9, 9, 9]
```


**Output:**
```
[1, 0, 0, 0]
```



**Explanation:**
The number represented by the array is 999. After adding one, the new number is 1000, which is represented by `[1, 0, 0, 0]`.

---

## Constraints

- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`

---

## Complexity Analysis

- **Time Complexity:** O(n), where n is the number of digits.
- **Space Complexity:** O(n)

---

## Additional Details

This problem simulates the behavior of an odometer or a digital counter. When a digit reaches `9` and is incremented, it becomes `0` and causes a carry to the next significant digit. This process continues until no further carry is needed or all digits have been processed.
