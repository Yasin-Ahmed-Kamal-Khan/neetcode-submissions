class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    if nums == []:
      return 0
    
    numSet = set(nums)
    seen = set()
    longest = 1
    currentLength = 1
    for currentNum in nums:
      if currentNum in seen:
        next
        
      while True:
        seen.add(currentNum)
        if currentNum + 1 in numSet:
          currentNum += 1
          currentLength += 1
        else:
          if currentLength > longest:
            longest = currentLength
          currentLength = 1
          break
          
    return longest