#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        return cleaned == cleaned[::-1]


      
        
# @lc code=end

