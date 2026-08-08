class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left = 0
        startEnds = set()
        while height[left] == 0:
            left += 1
            if left >= len(height):
                return 0

        while left < len(height):
            leftHeight = height[left]
            right = left + 1
            if right >= len(height):
                break
            while height[right] < leftHeight:
                right += 1
                if right >= len(height):
                    left = right
                    break
                if height[right] >= leftHeight:
                    startEnds.add((left, right))
                    break

            left = right

        right = len(height) - 1
        while height[right] == 0:
            right -= 1
            if right < 0:
                return 0

        while right >= 0:
            rightHeight = height[right]
            left = right - 1
            if left < 0:
                break
            while height[left] < rightHeight:

                left -= 1
                if left < 0:
                    right = left
                    break
                if height[left] >= rightHeight:
                    startEnds.add((left, right))
                    break

            right = left
        total = 0
        print(startEnds)
        for (left, right) in startEnds:
            maxHeight = min(height[left], height[right])
            i = left + 1
            while i < right:
                total += maxHeight - height[i]
                i += 1


        return total