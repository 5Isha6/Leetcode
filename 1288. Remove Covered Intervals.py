#1288. Remove Covered Intervals
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        c = 0
        for a,(ax,bx) in enumerate(intervals):
            for d, (dy,ey) in enumerate(intervals):
                if a == d:
                    continue
                if dy<= ax <= bx <= ey:
                    c += 1
                    break
                    
                
        return N - c
                
        