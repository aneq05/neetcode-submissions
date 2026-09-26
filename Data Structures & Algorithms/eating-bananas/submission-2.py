import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def possible(speed):

            hours = 0

            for pile in piles:
                hours += math.ceil(pile/speed)

            return hours <= h


        left = 1
        right = max(piles)

        while left < right:
            mid = (right + left) // 2

            if possible(mid):
                right = mid
            else:
                left = mid + 1

        return left

