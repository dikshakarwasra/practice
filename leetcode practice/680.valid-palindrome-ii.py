#
# @lc app=leetcode id=680 lang=python
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution(object):
    def validPalindrome(self, s):
        def isPalindromeRange(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return isPalindromeRange(left + 1, right) or isPalindromeRange(left, right - 1)
            left += 1
            right -= 1
        
        return True
        
        
# @lc code=end

