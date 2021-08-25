#118. Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
#         j = 0
#         op = [[1],[1,1]]
#         t = []
#         for i in range(numRows-1):
#             t.append(len(op))
            
        t = []
        for i in range(numRows):
            
            row = [None for _ in range(i+1)]
            row[0], row[-1] = 1, 1
            for j in range(1,len(row)-1):
                row[j] = t[i-1][j-1] + t[i-1][j]
            t.append(row)
        return t
