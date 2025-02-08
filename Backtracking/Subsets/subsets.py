class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset=[]
        
        def back_track(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])

            back_track(i+1)
            subset.pop()
            back_track(i+1)
        i=0
        back_track(i)
        return result


                
