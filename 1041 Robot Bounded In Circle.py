#104 Robot Bounded In Circle
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        d = 0
        x, y = 0, 0
        direct = [(0,1), (-1,0), (0, -1), (1, 0)]
        for i in instructions:
            if i == 'G':
                x += direct[d%4][0]
                y += direct[d%4][1]
            elif i == 'L':
                d += 1
            elif i == 'R':
                d -= 1
            # print(x,y,d)
        return (x,y) == (0,0) or d%4 != 0
        