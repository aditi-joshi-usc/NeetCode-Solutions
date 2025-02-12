class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in sum_dict:
                return [sum_dict[nums[i]], i]
            else:
                sum_dict[diff] = i
        
        return [0,1]
