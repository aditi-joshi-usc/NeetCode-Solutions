class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        
        l = 0
        r = len(matrix) - 1
        
        while l <= r:
            m = (r+l)//2
            
            if target< matrix[m][0]:
                r = m-1
            elif target > matrix[m][-1]:
                l = m+1
            else:
                break

        if not l<=r:
            return False
        
        final_m = matrix[(l+r)//2]

        l=0
        r = len(final_m) - 1
        
        while l <= r:
            m = (r+l)//2
            if target< final_m[m]:
                r = m -1
            elif target > final_m[m]:
                l = m+1
            else:
                return True
        return False
