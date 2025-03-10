class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:



        ROW = len(grid)
        COL = len(grid[0])
        q = deque()

        visit = set()

        def addcell(r,c):
            if min(r,c) < 0 or r>= ROW or c>= COL or grid[r][c] == -1 or (r,c) in visit:
                return
            visit.add((r,c))
            q.append((r,c))


        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visit.add((i,j))

        dist =0
        while q:
            qlen = len(q)
            for i in range(qlen):
                r, c = q.popleft()
                grid[r][c] = dist
                addcell(r+1,c)
                addcell(r,c+1)
                addcell(r-1,c)
                addcell(r,c-1)
            dist+=1
        # Time Complexity = O (m*n)
        # Space Complexity = O(m*n) 

