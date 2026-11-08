class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k > sum(candies):
            return 0
        
        left = 1
        right = max(candies)
        ans = 0

        # splitting piles is allowed
        def possible(value):
            total_portions = sum(candy // value for candy in candies)

            return total_portions>=k

        while left <= right:
            mid = (left+right) // 2
            if possible(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans