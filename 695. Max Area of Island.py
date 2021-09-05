# 695. Max Area of Island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        area = [0]
        c = 0
        def dfs(i, j):
            
            if (i < 0 or i >= m) or (j < 0 or j >= n):
                #grid[i][j] = 0
                return 0
            
            if grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i+1,j) + dfs(i,j+1) + dfs(i-1,j) + dfs(i, j - 1)                
            else:
                return 0
        
        for i in range(m):
            for j in range(n):
        
                if grid[i][j] :
                    c = dfs(i,j)

                    area.append(c)
        # print(area)
        return max(area)
        
       
            
        
