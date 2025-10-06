#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

        return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False
        counts, countT = {}, {}

        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in counts:
            if counts[c] != countT.get(c, 0):
                return False
        return True

       
# @lc code=end

