class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        x = False
        y = False
        z = False
        

        for t in triplets:
            x = x or (t[0] == target[0] and t[1]<= target[1] and t[2]<= target[2])
            y = y or (t[0] <= target[0] and t[1]== target[1] and t[2]<= target[2])
            z = z or (t[0] <= target[0] and t[1]<= target[1] and t[2]== target[2])
        
        if x and y and z:
            return True
        else:
            return False
      #Time complexity = O(n)
      #Space Complexity = O(1)
