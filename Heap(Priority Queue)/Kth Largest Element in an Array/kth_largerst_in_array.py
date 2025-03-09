class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums=[-n for n in nums]
        
        heapq.heapify(nums)
        res=0
        i = 0
        while i<k:
            res = heapq.heappop(nums)
            
            i+=1
        return -res

        
        #Time Complexity = O(nlogk)
