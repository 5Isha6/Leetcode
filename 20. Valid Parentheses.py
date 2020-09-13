#20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(',  '}':'{', ']':'['}
        for i in s:
            if i in ( '(', '{','['):
                stack.append(i)
            else:
                if stack != []:
                    t = stack.pop()
                    
                    if t != mapping[i]:
                        return False
                else:
                    return False
    
        
        return True if stack == [] else False