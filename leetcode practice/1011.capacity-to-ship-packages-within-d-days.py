#
# @lc app=leetcode id=1011 lang=python
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution(object):
    def shipWithinDays(self, weights, days):
        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2
            need_days = 1
            curr = 0

            for w in weights:
                if curr + w > mid:
                    need_days += 1
                    curr = 0
                curr += w

            if need_days > days:
                left = mid + 1
            else:
                right = mid

        return left
    
# @lc code=end

