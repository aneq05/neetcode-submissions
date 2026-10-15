"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 1:
            return 1
        
        room_count = 0
        intervals.sort(key=lambda x: x.start)
        heap = []
        # [(5,10),(15,20),(0,40)]

        for interval in intervals:
            begin = interval.start
            finish = interval.end
            
            if heap and begin >= heap[0]:
                heapq.heappop(heap)
            else:
                room_count += 1

            heapq.heappush(heap, finish)

        return room_count