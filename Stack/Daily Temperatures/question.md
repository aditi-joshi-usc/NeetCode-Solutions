# Daily Temperatures

## Problem Statement
You are given an array of integers `temperatures` where `temperatures[i]` represents the daily temperature on the `i-th` day.

Return an array `result` where `result[i]` is the number of days after the `i-th` day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the `i-th` day, set `result[i]` to `0` instead.

---

## Examples

### Example 1:
**Input:**  
`temperatures = [30,38,30,36,35,40,28]`  

**Output:**  
`[1,4,1,2,1,0,0]`  

**Explanation:**  
- For day 0 (temperature 30), the next warmer day is day 1 (temperature 38), so `result[0] = 1`.
- For day 1 (temperature 38), there is no warmer day in the future, so `result[1] = 0`.
- For day 2 (temperature 30), the next warmer day is day 3 (temperature 36), so `result[2] = 1`.
- For day 3 (temperature 36), the next warmer day is day 5 (temperature 40), so `result[3] = 2`.
- For day 4 (temperature 35), the next warmer day is day 5 (temperature 40), so `result[4] = 1`.
- For day 5 (temperature 40), there is no warmer day in the future, so `result[5] = 0`.
- For day 6 (temperature 28), there is no warmer day in the future, so `result[6] = 0`.

---

### Example 2:
**Input:**  
`temperatures = [22,21,20]`  

**Output:**  
`[0,0,0]`  

**Explanation:**  
There are no warmer days in the future for any of the given days.

---

## Constraints
- `1 <= temperatures.length <= 1000`
- `1 <= temperatures[i] <= 100`

---

## Recommended Time & Space Complexity
- **Time Complexity:** O(n), where `n` is the size of the input array.
- **Space Complexity:** O(n)

---

## Solution

### Approach
To solve this problem efficiently, we can use a **monotonic decreasing stack**:
1. Traverse the array from left to right.
2. Use a stack to keep track of indices of days with temperatures that haven't yet found a warmer day.
3. For each day:
   - While the stack is not empty and the current day's temperature is warmer than the temperature at the index stored at the top of the stack:
     - Pop the index from the stack.
     - Calculate the difference between the current day and the popped index, and store it in the result array.
   - Push the current day's index onto the stack.
4. After traversing the array, any indices left in the stack correspond to days with no warmer future day. Set their result to `0`.

---

### Algorithm
1. Initialize an empty stack and a result array filled with zeros.
2. Iterate through the `temperatures` array:
   - While the stack is not empty and the current temperature is greater than the temperature at the index stored at the top of the stack:
     - Pop the index from the stack.
     - Update the result for that index with the difference between the current index and the popped index.
   - Push the current index onto the stack.
3. Return the result array.

---

### Code Implementation
Here is the Python implementation:

```python
def dailyTemperatures(temperatures):
    n = len(temperatures)
    result = [0] * n  # Initialize result array with zeros
    stack = []  # Monotonic decreasing stack to store indices

    for i in range(n):
        # Check if the current temperature is warmer than the temperature at the top of the stack
        while stack and temperatures[i] > temperaturesstack1]]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index  # Calculate the difference in days
        stack.append(i)  # Push the current index onto the stack

    return result
