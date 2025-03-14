# Cheapest Flights Within K Stops

## Problem Description

There are `n` airports, labeled from `0` to `n - 1`, which are connected by a series of one-way flights. You are given an array `flights` where `flights[i] = [from_i, to_i, price_i]` represents a flight from airport `from_i` to airport `to_i` with cost `price_i`. All flights are unique and there are no self-loops (flights from an airport to itself).

You are also given three integers:
- `src`: the starting airport,
- `dst`: the destination airport (with `src != dst`), and
- `k`: the maximum number of stops allowed (note that stops do not include the source and destination).

Return the cheapest price from `src` to `dst` with at most `k` stops. If no such route exists, return `-1`.

---

## Examples

### Example 1

**Input:**
```
n = 4 flights = [[0,1,200],[1,2,100],[1,3,300],[2,3,100]] src = 0 dst = 3 k = 1
```



**Output:**
```
500
```
**Explanation:**
The optimal path with at most 1 stop is:
- Flight from 0 to 1 with cost 200.
- Flight from 1 to 3 with cost 300.

Total cost = 200 + 300 = 500.

Note that although the path `[0 -> 1 -> 2 -> 3]` costs 400, it requires 2 stops, which exceeds the limit.

---

### Example 2

**Input:**
```
n = 3 flights = [[1,0,100],[1,2,200],[0,2,100]] src = 1 dst = 2 k = 1
```



**Output:**
```
200
```

**Explanation:**
The cheapest option is taking the direct flight from 1 to 2 with a cost of 200.

---

## Constraints

- `1 <= n <= 100`
- `0 <= src, dst, k < n`
- `flights[i][0] != flights[i][1]` (No flight starts and ends at the same airport)
- `1 <= price_i <= 1000` for each flight

---

## Recommended Complexity

- **Time Complexity:** O(n + (m * k))  
  (where `n` is the number of airports, `m` is the number of flights, and `k` is the maximum allowed number of stops)
- **Space Complexity:** O(n)

---
