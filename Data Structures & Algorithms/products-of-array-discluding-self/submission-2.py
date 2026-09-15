import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros_count = nums.count(0)
        product = 1

        if zeros_count >=2:
            return [0] * len(nums)
        
        for num in nums:
            if num != 0:
                product *= num
        
        if zeros_count == 1:
            return [product if num == 0 else 0 for num in nums]

        return [product // num for num in nums]



