# Evaluate Reverse Polish Notation

## Problem Statement

You are given an array of strings `tokens` that represents a valid arithmetic expression in **Reverse Polish Notation (RPN)**.

Return the integer result of evaluating the expression.

- The operands may be integers or the results of other operations.
- The valid operators are `"+"`, `"-"`, `"*"`, and `"/"`.
- Assume that **division between integers always truncates toward zero**.

---

## Examples

### Example 1
**Input:**  
`tokens = ["1", "2", "+", "3", "*", "4", "-"]`

**Output:**  
`5`
**Explanation:**  
The expression evaluates as:
`((1 + 2) * 3) - 4 = 5`

---

## Constraints
- `1 <= tokens.length <= 1000`
- Each `tokens[i]` is one of the following:
  - `"+"`, `"-"`, `"*"`, `"/"`
  - A **string representation** of an integer in the range `[-100, 100]`.

---

## Recommended Time & Space Complexity
- **Time Complexity**: O(n), where `n` is the size of the input array.
- **Space Complexity**: O(n), as we use a stack to evaluate the expression.
