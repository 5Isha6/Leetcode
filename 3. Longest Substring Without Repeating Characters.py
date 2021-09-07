# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        st = 0
        used = {}
        ml = 0
        for i in range(len(s)):
            # print(s[i], used,ml)
            if s[i] in used and st <= used[s[i]]:
                st = used[s[i]] + 1
            else:
                ml = max(ml, i - st + 1)
                
            used[s[i]] = i
            # print(s[i], used,st,ml)
        return ml
                
        
        
