#1088. Confusing Number II
class Solution:
    def confusingNumberII(self, n: int) -> int:
        validDigit = [0, 1, 6, 8, 9]
        m = {0:0, 1:1, 6:9, 8:8, 9:6}
        
        def dfs (num, rot, digit):
            res = 0
            if num != rot:
                res += 1
            
            for d in validDigit:
                
                if d==0 and num ==0:
                    continue
                if num*10 + d <= n:
                    res += dfs(num*10+d,m[d]*digit+rot,digit*10)
                
            return res
        return dfs(0,0,1)
        
       
