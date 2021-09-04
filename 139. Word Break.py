#139. Word Break
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
        for i in range(n,-1,-1):
            for w in wordDict:
                
                if n - (i) >= len(w) and  s[i: i+len(w)] == w:
                    
                    if dp[i + len(w)]:
                        dp[i] = True
                    if dp[i]:
                        break
        
        return dp[0]
