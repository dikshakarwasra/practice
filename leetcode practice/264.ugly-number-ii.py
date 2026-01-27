#
# @lc app=leetcode id=264 lang=python
#
# [264] Ugly Number II
#

# @lc code=start
class Solution(object):
    def nthUglyNumber(self, n):
        u = [1]*n
        a = b = c = 0
        
        for i in range(1, n):
            u[i] = min(u[a]*2, u[b]*3, u[c]*5)
            if u[i] == u[a]*2: a += 1
            if u[i] == u[b]*3: b += 1
            if u[i] == u[c]*5: c += 1
        
        return u[-1]
        
        
# @lc code=end

