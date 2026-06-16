from typing import List
from collections import Counter

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    numDict = Counter(nums)
    finalSet = set()
    
    for numA, countA in numDict.items():
      for numB, countB in numDict.items():
        numC = - numA - numB
        
        if numC in numDict:
          
          CIsA = numC == numA
          BIsA = numB == numA
          BIsC = numB == numC
          
          if CIsA and BIsA and countA < 3:
            continue
          
          if ((BIsC or BIsA) and countB < 2) or (CIsA and countA < 2):
            continue
          
          triple = tuple(sorted([numA, numB, numC]))
          finalSet.add(triple)
          
          
    return [list(x) for x in finalSet]
  
x = Solution()
print(x.threeSum([0,0,0]))