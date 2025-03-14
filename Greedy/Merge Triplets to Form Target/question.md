# Merge Triplets to Form Target

## Problem Description

You are given a 2D array of integers `triplets`, where `triplets[i] = [a_i, b_i, c_i]` represents the *i*-th triplet. You are also given an integer array `target = [x, y, z]` which represents the triplet you want to obtain.

To obtain `target`, you may apply the following operation on `triplets` **zero or more times**:

- **Operation:** Choose two different triplets `triplets[i]` and `triplets[j]` and update `triplets[j]` to become:
```
[ max(a_i, a_j), max(b_i, b_j), max(c_i, c_j) ]
```



For example, if `triplets[i] = [1, 3, 1]` and `triplets[j] = [2, 1, 2]`, then updating `triplets[j]` will result in:
```
[ max(1, 2), max(3, 1), max(1, 2) ] = [2, 3, 2]
```


Return `true` if it is possible to obtain `target` as one of the elements in `triplets` after performing the above operations any number of times. Otherwise, return `false`.

---

## Examples

### Example 1

**Input:**
```
triplets = [[1,2,3],[7,1,1]] target = [7,2,3]
```



**Output:**
```
true
```



**Explanation:**  
Choose the first and second triplets and update the second triplet to become:
```
[ max(1, 7), max(2, 1), max(3, 1) ] = [7, 2, 3 ]
```


Now, `target` is present in `triplets`.

---

### Example 2

**Input:**
```
triplets = [[2,5,6],[1,4,4],[5,7,5]] target = [5,4,6]
```



**Output:**
```
false
```



**Explanation:**  
It is not possible to form `[5,4,6]` using the allowed operations.

---

## Constraints

- `1 <= triplets.length <= 1000`
- `1 <= a_i, b_i, c_i, x, y, z <= 100`

---

## Recommended Complexity

- **Time Complexity:** O(n), where n is the number of triplets.
- **Space Complexity:** O(1)
