#
# @lc app=leetcode id=48 lang=python
#
# [48] Rotate Image
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                topLeft = matrix[top][l + i]

                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topLeft

            l += 1
            r -= 1
        
# @lc code=end

