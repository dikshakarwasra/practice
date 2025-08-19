#
# @lc app=leetcode id=853 lang=python
#
# [853] Car Fleet
#

# @lc code=start
class Solution(object):
    def carFleet(self, target, position, speed):
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        stack = []
        for p, s in cars:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        
        
       
       




        
        
# @lc code=end

