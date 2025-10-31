#
# @lc app=leetcode id=518 lang=python
#
# [518] Coin Change II
#

# @lc code=start
class Solution(object):
    def change(self, amount, coins):
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)

        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]

        return dp[amount][0]


        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp=nextDP
        
        
# @lc code=end

