#
# @lc app=leetcode id=6 lang=python
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        row = 0
        increment = 1

        for c in s:
            rows[row] += c
            if row == 0:
                increment = 1
            elif row == numRows - 1:
                increment = -1
            row += increment

        return ''.join(rows)

                  

            



        
        
        
# @lc code=end

