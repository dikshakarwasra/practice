#
# @lc app=leetcode id=787 lang=python
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = list(prices)
            for s, d, p in flights:  
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices

        return -1 if prices[dst] == float("inf") else prices[dst]
        
        
# @lc code=end

