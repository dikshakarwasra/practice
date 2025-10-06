#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p[:]       
                    p_copy.insert(i, n)  
                    new_perms.append(p_copy)
            perms = new_perms

        return perms
        
        
# @lc code=end

