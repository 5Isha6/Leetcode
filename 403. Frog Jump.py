# 403. Frog Jump
from collections import defaultdict
class Solution:
    def canCross(self, stones: List[int]) -> bool:

        
        if stones[1] != 1:
            return False
        
        d = defaultdict(set)
        
        d[0].add(0)
        d[1].add(1)
        
        
        for i in stones[:-1]:
            
            for j in d[i]:
                
                for k in range(j-1,j+2):
                    
                    if k > 0:
                        d[i + k].add(k)
        
               
        return bool(d[stones[-1]])
        
      
