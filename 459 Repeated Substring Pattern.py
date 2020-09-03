#459 Repeated Substring Pattern
# return s in (s + s)[1:-1]

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
         
        size = len(s)
        rep = ''
        for i in range(size//2,0,-1):
          
            if size % i == 0:
                
                num_rep = size//i
                sub = s[0:i]
                                
                for j in range(num_rep):
                    rep+=sub
                
                if rep == s:
                    return True
                rep = ''    
        return False   