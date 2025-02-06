class Solution:
    
    def bin_search(self, left, right, nums, target):
        
        if left > right:
            return -1
        
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            return self.bin_search(mid+1, right, nums, target)
        else:
            return self.bin_search(left, mid-1, nums, target)




    def search(self, nums: List[int], target: int) -> int:
        
        return self.bin_search(0, len(nums) - 1, nums, target)
