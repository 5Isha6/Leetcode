# 980 Unique Paths III
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        totalzero = 0
        row = len(grid)
        col = len(grid[0])
        tp = 0
        def dfs(i,j, totalzero):
            
            if ( i<0 or j<0 or i> row-1 or j >col-1 or (grid[i][j] == 2 and totalzero != 0) or grid[i][j] == -1  or grid[i][j] == 99  ):

                return

            if grid[i][j] == 0 :
                totalzero-=1

            if grid[i][j] == 2 and totalzero == 0:
                nonlocal tp
                tp += 1
            
            temp = grid[i][j]
            grid[i][j] = 99

            dfs(i+1,j,totalzero)
            dfs(i-1,j,totalzero)
            dfs(i,j+1,totalzero)
            dfs(i,j-1,totalzero)

            grid[i][j] = temp

            # return tp
        
        
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0: totalzero += 1
                    
        
                    
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1: 
                    
                    dfs(i,j,totalzero)
                    
        return tp
        
        
       
        
    
        