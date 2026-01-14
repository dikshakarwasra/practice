#
# @lc app=leetcode id=190 lang=python
#
# [190] Reverse Bits
#

# @lc code=start
class Solution(object):
    def reverseBits(self, n):
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))

        return res
        
       
        
# @lc code=end

