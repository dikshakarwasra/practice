#
# @lc app=leetcode id=202 lang=python
#
# [202] Happy Number
#

# @lc code=start

class Solution(object):
    def isHappy(self, n,seen=None):
        if seen is None:
            seen = set()
        
        if n in seen:
            return False
        seen.add(n)
        
        s = sum(int(i) ** 2 for i in str(n))
        if s == 1:
            return True
        else:
            return self.isHappy(s, seen)

        
        

        
# @lc code=end

