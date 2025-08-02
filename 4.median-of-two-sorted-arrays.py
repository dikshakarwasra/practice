#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while True:
            i = (low + high) // 2
            j = (x + y + 1) // 2 - i

            leftX = nums1[i - 1] if i > 0 else float('-inf')
            rightX = nums1[i] if i < x else float('inf')

            leftY = nums2[j - 1] if j > 0 else float('-inf')
            rightY = nums2[j] if j < y else float('inf')

            if leftX <= rightY and leftY <= rightX:
                if (x + y) % 2:
                    return max(leftX, leftY)
                return (max(leftX, leftY) + min(rightX, rightY)) / 2.0
            elif leftX > rightY:
                high = i - 1
            else:
                low = i + 1
        
        
# @lc code=end

