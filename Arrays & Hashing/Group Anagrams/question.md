# Group Anagrams

## Problem Statement
Given an array of strings `strs`, group all anagrams together into sublists. Return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

## Examples

**Example 1:**  
Input: strs = ["act","pots","tops","cat","stop","hat"]  
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

**Example 2:**  
Input: strs = ["x"]  
Output: [["x"]]

**Example 3:**  
Input: strs = [""]  
Output: [[""]]

## Approach

To group anagrams together, we need to identify which strings are anagrams of each other. Two strings are anagrams if they contain the same characters with the same frequency. We can use a sorted string as a key to identify anagrams.

The algorithm works as follows:
1. Create a hashmap to store groups of anagrams
2. For each string in the input array:
   a. Sort the characters of the string to create a key
   b. Add the original string to the list associated with that key in the hashmap
3. Return the values of the hashmap (which are the anagram groups)

## Solution

```python
def groupAnagrams(strs):
    anagram_map = {}
    
    for s in strs:
        # Sort the string to create a key
        sorted_s = ''.join(sorted(s))
        
        # If we haven't seen this sorted string before, create a new list
        if sorted_s not in anagram_map:
            anagram_map[sorted_s] = []
        
        # Add the original string to its anagram group
        anagram_map[sorted_s].append(s)
    
    # Return all the anagram groups
    return list(anagram_map.values())

# Test with the examples
print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))  # [["hat"],["act", "cat"],["stop", "pots", "tops"]]
print(groupAnagrams(["x"]))  # [["x"]]
print(groupAnagrams([""])) # [[""]]
```

## Time and Space Complexity

- **Time Complexity**: O(m * n log n), where m is the number of strings and n is the length of the longest string. This is because for each string, we need to sort it which takes O(n log n) time.
- **Space Complexity**: O(m * n), where m is the number of strings and n is the length of the longest string. This is because in the worst case, each string forms its own group, and we need to store all strings.
