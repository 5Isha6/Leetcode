# 58 Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        if not arr :
            return 0
        else:
            return len(arr[-1])