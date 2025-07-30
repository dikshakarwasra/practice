#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = int(str(x)[::-1]) * sign

        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num

        
        
        
# @lc code=end


