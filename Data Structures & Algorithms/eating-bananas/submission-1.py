import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = math.ceil(sum(piles)/h)

        while True:
            hours = sum(math.ceil(p/k) for p in piles)

            if hours <= h:
                return k
            k += 1