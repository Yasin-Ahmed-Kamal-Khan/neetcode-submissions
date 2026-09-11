# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseSection(self, head, end, endOfPrevious=None):
        cur = head
        newNext = cur.next

        head.next = end
        while newNext != end:
            temp = newNext.next
            newNext.next = cur
            cur = newNext
            newNext = temp

        if endOfPrevious is not None:
            endOfPrevious.next = cur
        return cur

    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = None
        start = head
        cur = head
        counter = k
        endOfPrevious = None
        while cur is not None:
            cur = cur.next
            counter -= 1
            if counter == 0:
                temp = self.reverseSection(start, cur, endOfPrevious)
                if result is None:
                    result = temp
                if cur is not None:
                    endOfPrevious = start
                    start = cur
                    cur = cur.next
                    counter = k - 1

        return result


        
        
    