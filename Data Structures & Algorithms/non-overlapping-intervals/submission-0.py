class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        removeCount = 0
        ind = 0
        while ind < len(intervals) - 1:
            if intervals[ind][-1] > intervals[ind + 1][0]:
                if intervals[ind][-1] < intervals[ind + 1][-1]:
                    intervals[ind], intervals[ind + 1] = intervals[ind + 1], intervals[ind]
                removeCount += 1
            ind += 1
        
        return removeCount