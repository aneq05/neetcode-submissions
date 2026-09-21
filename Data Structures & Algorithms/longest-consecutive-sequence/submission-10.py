class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        seq = 1
        index = 0
        while index < len(nums)-1:
            if nums[index+1] - nums[index] == 1:
                seq += 1
            index += 1
        return seq

