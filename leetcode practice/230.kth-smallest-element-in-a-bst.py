#
# @lc app=leetcode id=230 lang=python
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        n=0
        stack=[]
        cur=root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            n+=1
            if n==k:
                return cur.val
            cur=cur.right    
        
        
# @lc code=end

