# Last Stone Weight

You are given an array of integers `stones` where `stones[i]` represents the weight of the *i-th* stone.

We want to run a simulation on the stones as follows:

1. At each step, choose the two heaviest stones with weights `x` and `y`.
2. Smash them together:
   - If `x == y`, both stones are destroyed.
   - If `x < y`, the stone with weight `x` is destroyed, and the stone with weight `y` has a new weight `y - x`.
3. Continue the simulation until no more than one stone remains.
4. Return the weight of the last remaining stone or return `0` if none remain.

---

## Examples

### Example 1

**Input:** `stones = [2, 3, 6, 2, 4]`

**Output:** `1`

**Explanation:**
1. Smash `6` and `4` (the two heaviest) → difference is `2`; they become `[2, 3, 2, 2]`.
2. Smash `3` and `2` → difference is `1`; they become `[1, 2, 2]`.
3. Smash `2` and `2` → both destroyed; they become `[1]`.
4. Only one stone remains, which has weight `1`.

### Example 2

**Input:** `stones = [1, 2]`

**Output:** `1`

---

## Constraints
- `1 <= stones.length <= 20`
- `1 <= stones[i] <= 100`

## Time & Space Complexity Requirements
- **Time Complexity:** O(n log n) or better
- **Space Complexity:** O(n) or better

Given the constraints (n up to 20), even simpler solutions would be performant enough, but we'll aim for a solution that scales using a **max-heap** (priority queue).

---

