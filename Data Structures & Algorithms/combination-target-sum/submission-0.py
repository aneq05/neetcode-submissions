class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(current.copy())
                return

            for i in range(start, len(nums)):
                num = nums[i]

                if num > remaining:
                    continue

                current.append(num)
                backtrack(i, remaining-num)
                current.pop()

        backtrack(0, target)
        return result
            