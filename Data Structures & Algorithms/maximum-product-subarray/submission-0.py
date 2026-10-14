class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        best = nums[0]

        for num in nums[1:]:
            a = num
            b = num * max_product
            c = num * min_product

            min_product = min(a,b,c)
            max_product = max(a,b,c)
            best = max(best, max_product)
        return best