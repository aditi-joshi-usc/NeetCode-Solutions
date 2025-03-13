class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = nums[0]

        cmin, cmax = 1,1

        for num in nums:
            tmp = cmax*num
            cmax = max(cmax * num, cmin * num, num)
            cmin = min(tmp, cmin * num, num)
            res = max(cmax, res)
        return res
        #Time Complexity = O(n)
        # Space complexity = O(1)
