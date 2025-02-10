class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Hash set
        # Time complexity = O(n)
        # Space complexity = O(n)
        # singles = []

        # for num in nums:
        #     if num in singles:
        #         singles.remove(num)
        #     else:
        #         singles.append(num)
        # return singles[0]
        

        # Bit Manipulation
        #Time complexity = O(n)
        # Space complexity = O(1)
        xor_value = 0

        for num in nums:
            xor_value = xor_value ^ num
        
        return xor_value
