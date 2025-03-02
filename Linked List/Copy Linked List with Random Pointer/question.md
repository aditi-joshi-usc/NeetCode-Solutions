# Copy Linked List with Random Pointer

## Problem Statement
You are given the head of a linked list of length `n`. Unlike a singly linked list, each node contains an additional pointer `random`, which may point to any node in the list, or `null`.

Create a **deep copy** of the list.

The deep copy should consist of exactly `n` new nodes, each including:
- The original value `val` of the copied node.
- A `next` pointer to the new node corresponding to the `next` pointer of the original node.
- A `random` pointer to the new node corresponding to the `random` pointer of the original node.

**Note:** None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

---

## Examples

### Example 1:
**Input:**  
`head = [[3,null],[7,3],[4,0],[5,1]]`  

**Output:**  
`[[3,null],[7,3],[4,0],[5,1]]`  

**Explanation:**  
The deep copy of the list has the same structure as the original list, but all nodes are new.

---

### Example 2:
**Input:**  
`head = [[1,null],[2,2],[3,2]]`  

**Output:**  
`[[1,null],[2,2],[3,2]]`  

**Explanation:**  
The deep copy of the list has the same structure as the original list, but all nodes are new.

---

## Constraints
- `0 <= n <= 100`
- `-100 <= Node.val <= 100`
- `random` is `null` or points to some node in the linked list.

---

## Recommended Time & Space Complexity
- **Time Complexity:** O(n), where `n` is the length of the given list.
- **Space Complexity:** O(n)

---

## Solution

### Approach
To create a deep copy of the linked list, we can use a **hash map** to store the mapping between the original nodes and their corresponding new nodes. This allows us to efficiently set the `next` and `random` pointers for the new nodes.

#### Steps:
1. **Create a mapping of original nodes to new nodes:**
   - Traverse the original list and create a new node for each original node.
   - Store the mapping between the original node and the new node in a hash map.

2. **Set the `next` and `random` pointers for the new nodes:**
   - Traverse the original list again.
   - Use the hash map to set the `next` and `random` pointers for each new node.

3. **Return the head of the new list.**

---

### Algorithm
1. If the input `head` is `null`, return `null`.
2. Create a hash map to store the mapping between original nodes and new nodes.
3. Traverse the original list:
   - For each node, create a new node with the same value and store it in the hash map.
4. Traverse the original list again:
   - For each node, set the `next` and `random` pointers for the corresponding new node using the hash map.
5. Return the new head (the node corresponding to the original head in the hash map).

---

### Code Implementation
Here is the Python implementation:

```python
class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head: Node) -> Node:
    if not head:
        return None

    # Step 1: Create a mapping from original nodes to new nodes
    old_to_new = {}

    current = head
    while current:
        old_to_new[current] = Node(current.val)
        current = current.next

    # Step 2: Set the next and random pointers for the new nodes
    current = head
    while current:
        if current.next:
            old_to_new[current].next = old_to_new[current.next]
        if current.random:
            old_to_new[current].random = old_to_new[current.random]
        current = current.next

    # Step 3: Return the new head
    return old_to_new[head]
