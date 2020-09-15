# 54 Insert Interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        push = False
        
        def merge(interval):
            output = []
            
            candidate = interval[0]
            
            for j in range(1,len(interval)):
                
                if  candidate[1] >= interval[j][0]:
                    candidate[1] = max(candidate[1],interval[j][1])
                else:
                    output.append(candidate)
                    candidate= interval[j]
            
            output.append(candidate)
            return output

        for i in intervals:
            if not push and newInterval[0] <= i[0]:
                output.append(newInterval)
                push = True
            output.append(i)
        
        if not push:
            output.append(newInterval)
        return merge(output)
        
       
                
                
            