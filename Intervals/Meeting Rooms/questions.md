# Meeting Rooms

Given an array of meeting time intervals (each interval represented by `[start, end]`), determine if a person could attend all meetings without any scheduling conflicts.

---

## Problem Statement

- We have an array of intervals, each interval represented by a pair `(start, end)`.
- The condition `start < end` must always hold for each interval.
- We want to check if there are any overlapping intervals. If there is at least one overlap, the answer is `false`; otherwise, `true`.
- Overlapping here means that one interval starts before another one finishes.

### Examples

1. **Example 1**
    - **Input**: `intervals = [(0, 30), (5, 10), (15, 20)]`
    - **Output**: `false`
    - **Explanation**: 
      - `(0, 30)` conflicts with `(5, 10)` (since 5 < 30).
      - `(0, 30)` also conflicts with `(15, 20)` (since 15 < 30).

2. **Example 2**
    - **Input**: `intervals = [(5, 8), (9, 15)]`
    - **Output**: `true`
    - **Note**: `(5, 8)` and `(9, 15)` do not overlap.

---

## Constraints

- `0 <= intervals.length <= 500`
- `0 <= intervals[i].start < intervals[i].end <= 1,000,000`

---

## Key Observations

- Overlap occurs if the start time of the current meeting is earlier than the end time of the previously scheduled meeting.
- If all intervals are sorted by their start time, we only need to check for overlap against the immediately previous interval in the sorted list.

---

## Approach

1. **Sort Intervals by Start Time**  
   Sort the list of intervals in ascending order of their start time.

2. **Check for Overlaps**  
   - Once sorted, iterate through the intervals.
   - For each interval, compare its start time with the end time of the previous interval.
   - If `current.start < previous.end`, then there is an overlap (return `false` immediately).

3. **Return True if No Overlap Found**  
   - If we finish iterating without finding any overlaps, return `true`.

### Time Complexity

- Sorting takes `O(n log n)` where `n` is the number of intervals.
- A single pass to check for overlaps takes `O(n)`.
- Overall complexity: `O(n log n)`.

### Space Complexity

- Sorting in-place yields `O(1)` additional space (depending on the sort implementation). Otherwise, `O(n)` if not in-place.
- We only keep track of the previous interval’s end time, so no additional data structure is needed.

---

