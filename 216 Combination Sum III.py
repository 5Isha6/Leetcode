#216 Combination Sum III
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        # copy = []
        def solve(rem, start, total, copy):
            
            if rem == 0:
                if total == n:
                    result.append(copy[:])
                return
            if total>n:
                return
            
            
            for i in range(start,10):
                solve(rem-1,i+1,total+i,copy + [i])
            
        solve(k,1,0,[])
        return result