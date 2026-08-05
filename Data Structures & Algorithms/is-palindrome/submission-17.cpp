
class Solution {
public:
    bool isPalindrome(std::string s) {
        toLower(s);
        std::cout << s << std::endl;
        auto left = 0;
        auto right = s.length() - 1;

        while (left <= right) {
            if (left >= s.length()) break;
            if (right < 0) break;

            if (not isAlphaNum(s[left])) left++;
            else if (not isAlphaNum(s[right])) right--;
            else if (s[left] != s[right]) {
                return false;
            }
            else {
                left++; right--;
            }
        }
        return true;
    }

    void toLower(std::string& s) {
        for (auto i = 0; i != s.length(); i++) {
            auto c = s[i];
            if (c <= 'Z' and c >= 'A') s[i] -= 'A' - 'a';
        }
    }

    bool isAlpha(char c) {
        return c >= 'a' and c <= 'z';
    }

    bool isNum(char c) {
        return c >= '0' and c < '9';
    }

    bool isAlphaNum(char c) {
        return isAlpha(c) or isNum(c);
    }
};
