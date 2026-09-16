class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i+1, len(numbers) - 1
            seeked = target - numbers[i]
            while l <= r:
                middle = l +(r-l) //2
                if numbers[middle] == seeked:
                    return [i+1, middle + 1]
                elif numbers[middle] < seeked:
                    l = middle + 1
                else:
                    r = middle - 1
        return []
