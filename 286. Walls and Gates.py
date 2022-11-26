#286. Walls and Gates
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
         
        def bfs(r, c):
            
            visited = [ra[:] for ra in rooms]
            # print("ROW ", r, c, "\n" , visited)
            q = deque()
            q.append([r,c,0])
            
            while q:
            
                r, c, cnt = q.popleft()
                for di in dire:
                    
                    nr = r + di[0]
                    nc = c + di[1]
                    
                    if 0 <= nr < M and 0 <= nc < N and visited[nr][nc] != -1 and visited[nr][nc] != 0:
                        rooms[nr][nc] = min(rooms[nr][nc], cnt +1)
                        visited[nr][nc] = -1
                        q.append([nr,nc,cnt+1])
 
        
        
        M = len(rooms)
        N = len(rooms[0])
        # count = 0
        dire = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for i in range(M):
            for j in range(N):
                if not rooms[i][j]:
                    bfs(i, j)
