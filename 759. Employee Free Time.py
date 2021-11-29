# 759. Employee Free Time
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        ints = []
        for i in schedule:
            [ints.append(x) for x in i]
            
        ints.sort(key = lambda x:x.start)
        
        merge = []
        
        for i in ints:
            if not merge or i.start > merge[-1].end:
                merge.append(i)
            else:
                merge[-1].end =  max(merge[-1].end, i.end)
        
        op = []
        for i in range(1, len(merge)):
            op.append(Interval(start = merge[i-1].end, end = merge[i].start))
        return op                    
            
        
