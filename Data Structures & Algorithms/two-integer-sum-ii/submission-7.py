class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(numbers):
            need = target - num
            if need in seen:
                return [seen[need] + 1, index + 1]
            seen[num] = index
        return []
