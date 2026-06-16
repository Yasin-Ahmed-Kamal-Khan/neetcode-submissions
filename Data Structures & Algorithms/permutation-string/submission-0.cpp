#include <array>


using namespace std;

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
      if (s1.length() > s2.length()) {
       return false;
      }

      std::array<int, 26> arr = {};

      for (char c : s1) {
        arr[c - 'a']++;
      }

      int l = 0;
      for (int r = s1.length() - 1; r != s2.length(); r++) {
        auto copy = arr;
        for (int c = l; c <= r; c++) {
          copy[s2[c] - 'a']--;
        }

        bool allZero = true;
        for (int i : copy) {
          if (i != 0) {
            allZero = false;
            break;
          }
        }
        if (allZero) {
          return true;
        }
        
        l++;
      }

      return false;
    }
};
