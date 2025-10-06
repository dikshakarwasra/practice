#
# @lc app=leetcode id=28 lang=python
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0

        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i : i + len(needle)] == needle:
                return i

        return -1

        
# @lc code=end

