# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        first = head
        second = head.next

        if second is None:
            return False

        while second is not None:
            second = second.next

            if second is None:
                return False
            
            second = second.next
            first = first.next

            if first == second:
                return True

        return False