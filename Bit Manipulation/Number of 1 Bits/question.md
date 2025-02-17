# Number of One Bits

## Difficulty: Easy

## Problem Description
You are given an unsigned integer `n`. Return the number of `1` bits in its binary representation.

You may assume `n` is a non-negative integer which fits within 32-bits.

## Examples

### Example 1:
```
Input: n = 00000000000000000000000000010111
Output: 4
```
**Explanation:** The binary number `00000000000000000000000000010111` has four '1' bits.

### Example 2:
```
Input: n = 01111111111111111111111111111101
Output: 30
```
**Explanation:** The binary number `01111111111111111111111111111101` has thirty '1' bits.

## Visual Example
For n = 10111 (in binary):
```
Binary:  0...0010111
Count:      ↑ ↑↑↑
Total 1s: 4
```

## Constraints
* The input must be a binary string of length 32
* Input represents a non-negative integer
