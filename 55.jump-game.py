#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        maxJump=0
        for i in range(len(nums)):
            if i>maxJump:
                return False
            maxJump=max(maxJump,i+nums[i])
        return True    

        
        
# @lc code=end

