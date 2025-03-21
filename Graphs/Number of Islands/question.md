
### Question: Number of Islands

Given a 2D grid `grid` where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

#### Example 1:
**Input:**
```plaintext
grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
```
**Output:**
```plaintext
1
```

#### Example 2:
**Input:**
```plaintext
grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
```
**Output:**
```plaintext
4
```

#### Constraints:
- `1 <= grid.length, grid[i].length <= 100`
- `grid[i][j]` is `'0'` or `'1'`.

#### Recommended Time & Space Complexity:
You should aim for a solution with `O(m * n)` time and `O(m * n)` space, where `m` is the number of rows and `n` is the number of columns in the grid.


