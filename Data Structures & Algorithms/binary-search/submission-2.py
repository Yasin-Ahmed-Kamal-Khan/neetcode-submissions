class Solution:
    def search(self, nums: List[int], target: int) -> int:
        upper = len(nums)
        pointer = len(nums) // 2
        lower = 0
        visited = set()

        while pointer not in visited:
            visited.add(pointer)
            if nums[pointer] == target:
                return pointer
            elif nums[pointer] > target:
                upper = pointer
            else:
                lower = pointer

            pointer = (lower + upper) // 2

        return -1