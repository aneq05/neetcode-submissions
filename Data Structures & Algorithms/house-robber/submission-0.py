class Solution:
    def rob(self, nums: List[int]) -> int:
        # cost = nums[i] + dp(i+1)
        memo = {}
        
        def dp(i):
            if i>=len(nums):
                return 0

            if i in memo:
                return memo[i]

            rob = nums[i] + dp(i+2)
            skip = dp(i+1)

            return max(skip, rob)

        return dp(0)