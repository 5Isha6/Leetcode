# 198 House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        if N == 1:
            return nums[0]
        
        v1, v2 = nums[0], max(nums[0], nums[1])
        
        for i in range(2, N):
            
            tmp =  v2
            v2 = max(v2, v1 + nums[i])
            v1 = tmp
        
        return v2