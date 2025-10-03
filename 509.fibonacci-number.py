#
# @lc app=leetcode id=509 lang=python
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        a, b = 0, 1
        i = 2
        while i <= n:
            a, b = b, a + b
            i += 1

        return b
        
        
# @lc code=end

