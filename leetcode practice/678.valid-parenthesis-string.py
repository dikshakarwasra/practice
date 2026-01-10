#
# @lc app=leetcode id=678 lang=python
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution(object):
    def checkValidString(self, s):
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1

            if leftMax < 0:
                return False

            if leftMin < 0:
                leftMin = 0

        return leftMin == 0

       
# @lc code=end

