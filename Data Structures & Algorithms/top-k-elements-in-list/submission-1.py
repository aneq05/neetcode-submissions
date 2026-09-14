class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}
        
        for num in nums:
            if num not in nums_count:
                nums_count[num] = 1
            else:
                nums_count[num] += 1
        
        return sorted(
            nums_count.keys(), 
            key=nums_count.get,
            reverse=True
        )[:k]