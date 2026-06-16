"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        # dictionary key is the node
        # value is the node that it matches in the copy

        oldToNew = dict()

        newHead = Node(head.val)


        cur = head
        curNew = newHead
        counter = 0

        while cur is not None:
            if cur.random is not None:
                print(f"{cur.random=}")

            oldToNew[cur] = curNew

            cur = cur.next
            if cur is not None:
                newNode = Node(cur.val)
            else:
                newNode = None
            curNew.next = newNode
            curNew = newNode
            counter += 1
            


        curNew = newHead
        cur = head
        newToOld = {v: k for k, v in oldToNew.items()}

        while curNew is not None:
            if cur.random is not None:
                print(f"{cur.random=}")
                nextRandomNode = oldToNew.get(cur.random)
                print(f"{nextRandomNode=}")
                if nextRandomNode is not None:
                    curNew.random = nextRandomNode
            curNew = curNew.next
            cur = cur.next


        return newHead