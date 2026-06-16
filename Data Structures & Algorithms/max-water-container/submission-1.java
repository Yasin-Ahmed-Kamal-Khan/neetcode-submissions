class Solution {
  public int maxArea(int[] heights) {
    int left = 0;
    int right = heights.length - 1;

    int most = 0;
    int area = 0;
    while (left != right) {
      area = Math.min(heights[left], heights[right]) * (right - left);

      most = Math.max(area, most);
      
      if (heights[left] < heights[right]) 
        left++;

      else 
        right--;
    }

    return most;
  }
}
