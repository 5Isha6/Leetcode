# 279. Perfect Squares
class Solution:
    def numSquares(self, n: int) -> int:
        
        q = {n} 
        ht = 0
        sq_nums = [ i * i for i in range(1, int(n**0.5) + 1)]
        
        
        while q:
            
            ht += 1
            nq = set()
            for i in q:
                
                for each in sq_nums:
                        
                    if i == each:
                        return ht
                    elif i < each:
                        break
                    else:    
                        nq.add(i - each)
            q = nq
        return ht
            
        
