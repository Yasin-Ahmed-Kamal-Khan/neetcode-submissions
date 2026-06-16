class Solution:
  def __init__(self) -> None:
    pass  
  
  def encode(self, strs: List[str]) -> str:
    #["we","say",":","yes"]
    #produces ["10,2,5,6,9,wesay:yes"]
    
    separators = []
    charNum = 0
    numberOfSeparators = len(strs) + 1
    for string in strs:
      for char in string:
        charNum += 1
      separators.append(str(charNum) + ",")
    separators = separators + strs
      
    return str(numberOfSeparators) + ',' + "".join(separators)

  def decode(self, s: str) -> List[str]:
    numberOfSeparators = int(s.split(',', 1)[0])
    separatedString = s.split(',', numberOfSeparators)
    
    finalList: List[str] = []
    string = separatedString[-1]
    for current, next in zip([0] + separatedString[1:-2], separatedString[1:-1]):
      finalList.append(string[int(current): int(next)])
    return finalList