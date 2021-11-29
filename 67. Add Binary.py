#67. Add Binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return "{0:b}".format(int(a,2) + int(b,2))
        x = int(a,2)
        y = int(b,2)
        while y:
            ans = x^y
            car = (x&y) << 1
            x, y = ans, car
        # print(x)
        return "{0:b}".format(x)
