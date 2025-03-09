class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []



        def backtrack(perm, pick):

            if len(nums) == len(perm):
                if perm not in self.res:
                    self.res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    backtrack(perm, pick)
                    perm.pop()
                    pick[i] = False
        
        backtrack([], [False]*len(nums))
        return self.res
