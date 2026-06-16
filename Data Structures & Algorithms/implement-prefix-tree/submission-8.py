class Node:
    end = False
    children = dict()

    def __init__(self):
      self.children = dict()

    def setEnd(self):
      self.end = True

    def contains(self, char):
        return char in self.children

    def nextNode(self, char):
       return self.children[char]

    def insert(self, c):
      self.children[c] = Node()

    def isEnd(self):
       return self.end

class PrefixTree:
    head = Node()

    def __init__(self):
       self.head = Node()

    def insert(self, word: str) -> None:
      cur = self.head
      for c in word:
        if not cur.contains(c):
          cur.insert(c)
        cur = cur.nextNode(c)

      cur.setEnd()



    def search(self, word: str) -> bool:
      cur = self.head
      for c in word:
          if not cur.contains(c):
             return False
          cur = cur.nextNode(c)

      return cur.isEnd()


    def startsWith(self, prefix: str) -> bool:
      cur = self.head
      print(cur.children)
      for c in prefix:
         if not cur.contains(c):
            return False

         cur = cur.nextNode(c)

      return True
