class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # if coins(len) == 1 and coins[0] < amount and amount % coins[0] != 0:
        #     return -1
        # if coins(len) == 1 and coins[0] > amount:
        #     return 0
        memo = {}
        def dp(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float("inf")
            if remaining in memo:
                return memo[remaining]

            best = float("inf")

            for coin in coins:
                candidate = 1 + dp(remaining - coin)
                best = min(candidate, best)
            memo[remaining] = best
            return best
        result = dp(amount)
        return result if result != float("inf") else -1