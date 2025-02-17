class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # self.last_index = len(nums) - 1
        # self.nums = nums


        # def dfs(i):
        #     if i>self.last_index:
        #         return False
        #     if i == self.last_index:
        #         return True
        #     val = False
        #     curr_range = self.nums[i]
        #     while curr_range>=1:
        #         val = val or dfs(i+curr_range)
        #         curr_range -=1
        #     return val
        # return dfs(0)

        curr_pos = len(nums) - 2
        goal = len(nums) -1

        while curr_pos>=0:
            if curr_pos + nums[curr_pos] >= goal:
                goal = curr_pos
            curr_pos-=1
        
        return goal == 0


        
