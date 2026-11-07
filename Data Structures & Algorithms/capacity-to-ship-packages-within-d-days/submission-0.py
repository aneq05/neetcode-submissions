class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def possible(weight_capacity):
            curr_load = 0
            needed_days = 1

            for w in weights:
                if curr_load + w > weight_capacity:
                    needed_days += 1
                    curr_load = 0
                curr_load += w

            return needed_days <= days
            

        left = max(weights) # conajmniej najcięższa paczka
        right = sum(weights) # wszystkie paczki

        while left < right:
            mid = (left+right) // 2

            if possible(mid):
                right = mid
            else:
                left = mid + 1

        return left