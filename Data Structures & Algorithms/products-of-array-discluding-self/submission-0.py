class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    leftToRight: List[int] = [1, nums[0]]
    rightToLeft: List[int] = [1, nums[-1]]
    for i in range(1, len(nums)-1):
      leftToRight.append(leftToRight[i] * nums[i])
      rightToLeft.append(rightToLeft[i] * nums[len(nums)-i-1])
    
    rightToLeft.reverse()
    
    return list(map(lambda x,y: x * y, leftToRight, rightToLeft))
    