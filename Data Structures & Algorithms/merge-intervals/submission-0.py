class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ind = 0
        stInd = 0
        res = []
        while ind < len(intervals) - 1:
            if intervals[ind][-1] >= intervals[ind + 1][0]:
                intervals[ind][-1] = max(intervals[ind][-1], intervals[ind + 1][-1])
                intervals[ind], intervals[ind + 1] = intervals[ind + 1], intervals[ind]
                ind += 1
            else:
                res.append(intervals[ind])
                ind += 1
        res.append(intervals[ind])

        return res