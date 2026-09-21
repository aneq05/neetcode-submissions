class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq = 0

        for num in nums_set:
            if num-1 not in nums_set:
                curr_num = num
                curr_seq = 1

                while curr_num+1 in nums_set:
                    curr_num += 1
                    curr_seq += 1
                
                max_seq = max(max_seq, curr_seq)
        return max_seq
