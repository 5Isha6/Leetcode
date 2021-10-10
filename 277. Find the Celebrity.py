# 277. Find the Celebrity
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        celeb = 0

        
        for i in range(n):

            if knows(celeb, i):
                celeb = i

        for i in range(0, celeb):
            if knows(celeb, i):
                return -1
            if not knows(i, celeb):
                return -1
            
        for i in range(celeb, n):
            if not knows(i,celeb):
                return -1
        return celeb
 
        
        
        
 
