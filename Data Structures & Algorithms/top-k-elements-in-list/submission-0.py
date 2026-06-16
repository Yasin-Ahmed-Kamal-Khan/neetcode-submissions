class Solution:
  def __init__(self) -> None:
    pass
  
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    numFreq = dict()
    for num in nums:
      if num not in numFreq:
        numFreq[num] = 1
        next
      
      numFreq[num] += 1
    
    biggestNums = set()
    for i in range (0,k):
      biggest = 0
      biggestFreq = 0
      for num, freq in numFreq.items():
          if biggestFreq < freq and num not in biggestNums:
            biggestFreq = freq
            biggest = num
      
      biggestNums.add(biggest)
      
    return list(biggestNums)