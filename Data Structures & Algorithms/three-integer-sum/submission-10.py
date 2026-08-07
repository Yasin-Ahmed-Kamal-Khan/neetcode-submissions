# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
# 
# 


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        last = None
        for i, num in enumerate(nums):
            if last == num:
                continue
            else:
                last = num
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = num + nums[left] + nums[right]
                if total == 0:
                    result.append([num, nums[left], nums[right]])
                    while True:
                        left += 1
                        if left >= len(nums):
                            break
                        if nums[left] != nums[left - 1]:
                            break

                    while True:
                        right -= 1
                        if right <= i:
                            break
                        if nums[right] != nums[right + 1]:
                            break
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return result

x = Solution()
print(x.threeSum([-1,0,1,2,-1,-4]))