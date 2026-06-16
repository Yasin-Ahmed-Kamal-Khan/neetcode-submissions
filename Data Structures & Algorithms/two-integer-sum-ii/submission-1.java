class Solution {
  public int[] twoSum(int[] numbers, int target) {
    int i = 0;
    int j = numbers.length -1;

    int total = numbers[i] + numbers[j];

    while (total != target) {
      if (total < target) i++;
      else j--;

      total = numbers[i] + numbers[j];
    }

    return new int[] {i+1, j+1};
  }
}
