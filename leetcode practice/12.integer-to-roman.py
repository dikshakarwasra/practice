#
# @lc app=leetcode id=12 lang=python
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num):
        val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        sym=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        roman=""
        for i in range(len(val)):
            while num>=val[i]:
                roman+=sym[i]
                num-=val[i]
        return roman        

        
        
        
# @lc code=end

