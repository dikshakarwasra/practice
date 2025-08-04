#
# @lc app=leetcode id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        def helper(x,n):
            if x==0: return 0
            if n==0: return 1

            res=helper(x*x,n//2)
            return x*res if n%2 else res

        res = helper(x,abs(n))
        return res if n>=0 else 1/res   
        
       
        
# @lc code=end

