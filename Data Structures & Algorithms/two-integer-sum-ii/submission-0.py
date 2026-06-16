class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    i = 0
    j = len(numbers) - 1
    
    total = numbers[i] + numbers[j]
    while total != target:
      if total < target:
        i += 1
      else:
        j -= 1
      total = numbers[i] + numbers[j]
      
    return [i+1,j+1]