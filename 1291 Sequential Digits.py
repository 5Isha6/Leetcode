#1291 Sequential Digits
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for i in range(1,10):
            nxt = i 
            num = 0
            
            while num<= high and nxt<10:
                num = num*10+nxt
                if num>= low and num<= high:
                    res.append(num)
                nxt+=1
        return sorted(res)