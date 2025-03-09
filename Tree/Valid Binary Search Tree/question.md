# Valid Binary Search Tree

## Problem Statement
Given the root of a binary tree, return **true** if it is a valid binary search tree (BST), otherwise return **false**.

A valid binary search tree satisfies the following constraints:
- The left subtree of every node contains only nodes with keys **less than** the node's key.
- The right subtree of every node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees are also binary search trees.

---

## Examples

### Example 1:
**Input:**  
`root = [2,1,3]`  

**Output:**  
`true`

---

### Example 2:
**Input:**  
`root = [1,2,3]`  

**Output:**  
`false`  

**Explanation:**  
The root node's value is 1, but its left child's value is 2, which is greater than 1.

---

## Constraints
- `1 <= The number of nodes in the tree <= 1000`
- `-1000 <= Node.val <= 1000`

---

## Recommended Time & Space Complexity
You should aim for a solution with:
- **O(n)** time complexity
- **O(n)** space complexity,  
where **n** is the number of nodes in the given tree.
