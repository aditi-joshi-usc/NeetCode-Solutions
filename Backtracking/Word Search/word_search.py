class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(row, col, i):

            if i == len(word):
                return True

            
            if row< 0 or col< 0 or row>=len(board) or col>= len(board[0]):
                return False
            if word[i]!= board[row][col] or board[row][col] == '#':
                return False
            
            board[row][col] = '#'
            res = (dfs(row+1, col, i+1) or dfs(row, col+1, i+1) or dfs(row-1, col, i+1) or dfs(row, col-1, i+1))
            board[row][col] = word[i]
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0):
                    return True
        return False

        #Time complexity = O(m * 4^n)
        #where m is the number of cells and n is the word length
