# Linked List Cycle Detection

## Problem Statement

Given the head of a **singly linked list**, return `true` if there is a **cycle** in the linked list. Otherwise, return `false`.

A **cycle** exists if at least one node in the list can be visited **again** by following the `next` pointer.

### Cycle Formation:
- If `index >= 0`, the **tail node** connects to the `index-th` node (creating a cycle).
- If `index == -1`, the **tail node** points to `null` (no cycle).

> **Note:** The `index` value is **not provided as input**.

---

## Constraints

- `1 <= Length of the list <= 1000`
- `-1000 <= Node.val <= 1000`
- `index` is either `-1` or a **valid index** in the linked list.

---

## Example 1

**Input:**  
```
head = [1, 2, 3, 4], index = 1
```
Output:

```
true
```
Explanation:

The tail node connects to the 1st node (0-indexed), forming a cycle.
Example 2
Input:

```
head = [1, 2], index = -1
```
Output:

```

false
```
Explanation:

The tail node points to null, meaning no cycle exists.
