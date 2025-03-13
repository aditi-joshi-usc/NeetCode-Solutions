# Word Break

## Problem Statement

Given a string `s` and a dictionary of strings `wordDict`, determine if `s` can be segmented into a space-separated sequence of one or more dictionary words. You may reuse the words from the dictionary as many times as needed. Assume all dictionary words are unique.

## Examples

- **Example 1:**
  - **Input:** `s = "neetcode"`, `wordDict = ["neet", "code"]`
  - **Output:** `true`
  - **Explanation:** The string `"neetcode"` can be segmented into `"neet"` and `"code"`.

- **Example 2:**
  - **Input:** `s = "applepenapple"`, `wordDict = ["apple", "pen", "ape"]`
  - **Output:** `true`
  - **Explanation:** The string can be segmented as `"apple"`, `"pen"`, and `"apple"`. Reusing dictionary words is allowed.

- **Example 3:**
  - **Input:** `s = "catsincars"`, `wordDict = ["cats", "cat", "sin", "in", "car"]`
  - **Output:** `false`
  - **Explanation:** There is no way to segment `"catsincars"` entirely using the provided dictionary.

## Constraints

- `1 <= s.length <= 200`
- `1 <= wordDict.length <= 100`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters

## Recommended Time and Space Complexity

- **Time Complexity:** O(n * m * t) worst-case, where `n` is the length of `s`, `m` is the number of words in `wordDict`, and `t` is the maximum length of any word in `wordDict`.
- **Space Complexity:** O(n), using a DP array of size `n + 1`.

## Approach: Dynamic Programming

We can solve this problem using dynamic programming. The idea is to use a DP array `dp` where `dp[i]` is `true` if the substring `s[0:i]` can be segmented into dictionary words, and `false` otherwise.

### Steps:
1. **Initialization:**
   - Create a DP array `dp` of length `len(s) + 1` and initialize all elements to `false`.
   - Set `dp[0] = true` since an empty string is considered segmented.

2. **DP Transition:**
   - For each index `i` from 1 to `len(s)`, check every index `j` from `0` to `i`.
   - If `dp[j]` is `true` (meaning `s[0:j]` can be segmented) and the substring `s[j:i]` is in `wordDict`, then set `dp[i]` to `true` and break out of the inner loop.

3. **Final Decision:**
   - The answer is the value of `dp[len(s)]`, which indicates if the entire string can be segmented.

## Python Implementation

```python
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert list to set for faster look-ups.
        wordSet = set(wordDict)
        n = len(s)
        # dp[i] is True if s[0:i] can be segmented into words in the dictionary.
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: Empty string can be segmented.

        # Check all possible substrings s[0:i]
        for i in range(1, n + 1):
            # Try every possible split position j (0 <= j < i)
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  # Found a valid segmentation, no need to check further.
                    
        return dp[n]

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    # Example 1
    s1 = "neetcode"
    wordDict1 = ["neet", "code"]
    print(solution.wordBreak(s1, wordDict1))  # Expected output: True

    # Example 2
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen", "ape"]
    print(solution.wordBreak(s2, wordDict2))  # Expected output: True

    # Example 3
    s3 = "catsincars"
    wordDict3 = ["cats", "cat", "sin", "in", "car"]
    print(solution.wordBreak(s3, wordDict3))  # Expected output: False
