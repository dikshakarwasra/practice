#
# @lc app=leetcode id=973 lang=python
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution(object):
    def kClosest(self, points, k):
        minHeap = []
        for x, y in points:
            dist = (x * x) + (y * y)  # Correct distance formula
            minHeap.append((dist, x, y))
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res
       
        
# @lc code=end

