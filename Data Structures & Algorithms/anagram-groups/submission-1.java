class Solution {
  public List<List<String>> groupAnagrams(String[] strs) {
    int[] numberOfEachLetter = new int[26];
    Map<Integer, Integer> letterHashToIndex = new HashMap<>();
    List<List<String>> finalList = new ArrayList<>(); 
    int index = 0;
    for (String str : strs) {

        for (int i = 0; i != str.length(); i++) {
          numberOfEachLetter[str.charAt(i) - 'a']++;
        }
        int hashValue = Arrays.hashCode(numberOfEachLetter);

        if (!letterHashToIndex.containsKey(hashValue)) {
          letterHashToIndex.put(hashValue, index);
          index++;
          finalList.add(new ArrayList<>());
        }

        finalList.get(letterHashToIndex.get(hashValue)).add(str);
        Arrays.fill(numberOfEachLetter, 0);
    }
    return finalList;      
  }
}
