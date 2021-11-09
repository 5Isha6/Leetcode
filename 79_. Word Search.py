#79. Word Search
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if len(word) == 0 or not board or not board[0]:
            return False
            
        row = len(board)
        col = len(board[0])
        
        def helper(i, j, k):
           
            if  i < 0 or i > row - 1 or j < 0 or j > col - 1 or  k >= len(word) or  board[i][j] != word[k]:
                return False
                               
            if k == len(word) - 1:
                return True
            tmp = board[i][j]
            board[i][j] = '*'
            res =  helper(i + 1, j, k+1) or  helper(i - 1, j, k+1) or  helper(i, j + 1, k+1) or  helper(i, j - 1, k+1)
            board[i][j] = tmp
            
            return res
                                           
        for i in range(row):
            for j in range(col):
                # print(i,j)
                if helper(i,j,0):
                    return True
        return False
            
            
        
        
