import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxNum = max(piles)
        minNum = max(min(min(piles), math.ceil(maxNum / h)), 1)

        bestTime, bestNum = h, maxNum
        while minNum <= maxNum:
            n = (maxNum + minNum) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / n)

            if hours > h:
                minNum = n + 1
            elif hours <= h:
                maxNum = n - 1

                if n < bestNum:
                    bestTime, bestNum = hours, n

        return bestNum
