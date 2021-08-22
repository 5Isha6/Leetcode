# Lintcode 1893 · the Valid String
from collections import defaultdict, Counter

class Solution:
    """
    @param s: a string
    @return: if valid return "YES" else return "NO"
    """
    def isValid(self, s):
        # write your code here
        d = Counter(s)
        print(d)
        set_d = set(d.values())
     
        print(set_d)
        if len(set_d) == 1:
            return 'YES'
        if len(set_d)> 2:
            return 'NO'
        dic=defaultdict(int)
        for i in d.values():
            dic[i] +=1
        if 1 in dic.keys() and dic[1]== 1:
            return 'YES'
        maxi, mini = max(set_d),min(set_d)
        if dic[maxi] == 1 and maxi == mini + 1:
            return 'YES'

        return 'NO'


        # return 'yes'
