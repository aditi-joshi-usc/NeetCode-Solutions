# Two Integer Sum II

Given an array of integers `numbers` that is sorted in **non-decreasing order**, return the indices **(1-indexed)** of two numbers, `[index1, index2]`, such that:

`numbers[index1] + numbers[index2] == target`

with the condition `index1 < index2`. 

- The indices should be **1-based** (not 0-based).
- You **may not use the same element twice**.
- There will always be **exactly one valid solution**.

## Example

### Example 1
**Input**:  
`numbers = [1, 2, 3, 4], target = 3`


**Output**:  
`
[1, 2]
`

**Explanation**:  
`numbers[1] + numbers[2] = 1 + 2 = 3`

Since the array is **1-indexed**, the result is `[1, 2]`.

## Constraints
- `2 <= numbers.length <= 1000`
- `-1000 <= numbers[i] <= 1000`
- `-1000 <= target <= 1000`

## Recommended Time & Space Complexity
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
