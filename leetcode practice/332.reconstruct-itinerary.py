#
# @lc app=leetcode id=332 lang=python
#
# [332] Reconstruct Itinerary
#

# @lc code=start
from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
        res = []
        def dfs(airport):
            while adj[airport]:
                dfs(adj[airport].pop())
            res.append(airport)
        dfs("JFK")
        return res[::-1]
        

        
        
# @lc code=end

