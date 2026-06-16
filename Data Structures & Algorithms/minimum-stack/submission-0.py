class MinStack:
  def __init__(self):
    self.minStack = []
    self.mainStack = []

  def push(self, val: int) -> None:
    self.mainStack.append(val)
    
    if len(self.minStack) == 0:
      self.minStack.append(val)
    
    elif val < self.minStack[-1]:
      self.minStack.append(val)
      
    else:
      self.minStack.append(self.minStack[-1])
    
  def pop(self) -> None:
    self.mainStack.pop()
    self.minStack.pop()

  def top(self) -> int:
    return self.mainStack[-1]

  def getMin(self) -> int:
    return self.minStack[-1]