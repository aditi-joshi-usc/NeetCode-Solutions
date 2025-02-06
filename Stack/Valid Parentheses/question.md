# Valid Parentheses

## Problem Statement

You are given a string `s` consisting of the following characters: `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`.

The input string `s` is **valid** if and only if:

1. Every open bracket is closed by the same type of close bracket.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Return `true` if `s` is a valid string, and `false` otherwise.

---

## **Examples**

### Example 1:

**Input:**\
`s = "[]"`\
**Output:**\
`true`

### Example 2:

**Input:**\
`s = "([{}])"`\
**Output:**\
`true`

### Example 3:

**Input:**\
`s = "[(])"`\
**Output:**\
`false`\
**Explanation:** The brackets are not closed in the correct order.

---

## **Constraints**

- `1 <= s.length <= 1000`
- `s` consists only of `'(){}[]'` characters.

---

## **Solution Approach**

The problem can be solved using a **stack** data structure:

1. Push open brackets `(`, `{`, `[` onto a stack.
2. When encountering a closing bracket `)`, `}`, `]`:
   - Check if the stack is **not empty** and the top of the stack is the corresponding **matching** open bracket.
   - If yes, pop the stack.
   - If no, return `false`.
3. After processing the string, the stack should be **empty** for a valid string.


