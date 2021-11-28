# 399. Evaluate Division
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = defaultdict(defaultdict)
        
        for i,j in zip(equations, values):
            self.graph[i[0]][i[1]] = j
            self.graph[i[1]][i[0]] = 1/j
        
        # print(self.visit)
        def dfs(div, divi, prod, visit):
            visit.add(div)
            ret = -1.0
            neigh = self.graph[div]            
            if divi in neigh:
                return prod * neigh[divi]
            
            else:
                for i,val in neigh.items():
                    if i in visit:
                        continue
                    
                    ret = dfs(i, divi, prod * val, visit)
                    if ret != -1.0:
                        break
                
            return ret
        
        op = []
        for div, divi in queries:
            if div not in self.graph or divi not in self.graph:
                ret = -1.0
            elif div == divi:
                ret = 1.0
            else:
                visit = set()
                ret = dfs(div, divi, 1, visit)
            op.append(ret)
        return op
