# 815. Bus Routes
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        dic = defaultdict(set)
        
        for i, r_i in enumerate(routes):
            for j in r_i:
                dic[j].add(i)
                
        queue = [(source,0)]
        seen = set([source])
        
        for stop, cnt in queue:
            
            if stop == target:
                return cnt
            
            for r in dic[stop]:
                for j in routes[r]:
                    if j not in seen:
                        queue.append((j, cnt + 1))
                        seen.add(j)

            
                routes[r] = []
            # print(seen)
        return -1
        
        
        
        
        
        
   
        
