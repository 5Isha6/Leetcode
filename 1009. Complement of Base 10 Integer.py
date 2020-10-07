# 1009. Complement of Base 10 Integer
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        arr = []
        def bini(n):
            
            if n > 1:
                # n = n//2
                bini(n//2)
            arr.append(n % 2)
            return arr
        
        a = bini(N)
        
        
        print(N, a)
        if all(a):
            return 0
        num = 1
        r = 0
        for i in a:
            r <<= 1
            r += i^1
            
        return r
                
                
        