#1094 Car Pooling
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for passengers, start, end in trips:
            events.append((start,passengers))
            events.append((end,-passengers))
            
        events.sort()
        cp = 0
        for st, cap in events:
            cp += cap
            if not 0<= cp <= capacity:
                return False
        return True
            
    
                
                
        