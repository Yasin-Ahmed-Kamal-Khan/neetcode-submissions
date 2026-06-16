class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    numbersInGroup = {str(i): 0 for i in range(1,10)}
    numbersInGroup['.'] = 0

    #check rows
    for row in range(0,9):
      for boxInRow in range(0,9):
        numbersInGroup[board[row][boxInRow]] += 1
      
      if any(i > 1 for i in list(numbersInGroup.values())[:-1]):
        return False

      for key in numbersInGroup:
        numbersInGroup[key] = 0
        
    for column in range(0,9):
      for boxInColumn in range(0,9):
        numbersInGroup[board[boxInColumn][column]] += 1
      
      if any(i > 1 for i in list(numbersInGroup.values())[:-1]):
        return False

      for key in numbersInGroup:
        numbersInGroup[key] = 0

    for column in range(0,7,3):
      for row in range(0,7,3):
        for i in range(3):
          for j in range(3):
            numbersInGroup[board[row+i][column+j]] += 1
                
        if any(i > 1 for i in list(numbersInGroup.values())[:-1]):
          return False

        for key in numbersInGroup:
          numbersInGroup[key] = 0
        
    return True