class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        result = []

        for begin, finish in intervals[1:]:
            if begin <= end:
                end = max(end, finish)
            else:
                result.append([start, end])
                start = begin
                end = finish
        result.append([start, end])
        return result