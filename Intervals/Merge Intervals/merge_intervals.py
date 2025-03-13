class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_val  = max(interval[0] for interval in intervals)

        mp = [0] * (max_val +1)

        for start, end in intervals:
            mp[start] = max(end+1, mp[start])
        
        res = []
        finish = -1
        curr_interval = -1

        for i in range(len(mp)):

            if mp[i] != 0:
                if curr_interval == -1:
                    curr_interval = i
                finish = max(mp[i]-1, finish)
            if finish == i:
                res.append([curr_interval, finish])
                finish = -1
                curr_interval = -1

            
        if curr_interval != -1:
            res.append([curr_interval, finish])
        return res
            
# Time Complexity = O(n)
# Space Complexity = O(n)
