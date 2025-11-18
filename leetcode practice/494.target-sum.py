#
# @lc app=leetcode id=494 lang=python
#
# [494] Target Sum
#

# @lc code=start
class Solution(object):
    def findTargetSumWays(self, nums, target):
        dp = {}   

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) +
                               backtrack(i + 1, total - nums[i]))

            return dp[(i, total)]

        return backtrack(0,0)
        
       
        
# @lc code=end

