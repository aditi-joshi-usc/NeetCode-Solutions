# Binary Tree Right Side View

## Problem Statement

You are given the root of a binary tree. Return only the values of the nodes that are **visible from the right side** of the tree, ordered from top to bottom.

### Examples

**Example 1:**

- **Input:** 
  - `root = [1,2,3]`
- **Output:** `[1,3]`

**Example 2:**

- **Input:** 
  - `root = [1,2,3,4,5,6,7]`
- **Output:** `[1,3,7]`

## Constraints

- `0 <= number of nodes in the tree <= 100`
- `-100 <= Node.val <= 100`

## Recommended Time & Space Complexity

Aim for a solution with **O(n)** time and **O(n)** space, where `n` is the number of nodes in the given tree.

## Solution Approach

### Right Side View

To obtain the right side view of a binary tree, we can use a **Breadth-First Search (BFS)** approach. This method allows us to traverse the tree level by level, ensuring that we capture the last node at each level, which is the rightmost node visible from that level.

### Algorithm

1. Initialize a queue to facilitate level order traversal.
2. Start with the root node and enqueue it.
3. While the queue is not empty:
   - Determine the number of nodes at the current level.
   - For each node at this level, dequeue it and enqueue its children (right child first, then left child).
   - The last node processed at this level will be part of the right side view.
4. Collect the values of the last nodes from each level into a result list.

### Python Code Example

Here is a Python implementation of the right side view:

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: TreeNode) -> list[int]:
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.popleft()
            # If it's the last node in the current level, add to result
            if i == level_size - 1:
                result.append(node.val)
            # Enqueue right child first, then left child
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
    
    return result
