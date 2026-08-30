"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        for interval in intervals:
            times.append((interval.start, 1))
            times.append((interval.end, -1))
        times.sort()

        res = count = 0

        for time in times:
            count += time[1]
            res = max(res, count)

        return res