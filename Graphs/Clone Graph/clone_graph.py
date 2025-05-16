"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        old_new = {}

        def dfs(root):
            if root is None:
                return 
            
            if root in old_new:
                return old_new[root]
            
            old_new[root] = Node(root.val)

            for child in root.neighbors:                    
                old_new[root].neighbors.append(dfs(child))

            return old_new[root]

        return dfs(node) if node else None
# time complexity = O(n) where n is the number of nodes
