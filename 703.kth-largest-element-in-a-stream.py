#
# @lc app=leetcode id=703 lang=python
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)

        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val):
        heapq.heappush(self.minheap, val)

        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

        return self.minheap[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

