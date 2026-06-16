class Solution {
public:
    int characterReplacement(std::string s, int k) {
      int l = 0;
      int res = 0;
      std::unordered_map<char, int> map;

      for (auto r = 0; r != s.size(); r++) {
        char c = s[r];

        if (map.find(c) == map.end()) {
          map[c] = 1;
        } else {
          map[c]++;
        }

        int length = r - l + 1;

        if (length - biggestInMap(map) > k) {
          map[s[l]]--;
          l++;
        } else if (length > res) {
          res = length;
        }
      }
      return res;
    }

    int biggestInMap(std::unordered_map<char, int> map) {
      int biggest = 0;
      for (const auto& pair : map) {
        if (pair.second > biggest) {
          biggest = pair.second;
        }
      }
      return biggest;
    }
};
