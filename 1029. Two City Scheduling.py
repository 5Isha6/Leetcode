# 1029. Two City Scheduling
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key = lambda s : (s[0]-s[1]))
        n = len(costs)//2
        total = 0
        for i in range(n):
            total += costs[i][0] + costs[i+n][1]
        
        
        return total
