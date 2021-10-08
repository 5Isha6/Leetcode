# 531. Lonely Pixel I
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        
        cnt = 0
        
        for col in zip(*picture):
           
            
                if col.count('B') == 1 and picture[col.index('B')].count('B') == 1:
                    cnt += 1
        return cnt
   
