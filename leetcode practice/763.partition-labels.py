#
# @lc app=leetcode id=763 lang=python
#
# [763] Partition Labels
#

# @lc code=start
class Solution(object):
    def partitionLabels(self, s):
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size, end = 0, 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0

        return res
       
# @lc code=end

