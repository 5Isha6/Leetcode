#1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        l, r = 0, 0
        mind, maxd = deque(), deque()
        res = 0
        
        while r < len(nums):
        
            while mind and nums[mind[-1]] >= nums[r]: mind.pop()
            while maxd and nums[maxd[-1]] < nums[r]: maxd.pop()
            
            mind.append(r)
            maxd.append(r)
        
            while nums[maxd[0]] - nums[mind[0]] > limit:
                l += 1
                if l > mind[0]:
                    mind.popleft()
                if l > maxd[0]:
                    maxd.popleft()
            res = max(res, r - l +1)
            r += 1
        return res
                    
        
