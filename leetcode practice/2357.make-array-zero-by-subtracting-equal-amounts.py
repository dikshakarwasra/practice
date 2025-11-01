#
# @lc app=leetcode id=2357 lang=python
#
# [2357] Make Array Zero by Subtracting Equal Amounts
#

# @lc code=start
class Solution(object):
    def minimumOperations(self, nums):
        s=set()
        for n in nums:
            if n>0:
                s.add(n)
        return len(s)        
        
        
# @lc code=end

