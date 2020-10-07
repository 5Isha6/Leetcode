# 39. Combination Sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.cand = candidates
        self.result = []
        self.bck([],target,0)
        return self.result
    def bck(self, path,target, idx):
        if target == 0:
            self.result.append(path)    
            return
        if target < 0:
            return
        for i in range(idx,len(self.cand)):
            self.bck(path+[self.cand[i]],target-self.cand[i],i)

        