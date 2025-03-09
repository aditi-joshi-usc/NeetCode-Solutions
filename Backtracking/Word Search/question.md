# Word Search

## Problem Statement

Given a 2-D grid of characters `board` and a string `word`, return `true` if the word is present in the grid, otherwise return `false`.

For the word to be present, it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

### Examples

- **Example 1**:
  - **Input**: 
    ```plaintext
    board = [
      ["A","B","C","D"],
      ["S","A","A","T"],
      ["A","C","A","E"]
    ],
    word = "CAT"
    ```
  - **Output**: `true`

- **Example 2**:
  - **Input**: 
    ```plaintext
    board = [
      ["A","B","C","D"],
      ["S","A","A","T"],
      ["A","C","A","E"]
    ],
    word = "BAT"
    ```
  - **Output**: `false`

### Constraints

- `1 <= board.length, board[i].length <= 5`
- `1 <= word.length <= 10`
- `board` and `word` consist of only lowercase and uppercase English letters.

## Recommended Time & Space Complexity

You should aim for a solution with **O(m * (4^n))** time and **O(n)** space, where `m` is the number of cells in the given board and `n` is the size of the given word.
