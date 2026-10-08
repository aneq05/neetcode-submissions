class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        
        def backtrack(i):
            if i == len(nums):
                result.append(current.copy())
                return

            # TAKE
            current.append(nums[i])
            backtrack(i+1)

            # UNDO
            current.pop()

            # SKIP
            backtrack(i+1)

        backtrack(0)
        return result