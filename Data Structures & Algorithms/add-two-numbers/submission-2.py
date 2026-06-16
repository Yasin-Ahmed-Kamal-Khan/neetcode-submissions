# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        head = None
        carry = False
        last = None
        while cur1 is not None or cur2 is not None:
            val1 = 0
            if cur1 is not None:
                val1 = cur1.val

            val2 = 0
            if cur2 is not None:
                val2 = cur2.val

            digit = val1 + val2
            if carry:
                digit += 1 
                carry = False
                
            if digit >= 10:
                carry = True
                digit -= 10

            newNode = ListNode(digit)

            if head is None:
                head = newNode
            else:
                last.next = newNode

            last = newNode
        
            if cur1 is not None:
                cur1 = cur1.next

            if cur2 is not None:
                cur2 = cur2.next

        if carry:
            last.next = ListNode(1)

        return head