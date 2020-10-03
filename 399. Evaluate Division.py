# 399. Evaluate Division
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        names = dict()
        idx = 0
        for x,y in equations:
            if x not in names:
                names[x] = idx
                idx += 1
            if y not in names:
                names[y] = idx
                idx += 1
        
        N = len(names)
        g = [[None]*N for x in range(N)]
        
        for i, (x,y) in enumerate(equations):
            g[names[x]][names[y]] = values[i]
            g[names[y]][names[x]] = 1.0/values[i]
            
        for k in range(N):
            for l in range(N):
                for m in range(N):
                    if g[l][m] is None and g[l][k] is not None and g[k][m] is not None:
                        g[l][m] = g[l][k]*g[k][m]
        res = []
        for x,y in queries:
            if x not in names or y not in names:
                res.append(-1)
                continue
            if g[names[x]][names[y]] is not None:
                res.append(g[names[x]][names[y]])
            else:
                res.append(-1)
                
        return res