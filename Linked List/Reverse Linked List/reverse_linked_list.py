# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Iteration
        if not head:
            return None

        curr  = head
        back_val = None
        while curr:
            sec_val = curr.next
            if curr == head:
                curr.next = None
            else:
                curr.next = back_val
            back_val = curr
            curr = sec_val
        return back_val

        #recursion
        # if head is None:
        #     return None

        # curr = head

        # if curr.next:
        #     curr = self.reverseList(head.next)
        #     head.next.next = head
        
        # head.next = None

        # return curr

