class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries_sorted = sorted(queries)
        intervals.sort()
        min_heap = []
        res = {}
        intervalInd = 0

        for q in queries_sorted:
            if res.get(q):
                continue
            while intervalInd < len(intervals):
                if intervals[intervalInd][0] <= q:
                    heapq.heappush(min_heap, (intervals[intervalInd][1] - intervals[intervalInd][0] + 1, intervals[intervalInd][1]))
                else:
                    break
                intervalInd += 1
            # print(min_heap)
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            if not min_heap:
                res[q] = -1
            else:
                # ele = heapq.heappop(min_heap)
                res[q] = min_heap[0][0]
        
        fin_res = [res[q] for q in queries]
        return fin_res