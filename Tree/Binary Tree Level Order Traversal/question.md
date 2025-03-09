# Binary Tree Level Order Traversal

## Problem Statement

Given a binary tree `root`, return the **level order traversal** of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

### Examples

**Example 1:**

- **Input:** 
  - `root = [1,2,3,4,5,6,7]`
- **Output:** `[[1],[2,3],[4,5,6,7]]`

**Example 2:**

- **Input:** 
  - `root = [1]`
- **Output:** `[[1]]`

**Example 3:**

- **Input:** 
  - `root = []`
- **Output:** `[]`

## Constraints

- `0 <= The number of nodes in both trees <= 1000`
- `-1000 <= Node.val <= 1000`

## Recommended Time & Space Complexity

Aim for a solution with **O(n)** time and **O(n)** space, where `n` is the number of nodes in the given tree.

