# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        nodes = 1
        if fast is None:
            return head
        while True:
            if fast.next is not None:
                nodes += 1
                fast = fast.next
            else:
                break

            if fast.next is not None:
                nodes += 1
                fast = fast.next
            else:
                break

            slow = slow.next

        if nodes % 2 == 0:
            slow = slow.next
        if nodes <= 2:
            return
        prev = slow
        current = prev.next
        prev.next = None
        while True:
            print(nodes)
            if current.next is None:
                current.next = prev
                break
            temp = current.next
            current.next = prev
            prev = current
            current = temp


        left = head
        end = current

        while True:
            if left.next is None:
                break

            t1 = left.next
            left.next = current

            if current.next is None:
                break
            t2 = current.next
            current.next = t1
            left = t1
            current = t2


