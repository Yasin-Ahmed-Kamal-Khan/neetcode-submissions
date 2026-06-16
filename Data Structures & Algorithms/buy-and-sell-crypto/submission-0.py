class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    left, right = 0, 0
    maxDiff = 0
    length = len(prices)
    while right != length:
      maxDiff = max(maxDiff, prices[right] - prices[left])
      if prices[left] > prices[right]:
        left = right
      else:
        right += 1
        
    return maxDiff