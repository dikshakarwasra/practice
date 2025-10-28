#
# @lc app=leetcode id=647 lang=python
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        res=0
        for i in range(len(s)):
            res+=self.countPali(s,i,i)
            res+=self.countPali(s,i,i+1)
        return res
    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res  
        
        
# @lc code=end

