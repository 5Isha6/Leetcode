# 797. All Paths From Source to Target
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def dfs(curr, path):
            
            if len(graph) - 1 == curr:
                res.append(path)
            else:
                for i in graph[curr]:
                    dfs(i,path+[i])
                
                
        dfs(0,[0])
        return res
