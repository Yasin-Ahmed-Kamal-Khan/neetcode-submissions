class Solution:
    def toShifted(self, num):
        if num + self.shift >= self.length:
            return num + self.shift - self.length

        return num + self.shift

    def fromShifted(self, num):
        if num - self.shift < 0:
            return num - self.shift + self.length

        return num - self.shift

    def search(self, nums: List[int], target: int) -> int:
        self.length = len(nums)
        left = 0
        right = len(nums) - 1
        while nums[left] > nums[right] and abs(left - right) > 1:
            middle = (left + right) // 2
            if nums[middle] > nums[left]:
                left = middle + 1
            else:
                right = middle
        self.shift = right
        if nums[left] < nums[right]:
            self.shift = left
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[self.toShifted(middle)] < target:
                left = middle + 1
            elif nums[self.toShifted(middle)] > target:
                right = middle - 1
            else:
                return self.toShifted(middle)
        return -1
        
