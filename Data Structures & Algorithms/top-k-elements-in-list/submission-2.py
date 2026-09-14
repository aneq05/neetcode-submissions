class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}
        
        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1
        
        return sorted(
            nums_count.keys(), 
            key=nums_count.get,
            reverse=True
        )[:k]