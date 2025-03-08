# Add Two Numbers - Linked List

## Problem Statement
You are given two non-empty linked lists, `l1` and `l2`, where each represents a non-negative integer. The digits are stored in **reverse order**, meaning that the number 123 is represented as `3 -> 2 -> 1` in the linked list. Each node contains a single digit. You may assume that the two numbers do not contain any leading zero, except for the number 0 itself.

### Input
- `l1 = [1,2,3]`
- `l2 = [4,5,6]`

### Output
- `[5,7,9]`

### Explanation
The linked lists represent the numbers 321 and 654. When added together, they yield 975, which is represented as `5 -> 7 -> 9`.

### Example 2
- **Input:** `l1 = [9]`, `l2 = [9]`
- **Output:** `[8,1]`

### Constraints
- `1 <= l1.length, l2.length <= 100`
- `0 <= Node.val <= 9`

## Recommended Time & Space Complexity
Aim for a solution with **O(m + n)** time and **O(1)** space, where `m` is the length of list `l1` and `n` is the length of list `l2`.

## Solution Approach
To solve this problem, you can follow these steps:

1. Initialize a dummy node to help build the result linked list.
2. Use a pointer to traverse the linked lists.
3. Maintain a carry variable to handle sums greater than 9.
4. Iterate through both linked lists until you reach the end of both:
   - Add the values of the current nodes and the carry.
   - Create a new node with the digit value (sum % 10).
   - Update the carry (sum / 10).
5. If there's any carry left after the loop, add a new node with the carry value.
6. Return the next node of the dummy node as the head of the result linked list.
