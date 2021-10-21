#1423. Maximum Points You Can Obtain from Cards
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)
        
        if k > n:
            return sum(cardPoints)
        
        prefixsum = sum(cardPoints[-k:])
        maxscore = prefixsum
        for i in range(k):
            
            
            prefixsum = cardPoints[i] + prefixsum - cardPoints[n - k + i ]

            maxscore = max(maxscore, prefixsum)
           
        return maxscore
                
        
