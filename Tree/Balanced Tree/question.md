
# Balanced Binary Tree

## Problem Statement
Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is defined as a binary tree where the left and right subtrees of every node differ in height by no more than 1.

## Examples

### Example 1
```java
Input: root = [1,2,3,null,null,4]
Output: true
```

### Example 2
```java
Input: root = [1,2,3,null,null,4,null,5]
Output: false
```

### Example 3
```java
Input: root = []
Output: true
```

## Approach 1: Bottom-up DFS

### Intuition
We can use a bottom-up approach where we calculate the height of each subtree and simultaneously check if it's balanced. If at any point we find an unbalanced subtree, we can return early.

### Algorithm
1. Create a helper function that returns the height of a subtree and -1 if it's unbalanced
2. For each node:
   - Recursively check left and right subtrees
   - If either subtree is unbalanced (returns -1), propagate -1 upward
   - If height difference > 1, return -1
   - Otherwise, return max height of subtrees + 1

### Java Solution
```java
class Solution {
    public boolean isBalanced(TreeNode root) {
        return checkHeight(root) != -1;
    }
    
    private int checkHeight(TreeNode node) {
        if (node == null) return 0;
        
        int leftHeight = checkHeight(node.left);
        if (leftHeight == -1) return -1;
        
        int rightHeight = checkHeight(node.right);
        if (rightHeight == -1) return -1;
        
        if (Math.abs(leftHeight - rightHeight) > 1) return -1;
        
        return Math.max(leftHeight, rightHeight) + 1;
    }
}
```

### Complexity Analysis
- Time Complexity: O(n), where n is the number of nodes
- Space Complexity: O(h), where h is the height of the tree (due to recursion stack)
  - In the worst case (skewed tree): O(n)
  - In the best case (balanced tree): O(log n)

## Notes
- An empty tree is considered height-balanced
- The solution handles both balanced and unbalanced cases efficiently by using early returns
- The approach combines height calculation and balance checking to avoid multiple tree traversals
