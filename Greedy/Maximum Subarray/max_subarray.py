class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #Kadane's Algorithm
        maxSum = nums[0]
        currentSum = 0

        for num in nums:

            currentSum = max(currentSum, 0)
            currentSum += num
            maxSum = max(currentSum, maxSum)
        return maxSum
        
