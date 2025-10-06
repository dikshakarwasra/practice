#
# @lc app=leetcode id=29 lang=python
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution(object):
    def divide(self,dividend, divisor):
        l = 2**31 - 1
        d = abs(dividend)
        dv = abs(divisor)
        output = 0

        while d >= dv:
            tmp = dv
            mul = 1
            while d >= tmp + tmp:
                tmp += tmp
                mul += mul
            d -= tmp
            output += mul

        if (dividend < 0) != (divisor < 0):
            output = -output

        return min(2**31 - 1, max(-2**31, output))
        
    
    

                 
        

        
# @lc code=end

