"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        count=0
        end_idx=0
        s=sorted(interval.start for interval in intervals)
        e=sorted(interval.end for interval in intervals)
        for i in s:
            if i<e[end_idx]:
                count+=1
            else:
                end_idx+=1
        return count