# Merge Two Sorted Linked Lists

Given the heads of two sorted linked lists `list1` and `list2`, merge the two lists into one sorted linked list and return the head of the new list. The new list should be made by splicing together the nodes of the first two lists.

---

## Problem Statement

- We have two singly linked lists, `list1` and `list2`. 
- Both lists are individually sorted in non-decreasing order.
- Our task is to merge them into one single linked list (also sorted in non-decreasing order).
- The resulting list should be composed of the original nodes from both lists.

### Examples

1. **Example 1**

    - **Input**: `list1 = [1, 2, 4]`, `list2 = [1, 3, 5]`
    - **Output**: `[1, 1, 2, 3, 4, 5]`

2. **Example 2**

    - **Input**: `list1 = []`, `list2 = [1, 2]`
    - **Output**: `[1, 2]`

3. **Example 3**

    - **Input**: `list1 = []`, `list2 = []`
    - **Output**: `[]`

---

## Constraints

- Let `n` be the length of `list1` and `m` be the length of `list2`.
- `0 <= n, m <= 100`
- `-100 <= Node.val <= 100`
- Time Complexity: `O(n + m)`
- Space Complexity: `O(1)` (we just manipulate the pointers of the existing lists)

---

