class Solution:
  def maxArea(self, heights: List[int]) -> int:
    left = 0
    right = len(heights) - 1
    
    most = 0
    
    while left != right:
      leftHeight = heights[left]
      rightHeight = heights[right]
      
      volume = min(leftHeight, rightHeight) * (right - left)
      most = max(most, volume)
      
      if leftHeight < rightHeight:
        left += 1
        
      else:
        right -= 1
        
    return most