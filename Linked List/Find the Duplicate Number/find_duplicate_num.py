class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # visited =set()

        # for num in nums:
        #     if  num in visited:
        #         return num
        #     else:
        #         visited.add(num)
        # return -1


        fast = 0
        slow = 0


        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
            
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
