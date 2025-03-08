# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        carry = 0

        res = ListNode(0)

        dummy = res


        while l1 or l2:

            sum = 0
            if l1:
                sum+= l1.val
                l1 = l1.next
            if l2:
                sum+=l2.val
                l2 = l2.next
            sum+= carry
            res.next = ListNode(sum %10)
            res = res.next
            carry = sum // 10

        if carry>0:
            res.next = ListNode(carry, None)
        return dummy.next
            


        
