class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        seq = 1
        max_seq = 1
        index = 0
        while index < len(nums)-1:
            if nums[index+1] - nums[index] == 1:
                seq += 1
            elif nums[index+1] - nums[index] > 1:
                max_seq = max(max_seq, seq)
                seq = 1
            index += 1
        return max(max_seq, seq)

