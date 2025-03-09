# Count Good Nodes in Binary Tree

## Problem Statement

Within a binary tree, a node `x` is considered **good** if the path from the root of the tree to the node `x` contains no nodes with a value greater than the value of node `x`. Given the root of a binary tree, return the number of good nodes within the tree.

### Examples

**Example 1:**

- **Input:** 
  - `root = [2,1,1,3,null,1,5]`
- **Output:** `3`

**Example 2:**

- **Input:** 
  - `root = [1,2,-1,3,4]`
- **Output:** `4`

## Constraints

- `1 <= number of nodes in the tree <= 100`
- `-100 <= Node.val <= 100`

## Recommended Time & Space Complexity

Aim for a solution with **O(n)** time and **O(n)** space, where `n` is the number of nodes in the given tree.

## Solution Approach

### Definition of Good Nodes

A node is considered good if all the values along the path from the root to that node are less than or equal to the value of the node itself. This means we need to keep track of the maximum value encountered along the path from the root to the current node.

### Algorithm

1. Use a depth-first search (DFS) approach to traverse the tree.
2. Maintain a variable to track the maximum value encountered along the path from the root to the current node.
3. For each node:
   - If the node's value is greater than or equal to the maximum value encountered so far, it is a good node.
   - Update the maximum value if the current node's value is greater.
   - Recursively check the left and right children.
4. Count the total number of good nodes.

### Python Code Example

Here is a Python implementation of the solution:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root: TreeNode) -> int:
    def dfs(node, max_val):
        if not node:
            return 0
        
        good_count = 1 if node.val >= max_val else 0
        max_val = max(max_val, node.val)
        
        good_count += dfs(node.left, max_val)
        good_count += dfs(node.right, max_val)
        
        return good_count
    
    return dfs(root, root.val)
