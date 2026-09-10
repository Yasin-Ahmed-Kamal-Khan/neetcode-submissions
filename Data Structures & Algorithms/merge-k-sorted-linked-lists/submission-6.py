# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = list(filter(lambda x: x is not None, lists))
        
        if nodes == []:
            return None

        i, result = min(enumerate(nodes), key=lambda pair: pair[1].val)
        back = result
        nodes[i] = nodes[i].next
        count = 0
        while True:
            last = back.val
            smallestNode = None
            index = None
            atLeastOneNode = False
            index = None
            for i, node in enumerate(nodes):
                if node is None:
                    continue

                atLeastOneNode = True

                if smallestNode is None:
                    smallestNode = node
                    index = i
                else:
                    if smallestNode.val > node.val:
                        smallestNode = node
                        index = i
                if smallestNode.val == last:
                    break

            if not atLeastOneNode:
                back.next = None
                return result

            count += 1
            back.next = smallestNode
            back = smallestNode
            if smallestNode.next:
                nodes[index] = smallestNode.next
            else:
                nodes.pop(index)


                
