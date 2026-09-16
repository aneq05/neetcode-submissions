class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            l, r = i, len(nums)-1
            while l <= r:
                mid = l + (r-l)//2
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    r = mid -1
                else:
                    l = mid +1
        return -1