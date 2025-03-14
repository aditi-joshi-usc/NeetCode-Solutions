class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0

        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            
            if intervals[i][0] >= prev_end:
                prev_end = intervals[i][1]
                continue
            else:
                prev_end = min(intervals[i][1], prev_end)
                res+=1
        return res
#Time complexity = O(nlogn)
#Space complexity = O(1)
            
