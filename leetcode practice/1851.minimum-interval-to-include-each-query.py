#
# @lc app=leetcode id=1851 lang=python
#
# [1851] Minimum Interval to Include Each Query
#

# @lc code=start
import heapq
class Solution(object):
    def minInterval(self, intervals, queries):
        intervals.sort()

        minHeap = []
        res, i = {}, 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            res[q] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]
        
        
        
# @lc code=end

