class Solution:
  def isPalindrome(self, s: str) -> bool:
    newS = re.sub(r'[^\w]', '', s).lower()
    print(newS)
    
    reversedS = newS[::-1]
    return reversedS == newS