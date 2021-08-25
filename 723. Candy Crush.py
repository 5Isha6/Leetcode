# 723. Candy Crush
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        r = len(board)
        c = len(board[0])
        
        todo = False
        
        for rows in range(r):
            for cols in range(c-2):
                if abs(board[rows][cols]) == abs(board[rows][cols+1]) == abs(board[rows][cols+2]) != 0 :
                    todo = True
                    board[rows][cols]=board[rows][cols+1]=board[rows][cols+2] = -abs(board[rows][cols])
                    
        for rows in range(r-2):
            for cols in range(c):
                if abs(board[rows][cols]) == abs(board[rows+1][cols]) == abs(board[rows+2][cols]) != 0 :
                    todo = True
                    board[rows][cols]=board[rows+1][cols]=board[rows+2][cols] = -abs(board[rows][cols])

        for co in range(c):            
            cc = r - 1
            
            for ro in range(r-1,-1,-1):
                if board[ro][co] > 0 :
                    board[cc][co] = board[ro][co]
                    cc -= 1
            for i in range(cc,-1,-1):
                board[i][co] = 0
            
        return self.candyCrush(board) if todo else board
            
        
