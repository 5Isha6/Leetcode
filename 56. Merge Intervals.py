# 56. Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        heap = []
        
        for interval in sorted(intervals):
            
            in_f = interval[0]
            in_s = interval[1]
            if heap and in_f <= heap[-1][1]:
                heap[-1][1] = max(heap[-1][1],in_s)

            else:

                heap.append(interval)
                
        return heap
                
