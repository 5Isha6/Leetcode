# 657. Robot Return to Origin
class Solution:
    """
    @param moves: a sequence of its moves
    @return: if this robot makes a circle
    """
    def judgeCircle(self, moves):
        # Write your code here
        x, y = 0, 0
        for i in moves:
            if i == 'L':
                x -= 1
            elif i == 'R':
                x += 1
            elif i == 'U':
                y -= 1
            elif i == 'D':
                y += 1
            
        if (x,y) == (0,0):
            return True
        else:
            return False
