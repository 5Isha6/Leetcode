# 495. Teemo Attacking
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        last_p = -100000000
        p = 0
        timeSeries.sort()
        for i in timeSeries:
            if i >= last_p:
                p += duration
                last_p = i + duration
            else:
                
                p += i + duration - last_p
                last_p = i + duration
        return p
        
        
        
        
        
        
        