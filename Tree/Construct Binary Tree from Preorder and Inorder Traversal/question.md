# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
You are given two integer arrays `preorder` and `inorder`:
- `preorder` is the preorder traversal of a binary tree.
- `inorder` is the inorder traversal of the same tree.

Both arrays are of the same size and consist of unique values. Your task is to rebuild the binary tree from the given traversals and return its root.

### Constraints
- **1 <= inorder.length <= 1000**
- **inorder.length == preorder.length**
- **-1000 <= preorder[i], inorder[i] <= 1000**

## Examples

### Example 1
**Input:**  
```
preorder = [1,2,3,4], inorder = [2,1,3,4]
```
**Output:**
```
[1,2,3,null,null,null,4]
```
### Example 2

**Input:**
```
preorder =, inorder =
```
**Output:**


### Recommended Time & Space Complexity
Aim for a solution with O(n) time and O(n) space complexity, where n is the number of nodes in the tree.
