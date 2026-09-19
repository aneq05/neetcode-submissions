class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        output = set()

        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result = [nums[i],nums[j],nums[k]]
                        output.add(tuple(result))
        return [list(tup) for tup in output]



