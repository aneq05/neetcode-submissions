import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        length = len(piles)
        bananas_sum = sum(piles)

        if(length == h):
            return max(piles)
        else:
            return math.ceil(bananas_sum/h)