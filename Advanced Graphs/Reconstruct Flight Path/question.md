# Reconstruct Flight Path

## Difficulty: Hard

You are given a list of flight tickets `tickets` where `tickets[i] = [from_i, to_i]` represent the source airport and the destination airport.

Each `from_i` and `to_i` consists of three uppercase English letters.

Reconstruct the itinerary in order and return it.

All of the tickets belong to someone who originally departed from `"JFK"`. Your objective is to reconstruct the flight path that this person took, assuming each ticket was used exactly once.

If there are multiple valid flight paths, return the lexicographically smallest one.
* For example, the itinerary `["JFK", "SEA"]` has a smaller lexical order than `["JFK", "SFO"]`.

You may assume all the tickets form at least one valid flight path.

## Example 1:

```
Input: tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]
Output: ["JFK","BUF","HOU","SEA"]
```

## Example 2:

```
Input: tickets = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]
Output: ["JFK","HOU","JFK","SEA","JFK"]
```

**Explanation:** Another possible reconstruction is `["JFK","SEA","JFK","HOU","JFK"]` but it is lexicographically larger.

## Constraints:
* `1 <= tickets.length <= 300`
* `from_i != to_i`

## Recommended Time & Space Complexity
You should aim for a solution with `O(ElogE)` time and `O(E)` space, where `E` is the number of tickets (edges).

## Hints
1. Build a graph where vertices are airports and edges are flights
2. Use a priority queue to get the lexicographically smallest destination first
3. Apply depth-first search (DFS) to traverse the graph
4. This is actually an Eulerian path problem - find a path that uses every edge exactly once
