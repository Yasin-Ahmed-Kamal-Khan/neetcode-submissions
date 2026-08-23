class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        occurences = dict()
        longest = 0

        while right != len(s):
            if s[right] in occurences:
                occurences[s[right]] += 1
            else:
                occurences[s[right]] = 1

            mostFreq = max(occurences.values())

            nonMostFreqChar = right - left + 1 - mostFreq

            while nonMostFreqChar > k:

                occurences[s[left]] -= 1
                left += 1
                mostFreq = max(occurences.values())
                nonMostFreqChar = right - left + 1 - mostFreq


            longest = max(longest, right - left + 1)
            right += 1

        return longest