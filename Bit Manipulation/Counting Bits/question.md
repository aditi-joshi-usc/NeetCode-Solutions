# Counting Bits

## Problem Statement

**Difficulty**: Easy

Given an integer `n`, count the number of `1`'s in the binary representation of every number in the range `[0, n]`.

Return an array `output` where `output[i]` is the number of `1`'s in the binary representation of `i`.

### Examples

**Example 1:**
```
Input: n = 4
Output: [0,1,1,2,1]
Explanation: 
0 --> 0     (0 ones)
1 --> 1     (1 one)
2 --> 10    (1 one)
3 --> 11    (2 ones)
4 --> 100   (1 one)
```

### Constraints:
- `0 <= n <= 1000`

## Solution Approaches

### Approach 1: Brute Force

A straightforward approach is to count the number of 1's in the binary representation of each number from 0 to n.

```java
public int[] countBits(int n) {
    int[] result = new int[n + 1];
    
    for (int i = 0; i <= n; i++) {
        result[i] = countOnes(i);
    }
    
    return result;
}

private int countOnes(int num) {
    int count = 0;
    while (num > 0) {
        count += num & 1;  // Check if the least significant bit is 1
        num >>= 1;         // Right shift by 1
    }
    return count;
}
```

**Time Complexity**: O(n log n)
- We process n+1 numbers, and each number takes O(log n) operations to count its bits.

**Space Complexity**: O(1) (excluding the output array)

### Approach 2: Dynamic Programming - Least Significant Bit

We can use dynamic programming to avoid recounting bits:
- For any number x, the number of 1's in x is equal to the number of 1's in x/2 plus 1 if x is odd.

```java
public int[] countBits(int n) {
    int[] result = new int[n + 1];
    
    for (int i = 1; i <= n; i++) {
        result[i] = result[i >> 1] + (i & 1);
    }
    
    return result;
}
```

**Time Complexity**: O(n)
**Space Complexity**: O(1) (excluding the output array)

### Approach 3: Dynamic Programming - Last Set Bit

Another DP approach uses the property that removing the last set bit of x results in a smaller number whose bit count we already know.

```java
public int[] countBits(int n) {
    int[] result = new int[n + 1];
    
    for (int i = 1; i <= n; i++) {
        result[i] = result[i & (i - 1)] + 1;
    }
    
    return result;
}
```

**Time Complexity**: O(n)
**Space Complexity**: O(1) (excluding the output array)

## Explanation of DP Approaches

### Approach 2 Explained:
For any number `i`:
- If `i` is even, its binary representation ends with 0. Dividing by 2 (right shifting by 1) removes this 0, and the number of 1's remains the same.
- If `i` is odd, its binary representation ends with 1. Dividing by 2 (right shifting by 1) removes this 1, so the number of 1's decreases by 1.

Therefore:
- If `i` is even: `bits[i] = bits[i/2]`
- If `i` is odd: `bits[i] = bits[i/2] + 1`

This can be combined into a single formula: `bits[i] = bits[i >> 1] + (i & 1)`

### Approach 3 Explained:
The expression `i & (i - 1)` clears the least significant set bit of `i`.

For example:
- If `i = 12` (1100 in binary), then `i - 1 = 11` (1011 in binary)
- `i & (i - 1) = 1100 & 1011 = 1000 = 8`
- This removes the least significant set bit (the rightmost 1).

Therefore, `bits[i] = bits[i & (i - 1)] + 1` means "the number of 1's in `i` equals the number of 1's in `i` with the rightmost 1 removed, plus 1."

## Example Walkthrough

Let's trace through the DP approach (Approach 2) for n = 4:

1. Initialize `result = [0, 0, 0, 0, 0]`
2. For i = 1:
   - i >> 1 = 0, result[0] = 0
   - i & 1 = 1 (odd number)
   - result[1] = result[0] + 1 = 0 + 1 = 1
3. For i = 2:
   - i >> 1 = 1, result[1] = 1
   - i & 1 = 0 (even number)
   - result[2] = result[1] + 0 = 1 + 0 = 1
4. For i = 3:
   - i >> 1 = 1, result[1] = 1
   - i & 1 = 1 (odd number)
   - result[3] = result[1] + 1 = 1 + 1 = 2
5. For i = 4:
   - i >> 1 = 2, result[2] = 1
   - i & 1 = 0 (even number)
   - result[4] = result[2] + 0 = 1 + 0 = 1

Final result: `[0, 1, 1, 2, 1]`

## Implementation Tricks

1. **Built-in functions**: Some languages have built-in functions to count bits:
   - Java: `Integer.bitCount(i)`
   - C++: `__builtin_popcount(i)`
   - Python: `bin(i).count('1')`

2. **Brian Kernighan's Algorithm**: An efficient way to count set bits:
   ```java
   int count = 0;
   while (num > 0) {
       num &= (num - 1);  // Clears the least significant set bit
       count++;
   }
   ```

## Conclusion

The dynamic programming approaches offer an elegant O(n) solution to this problem by leveraging patterns in binary representation. Approach 2 (based on least significant bit) is generally the most intuitive, while Approach 3 (based on clearing the last set bit) offers a fascinating insight into bit manipulation.
