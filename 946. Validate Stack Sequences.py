#946. Validate Stack Sequences
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popy = popped[0]
        stack = []
        j = 0
        for i in pushed:
            stack.append(i)
            
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1 
        
                
        
        return len(stack) == 0
