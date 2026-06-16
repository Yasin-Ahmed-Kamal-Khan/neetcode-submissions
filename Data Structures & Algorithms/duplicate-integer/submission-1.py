class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            counter = 0
            for j in nums:
                if i == j:
                    counter+=1
            if counter > 1:
                return True
        return False
         