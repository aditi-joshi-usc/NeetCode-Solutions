# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes.

### **Input:**
- The root of a binary tree `root`.

### **Output:**
- Return the diameter of the tree (an integer).

## **Examples**

### **Example 1:**
#### **Input:**
```plaintext
root = [1,null,2,3,4,5]
```
#### **Output:**
```plaintext
3
```
#### **Explanation:**
The longest path is either `[1,2,3,5]` or `[5,3,2,4]` with a length of 3 edges.

---

### **Example 2:**
#### **Input:**
```plaintext
root = [1,2,3]
```
#### **Output:**
```plaintext
2
```
#### **Explanation:**
The longest path is `[2,1,3]` with a length of 2 edges.

## **Constraints**
- `1 <= number of nodes in the tree <= 100`
- `-100 <= Node.val <= 100`

---

## **Solution Approach**
### **Algorithm (Iterative DFS using a Stack)**
1. Use an **iterative depth-first search (DFS)** approach with a stack to traverse the tree.
2. Maintain a dictionary `mp` to store **height and diameter** for each node.
3. Use **postorder traversal** to compute values bottom-up.
4. At each node:
   - Compute its height as `1 + max(leftHeight, rightHeight)`.
   - Compute its diameter as `max(leftHeight + rightHeight, leftDiameter, rightDiameter)`.
5. Return the diameter stored at the root node.

---

## **Code Implementation (Python)**
```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {None: (0, 0)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                leftHeight, leftDiameter = mp[node.left]
                rightHeight, rightDiameter = mp[node.right]
                
                mp[node] = (1 + max(leftHeight, rightHeight),
                            max(leftHeight + rightHeight, leftDiameter, rightDiameter))
        
        return mp[root][1]
```

---

## **Complexity Analysis**
- **Time Complexity:** `O(n)`, as we traverse each node exactly once.
- **Space Complexity:** `O(n)`, since we store height and diameter information for each node.

---

## **Key Takeaways**
- Uses **iterative DFS with a stack** instead of recursion.
- Maintains **height and diameter values** for each node in a dictionary.
- Computes diameter in **O(n) time and O(n) space**, which is optimal for this problem.

---

## **Alternative Approach (Recursive DFS)**
We can also solve this using a recursive DFS approach.
```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.diameter
```
This approach has the same time and space complexity but is **simpler and more intuitive**.

---

## **Conclusion**
This problem can be efficiently solved using **both iterative and recursive DFS**. The iterative approach avoids recursion depth issues, while the recursive approach is more concise. The key idea is to compute **height and diameter at each node** and use the **maximum path sum** of two subtree heights to determine the final diameter.

