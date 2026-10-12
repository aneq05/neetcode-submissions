class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best, curr = nums[0], nums[0]

        for num in nums[1:]:
            curr = max(num, curr+num)
            best = max(best, curr)

        return best