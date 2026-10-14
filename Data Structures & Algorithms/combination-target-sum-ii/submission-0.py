class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current = []

        candidates.sort()

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(current.copy())
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if i > start and candidates[i] == candidates[i-1]:
                    continue

                if num > remaining:
                    continue

                current.append(num)
                backtrack(i+1, remaining-num)
                current.pop()

        backtrack(0, target)
        return result            
        