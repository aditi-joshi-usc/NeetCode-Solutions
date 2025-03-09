# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
            
        def isV(root, left, right):
            
            if root is None:
                return True
            
            if not (left < root.val < right):
                return False
            
            return isV(root.left, left, root.val) and isV(root.right, root.val, right)


        return isV(root, float('-inf'), float('inf'))
