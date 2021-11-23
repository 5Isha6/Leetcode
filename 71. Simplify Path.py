#71. Simplify Path
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        inp = path.split('/')
        
        stack = []
        for idx in range(len(inp)):
            
            if inp[idx] == '.' or inp[idx] == '':
                continue
            if inp[idx] == '..' :
                if len(stack) != 0:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(inp[idx])
        
        
        op = "/".join(stack)
        # print(op)
        return '/'+op
                
                
