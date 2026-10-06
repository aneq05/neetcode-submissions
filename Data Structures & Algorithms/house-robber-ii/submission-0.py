class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = {}

        def dp(i, end):
            if i >= end:
                return 0

            if (i, end) in memo:
                return memo[(i, end)]

            take = nums[i] + dp(i + 2, end)
            skip = dp(i + 1, end)

            memo[(i, end)] = max(take, skip)
            return memo[(i, end)]

        return max(
            dp(0, len(nums) - 1),  # domy 0 ... n-2
            dp(1, len(nums))       # domy 1 ... n-1
        )