# 22. Generate Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_b, close_b = n, n
        result = []
        
        def solve(open_b,close_b,op):
            
            if open_b == 0 and close_b == 0:
                result.append(op)
                
            
            if open_b != 0:
                solve(open_b - 1, close_b , op + '(')
                
            if close_b > open_b:
                solve(open_b, close_b -1, op + ')')
            
        solve(open_b, close_b,"")
        return result