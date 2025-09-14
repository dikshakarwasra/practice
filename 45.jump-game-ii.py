#
# @lc app=leetcode id=45 lang=python
#
# [45] Jump Game II
#

# @lc code=start
class Solution(object):
    def jump(self, nums):
        jumps = 0
        end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                jumps += 1
                end = farthest

        return jumps


       
        
# @lc code=end

