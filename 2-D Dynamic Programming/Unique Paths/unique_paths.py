class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # grid = [[0]*n for _ in range(m)]
        # grid[0][0] = 1
        # for i in range(m):
        #     for j in range(n):
        #         if i-1>=0:
        #             grid[i][j] += grid[i-1][j]
        #         if  j-1>=0:
        #             grid[i][j] += grid[i][j-1]
        # return grid[m-1][n-1]

        #Math solution

        if m==1 or n==1:
            return 1
        if m< n:
            m,n = n,m
        
        result = j = 1
        for i in range(m, m+n-1):
            result = result * i
            result = result//j
            j+=1
        
        return result




