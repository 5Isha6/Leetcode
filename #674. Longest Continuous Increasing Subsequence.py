#674. Longest Continuous Increasing Subsequence
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = 0
        
        maxi_l = 1
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                l = i
            
            maxi_l = max(maxi_l, i - l + 1)
        return maxi_l
