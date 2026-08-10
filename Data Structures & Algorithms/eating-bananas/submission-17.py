from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        biggest = max(piles)
        smallest = 1

        possible = biggest

        while smallest < biggest:
            middle = (biggest + smallest) // 2
            sessions = 0
            for num in piles:
                sessions += ceil(num / middle)

            print(sessions)
            if sessions <= h:
                biggest = middle 
                possible = min(middle, possible)

            elif sessions > h:
                smallest = middle + 1

            

        return possible