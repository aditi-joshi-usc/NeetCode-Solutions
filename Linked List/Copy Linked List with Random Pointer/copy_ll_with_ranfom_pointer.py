"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldnew = {None: None}

        node = head
        while node:
            oldnew[node] = Node(node.val)
            node = node.next
        

        node = head

        while node:
            oldnew[node].next = oldnew[node.next]
            oldnew[node].random = oldnew[node.random]
            node = node.next
        return oldnew[head]
