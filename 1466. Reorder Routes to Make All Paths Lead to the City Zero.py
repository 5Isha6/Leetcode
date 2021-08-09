#1466. Reorder Routes to Make All Paths Lead to the City Zero
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        edges = {(a, b) for a,b in connections}
        neighbours = { i: [] for i in range(n)}
        visit = set()
        chgs = 0
        
        
        for a, b in connections:
                neighbours[a].append(b)
                neighbours[b].append(a)
        
        def dfs(city):
            nonlocal visit, edges, neighbours, chgs 
           
            for i in neighbours[city]:
                if i in visit:
                    continue
                if (i, city) not in edges:
                    chgs += 1
                visit.add(i)
                dfs(i)
        visit.add(0)
        dfs(0)
        return chgs
