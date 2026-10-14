class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dp(i):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]

            one_step = cost[i] + dp(i+1) 
            two_steps = cost[i] + dp(i+2)
            min_steps = min(one_step, two_steps)
            memo[i] = min_steps

            return min_steps
        
        return min(dp(0), dp(1))
