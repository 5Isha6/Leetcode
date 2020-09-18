# 121 Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        mini = float("inf")
        
        for price in prices:
            mini = min(mini, price)
            best = max(best,price-mini)
        
        
        return best
        
        
    
                    
        
        