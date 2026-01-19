#
# @lc app=leetcode id=133 lang=python
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def _init_(self, value=0, neighbors=None):
        self.val = value
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        oldToNew = {}

        def dfs(curr):
            if curr in oldToNew:
                return oldToNew[curr]

            copy = Node(curr.val)
            oldToNew[curr] = copy

            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        if node is None:
            return None

        return dfs(node)
    
# @lc code=end

