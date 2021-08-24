# 54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        up = 0
        left = 0
        right = cols - 1
        down = rows-1
        
        op = []
        while len(op) < cols*rows:
            
            for c in range(left,right+1):
                op.append(matrix[up][c])
            
            for r in range(up+1,down + 1):
                op.append(matrix[r][right])
            
            if up!= down:
                for c in range(right-1,left-1,-1):
                    op.append(matrix[down][c])

            if left != right:
            
                for r in range(down-1,up, -1):
                    op.append(matrix[r][left])

            up += 1
            down -= 1
            left +=1
            right -= 1
        return op
