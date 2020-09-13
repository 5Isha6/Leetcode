#152 Maximum Product Subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxP, minP, best = 1, 1 ,nums[0]
        
        for i in nums:
            if i < 0:
                minP, maxP = maxP, minP
            maxP = max(i*maxP, i)
            minP = min(i*minP, i)
            # print(i,maxP,minP)
            best = max(maxP,best)
        return best
        
        
        
        
            
        