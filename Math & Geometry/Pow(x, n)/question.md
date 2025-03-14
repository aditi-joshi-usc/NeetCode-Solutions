# Pow(x, n)

## Problem Description

Implement the function `myPow(x, n)` that calculates `x` raised to the power `n` (i.e., x^n) for a given floating-point number `x` and an integer `n`. **Do not use any built-in library functions** for exponentiation.

---

## Examples

### Example 1

**Input:**  
```
x = 2.00000, n = 5
```



**Output:**  
```
32.00000
```



**Explanation:**  
2.00000 raised to the power of 5 equals 32.00000.

---

### Example 2

**Input:**  
```
x = 1.10000, n = 10
```



**Output:**  
```
2.59374
```


---

### Example 3

**Input:**  
```
x = 2.00000, n = -3
```


**Output:**  
```
0.12500
```



---

## Constraints

- `-100.0 < x < 100.0`
- `-1000 <= n <= 1000`
- `n` is an integer.
- If `x = 0`, then `n` will be positive.

---

## Recommended Time & Space Complexity

- **Time Complexity:** O(log n)
- **Space Complexity:** O(log n)
