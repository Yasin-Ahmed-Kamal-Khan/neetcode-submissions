# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if head == None:
         return None

      second = head
      if second.next == None:
         return head

      first = second.next
      second.next = None
      while first.next != None:
        new_first = first.next
        first.next = second
        second = first
        first = new_first
        print(f"{new_first.val=} {second.val=}, {new_first.next=} {second.next=}")

      first.next = second
      cur = first
      print(f"{cur.val} {cur.next}")

      while cur.next != None:
        print(cur.val)
        cur = cur.next
      return first


# a b c d
