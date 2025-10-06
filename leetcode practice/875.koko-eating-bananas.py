#
# @lc app=leetcode id=875 lang=python
#
# [875] Koko Eating Bananas
#

# @lc code=start

class Solution(object):
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours +=(p+k-1)//k

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res



        
        
# @lc code=end

