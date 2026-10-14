class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(i, end):
            if i >= end:
                return 0
            if (i, end) in memo:
                return memo[(i, end)]

            take_curr = nums[i] + dp(i+2, end)
            take_next = dp(i+1, end)
            max_amount = max(take_curr, take_next)
            memo[(i, end)] = max_amount

            return max_amount

        return max(
            dp(0, len(nums)-1),
            dp(1, len(nums))
        )