class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        seq = 1
        index = 0
        while index < len(nums)-1:
            if nums[index+1] - nums[index] == 1:
                seq += 1
            index += 1
        return seq

