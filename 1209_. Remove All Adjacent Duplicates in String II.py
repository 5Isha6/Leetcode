# 1209. Remove All Adjacent Duplicates in String II
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
       
        stack = [['#',0]]
        
        for i in s:
            
            if i == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] >= k:
                    stack.pop()
            else:
                stack.append([i,1])   
        return ''.join(c * k for c, k in stack)  
                
                
        
