# 22. Generate Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        curr =''
        l,r = 0,0
        def bt(l,r,curr):
            #print('curr',curr)
            if len(curr) == 2*n:
                #print('curr', curr)
                res.append(curr)
                
                
            if l < n:
                #print('l',l,r)
                bt(l+1,r,curr + '(')
            if r < l:
                #print('r',l,r)
                bt(l, r+1, curr + ')') 
        bt(0,0,curr)
        return res
      
            
        
