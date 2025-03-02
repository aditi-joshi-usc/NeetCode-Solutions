# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # lenll = 0
        # node = head
        # while node:
        #     node = node.next
        #     lenll+=1
        
        # n = lenll-n-1
        # node = head
        # if n <0:
        #     if lenll == 1:
        #         return None
        #     else:
        #         head=head.next
        # while n>0:
        #     node = node.next
        #     n-=1
        # node.next = node.next.next

        # return head
        dummy = ListNode(0,head)
        right = head
        left = dummy


        while n>0 and right:
            right = right.next
            n-=1
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next
