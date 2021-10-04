# 57. Insert Interval
class Solution:
        def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            s, e = newInterval #[0], newInterval[1]
            # print(s,e)
            l, r = [], []
            res = []

            for i in intervals:

                if i[1] < s:
                    l += i,

                elif i[0] > e:
                    r += i,

                else:
                    s = min(s,i[0])
                    e = max(e,i[1])
            # print(l,r)    
            res = l + [[s,e]] + r
            return res
