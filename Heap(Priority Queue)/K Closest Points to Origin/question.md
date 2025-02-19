
# K Closest Points to Origin

## Problem Statement
Given a 2D array of points and an integer k, find the k closest points to the origin (0, 0). The distance between points is calculated using the Euclidean distance formula: sqrt((x1 - x2)² + (y1 - y2)²).

## Examples

### Example 1
```java
Input: points = [[0,2],[2,2]], k = 1
Output: [[0,2]]
```
Explanation: (0,2) is closer to origin than (2,2) as distance is 2 vs 2.82842.

### Example 2
```java
Input: points = [[0,2],[2,0],[2,2]], k = 2
Output: [[0,2],[2,0]]
```
Explanation: Both answers [2,0],[0,2] and [0,2],[2,0] are acceptable.

