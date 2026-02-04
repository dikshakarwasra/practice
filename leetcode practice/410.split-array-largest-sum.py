#
# @lc app=leetcode id=410 lang=python
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution(object):
    def splitArray(self, nums, m):
        def canSplit(largest):
            subarray = 1
            curSum = 0

            for n in nums:
                if curSum + n <= largest:
                    curSum += n
                else:
                    subarray += 1
                    curSum = n

            return subarray <= m

        l = max(nums)
        r = sum(nums)
        res = r

        while l <= r:
            mid = l + ((r - l) // 2)
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res
       
       
        
# @lc code=end

