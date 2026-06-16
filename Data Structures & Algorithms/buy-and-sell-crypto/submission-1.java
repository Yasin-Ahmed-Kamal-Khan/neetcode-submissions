class Solution {
  public int maxProfit(int[] prices) {
    int left = 0;
    int right = 0;
    int maxDiff = 0;

    while (right != prices.length) {
      maxDiff = Math.max(maxDiff, prices[right] - prices[left]);
      
      if (prices[right] < prices[left]) 
        left = right;

      else 
        right++;
    }

    return maxDiff;
  }
}
