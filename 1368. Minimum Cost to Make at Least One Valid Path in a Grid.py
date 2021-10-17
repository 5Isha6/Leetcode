# 1368. Minimum Cost to Make at Least One Valid Path in a Grid
from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxi = float('inf')
        dp = [[maxi] * n for i in range(m)]
        cot = 0
        q = deque()
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(i, j):
          
            if  i < 0 or i >= m or j < 0 or j >= n or dp[i][j] != maxi:
                
                return
           
            dp[i][j] = cot
            q.append((i,j))
            ni,nj =  dirs[grid[i][j] - 1]
            di = i + ni
            dj = j + nj
            dfs(di,dj)
                
            
        
        dfs(0,0)
        
        while q:
            cot+=1
            size = len(q)
            for _ in range(size):
            
            
                i,j = q.popleft()
                for x, y in dirs:
                    dfs(i+x, j +y)
        #print(dp)
        return dp[-1][-1]
