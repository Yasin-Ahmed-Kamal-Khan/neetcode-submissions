from typing import List

class Solution:
  def __init__(self) -> None:
    pass
   
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashMap = dict()
    for i, n in enumerate(nums):
      diff = target - n
      if diff in hashMap:
        return [hashMap[diff], i]
      hashMap[n] = i