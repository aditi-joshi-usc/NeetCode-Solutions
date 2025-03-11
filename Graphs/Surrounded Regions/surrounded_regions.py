class Solution:
    def solve(self, board: List[List[str]]) -> None:


        ROW = len(board)
        COL = len(board[0])

        def capture(r,c):
            if (r<0 or c< 0 or r==ROW or c == COL or board[r][c] != 'O'):
                return
            board[r][c] = 'T'
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)



        for r in range(ROW):
            if board[r][0] == 'O':
                capture(r,0)
            if board[r][COL-1] == 'O':
                capture(r,COL-1)
        
        for c in range(COL):
            if board[0][c] == 'O':
                capture(0, c)
            if board[ROW-1][c] == 'O':
                capture(ROW-1,c)


        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == "T":
                    board[r][c] = "O"


# Time Complexity = O(m*n)
# Space Complexity = O(m*n)
