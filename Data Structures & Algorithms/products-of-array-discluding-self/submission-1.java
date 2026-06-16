class Solution {
  public static int[] productExceptSelf(int[] nums) {
    int size = nums.length;

    int[] leftToRight = new int[size];
    int[] rightToLeft = new int[size];

    leftToRight[0] = 1;
    leftToRight[1] = nums[0];

    rightToLeft[0] = 1;
    rightToLeft[1] = nums[size - 1];
    
    for (int i = 2; i != size; i++) {
      rightToLeft[i] = rightToLeft[i - 1] * nums[size - i];
      leftToRight[i] = leftToRight[i - 1] * nums[i - 1];
    }

    System.out.println(Arrays.toString(rightToLeft));

    int[] finalArray = new int[size];
    for (int i = 0; i != size; i++) {
      finalArray[i] = leftToRight[i]  * rightToLeft[size - 1 -i];
    }
    
    return finalArray;
  }
}  
