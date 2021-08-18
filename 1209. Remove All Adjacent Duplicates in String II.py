
#1209. Remove All Adjacent Duplicates in String IIclass Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['$', 0]]
        for i in s:
           
            if stack[-1][0] == i:
                #print(stack[-1],i )
                stack[-1][1] += 1
                
                if stack[-1][1] ==k:
                    stack.pop()
                
            else:
                stack.append([i, 1])

        res = ""
        for c, f in stack:
            res += c * f

        
        return res
                
                 
