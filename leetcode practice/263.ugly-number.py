#
# @lc app=leetcode id=263 lang=python
#
# [263] Ugly Number
#

# @lc code=start
class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False

        for i in [2, 3, 5]:
            while n % i == 0:
                n //= i

        return n == 1
        
        
# @lc code=end

