#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]

        for word in strs:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
        return prefix
        
        
# @lc code=end

