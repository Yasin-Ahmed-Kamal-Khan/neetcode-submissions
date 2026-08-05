class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)
        print(len(numSet))
        return len(numSet) != len(nums)
            