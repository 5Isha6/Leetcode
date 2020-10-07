#967. Numbers With Same Consecutive Differences
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        results = []
        if n == 1:
            results.append(0)
        def recurse(current,ldigit, left):
            if left == 0:
                results.append(current)
                return

            for d in [-1,1]:
                new = ldigit + d * k
                if k == 0 and d > 0:
                    continue
                if 0<=new<= 9:
                    recurse(current*10+new,new,left -1)
                
        for i in range(1,10):
            recurse(i,i,n-1)
            
                
        return results
                
            
            
        