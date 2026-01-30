#
# @lc app=leetcode id=912 lang=python
#
# [912] Sort an Array
#

# @lc code=start
class Solution(object):
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        i = j = 0
        res = []

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        return res + left[i:] + right[j:]
       # @lc code=end

