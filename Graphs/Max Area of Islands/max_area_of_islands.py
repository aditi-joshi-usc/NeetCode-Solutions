class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.mat = grid

        self.matlen = len(grid)
        self.mat_in_len = len(grid[0])
        self.directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(i,j):
            if i>=self.matlen or i<0 or j<0 or j>=self.mat_in_len :
                return 0
            if self.mat[i][j] == 0:
                return 0
            cnt=0
            self.mat[i][j] = 0
            for dr, dc in self.directions:
                cnt += dfs(i+dr, j+dc)
            
            return cnt+1
            
            

        maxcnt = 0

        for i in range(self.matlen):
            for j in range(self.mat_in_len):
                if self.mat[i][j] == 1:
                  maxcnt = max(maxcnt, dfs(i,j))  
        return maxcnt
