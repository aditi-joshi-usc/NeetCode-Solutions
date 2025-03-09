# Lowest Common Ancestor in Binary Search Tree

## Problem Statement

Given a binary search tree (BST) where all node values are unique, and two nodes from the tree `p` and `q`, return the **lowest common ancestor (LCA)** of the two nodes. The lowest common ancestor between two nodes `p` and `q` is the lowest node in a tree `T` such that both `p` and `q` are descendants. The ancestor is allowed to be a descendant of itself.

### Examples

**Example 1:**

- **Input:** 
  - `root = [5,3,8,1,4,7,9,null,2]`
  - `p = 3`
  - `q = 8`
- **Output:** `5`

**Example 2:**

- **Input:** 
  - `root = [5,3,8,1,4,7,9,null,2]`
  - `p = 3`
  - `q = 4`
- **Output:** `3`
- **Explanation:** The LCA of nodes `3` and `4` is `3`, since a node can be a descendant of itself.

## Constraints

- `2 <= The number of nodes in the tree <= 100`
- `-100 <= Node.val <= 100`
- `p != q`
- `p` and `q` will both exist in the BST.

## Recommended Time & Space Complexity

Aim for a solution as good or better than **O(h)** time and **O(h)** space, where `h` is the height of the given tree.

## Solution Approach

### Properties of BST

In a binary search tree, for any given node:
- All values in the left subtree are less than the node's value.
- All values in the right subtree are greater than the node's value.

### Algorithm

1. Start from the root of the BST.
2. Compare the values of `p` and `q` with the current node's value:
   - If both `p` and `q` are less than the current node, move to the left child.
   - If both `p` and `q` are greater than the current node, move to the right child.
   - If one of `p` or `q` is equal to the current node, or if `p` is on one side and `q` is on the other, then the current node is the LCA.

### Python Code Example

Here is a Python implementation of the above approach:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
