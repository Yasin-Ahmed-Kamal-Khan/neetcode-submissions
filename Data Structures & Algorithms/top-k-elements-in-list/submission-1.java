class Solution {
  public static int[] topKFrequent(int[] nums, int k) {
    HashMap<Integer, Integer> numFreq = new HashMap<Integer, Integer>();
    
    Arrays.stream(nums).forEach(num -> {
      numFreq.compute(num, (key, freq) -> (freq == null) ? 0 : freq + 1);
    });
    
    List<List<Integer>> numFreqList = new ArrayList<>(nums.length);
    
    for (int i = 0; i != nums.length; i++) {
      numFreqList.add(new ArrayList<>());
    }
    
    numFreq.forEach((num, freq) -> { 
      numFreqList.get(freq).add(num);
    });

    int[] finalList = new int[k];
    
    int left = k - 1;

    for (int i = numFreqList.size() - 1; i !=  -1; i--) {
      for (int j = 0; j != numFreqList.get(i).size(); j++) {
        finalList[left] = numFreqList.get(i).get(j);
        left--;

        if (left == -1) {
          return finalList;
        }
      }
    }

    System.out.println("stuffffffff");
    return null;
  }
}
