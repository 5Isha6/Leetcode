# 216. Combination Sum III
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:


        def backtrack(comb, rem,  results, curr):

            if rem == 0 and len(comb) == k:
                results.append(comb[:])
                return
            elif rem < 0 or len(comb) == k : 
                return

            for i in range(curr, 10):
                comb.append(i)
                backtrack(comb, rem - i , results,  1 + i)
                comb.pop()
        
        results = []
        backtrack([], n, results, 1)
        
        return results
