
class Solution {
    public boolean isAnagram(String s, String t) {
    
    if (s.length() != t.length()) {
      return false;
    }

    HashMap<Character, Integer> hashMap = new HashMap<>();
    
    for (char letter = 'a'; letter <= 'z'; letter++) {
      hashMap.put(letter, 0);
    }

    for (int i = 0; i != s.length(); i++) {
      hashMap.put(t.charAt(i), hashMap.get(t.charAt(i)) - 1); 
      hashMap.put(s.charAt(i), hashMap.get(s.charAt(i)) + 1); 
    }

    return hashMap.values().stream().allMatch(x -> x == 0);
  }
}
