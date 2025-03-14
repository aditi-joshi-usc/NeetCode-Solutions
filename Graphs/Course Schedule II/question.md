# Course Schedule II

## Problem Statement

You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you must take course `b` first if you want to take course `a`. There are a total of `numCourses` courses you are required to take, labeled from `0` to `numCourses - 1`.

Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.

### Examples

**Example 1:**

- **Input:** `numCourses = 3`, `prerequisites = [[1,0]]`
- **Output:** `[0,1,2]`
- **Explanation:** We must ensure that course `0` is taken before course `1`.

**Example 2:**

- **Input:** `numCourses = 3`, `prerequisites = [[0,1],[1,2],[2,0]]`
- **Output:** `[]`
- **Explanation:** It's impossible to finish all courses due to a cycle.

## Constraints

- `1 <= numCourses <= 1000`
- `0 <= prerequisites.length <= 1000`
- All prerequisite pairs are unique.

## Recommended Time & Space Complexity

You should aim for a solution with **O(V + E)** time and **O(V + E)** space, where `V` is the number of courses (nodes) and `E` is the number of prerequisites (edges).
