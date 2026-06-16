class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while right - left > 1:
            print(f"{left=}, {right=}, {nums[left]=}, {nums[right]=}")
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[left] < target and target < nums[mid]:
                right = mid

            elif nums[right] > target and target > nums[mid]:
                left = mid

            elif nums[mid] > target and nums[left] < nums[mid]:
                left = mid

            elif nums[mid] < target and nums[right] > nums[mid]:
                right = mid

            elif nums[mid] < target:
                left = mid

            else:
                right = mid

        if nums[left] == target:
                return left
        elif nums[right] == target:
            return right

        return -1 