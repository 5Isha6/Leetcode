#131. Palindrome Partitioning
import copy
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        
        
        def ispal(s):
            l=0;
            r=len(s)-1
            if(l==r): return True
            while(l<r):
                if(s[l]!=s[r]):return False
                l+=1
                r-=1
            
            return True
        
        def findAll(s,res,temp):
            
            if len(s) == 0:
                # t = temp
                t = copy.deepcopy(temp)
                res.append(t)
            
            for i in range(len(s)):
                sleft = s[:i+1]
                if ispal(sleft):
                    temp.append(sleft)
                    findAll(s[i+1:], res, temp)
                    del temp[len(temp)-1]
                    # temp.clear()
        
        
        findAll(s,res,[])
        return res
        
		