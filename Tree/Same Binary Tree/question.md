# Same Binary Tree

## Problem Statement
Given the roots of two binary trees `p` and `q`, return `true` if the trees are equivalent, otherwise return `false`.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

---

## Examples

### Example 1:
**Input:**  
`p = [1,2,3]`, `q = [1,2,3]`  

**Output:**  
`true`  

**Explanation:**  
Both trees have the same structure and node values.

---

### Example 2:
**Input:**  
`p = [4,7]`, `q = [4,null,7]`  

**Output:**  
`false`  

**Explanation:**  
The structure of the trees is different; the second tree has a null left child for the root.

---

### Example 3:
**Input:**  
`p = [1,2,3]`, `q = [1,3,2]`  

**Output:**  
`false`  

**Explanation:**  
The trees have the same values but different structures.

---

## Constraints
- `0 <= The number of nodes in both trees <= 100`
- `-100 <= Node.val <= 100`

---

## Recommended Time & Space Complexity
- **Time Complexity:** O(n), where `n` is the number of nodes in the tree.
- **Space Complexity:** O(n)

---

## Solution

### Approach
To determine if two binary trees are the same, we can use a **recursive approach**:
1. If both nodes are `null`, they are considered the same.
2. If one of the nodes is `null` and the other is not, they are not the same.
3. If the values of the nodes are different, the trees are not the same.
4. Recursively check the left and right subtrees.

---

### Algorithm
1. Define a recursive function that takes two nodes as input.
2. Check the base cases:
   - If both nodes are `null`, return `true`.
   - If one node is `null` and the other is not, return `false`.
   - If the values of the nodes are different, return `false`.
3. Recursively call the function for the left and right children of both nodes.
4. Return the result of the recursive calls.

---

### Code Implementation
Here is the Python implementation:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
