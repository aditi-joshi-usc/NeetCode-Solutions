class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]


        pacific = set()
        atlantic = set()

        def dfs(r,c, visit, prevht):
            if ((r,c) in visit or r<0 or c< 0 or r == ROW or c == COL or heights[r][c] < prevht ):
                return
            
            visit.add((r,c))
            
            for dr, dc in directions:
                dfs(r+dr, c+dc, visit, heights[r][c])
            
        for c in range(COL):
            dfs(0,c, pacific, heights[0][c])
            dfs(ROW-1, c, atlantic, heights[ROW-1][c])
        
        for r in range(ROW):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COL-1, atlantic, heights[r][COL-1])

        res = []

        for r in range(ROW):
            for c in range(COL):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res


        #Time complexity =  O(m*n)
        # Space complexity = O(m*n)
