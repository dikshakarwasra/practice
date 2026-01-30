#
# @lc app=leetcode id=219 lang=python
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        for i, n in enumerate(nums):
            if n in seen and i - seen[n] <= k:
                return True
            seen[n] = i
        return False
       
# @lc code=end

