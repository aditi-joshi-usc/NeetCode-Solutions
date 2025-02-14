class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

   

        def dfs(i, subset, total):
            if total == target:
                result.append(subset.copy())
                return
            if i>=len(nums) or total > target:
                return 

            for j in range(i, len(nums)):
                if total+nums[j]>target:
                    return
                subset.append(nums[j])
                dfs(j,subset, total+nums[j])
                subset.pop()
                
                
        nums.sort()
        dfs(0, [], 0)
        return result
            
        
