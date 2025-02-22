# Top K Frequent Elements

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements in the array.

You may return the answer in any order.

## Examples

**Example 1:**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**
```
Input: nums = [1], k = 1
Output: [1]
```

## Constraints
- `1 <= nums.length <= 10^4`
- `-1000 <= nums[i] <= 1000`
- `k` is in the range `[1, the number of unique elements in the array]`
- It is guaranteed that the answer is unique

## Recommended Time & Space Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)
where n is the size of the input array.

## Solution Approaches

### Approach 1: Hash Map + Heap
1. Count the frequency of each element using a hash map
2. Use a min-heap of size k to keep track of the k most frequent elements
3. Return the elements in the heap

### Approach 2: Hash Map + Bucket Sort
1. Count the frequency of each element using a hash map
2. Create a bucket array where the index represents frequency
3. Iterate through the bucket array from highest frequency to lowest
4. Collect the k most frequent elements

## Python Implementation (Bucket Sort)

```python
from collections import defaultdict

def topKFrequent(nums, k):
    # Count frequency of each number
    counter = defaultdict(int)
    for num in nums:
        counter[num] += 1
    
    # Create frequency buckets
    bucket = [[] for _ in range(len(nums) + 1)]
    for num, freq in counter.items():
        bucket[freq].append(num)
    
    # Collect k most frequent elements
    result = []
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result  # This line should never be reached given the constraints
```

## Complexity Analysis
- Time Complexity: O(n) where n is the length of nums
- Space Complexity: O(n) for storing the frequency map and bucket array
