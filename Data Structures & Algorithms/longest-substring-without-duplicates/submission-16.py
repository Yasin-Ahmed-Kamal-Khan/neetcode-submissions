class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        charPos = dict()


        pointer = 0
        longest = 0
        start = 0
        while pointer < len(s):
            if s[pointer] in charPos:
                start = max(charPos[s[pointer]] + 1, start)
            charPos[s[pointer]] = pointer
            longest = max(pointer - start + 1, longest)
            pointer += 1

        return longest