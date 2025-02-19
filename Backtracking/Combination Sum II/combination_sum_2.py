class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        sumval =0
        res = []
        candidates.sort()
        def dfs(sub, sumval, target, ind):
            if sumval == target:
                res.append(sub.copy())
                return
            
            
            else:

                for i in range(ind, len(candidates)):
                    
                    if ind < i and candidates[i] == candidates[i-1]:
                        continue
                    sumval += candidates[i]
                    if sumval>target:
                        sumval-= candidates[i]
                        break
                    sub.append(candidates[i])
                    dfs(sub, sumval, target, i+1)
                    sumval-= candidates[i]
                    sub.pop()
        dfs([], 0, target, 0)
        return res


