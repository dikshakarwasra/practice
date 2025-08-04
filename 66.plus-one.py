#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        num = int(''.join(map(str, digits))) + 1
        return list(map(int, str(num)))

       
        
# @lc code=end

