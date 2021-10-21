# 56. Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x : x[0])
        # print(intervals)
        res = []
        item = 0
        for item in range(len(intervals)):
            if not res or  res[-1][1] < intervals[item][0]:
                res.append(intervals[item])
            else:
                res[-1][1] = max(res[-1][1], intervals[item][1])
                
            


        return res
