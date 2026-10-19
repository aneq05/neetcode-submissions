class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        result = [] # O(n) -> potem O(1)

        for i, (begin, finish) in enumerate(intervals):
            # przedział przed nowym
            if finish < start:
                result.append([begin, finish])
            # przedział za nowym
            elif begin > end:
                result.append([start, end])
                result.extend(intervals[i:])
                return result
            # przedziały nachodzą na siebie
            else:
                start = min(start, begin)
                end = max(end, finish)

        result.append([start, end])
        return result