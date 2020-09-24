# 389 Find the Difference 
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = 0
        for i in s:
            diff ^= ord(i)
        for j in t:
            diff ^= ord(j)
        return chr(diff)

            
        