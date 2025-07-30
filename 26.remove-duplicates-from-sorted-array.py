#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)
        if n==0:
            return 0
        left=0
        for right in range(1,n):
            if nums[right]!=nums[left]:
                left+=1
                nums[left]=nums[right]
        return left+1            


        
        
# @lc code=end

