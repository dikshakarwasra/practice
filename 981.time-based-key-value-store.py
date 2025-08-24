#
# @lc app=leetcode id=981 lang=python
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap:
    def __init__(self):
        self.store = {}   

    def set(self,key,value,timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self,key,timestamp):
        values = self.store.get(key, [])
        l, r = 0, len(values) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

    
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

