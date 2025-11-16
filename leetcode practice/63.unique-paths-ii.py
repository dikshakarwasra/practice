#
# @lc app=leetcode id=63 lang=python
#
# [63] Unique Paths II
#

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * N
        dp[N - 1] = 1
        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c < N - 1:
                    dp[c] = dp[c] + dp[c + 1]

        return dp[0]
        
        
# @lc code=end

