# Surrounded Regions

## Problem Statement

You are given a 2-D matrix `board` containing 'X' and 'O' characters. If a continuous, four-directionally connected group of 'O's is surrounded by 'X's, it is considered to be surrounded. Your task is to change all surrounded regions of 'O's to 'X's and do so in-place by modifying the input `board`.

## Example

**Input:**
```
board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]
```
**Output:**
```


[
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","O"]
]
```
**Explanation:** The 'O's surrounded by 'X's are replaced with 'X's.
**Constraints**
1 <= board.length, board[i].length <= 200
board[i][j] is 'X' or 'O'.
