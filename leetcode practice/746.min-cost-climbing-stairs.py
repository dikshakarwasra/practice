#
# @lc app=leetcode id=746 lang=python
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        first = cost[0]
        second = cost[1]
        for i in range(2, n):
            current = cost[i] + min(first, second)
            first, second = second, current  

        return min(first, second)
        
        
# @lc code=end

