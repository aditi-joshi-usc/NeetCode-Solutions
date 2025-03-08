# Subtree of Another Tree

## Problem Statement
Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values as `subRoot`, and `false` otherwise. A subtree of a binary tree consists of a node in the tree and all of this node's descendants. The tree can also be considered as a subtree of itself.

### Example 1
- **Input:** `root = [1,2,3,4,5]`, `subRoot = [2,4,5]`
- **Output:** `true`

### Example 2
- **Input:** `root = [1,2,3,4,5,null,null,6]`, `subRoot = [2,4,5]`
- **Output:** `false`

## Constraints
- `0 <= The number of nodes in both trees <= 100`
- `-100 <= root.val, subRoot.val <= 100`

## Recommended Time & Space Complexity
Aim for a solution with **O(m * n)** time and **O(m + n)** space, where `n` and `m` are the number of nodes in `root` and `subRoot`, respectively.

## Solution Approach
To determine if `subRoot` is a subtree of `root`, you can follow these steps:

1. **Tree Traversal**: Traverse the `root` tree and for each node, check if the subtree starting from that node matches `subRoot`.
2. **Subtree Comparison**: Implement a helper function that checks if two trees are identical. This function will compare the values of the nodes and recursively check their left and right children.
3. **Recursive Search**: For each node in `root`, if the node's value matches the root of `subRoot`, call the subtree comparison function.

## Example Code
Here is a sample implementation in Python:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    if not root:
        return False
    if isSameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val) and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
