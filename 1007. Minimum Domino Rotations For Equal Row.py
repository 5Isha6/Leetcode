#1007. Minimum Domino Rotations For Equal Row
from collections import defaultdict, Counter
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        
        for a in (tops[0], bottoms[0]):
            if all(a in b for b in zip(tops, bottoms)):
                return len(tops) - max(tops.count(a), bottoms.count(a))
        return -1
        
        
        
        
        
        

                
