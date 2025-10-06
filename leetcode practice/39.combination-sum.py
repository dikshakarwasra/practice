#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        res=[]
        def dfs(i,cur,total):
            if total==target:
                res.append(cur[:])
                return
            if i>=len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i,cur,total+candidates[i])
            cur.pop()
            dfs(i+1,cur,total)
        dfs(0,[],0)
        return res  
        
# @lc code=end

