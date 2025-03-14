class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # l = 0        
        # tank = 0
        # r = 0
        # count = 0
        # while l < len(gas): 
        #     if tank + gas[r] >= cost[r]:
        #         tank += gas[r] - cost[r]
        #         r+=1 
        #         count+=1
        #         if r >= len(gas):
        #             r = 0
        #         if count == len(gas):
        #             return l
        #     else:
        #         l+=1
        #         count = 0
        #         r = l
        #         tank =0
        # return -1
            
        if sum(gas) < sum(cost):
            return -1
        res = 0
        tank =0
        for i in range(len(gas)):
            tank += (gas[i] - cost[i])

            if tank < 0:
                tank = 0
                res = i+1
  
        return res
        
