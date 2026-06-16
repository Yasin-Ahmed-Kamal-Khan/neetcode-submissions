# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        item_a = list1
        item_b = list2

        if item_a is None:
            return item_b
        elif item_b is None:
            return item_a

        if item_a.val < item_b.val:
            last = item_a
            item_a = item_a.next
        else:
            last = item_b
            item_b = item_b.next


        first = last
        while item_a is not None and item_b is not None:
            if item_a.val < item_b.val:
                last.next = item_a
                last = item_a
                item_a = item_a.next

            else:
                last.next = item_b
                last = item_b
                item_b = item_b.next

        if item_a is None:
            last.next = item_b
        else:
            last.next = item_a

        return first