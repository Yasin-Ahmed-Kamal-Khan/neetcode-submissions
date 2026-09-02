
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.nex = None 

class LinkedList:
    def __init__(self):
        self.head = None
        self.back = None

    def pop_back(self):
        if self.back is None:
            return

        oldBack = self.back

        if oldBack == self.head:
            self.back = None
            self.head = None
            return oldBack.value

        self.back = oldBack.prev
        self.back.nex = None
        return oldBack.value

    def remove_and_insert_front(self, node):        
        if node.prev is None and node.nex is None:
            return

        if node.nex is None:

            node.prev.nex = None
            self.back = node.prev
            node.nex = self.head
            self.head.prev = node
            self.head = node
            node.prev = None

            return

        if node.prev is None:
            return
    

        prev = node.prev
        nex = node.nex
        prev.nex = nex
        nex.prev = prev

        node.prev = None
        node.nex = self.head
        self.head.prev = node

        self.head = node
        return


    def push_front(self, node):
        if self.head is not None:
            self.head.prev = node
            node.nex = self.head

        else:
            self.back = node
        self.head = node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curSize = 0
        self.hashMap = dict()
        self.recents = LinkedList()

    def get(self, key: int) -> int:
        if key in self.hashMap:
            val, node = self.hashMap[key]
            self.recents.remove_and_insert_front(node)
            return val

        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            val, node = self.hashMap[key]
            self.recents.remove_and_insert_front(node)
            self.hashMap[key] = (value, node)


        else:
            node = Node(key)
            self.recents.push_front(node)
            self.hashMap[key] = (value, node)
            self.curSize += 1
            if self.curSize > self.capacity:
                keyToRemove = self.recents.pop_back()
                if keyToRemove not in self.hashMap:
                    return

                self.hashMap.pop(keyToRemove)
        
