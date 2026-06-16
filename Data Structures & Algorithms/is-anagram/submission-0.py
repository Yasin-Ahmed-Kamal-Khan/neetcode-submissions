import string
class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
      char_dict = {char: 0 for char in string.ascii_lowercase}
       
      for char in s:
         char_dict[char] += 1
      
      for char in t:
         char_dict[char] -= 1
      
      return all(map(lambda x: x == 0, char_dict.values()))
        