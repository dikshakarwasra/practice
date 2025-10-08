#
# @lc app=leetcode id=1122 lang=python
#
# [1122] Relative Sort Array
#

# @lc code=start
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        order = {num: i for i, num in enumerate(arr2)}
        arr1.sort(key=lambda x: (order.get(x, len(arr2)), x))
        return arr1
        
# @lc code=end

