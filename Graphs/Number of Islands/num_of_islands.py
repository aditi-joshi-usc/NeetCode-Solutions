class gridClass:
    def __init__(self, grid):
        self.grid = grid

    def find_islands(self):

        count = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == '1':
                    temp =  self.dfs(i,j)
                    if temp>0:
                        count += 1
        return count

    def dfs(self, i,j):
        cnt = 0
        self.grid[i][j] = 0
        if i+1<len(self.grid) and self.grid[i+1][j] == '1':
            cnt += self.dfs(i+1,j) 
        if j+1< len(self.grid[i]) and self.grid[i][j+1] == '1':
            cnt += self.dfs(i,j+1) 
        if i-1>=0 and self.grid[i-1][j] == '1':
            cnt += self.dfs(i-1,j) 
        if j-1 >= 0 and self.grid[i][j-1] == '1':
            cnt += self.dfs(i,j-1)
        return 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        gr = gridClass(grid)
        return gr.find_islands()
