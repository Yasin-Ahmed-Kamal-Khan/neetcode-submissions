class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        smallest = min(nums[left], nums[right])
        attempts = 0
        while abs(right - left) >= 1:
            attempts += 1
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid
                print(f"{left=}, {right=}")

            elif nums[mid] < nums[left]:
                right = mid
                smallest = min(nums[mid], smallest)
            if attempts > 10:
                break

        return smallest