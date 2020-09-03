# 949 Largest Time for Given Digits
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        best = -1
        for h2,h1,m2, m1 in permutations(A):
            

            hour = h2*10 + h1
            minute = m2*10+m1
            if hour < 24 and minute < 60:
            
                best = max(best,hour*60 + minute)
        if best<0:
            return ""
            
#         hour = best//60
#         mini = best%60
        hour, mini = divmod(best,60)
        return f"{hour:02}:{mini:02}"
        
        