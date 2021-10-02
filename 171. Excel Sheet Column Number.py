# 171. Excel Sheet Column Number
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
    
        col = 0
    
        if columnTitle == '':
            return -1
        
        for i in range(len(columnTitle)):
            # col *=26;
            # col += ord(s[i]) - ord(s['A']) + 1;
            col = (col * 26) + (ord(columnTitle[i]) - ord('A') + 1)
            




        return col
