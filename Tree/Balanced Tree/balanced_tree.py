# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def find_height(root):
            if root is None:
                return [True, 0]
           
            l, left_height = find_height(root.left)

            r, right_height = find_height(root.right)

            balanced = l and r and abs( left_height - right_height) <=1

            return [balanced, max(left_height, right_height) + 1]

        ans1, _ = find_height(root)
        return ans1
