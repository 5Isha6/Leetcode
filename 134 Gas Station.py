# 134 Gas Station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
      
        tank, shortage, start = 0, 0, 0
        
        for i in range(len(gas)):
            tank += gas[i]
            
            if tank >= cost[i]:
                tank -= cost[i]
            else:
                shortage += cost[i] - tank
                start = i + 1
                tank = 0
                
        if start == len(gas) or shortage > tank:
            return -1
        return start
            