#
# @lc app=leetcode id=853 lang=python
#
# [853] Car Fleet
#

# @lc code=start
class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos,spd in cars:
            time = (float)(target - pos)/spd
            if not stack or time >stack[-1]:
                stack.append(time)
        return len(stack)
        
        
        
       
       




        
        
# @lc code=end

