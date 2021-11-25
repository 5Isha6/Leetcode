#1249. Minimum Remove to Make Valid Parentheses
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        
        list_s= list(s)
        
        for i, ch in enumerate(list_s):
            if ch == ('('):
                stack.append(i)
            elif ch == (')'):
                if len(stack) > 0:
                    stack.pop()
                else:
                    list_s[i] = ''
        print(stack)
        while len(stack) > 0:
            temp = stack.pop()
            list_s[temp] = ''
        
        return ''.join(list_s)
            
