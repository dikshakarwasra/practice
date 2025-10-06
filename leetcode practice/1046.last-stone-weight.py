#
# @lc app=leetcode id=1046 lang=python
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution(object):
    def lastStoneWeight(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones, -(first - second))

        return -stones[0] if stones else 0
        
        
# @lc code=end

