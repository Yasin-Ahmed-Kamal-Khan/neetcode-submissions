class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pointer, biggest, soFar = 0, 0, 0
        charsSoFar = dict()
        counter = 0
        while pointer != len(s):
            print(f"{pointer=}, {s[pointer]=}")
            if s[pointer] not in charsSoFar:
                charsSoFar[s[pointer]] = pointer
                soFar += 1
                pointer += 1
            else:
                if s[pointer] != s[pointer - 1]:
                    pointer = charsSoFar[s[pointer]] + 1
                
                biggest = max(biggest, soFar)
                soFar = 0
                charsSoFar = dict()

            counter += 1
            # if counter > 100:
            #     break

        return max(biggest, soFar)