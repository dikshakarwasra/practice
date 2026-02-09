#
# @lc app=leetcode id=1095 lang=python
#
# [1095] Find in Mountain Array
#

# @lc code=start
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        length = mountain_arr.length()
        l, r = 1, length - 2
        while l <= r:
            m = (l + r) // 2
            left = mountain_arr.get(m - 1)
            mid = mountain_arr.get(m)
            right = mountain_arr.get(m + 1)

            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        peak = m

        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            val = mountain_arr.get(m)
            if val == target:
                return m
            elif val < target:
                l = m + 1
            else:
                r = m - 1

        l, r = peak + 1, length - 1
        while l <= r:
            m = (l + r) // 2
            val = mountain_arr.get(m)
            if val == target:
                return m
            elif val > target:
                l = m + 1
            else:
                r = m - 1

        return -1
        
# @lc code=end

