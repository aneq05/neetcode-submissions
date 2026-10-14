class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        memo = {}
        def dp(i, remaining):
            if remaining == 0:
                return True
            if i == len(nums) or remaining < 0:
                return False
            if (i, remaining) in memo:
                return memo[(i, remaining)]
            
            take = dp(i+1, remaining - nums[i])
            skip = dp(i+1, remaining)

            result = take or skip 
            memo[(i, remaining)] = result

            return result
        
        return dp(0, target)

