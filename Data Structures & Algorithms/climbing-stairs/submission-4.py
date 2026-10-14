class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(i): # i -> the remaining number of steps till the end
            if i == 0:
                return 1
            if i < 0:
                return 0
            if i in memo:
                return memo[i]

            ways = dp(i-1) + dp(i-2)
            memo[i] = ways
            return ways

        return dp(n)
