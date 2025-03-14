# Non-overlapping Intervals

## Problem Description

Given an array of intervals `intervals` where each interval is represented as `intervals[i] = [start_i, end_i]`, return the minimum number of intervals you need to remove to make the remaining intervals non-overlapping.

**Note:** Intervals are considered non-overlapping even if they share a common point. For example, `[1, 3]` and `[2, 4]` are overlapping, but `[1, 2]` and `[2, 3]` are non-overlapping.

---

## Examples

### Example 1

**Input:**
```
intervals =1,2],[2,41,4]]
```



**Output:**
```
1
```



**Explanation:**

After removing the interval `[1,4]`, the remaining intervals `[1,2]` and `[2,4]` do not overlap.

---

### Example 2

**Input:**
```
intervals = [[1,2],[2,4]]
```


**Output:**
```
0
```



**Explanation:**

The intervals `[1,2]` and `[2,4]` are already non-overlapping, so no interval needs to be removed.

---

## Constraints

- `1 <= intervals.length <= 1000`
- `intervals[i].length == 2`
- `-50000 <= start_i < end_i <= 50000`

---

## Recommended Time and Space Complexity

- **Time Complexity:** O(n log n) (due to the sorting step)
- **Space Complexity:** O(n)
