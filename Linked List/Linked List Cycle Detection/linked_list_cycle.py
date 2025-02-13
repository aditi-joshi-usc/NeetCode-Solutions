# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Hashing 
        # Time Complexity = O(n)
        # Space Complexity = O(n)
        # visited = set()

        # while head:
        #     if head.val in visited:
        #         return True
            
        #     visited.add(head.val)
        #     head = head.next
            
        # return False

        # slow fast pointers
        # Time Complexity = O(n)
        # Space Complexity = O(1)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
