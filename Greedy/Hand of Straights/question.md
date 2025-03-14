# Hand of Straights

## Problem Description

You are given an integer array `hand` where `hand[i]` is the value written on the `i-th` card, and an integer `groupSize`.

Your task is to rearrange the cards into groups so that:
- Each group is of size `groupSize`.
- The card values in each group are consecutive and increasing by 1.

Return `true` if it is possible to rearrange the cards in this way, otherwise return `false`.

---

## Examples

### Example 1

**Input:**
```
hand = [1, 2, 4, 2, 3, 5, 3, 4] groupSize = 4
```



**Output:**
```
true
```



**Explanation:**

The cards can be rearranged into the groups `[1, 2, 3, 4]` and `[2, 3, 4, 5]`.

---

### Example 2

**Input:**
```
hand = [1, 2, 3, 3, 4, 5, 6, 7] groupSize = 4
```


**Output:**
```
false
```



**Explanation:**

The closest grouping possible is `[1, 2, 3, 4]` and `[3, 5, 6, 7]`, but the cards in the second group are not consecutive.

---

## Constraints

- `1 <= hand.length <= 1000`
- `0 <= hand[i] <= 1000`
- `1 <= groupSize <= hand.length`

---

## Complexity Analysis

- **Time Complexity:** O(n log n) or better (where n is the number of cards).
- **Space Complexity:** O(n)
