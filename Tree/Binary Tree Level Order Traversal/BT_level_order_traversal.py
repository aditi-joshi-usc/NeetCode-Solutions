# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      #DFS  
      # track = defaultdict(list)

        # def level_list(root, level):
        #     if root is None:
        #         return
            
        #     track[level].append(root.val)
        #     level_list(root.left, level+1)
        #     level_list(root.right, level+1)

        # level_list(root, 0)
        # res=[]
        # for key, value in track.items():
        #     res.append(value)
        # return res

        res = []
        q = collections.deque()
        q.append(root)
        
      #BFS

        while q:

            lenq = len(q)
            level_list = []

            for i in range(lenq):
                node = q.popleft()
                
                
                if node:
                    level_list.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level_list:
                res.append(level_list)
        return res

