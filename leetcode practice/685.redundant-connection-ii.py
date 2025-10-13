#
# @lc app=leetcode id=685 lang=python
#
# [685] Redundant Connection II
#

# @lc code=start
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        def find(x):
            if root[x]!=x:
                root[x]=find(root[x])
            return root[x]    
        def union(x,y):
            rx,ry=find(x),find(y)
            if rx==ry:
                return False
            root[ry]=rx
            return True
        n=len(edges)
        parent={}
        cand1=cand2=None
        for u,v in edges:
            if v in parent:
                cand1=[parent[v],v]
                cand2=[u,v]
                break
            parent[v]=u
        root={i:i for i in range(1,n+1)}
        for u,v in edges:
            if[u,v]==cand2:
                continue
            if not union(u,v):
                if cand1:
                    return cand1
                else:
                    return[u,v]
        return cand2
        
# @lc code=end

