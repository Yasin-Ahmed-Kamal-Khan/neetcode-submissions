class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while nums[left] > nums[right] and abs(left - right) > 1:
            print(f"{left=}, {right=}")
            middle = (left + right) // 2
            if nums[middle] > nums[left]:
                left = middle + 1
            else:
                right = middle
        return min(nums[right], nums[left])