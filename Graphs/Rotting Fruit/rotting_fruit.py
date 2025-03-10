class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        ROW = len(grid)
        COL = len(grid[0])
        q = deque()

        visit = set()

        self.fresh_fruit = 0

        def addcell(r,c):
            if r<0 or c< 0 or r>=ROW or c>= COL or grid[r][c] != 1 or (r,c) in visit:
                return
            visit.add((r,c))
            q.append((r,c)) 
            self.fresh_fruit-=1

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visit.add((i,j))
                elif grid[i][j] == 1:
                    self.fresh_fruit+=1

        time = 0
        while q and self.fresh_fruit>0:
            lenq = len(q)
            
            for i in range(lenq):
                r, c = q.popleft()

                addcell(r+1,c)
                addcell(r-1,c)
                addcell(r,c+1)
                addcell(r,c-1)
            time+=1
        if self.fresh_fruit <= 0:
            return time
        else:
            return -1

# Time Complexity = O(m*n)
# Space Complexity = O(m*n)
