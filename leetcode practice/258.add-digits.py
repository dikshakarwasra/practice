#
# @lc app=leetcode id=258 lang=python
#
# [258] Add Digits
#

# @lc code=start
class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            s = 0
            for digit in str(num):
                s += int(digit)
            num = s
        return num
    

       
        
# @lc code=end

