
class Solution {
    public int characterReplacement(String s, int k) {
      Map<Character, Integer> map = new HashMap<>();

      char[] chars = s.toCharArray();
      int left = 0;
      int res = 0;
      for (int right = 0; right != chars.length; right++) {
        char cRight = chars[right];
        char cLeft = chars[left];
        map.put(cRight, map.getOrDefault(cRight, 0) + 1);

        int length = right - left + 1;
        if (length - mostCommon(map) > k) {
          map.put(cLeft, map.get(cLeft) - 1);
          left++;
        } else if (length > res) {
          res = length;
        }
      }

      return res;
    }

    public int mostCommon(Map<Character, Integer> pairsMap) {
      int max = 0;
      for (int entry : pairsMap.values()) {
        if (entry > max) {
          max = entry;
        }
      }
      return max;
    }
}
