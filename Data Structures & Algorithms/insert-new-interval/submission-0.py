class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        mergedInterval = [100001, -1]
        for interval in intervals:
            if not (interval[1] < newInterval[0] or interval[0] > newInterval[1]):
                mergedInterval[0] = min(interval[0], newInterval[0], mergedInterval[0])
                mergedInterval[1] = max(interval[1], newInterval[1], mergedInterval[1])
            else:
                res.append(interval)
        if mergedInterval == [100001, -1]:
            res.append(newInterval)
        else:
            res.append(mergedInterval)
        
        return sorted(res)