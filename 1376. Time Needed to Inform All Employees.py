# 1376. Time Needed to Inform All Employees
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        dict_m = defaultdict(list)
        for idx,i in enumerate(manager):
            if i != -1:
                dict_m[i].append(idx)
                
        def helper(i):
            return max([helper(j) for j in dict_m[i]] or [0])   + informTime[i]
        return helper(headID)      
                
                
