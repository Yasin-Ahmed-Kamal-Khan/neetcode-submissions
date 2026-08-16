# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left = list1
        right = list2

        head = left
        if left is None:
            return right
        elif right is None:
            return left

        if left.val > right.val:
            head = right
            right = right.next
        else:
            left = left.next

        current = head

        while left is not None and right is not None:
            if left.val <= right.val:
                temp = left
                left = left.next
                current.next = temp
            else:
                temp = right
                right = right.next
                current.next = temp
            current = current.next


        if left is None:
            current.next = right

        else:
            current.next = left
        
        return head