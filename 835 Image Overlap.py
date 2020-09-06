#835 Image Overlap
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        size = len(A)
        
        maxi = 0
        for dx,dy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            for shiftx in range(size):
                for shifty in range(size):
                    count = 0
                    for x in range(size):
                        for y in range(size):
                        
                            if A[x][y] == 1:
                                nx, ny = x + dx*shiftx, y+dy*shifty
                                if 0<=nx<size and 0<=ny<size and B[nx][ny] == 1:
                                    count+=1
                    maxi = max(count,maxi)
        return maxi