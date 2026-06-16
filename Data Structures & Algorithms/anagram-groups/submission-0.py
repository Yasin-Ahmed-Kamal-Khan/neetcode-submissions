class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      finalList = []
      anagramGroups = dict()
      groupNumber = 0
      for string in strs:
        sortedString = str(sorted(string))
        if sortedString not in anagramGroups:
          anagramGroups[sortedString] = groupNumber
          groupNumber += 1
          finalList.append([])
      
        finalList[anagramGroups[sortedString]].append(string)
      return finalList