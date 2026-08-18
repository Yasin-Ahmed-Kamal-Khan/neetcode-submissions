# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointerA = head
        pointerB = head

        if pointerA is None:
            return False

        while True:
            if pointerA.next is None:
                return False
            pointerA = pointerA.next

            if pointerA.next is None:
                return False
            pointerA = pointerA.next

            pointerB = pointerB.next

            if pointerB == pointerA:
                return True
