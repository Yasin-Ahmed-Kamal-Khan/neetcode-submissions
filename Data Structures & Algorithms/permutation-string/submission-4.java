
class Solution {
    public boolean checkInclusion(String s1, String s2) {
      if (s1.length() > s2.length()) {
        return false;
      }

      int[] s1Chars = new int[26];
      int[] s2Chars = new int[26];
      int matches = 0;

      for (char c : s1.toCharArray()) {
        s1Chars[c - 'a']++;
      }

      for (int i = 0; i < s1.length(); i++) {
        s2Chars[s2.charAt(i) - 'a']++;
      }

      for (int i = 0; i != 26; i++) {
        if (s1Chars[i] == s2Chars[i]) {
          matches++;
        }
      }
      System.out.println(matches);


      int l = 0;
      for (int r = s1.length(); r != s2.length(); r++) {
        if (matches == 26) return true;
        int rChar = s2.charAt(r) - 'a';
        int lChar = s2.charAt(l) - 'a';

        s2Chars[rChar]++;

        if (s2Chars[rChar] == s1Chars[rChar]) {
          matches++;
        } else if (s2Chars[rChar] - 1 == s1Chars[rChar]) {
          matches--;
        }

        s2Chars[lChar]--;
        if (s2Chars[lChar] == s1Chars[lChar]) {
          matches++;
        } else if (s2Chars[lChar] + 1 == s1Chars[lChar]) {
          matches--;
        }

        System.out.println("matches=" + matches + "\nlchar=" + lChar);
        l++;


      }

      return matches == 26;
    }
}
