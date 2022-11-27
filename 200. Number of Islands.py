#200. Number of Islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:   
    
        # bfs
        
        if not grid:
            return 0
    
        visit = set()
        M = len(grid)
        N = len(grid[0])
        island_cnt = 0
        # dire = [(1,0),(0,1),(-1,0),(0,-1)]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def bfs(ii, jj):
            q = collections.deque([(ii,jj)])
            visit.add((ii,jj))


            while q:
                r,c = q.popleft()

                for dr, dc in directions:
                    # print(di[0], di[1])
                    nr = r + dr
                    nc = c + dc
                    if (nr in range(M) and nc in range(N) and grid[nr][nc] == "1" and (nr,nc) not in visit):
                        q.append((nr,nc))
                        visit.add((nr,nc))

        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1" and (i,j) not in visit:
                    bfs(i, j)
                    island_cnt += 1


        
        return island_cnt
                
        
#dfs    
#     def numIslands(self, grid: List[List[str]]) -> int:
        
        
#         M = len(grid)
#         N = len(grid[0])
#         num_islands = 0
        
#         def ispartofIslands( i, j):
            
#             if i < 0 or i >= M or j < 0 or j >= N or grid[i][j] == '0':
#                 return
            
#             grid[i][j] = '0'
#             ispartofIslands(i + 1, j)
           
#             ispartofIslands(i - 1, j)
#             ispartofIslands(i , j + 1)
#             ispartofIslands(i, j - 1)
        
        
        
#         if not M:
#             return 0
        
#         for i in range(M):
#             for j in range(N):
#                 if grid[i][j] == '1':
#                     num_islands += 1
#                     ispartofIslands(i, j)
       
#         return num_islands
