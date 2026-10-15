"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)

        i = 0
        j = 0
        rooms = 0
        max_rooms = 0

        while i < len(starts):
            if starts[i] < ends[j]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                i += 1
            else:
                rooms -= 1
                j += 1

        return max_rooms