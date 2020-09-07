#54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        M = len(matrix)
        if M==0 :
            return []
        N = len(matrix[0])
        
        
        di = 0
        t = 0
        l = 0
        r = N-1
        b = M-1
        i = 0
        result = []
        
        while t<= b and l<= r:
            
            if di == 0 :
                # print(t,l,b,r, matrix[t][i])
                for i in range(l,r+1,1):
                    result.append(matrix[t][i])
                t+=1
            elif di == 1:
                for i in range(t,b+1,1):
                    result.append(matrix[i][r])
                r-=1
            elif di == 2:
                for i in range(r,l-1,-1):
                    result.append(matrix[b][i])
                b-=1
            elif di == 3:
                for i in range(b,t-1,-1):
                    result.append(matrix[i][l])
                l+=1
            di=(di+1)%4
    
        return result

        