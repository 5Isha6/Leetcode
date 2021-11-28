#340. Longest Substring with At Most K Distinct Characters
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        st = 0 
        win = 0
        visit = defaultdict(int)
        
        for i in range(len(s)):
            visit[s[i]] += 1
                
            while len(visit) > k:
                
                visit[s[st]] -= 1
                
                if visit[s[st]] == 0:
                    del visit[s[st]]
                
                st += 1
                
            
            win = max(win, i - st + 1)
            
        return win
        
