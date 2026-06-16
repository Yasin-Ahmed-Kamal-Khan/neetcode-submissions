class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      sortedNums = sorted(nums)
      i = 0
      j = len(nums) - 1

      while (sortedNums[i] + sortedNums[j] != target):
        if sortedNums[i + 1] + sortedNums[j] > target:
          j -= 1
               
        else:
          i += 1

      for it in range(0, len(nums)):
        if sortedNums[i] == nums[it]:
          i = it
          break

      for it in range(0, len(nums)):
        if sortedNums[j] == nums[it] and it != i:
          j = it
          break  

      if i > j:
        return [j, i]
      return [i, j]     