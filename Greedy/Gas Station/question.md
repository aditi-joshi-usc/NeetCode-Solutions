# Gas Station Problem

## Problem Description

There are `n` gas stations located along a circular route. You are given two integer arrays:

- **`gas`**: `gas[i]` represents the amount of gas available at the `i-th` station.
- **`cost`**: `cost[i]` represents the amount of gas required to travel from the `i-th` station to the `(i + 1)-th` station. (The last station connects back to the first station.)

You have a car with an **unlimited gas tank**, but you start with an **empty tank** at one of the gas stations.

Your task is to determine the **starting gas station's index** from which you can travel around the circuit once in the clockwise direction. If it is impossible to complete the circuit, return `-1`.

**Note:** It is guaranteed that at most one solution exists.

---

## Constraints

- `1 <= gas.length == cost.length <= 1000`
- `0 <= gas[i], cost[i] <= 1000`

---

## Examples

### Example 1

**Input:**
```
gas = [1, 2, 3, 4] cost = [2, 2, 4, 1]
```



**Output:**
```
3
```



**Explanation:**

1. **Begin at station 3:**
   - Start by refueling `gas[3]` (4 units).  
     Tank becomes: `0 + 4 = 4`
2. **Travel from station 3 to station 0:**
   - Spend `cost[3]` (1 unit) to travel.
   - At station 0, refuel `gas[0]` (1 unit).  
     Tank becomes: `4 - 1 + 1 = 4`
3. **Travel from station 0 to station 1:**
   - Spend `cost[0]` (2 units) to travel.
   - At station 1, refuel `gas[1]` (2 units).  
     Tank becomes: `4 - 2 + 2 = 4`
4. **Travel from station 1 to station 2:**
   - Spend `cost[1]` (2 units) to travel.
   - At station 2, refuel `gas[2]` (3 units).  
     Tank becomes: `4 - 2 + 3 = 5`
5. **Travel from station 2 back to station 3:**
   - Spend `cost[2]` (4 units) to travel.  
     Tank becomes: `5 - 4 = 1`

The circuit is completed successfully starting at station `3`.

---

### Example 2

**Input:**
```
gas = [1, 2, 3] cost = [2, 3, 2]
```



**Output:**
```
-1
```



**Explanation:**

No matter which station you start at, you will run out of gas before completing the circuit.

---

## Problem Summary

Given two arrays, `gas` and `cost`, representing the amount of gas at each station and the cost to travel to the next station, determine the starting station's index that allows you to complete a full circuit. If no valid starting station exists, return `-1`.
