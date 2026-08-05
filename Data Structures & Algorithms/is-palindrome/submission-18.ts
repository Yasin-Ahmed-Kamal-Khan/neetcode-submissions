class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
  isPalindrome(s: string): boolean {
      s = s.toLowerCase()
      let left: number = 0;
      let right = s.length - 1;

      while (left < right) {
        if (left >= s.length) break;
        else if (right < 0) break;
        else if (!this.isAlphaNum(s[left])) left++;
        else if (!this.isAlphaNum(s[right])) right--;
        else if (s[left] == s[right]) {
          left++; right--;
        }
        else return false;
      }
    return true;
  }

  isAlphaNum(c: string): boolean {
    if (c.valueOf() >= 'a' && c.valueOf() <= 'z') return true;
    if (c.valueOf() >= '0' && c.valueOf() <= '9') return true;
    return false;
  }
}
