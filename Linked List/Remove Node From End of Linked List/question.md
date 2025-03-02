# Remove Node From End of Linked List

## Problem Statement
You are given the beginning of a linked list `head`, and an integer `n`.

Remove the **nth node** from the end of the list and return the beginning of the list.

---

## Examples

### Example 1:
**Input:**  
`head = [1,2,3,4]`, `n = 2`  

**Output:**  
`[1,2,4]`  

**Explanation:**  
The second node from the end is `3`, which is removed from the list.

---

### Example 2:
**Input:**  
`head = [5]`, `n = 1`  

**Output:**  
`[]`  

**Explanation:**  
The only node in the list is removed, resulting in an empty list.

---

### Example 3:
**Input:**  
`head = [1,2]`, `n = 2`  

**Output:**  
`[2]`  

**Explanation:**  
The first node from the end is `1`, which is removed from the list.

---

## Constraints
- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

---

## Recommended Time & Space Complexity
- **Time Complexity:** O(N), where N is the length of the given list.
- **Space Complexity:** O(1)

---

## Solution

### Approach
To remove the nth node from the end of the linked list efficiently, we can use the **two-pointer technique**:
1. Initialize two pointers, `first` and `second`, both pointing to the head of the list.
2. Move the `first` pointer `n` steps ahead in the list.
3. Move both pointers (`first` and `second`) simultaneously until the `first` pointer reaches the end of the list.
4. At this point, the `second` pointer will be pointing to the node just before the node that needs to be removed.
5. Adjust the `next` pointer of the `second` node to skip the nth node from the end.

---

### Algorithm
1. Initialize `first` and `second` pointers to the head of the list.
2. Move the `first` pointer `n` steps ahead.
3. If `first` reaches the end after moving `n` steps, return `head.next` (removing the head).
4. Move both pointers until `first` reaches the end:
   - Move `first` one step forward.
   - Move `second` one step forward.
5. Adjust the `next` pointer of the `second` pointer to skip the nth node.
6. Return the modified list starting from `head`.

---

### Code Implementation
Here is the Python implementation:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)  # Create a dummy node to simplify edge cases
    first = dummy
    second = dummy

    # Move first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next

    # Move both pointers until first reaches the end
    while first:
        first = first.next
        second = second.next

    # Remove the nth node from the end
    second.next = second.next.next

    return dummy.next  # Return the head of the modified list
