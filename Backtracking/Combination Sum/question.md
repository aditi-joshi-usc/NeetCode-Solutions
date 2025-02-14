# Combination Sum

You are given:
- An array of **distinct** integers `nums`.
- A target integer `target`.

**Objective:**  
Return a list of *all unique combinations* of `nums` where the chosen numbers *sum* to `target`.  
You can choose the same number from `nums` any number of times.  
Two combinations are the same if they have the same frequency of each chosen number.  
You may return the combinations in any order, and within each combination, the numbers can be in any order.

---

## Examples

### Example 1

**Input:**
nums = [2,5,6,9] target = 9

makefile
Copy
Edit

**Output:**
[[2,2,5], [9]]

markdown
Copy
Edit

**Explanation:**
- We can achieve `9` either as `2 + 2 + 5` or with a single `9`.

### Example 2

**Input:**
```
nums = [3,4,5] target = 16
```

**Output:**
```
[[3,3,3,3,4], [3,3,5,5], [4,4,4,4], [3,4,4,5]]

```

### Example 3

**Input:**
```
nums = [3] target = 5
```

**Output:**
```
[]
```

Since `3` is the only number, we can't make `5` exactly with multiples of `3`.

---

## Constraints
- All elements of `nums` are distinct.
- `1 <= nums.length <= 20`
- `2 <= nums[i] <= 30`
- `2 <= target <= 30`

---

## Recommended Time & Space Complexity
- **Time Complexity:** O(2^(t/m)), where:
  - `t` is `target`
  - `m` is the minimum value in `nums`
- **Space Complexity:** O(t/m)

This complexity follows from the fact that in the worst case, we explore combinations using the smallest number `m` to build up to `target`.

---
