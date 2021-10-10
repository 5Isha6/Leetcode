# 348. Design Tic-Tac-Toe
class TicTacToe:

    def __init__(self, n: int):
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.antidiag = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        
        
       
        # if row != col or row != self.n - col - 1:
        if player == 1:
            self.row[row] += 1
            self.col[col] += 1

        else:
            self.row[row] -= 1
            self.col[col] -= 1
        # else:
        if row == col:

            self.diag += 1 if player == 1 else -1
            if row + col == self.n - 1 :
                self.antidiag += 1 if player == 1 else -1
        elif row != col and row + col == self.n - 1 :
            self.antidiag += 1 if player == 1 else -1
        
        if abs(self.row[row]) == self.n  or abs(self.col[col]) == self.n or abs(self.diag) == self.n or abs(self.antidiag)== self.n :
            return player
        else:
            return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
