# 417. Pacific Atlantic Water Flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        #bfs
        if not heights or not heights[0]:
            return []

        pac = collections.deque()
        atl = collections.deque()

        M = len(heights)
        N = len(heights[0])

        for i in range(M):
            pac.append((i,0))
            atl.append((i, N-1))

        for j in range(N):
            pac.append((0,j))
            atl.append((M-1, j))

        # print(pac,atl) 
        def bfs(qu):
            
            visit = set()
            while qu:
                (ro, co) = qu.popleft()
                visit.add((ro,co))
                for (r,c) in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr, nc = ro + r , co + c

                    if 0 <= nr < M and 0 <= nc < N  and heights[ro][co] <= heights[nr][nc] and (nr,nc) not in visit:
                        qu.append((nr,nc))
                        
                
            return visit

        pac_list = bfs(pac)
        atl_list = bfs(atl)
        
        print(atl_list,pac_list)
        return list(atl_list.intersection(pac_list))

        #dfs
        # if not heights or not heights[0]:
        #     return []

        # M = len(heights)
        # N = len(heights[0])

        # pac_visit = set()
        # atl_visit = set()

        # def dfs(i, j, visit):
        #     visit.add((i,j))
        #     directions = [[1,0],[-1,0],[0,1],[0,-1]]
        #     for r,c in directions:
                
        #         nr, nc = i + r, j + c

        #         if  0 <= nr < M and 0 <= nc < N and heights[i][j] <= heights[nr][nc] and (nr,nc) not in visit:
                    
        #             dfs(nr,nc,visit)

            
        # for i in range(M):
        #     dfs(i, N - 1, atl_visit)
        #     dfs(i, 0, pac_visit)

        # for j in range(N):
        #     dfs(0,j, pac_visit)
        #     dfs(M - 1,j, atl_visit)

        # return list(pac_visit.intersection(atl_visit))


        
