# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, counter = head, 0

        while first is not None:
            first = first.next
            counter += 1

        print(f"{counter=}")

        if n == counter:
            if head.next is None:
                return None
            else:
                return head.next


        prev, cur = head, head.next
        while counter - n > 1:
            counter = counter - 1
            cur = cur.next
            prev = prev.next
        
        if cur is None:
            prev.next = None
        else:
            prev.next = cur.next

        return head


        
        