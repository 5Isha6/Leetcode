# 7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
       
        num = abs(x)
        rev = 0
        
        while num > 0:
            q = num % 10
            rev = rev * 10 + q
            num = num // 10
            
        if rev >= 2**31 - 1:
            return 0
            
        sign = [1,-1][x < 0]

        
    
        return sign*rev
        
