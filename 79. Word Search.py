#79. Word Search
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def search(i,j,idx):
            n= len(board)
            if idx== len(word)-1:
                return True
			# To check visited array	
            board[i][j] = chr(ord(board[i][j]) - 65)
                
            if i>0 and board[i-1][j] == word[idx+1] and search(i-1,j,idx+1):
                return True
            if i<n-1 and board[i+1][j] == word[idx+1] and search(i+1,j,idx+1):
                return True
            if j>0 and board[i][j-1] == word[idx+1] and search(i,j-1,idx+1):
                return True
            if j<len(board[0])-1 and board[i][j+1] == word[idx+1] and search(i,j+1,idx+1):
                return True

            # To check visited array         
            board[i][j] = chr(ord(board[i][j]) + 65)
            return False       
        
                 
        idx = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                
                if board[i][j] == word[0] and search(i,j, idx):
                    return True
                
        return False
                    