#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap,-num)
        while k > 0:
            res = heapq.heappop(heap)
            k -=1
        return -res
        
        
# @lc code=end

